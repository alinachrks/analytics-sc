import streamlit as st
from streamlit_lottie import st_lottie
import json
import streamlit.components.v1 as components
import base64
import os

# Function to load image as base64
def get_base64_of_bin_file(bin_file):
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()

# Function to set background
def set_background(png_file):
    try:
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
    except FileNotFoundError:
        st.error("Файл для фона не найден: {}".format(png_file))

# Caching HTML files for performance
@st.cache_data(ttl=3600)  # Cache with 1-hour lifetime
def load_map_html(file_path):
    try:
        with open(file_path, "r", encoding='utf-8') as f:
            return f.read()
    except FileNotFoundError:
        return f"<p>Карта недоступна. Проверьте файл: {file_path}</p>"

# Function to render maps
def render_map(tab, subheader, description, file_path, height=800):
    with tab:
        st.subheader(subheader)
        st.markdown(description)
        map_html = load_map_html(file_path)
        components.html(map_html, height=height, scrolling=True)

# Footer button renderer
def render_footer_button(text, link):
    st.markdown(f'''
        <div class="footer-button">
            <a href="{link}" target="_blank">
                <button>{text}</button>
            </a>
        </div>
    ''', unsafe_allow_html=True)

def app():
    st.set_page_config(page_title="Analytics SC", page_icon="🌇", layout="wide", initial_sidebar_state="collapsed")

    # Set background image
    set_background("images/fotor-ai-2024070273312.jpg")

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
        margin-top: -50px;
        padding-left: 20px;
        padding-right: 20px;
        font-size: 48px;
        font-weight: bold;
        color: #FFFFFF;
    }
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
    </style>
    """
    st.markdown(page_element, unsafe_allow_html=True)

    # Page header
    st.markdown('<div class="st-title-container"><h1>Социально-экономический портрет города</h1></div>', unsafe_allow_html=True)

    # Tabs for maps
    tabs = st.tabs([
        "Качество жизни", "Благоустройство", "Велодорожки", "Парковки для самокатов", "Инфраструктура",
        "Жильё", "Бизнес", "Реновация", "Плотность населения", "Демография",
        "Спрос и предложение", "Привлекательность", "Гостиницы", "Налоги"
    ])

    # Maps for each tab
    render_map(tabs[0], "Индикаторы качества жизни по районам", "Карта показывает динамику развития районов по качеству жизни", "components/indicators.html")
    render_map(tabs[1], "Благоустройство | Абаттандыру", "Карта показывает шаговую доступность к зелёным зонам и зонам рекреации", "components/new_buildings.html")
    render_map(tabs[2], "Велодорожки | Велосипедные дорожки", "Карта отображает текущую сеть велодорожек города и рекомендации по развитию", "components/bicycle_lanes.html")
    render_map(tabs[3], "Парковки для самокатов | Велосипедные парковки", "Карта отображает текущие парковки для макромобильного транспорта", "components/bicycle_point.html")
    render_map(tabs[4], "Инфраструктура | Инфрақұрылым", "Эта карта отображает инфраструктурные объекты, доступные в городе.", "components/infra.html")
    render_map(tabs[5], "Жильё | Тұрғын үй", "Карта показывает распределение жилых объектов по всему городу.", "components/residential.html")
    render_map(tabs[6], "Бизнес | Бизнес", "Карта показывает расположение бизнес-центров и других объектов деловой активности.", "components/business.html")
    render_map(tabs[7], "Реновация участков | Реновация", "Интерактивная карта, показывающая информацию о реновации участков.", "components/renovation.html")
    render_map(tabs[8], "Плотность населения | Тығыздық", "Карта плотности населения в различных районах города.", "components/density.html")
    render_map(tabs[9], "Демография | Демография", "Карта показывает демографические данные по районам.", "components/demographics.html")
    render_map(tabs[10], "Спрос и предложение | Сұраныс пен ұсыныс", "Карта спроса и предложения на определённые виды недвижимости и услуг.", "components/supply_demand.html")
    render_map(tabs[11], "Привлекательность участков | Тартымдылық", "Информация о привлекательности участков для бизнеса и инвестиций.", "components/attractiveness.html")
    render_map(tabs[12], "Гостиницы | Гостиничные комплексы", "Карта отображает расположение гостиниц и других туристических объектов.", "components/hotels.html")
    render_map(tabs[13], "Налоги", "Учтены только те данные, которые находятся в общем доступе:", "components/taxes.html")

    # Footer button
    render_footer_button("Ситуационный центр", "https://demo.opendata.smartalmaty.kz/")

if __name__ == "__main__":
    app()
