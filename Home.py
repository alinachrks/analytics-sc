import streamlit as st
from streamlit_lottie import st_lottie
import json
import streamlit.components.v1 as components
import base64

# Function to load image as base64
def get_base64_of_bin_file(bin_file):
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()

# Function to set background
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

# Caching HTML files for performance
@st.cache_data
def load_map_html(file_path):
    with open(file_path, "r", encoding='utf-8') as f:
        return f.read()

def app():
    st.set_page_config(page_title="Analytics SC", page_icon="🏙️", layout="wide", initial_sidebar_state="collapsed")

    # Set background image
    set_background("images/fotor-ai-2024070273312.jpg")  # Применяем загруженный вами фон

    # Styling of the page
    page_element = """
    <style>
    [data-testid="stAppViewContainer"]{
        background-size: cover;
        padding-top: 0;
    }
    [data-testid="stHeader"]{
        background-color: rgba(0,0,0,0);
        padding-top: 0;
    }
    [data-testid="stToolbar"]{
        right: 2rem;
        background-size: cover;
    }
    .st-title-container {
        margin-top: -50px;  /* Поднимем заголовок выше */
        padding-left: 20px;
        padding-right: 20px;
        font-size: 48px;  /* Увеличенный размер заголовка */
        font-weight: bold;
        color: #FFFFFF;
    }
    .st-description {
        text-align: justify;
        color: white;
        padding-left: 20px;
        padding-right: 20px;
        font-size: 20px;  /* Увеличенный размер текста описания */
        line-height: 1.6;
        margin-top: 0;
    }
    .button-container {
        display: flex;
        justify-content: space-evenly;
        margin-top: 10px;
        margin-bottom: 10px;
        padding-left: 20px;
        padding-right: 20px;
    }
    .stButton > button {
        position: relative;
        color: #FFFFFF !important;
        background: linear-gradient(135deg, #0066cc, #003366) !important;
        border: none;
        padding: 20px 40px;
        border-radius: 10px;
        box-shadow: 0 2px 4px rgba(0, 0, 0, 0.2);
        width: 300px;
        height: 100px;
        font-size: 18px;
        transition: all 0.3s ease;
    }
    .stButton > button:hover {
        background: linear-gradient(135deg, #0055bb, #002255) !important;
        transform: translateY(-5px);
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.4);
    }

    /* Style for the Situation Center Button */
    .footer-button a {
        text-decoration: none;
    }

    .footer-button button {
        position: relative;
        color: #FFFFFF;
        background: linear-gradient(135deg, #ff9800, #ff5722);
        border: none;
        padding: 15px 40px;
        border-radius: 12px;
        font-size: 18px;
        font-weight: bold;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.2);
        transition: all 0.3s ease;
        cursor: pointer;
    }

    .footer-button button:hover {
        background: linear-gradient(135deg, #ff6f00, #e65100);
        transform: translateY(-5px);
        box-shadow: 0 6px 8px rgba(0, 0, 0, 0.4);
    }

    .footer-button button:active {
        background: linear-gradient(135deg, #e65100, #bf360c);
        transform: translateY(0);
        box-shadow: none;
    }

    /* Menu and tabs text styling */
    .stTabs .tab-container {
        font-size: 22px;  /* Увеличенный размер текста вкладок */
        font-weight: bold;
        color: white;
        background: rgba(0, 0, 0, 0.5);  /* Прозрачный темный фон для вкладок */
    }
    </style>
    """
    st.markdown(page_element, unsafe_allow_html=True)

    # Page header
    st.markdown('<div class="st-title-container"><h1>Социально-экономический портрет города</h1></div>', unsafe_allow_html=True)

    # Tabs for maps with new order
    tab1, tab2, tab3, tab4, tab5, tab6, tab7, tab8, tab9, tab10, tab11, tab12 = st.tabs(
        ["Благоустройство", "Велодорожки", "Парковки для самокатов", "Инфраструктура", 
         "Жильё", "Бизнес", "Реновация", "Плотность населения", "Демография", 
         "Спрос и предложение", "Привлекательность", "Гостиницы"]
    )

    # Display maps and comments within each tab
    with tab1:
        st.subheader("Благоустройство | Абаттандыру")
        st.markdown("Карта показывает шаговую доступность к зелёным зонам и зонам рекреации и рекомендации по развитию инфраструктуры")
        map_html = load_map_html("components/new_buildings.html")
        components.html(map_html, height=1000, scrolling=True)

    with tab2:
        st.subheader("Велодорожки | Велосипедные дорожки")
        st.write("Карта отображает текущую сеть велодорожек города и рекомендации по развитию")
        map_html = load_map_html("components/bicycle_lanes.html")
        components.html(map_html, height=1000, scrolling=True)

    with tab3:
        st.subheader("Парковки для самокатов | Велосипедные парковки")
        st.write("Карта отображает текущие парковки (онлайн) для макромобильного транспорта и рекомендации по разметкее")
        map_html = load_map_html("components/bicycle_point.html")
        components.html(map_html, height=1000, scrolling=True)

    with tab4:
        st.subheader("Инфраструктура | Инфрақұрылым")
        st.write("Эта карта отображает инфраструктурные объекты, доступные в городе.")
        map_html = load_map_html("components/infra.html")
        components.html(map_html, height=1000, scrolling=True)

    with tab5:
        st.subheader("Жильё | Тұрғын үй")
        st.write("Карта показывает распределение жилых объектов по всему городу.")
        map_html = load_map_html("components/residential.html")
        components.html(map_html, height=1000, scrolling=True)

    with tab6:
        st.subheader("Бизнес | Бизнес")
        st.write("Карта показывает расположение бизнес-центров и других объектов деловой активности.")
        map_html = load_map_html("components/business.html")
        components.html(map_html, height=1000, scrolling=True)

    with tab7:
        st.subheader("Реновация участков | Реновация")
        st.write("Интерактивная карта, показывающая информацию о реновации участков.")
        map_html = load_map_html("components/renovation.html")
        components.html(map_html, height=1000, scrolling=True)

    with tab8:
        st.subheader("Плотность населения | Тығыздық")
        st.write("Карта плотности населения в различных районах города.")
        map_html = load_map_html("components/density.html")
        components.html(map_html, height=1000, scrolling=True)

    with tab9:
        st.subheader("Демография | Демография")
        st.write("Карта показывает демографические данные по районам.")
        map_html = load_map_html("components/demographics.html")
        components.html(map_html, height=1000, scrolling=True)

    with tab10:
        st.subheader("Спрос и предложение | Сұраныс пен ұсыныс")
        st.write("Карта спроса и предложения на определённые виды недвижимости и услуг.")
        map_html = load_map_html("components/supply_demand.html")
        components.html(map_html, height=1000, scrolling=True)

    with tab11:
        st.subheader("Привлекательность участков | Тартымдылық")
        st.write("Информация о привлекательности участков для бизнеса и инвестиций.")
        map_html = load_map_html("components/attractiveness.html")
        components.html(map_html, height=1000, scrolling=True)

    with tab12:
        st.subheader("Гостиницы | Гостиничные комплексы")
        st.write("Карта отображает расположение гостиниц и других туристических объектов.")
        map_html = load_map_html("components/hotels.html")
        components.html(map_html, height=1000, scrolling=True)

    # Footer button with link and new style
    st.markdown('<div class="footer-button"><a href="https://demo.opendata.smartalmaty.kz/" target="_blank"><button>Ситуационный центр</button></a></div>', unsafe_allow_html=True)

if __name__ == "__main__":
    app()
