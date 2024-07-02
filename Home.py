import streamlit as st
from streamlit_lottie import st_lottie
import json
import streamlit.components.v1 as components
import base64

# Функция для загрузки данных из GeoJSON файла
def load_geojson_data(file_path):
    with open(file_path, "r") as f:
        geojson_data = json.load(f)
    return geojson_data

# Функция для загрузки изображения в base64
def get_base64_of_bin_file(bin_file):
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()

# Функция для установки фона
def set_background(png_file):
    bin_str = get_base64_of_bin_file(png_file)
    page_bg_img = '''
    <style>
    .stApp {
        background-image: url("data:image/png;base64,%s");
        background-size: cover;
        background-attachment: fixed;
    }
    </style>
    ''' % bin_str

    st.markdown(page_bg_img, unsafe_allow_html=True)

def app():
    st.set_page_config(page_title="Analytics SC", page_icon="📊", layout="wide", initial_sidebar_state="collapsed")

    # Load background image
    with open("images/fotor-ai-2024070273312.jpg", "rb") as image_file:
        encoded_background = base64.b64encode(image_file.read()).decode()

    page_element = """
    <style>
    [data-testid="stAppViewContainer"]{
        background-image: url("https://i.ibb.co.com/N17SRVN/back.png");
        background-size: cover;
    }
    [data-testid="stHeader"]{
        background-color: rgba(0,0,0,0);
    }
    [data-testid="stToolbar"]{
        right: 2rem;
        background-image: url("https://cdn.iconscout.com/icon/free/png-256/hamburger-menu-462145.png");
        background-size: cover;
    }
    </style>
    """
    st.markdown(page_element, unsafe_allow_html=True)

    # Установка фона
    # set_background('images/fotor-ai-2024070273312.jpg')

    # Custom CSS for styling
    st.markdown("""
        <style>
        body {
            margin: 0;
            padding: 0;
            background-color: #2E3B4E;
        }
        .css-1d391kg {
            padding-top: 0 !important;
            padding-bottom: 0 !important;
            padding-left: 0 !important;
            padding-right: 0 !important;
        }
        .sidebar .sidebar-content {
            background-color: #2E3B4E;
        }
        .sidebar .sidebar-content .element-container {
            color: #FFFFFF;
        }
        .css-1lcbmhc {
            color: #FFFFFF !important;
        }
        .css-qbe2hs {
            background-color: #FFFFFF !important;
            color: #2E3B4E !important;
        }
        .stMarkdown {
            padding: 10px;
            border-radius: 5px;
        }
        .stButton > button {
            color: #FFFFFF !important;
            background: linear-gradient(135deg, #0066cc, #003366) !important;
            border: none;
            padding: 20px 40px;
            border-radius: 10px;
            box-shadow: 0 2px 4px rgba(0, 0, 0, 0.2);
            width: 300px;
            height: 100px;
            font-size: 18px;
        }
        .stButton > button:hover {
            background: linear-gradient(135deg, #0055bb, #002255) !important;
        }
        .button-container {
            display: flex;
            justify-content: space-evenly;
            margin-top: 20px;
            margin-bottom: 20px;
        }
        .full-width {
            width: 100% !important;
            margin: 0 !important;
        }
        </style>
    """, unsafe_allow_html=True)

    # Заголовок страницы
    st.title("Социально-экономический портрет города")

    # Описание приложения
    st.markdown("""
    <div class="stMarkdown" style="text-align: justify; color: white;">
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
    col1, col2, col3, col4 = st.columns(4)

    if col1.button("Инфраструктура"):
        st.markdown("<style>.css-1y4p8pa {width: 100% !important; margin: 0 !important;}</style>", unsafe_allow_html=True)
        with open("components/infra.html", "r") as f:
            map_html = f.read()
            components.html(map_html, height=1200, scrolling=True)

    if col2.button("Текущие показатели города"):
        st.markdown("<style>.css-1y4p8pa {width: 100% !important; margin: 0 !important;}</style>", unsafe_allow_html=True)
        with open("components/portrait.html", "r") as f:
            map_html = f.read()
            components.html(map_html, height=1200, scrolling=True)

    if col3.button("Анализ покупательской способности"):
        st.markdown("<style>.css-1y4p8pa {width: 100% !important; margin: 0 !important;}</style>", unsafe_allow_html=True)
        st.markdown("""
            <div class="stMarkdown" style="text-align: justify; color: white;">
                <ul>
                    <li>По умолчанию на карте показано распределение свободных денег у проживающего населения</li>
                    <li>Выберите категорию бизнеса из выпадающего списка</li>
                    <li>Нажмите на участок для получения информации о нём</ли>
                    <li>Информация об участке будет отображаться в левой панели</ли>
                    <ли>Для сброса карты и удаления нарисованных полигонов используйте кнопку "Сбросить"</ли>
                    <ли>Кнопка "Во весь экран" позволяет перейти в полноэкранный режим для удобства просмотра</ли>
                </ul>
            </div>
            """, unsafe_allow_html=True)

        with open("components/buy_power.html", "r") as f:
            map_html = f.read()
            components.html(map_html, height=1200, scrolling=True)

    if col4.button("Анализ участков"):
        st.markdown("<style>.css-1y4p8pa {width: 100% !important; margin: 0 !important;}</style>", unsafe_allow_html=True)
        st.markdown("""#### Карта для получения информации по нарисованному полигону""")

        st.markdown("""
        <div class="stMarkdown" style="text-align: justify; color: white;">
            <ul>
                <li>По умолчанию на карте показана тепловая карта объектов инфраструктуры</ли>
                <li>Выберите стиль карты из выпадающего списка для изменения внешнего вида карты</ли>
                <ли>Нажмите на карту для начала рисования полигона на карте</ли>
                <ли>Старайтесь выбирать маленькие участки для получения более точной информации</ли>
                <ли>После завершения рисования полигона, информация об участке будет отображаться в левой панели</ли>
                <ли>Внизу боковой панели будут также отображены площадь и периметр участка</ли>
                <ли>Узнав площадь территории, вы можете рассчитать значения показателей в зависимости от количества домов</ли>
                <ли>Для сброса карты и удаления нарисованных полигонов используйте кнопку "Сбросить"</ли>
                <ли>Кнопка "Во весь экран" позволяет перейти в полноэкранный режим для удобства просмотра</ли>
            </ul>
        </div>
        """, unsafe_allow_html=True)

        st.header(" ")

        # Вставляем карту в приложение
        with open("components/combo.html", "r") as f:
            map_html = f.read()
            components.html(map_html, height=1200, scrolling=True)

    with st.sidebar:
        with open("data/comp.json", "r", errors='ignore') as f:
            data = json.load(f)
        st_lottie(data)

if __name__ == "__main__":
    app()
