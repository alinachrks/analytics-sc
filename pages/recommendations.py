import streamlit as st
from streamlit_lottie import st_lottie
import json
import streamlit.components.v1 as components

# Функция для загрузки данных из GeoJSON файла
def load_geojson_data(file_path):
    with open(file_path, "r") as f:
        geojson_data = json.load(f)
    return geojson_data

def app():
    st.set_page_config(page_title="Analytics SC", page_icon="📊", layout="wide")

    # Custom CSS for styling
    st.markdown("""
        <style>
        .sidebar .sidebar-content {
            background-color: #2E3B4E;
        }
        .sidebar .sidebar-content .element-container {
            color: #FFFFFF;
        }
        .css-1d391kg {
            background-color: #2E3B4E !important;
        }
        .css-1lcbmhc {
            color: #FFFFFF !important;
        }
        .css-qbe2hs {
            background-color: #FFFFFF !important;
            color: #2E3B4E !important;
        }
        </style>
    """, unsafe_allow_html=True)

    # Заголовок страницы
    st.title("Анализ по секторам")
    if st.button("Вернуться на главную"):
        st.session_state.current_page = "Главная"

    # Описание приложения
    st.markdown("""
    <div style="text-align: justify;">
    Данное веб-приложение предоставляет удобные инструменты для анализа и прогнозирования
    различных аспектов городской среды в Алматы. Приложение позволяет анализировать 
    распределение инфраструктуры и бизнеса, рассчитывать показатели плотности населения 
    и необходимых инфраструктурных объектов на участке. Оно также позволяет определить 
    привлекательность территории для конкретного типа бизнеса и проводить геоаналитику 
    для более эффективного планирования и развития городской инфраструктуры. 
    Приложение предоставляет интерактивные карты, инструменты для анализа и удобный интерфейс 
    для пользователей, интересующихся инвестициями и принятием решений в области городского развития.
    </div>
    """, unsafe_allow_html=True)

    st.header(" ")

    # Добавление кнопок и отображение карт
    show_business_button = st.button("Инфраструктура")
    if show_business_button:
        with open("components/infra.html", "r") as f:
            map_html = f.read()
            components.html(map_html, height=600)

            # Создаем и добавляем легенду
            legend_html = """
            <div class="legend">
                <div class="label-left">Минимум</div>
                <div class="gradient"></div>
                <div class="label-right">Максимум</div>
            </div>
            """
            st.markdown(legend_html, unsafe_allow_html=True)

            # CSS стили для легенды
            st.markdown(
                """
                <style>
                .legend {
                    position: relative;
                    width: 100%;
                    margin: 0 auto;
                    text-align: center;
                    background-color: white;
                    padding: 10px;
                    border-radius: 5px;
                    box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
                    margin-top: 20px;
                }
                .gradient {
                    width: calc(100% - 140px);
                    height: 20px;
                    background: linear-gradient(to right, rgba(241, 248, 246, 0.45), rgba(17, 87, 171, 0.65), rgba(0, 128, 128, 0.65), rgba(255, 255, 0, 0.65), rgba(126, 177, 16, 0.65), rgba(39, 116, 6, 0.65));
                    display: inline-block;
                    margin: 0 10px;
                }
                .label-left, .label-right {
                    display: inline-block;
                    width: 50px;
                    text-align: center;
                }
                .label-left {
                    float: left;
                }
                .label-right {
                    float: right;
                    margin-right: 20px;
                }
                </style>
                """,
                unsafe_allow_html=True
            )

    show_power_button = st.button("Текущие показатели города")
    if show_power_button:
        with open("components/portrait.html", "r") as f:
            map_html = f.read()
            components.html(map_html, height=600)

            # Создаем и добавляем легенду
            legend_html = """
            <div class="legend">
                <div class="label-left">Минимум</div>
                <div class="gradient"></div>
                <div class="label-right">Максимум</div>
            </div>
            """
            st.markdown(legend_html, unsafe_allow_html=True)

            # CSS стили для легенды
            st.markdown(
                """
                <style>
                .legend {
                    position: relative;
                    width: 100%;
                    margin: 0 auto;
                    text-align: center;
                    background-color: white;
                    padding: 10px;
                    border-radius: 5px;
                    box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
                    margin-top: 20px;
                }
                .gradient {
                    width: calc(100% - 140px);
                    height: 20px;
                    background: linear-gradient(to right, rgba(241, 248, 246, 0.45), rgba(17, 87, 171, 0.65), rgba(0, 128, 128, 0.65), rgba(255, 255, 0, 0.65), rgba(126, 177, 16, 0.65), rgba(39, 116, 6, 0.65));
                    display: inline-block;
                    margin: 0 10px;
                }
                .label-left, .label-right {
                    display: inline-block;
                    width: 50px;
                    text-align: center;
                }
                .label-left {
                    float: left;
                }
                .label-right {
                    float: right;
                    margin-right: 20px;
                }
                </style>
                """,
                unsafe_allow_html=True
            )

    show_power_button = st.button("Анализ покупательской способности")
    if show_power_button:
        st.markdown("""
            <div style="text-align: justify;">
                <ul>
                    <li>По умолчанию на карте показано распределение свободных денег у проживающего населения</li>
                    <li>Выберите категорию бизнеса из выпадающего списка</li>
                    <li>Нажмите на участок для получения информации о нём</li>
                    <li>Информация об участке будет отображаться в левой панели</li>
                    <li>Для сброса карты и удаления нарисованных полигонов используйте кнопку "Сбросить"</li>
                    <li>Кнопка "Во весь экран" позволяет перейти в полноэкранный режим для удобства просмотра</li>
                </ul>
            </div>
            """, unsafe_allow_html=True)

        with open("components/buy_power.html", "r") as f:
            map_html = f.read()
            components.html(map_html, height=600)

            # Создаем и добавляем легенду
            legend_html = """
            <div class="legend">
                <div class="label-left">Минимум</div>
                <div class="gradient"></div>
                <div class="label-right">Максимум</div>
            </div>
            """
            st.markdown(legend_html, unsafe_allow_html=True)

            # CSS стили для легенды
            st.markdown(
                """
                <style>
                .legend {
                    position: relative;
                    width: 100%;
                    margin: 0 auto;
                    text-align: center;
                    background-color: white;
                    padding: 10px;
                    border-radius: 5px;
                    box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
                    margin-top: 20px;
                }
                .gradient {
                    width: calc(100% - 140px);
                    height: 20px;
                    background: linear-gradient(to right, rgba(241, 248, 246, 0.45), rgba(17, 87, 171, 0.65), rgba(0, 128, 128, 0.65), rgba(255, 255, 0, 0.65), rgba(126, 177, 16, 0.65), rgba(39, 116, 6, 0.65));
                    display: inline-block;
                    margin: 0 10px;
                }
                .label-left, .label-right {
                    display: inline-block;
                    width: 50px;
                    text-align: center;
                }
                .label-left {
                    float: left;
                }
                .label-right {
                    float: right;
                    margin-right: 20px;
                }
                </style>
                """,
                unsafe_allow_html=True
            )

    with st.sidebar:
        with open("data/comp.json", "r", errors='ignore') as f:
            data = json.load(f)
        st_lottie(data)

    st.header(" ")
    st.markdown("""#### Карта для получения информации по нарисованному полигону""")

    st.markdown("""
    <div style="text-align: justify;">
        <ul>
            <li>По умолчанию на карте показана тепловая карта объектов инфраструктуры</li>
            <li>Выберите стиль карты из выпадающего списка для изменения внешнего вида карты</li>
            <li>Нажмите на карту для начала рисования полигона на карте</li>
            <li>Старайтесь выбирать маленькие участки для получения полее точной информации</li>
            <li>После завершения рисования полигона, информация об участке будет отображаться в левой панели</li>
            <li>Внизу боковой панели будут также отображены плащадь и периметр участка</li>
            <li>Узнав площадь территории, вы можете рассчитать значения показателей в зависимости от количества домов</li>
            <li>Для сброса карты и удаления нарисованных полигонов используйте кнопку "Сбросить"</li>
            <li>Кнопка "Во весь экран" позволяет перейти в полноэкранный режим для удобства просмотра</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

    st.header(" ")

    # Вставляем карту в приложение
    with open("components/combo.html", "r") as f:
        map_html = f.read()
        components.html(map_html, height=600)

        st.markdown("""##### Обеспеченность территорий городской инфраструктурой""")

        # Создаем и добавляем легенду
        legend_html = """
        <div class="legend">
            <div class="label-left">Минимум</div>
            <div class="gradient"></div>
            <div class="label-right">Максимум</div>
        </div>
        """
        st.markdown(legend_html, unsafe_allow_html=True)
        # CSS стили для легенды
        st.markdown(
            """
            <style>
            .legend {
                position: relative;
                width: 100%;
                margin: 0 auto;
                text-align: center;
                background-color: white;
                padding: 10px;
                border-radius: 5px;
                box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
                margin-top: 20px;
            }
            .gradient {
                width: calc(100% - 140px);
                height: 20px;
                background: linear-gradient(to right, rgba(241, 248, 246, 0.45), rgba(17, 87, 171, 0.65), rgba(0, 128, 128, 0.65), rgba(255, 255, 0, 0.65), rgba(126, 177, 16, 0.65), rgba(39, 116, 6, 0.65));
                display: inline-block;
                margin: 0 10px;
            }
            .label-left, .label-right {
                display: inline-block;
                width: 50px;
                text-align: center;
            }
            .label-left {
                float: left;
            }
            .label-right {
                float: right;
                margin-right: 20px;
            }
            </style>
            """,
            unsafe_allow_html=True
        )

if __name__ == "__main__":
    app()
