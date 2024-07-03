import streamlit as st
from streamlit_lottie import st_lottie
import json
import streamlit.components.v1 as components
import base64

# Function to load data from GeoJSON file
def load_geojson_data(file_path):
    with open(file_path, "r") as f:
        geojson_data = json.load(f)
    return geojson_data

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

def app():
    st.set_page_config(page_title="Analytics SC", page_icon="🏙️", layout="wide", initial_sidebar_state="collapsed")

    # Load background image
    with open("images/fotor-ai-2024070273312.jpg", "rb") as image_file:
        encoded_background = base64.b64encode(image_file.read()).decode()

    page_element = """
    <style>
    [data-testid="stAppViewContainer"]{
        background-image: url("https://i.ibb.co.com/N17SRVN/back.png");
        background-size: cover;
        padding-top: 0;
    }
    [data-testid="stHeader"]{
        background-color: rgba(0,0,0,0);
        padding-top: 0;
    }
    [data-testid="stToolbar"]{
        right: 2rem;
        background-image: url("https://cdn.iconscout.com/icon/free/png-256/hamburger-menu-462145.png");
        background-size: cover;
    }
    .st-title-container {
        margin-top: 0;
        padding-left: 20px;
        padding-right: 20px;
    }
    .st-description {
        text-align: justify;
        color: white;
        padding-left: 20px;
        padding-right: 20px;
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
    .stButton > button[data-tooltip]:hover::after {
        content: attr(data-tooltip);
        position: absolute;
        bottom: 120%;
        left: 50%;
        transform: translateX(-50%);
        background-color: #333;
        color: #fff;
        padding: 5px 10px;
        border-radius: 5px;
        white-space: nowrap;
        opacity: 1;
        visibility: visible;
        transition: opacity 0.3s ease, visibility 0.3s ease;
    }
    .stButton > button[data-tooltip]::after {
        opacity: 0;
        visibility: hidden;
    }
    .footer-container {
        margin-top: 50px;
        padding: 20px;
        background-color: rgba(0,0,0,0);
    }
    .footer-button {
        text-align: center;
        margin-top: 20px;
    }
    .footer-button a {
        text-decoration: none;
    }
    .footer-button button {
        color: #FFFFFF !important;
        background: rgba(0, 102, 204, 0.2);
        border: none;
        padding: 15px 30px;
        border-radius: 10px;
        box-shadow: 0 2px 4px rgba(0, 0, 0, 0.2);
        font-size: 18px;
        transition: all 0.3s ease;
    }
    .footer-button button:hover {
        background: rgba(0, 85, 187, 0.5);
        transform: translateY(-5px);
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.4);
    }
    </style>
    """
    st.markdown(page_element, unsafe_allow_html=True)

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
        </style>
    """, unsafe_allow_html=True)

    # Page header
    st.markdown('<div class="st-title-container"><h1>Социально-экономический портрет города</h1></div>', unsafe_allow_html=True)

    # App description
    st.markdown("""
    <div class="st-description">
    Приложение предоставляет удобные инструменты для анализа и прогнозирования
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

    # Adding buttons and displaying maps
    col1, col2, col3, col4 = st.columns(4)
    col5, col6, col7, col8 = st.columns(4)

    if col1.button("Инфраструктура | Инфрақұрылым", key="btn1"):
        st.markdown("<style>.css-1y4p8pa {width: 100% !important; margin: 0 !important;}</style>", unsafe_allow_html=True)
        with open("components/infra.html", "r") as f:
            map_html = f.read()
            components.html(map_html, height=1000, scrolling=True)

    if col2.button("Жильё | Тұрғын үй", key="btn2"):
        st.markdown("<style>.css-1y4p8pa {width: 100% !important; margin: 0 !important;}</style>", unsafe_allow_html=True)
        with open("components/residential.html", "r") as f:
            map_html = f.read()
            components.html(map_html, height=1000, scrolling=True)

    if col3.button("Бизнес | Бизнес", key="btn3"):
        st.markdown("<style>.css-1y4p8pa {width: 100% !important; margin: 0 !important;}</style>", unsafe_allow_html=True)
        with open("components/business.html", "r") as f:
            map_html = f.read()
            components.html(map_html, height=1000, scrolling=True)

    if col4.button("Реновация участков | Реновация", key="btn4"):
        st.markdown("<style>.css-1y4p8pa {width: 100% !important; margin: 0 !important;}</style>", unsafe_allow_html=True)
        with open("components/renovation.html", "r") as f:
            map_html = f.read()
            components.html(map_html, height=1000, scrolling=True)

    if col5.button("Плотность населения| Тығыздық", key="btn5"):
        st.markdown("<style>.css-1y4p8pa {width: 100% !important; margin: 0 !important;}</style>", unsafe_allow_html=True)
        with open("components/density.html", "r") as f:
            map_html = f.read()
            components.html(map_html, height=1000, scrolling=True)

    if col6.button("Демография | Демография", key="btn6"):
        st.markdown("<style>.css-1y4p8pa {width: 100% !important; margin: 0 !important;}</style>", unsafe_allow_html=True)
        with open("components/demographics.html", "r") as f:
            map_html = f.read()
            components.html(map_html, height=1000, scrolling=True)

    if col7.button("Спрос и предложение | Сұраныс пен ұсыныс", key="btn7"):
        st.markdown("<style>.css-1y4p8pa {width: 100% !important; margin: 0 !important;}</style>", unsafe_allow_html=True)
        with open("components/supply_demand.html", "r") as f:
            map_html = f.read()
            components.html(map_html, height=1000, scrolling=True)

    if col8.button("Привлекательность участков | Тартымдылық", key="btn8"):
        st.markdown("<style>.css-1y4p8pa {width: 100% !important; margin: 0 !important;}</style>", unsafe_allow_html=True)
        with open("components/attractiveness.html", "r") as f:
            map_html = f.read()
            components.html(map_html, height=1000, scrolling=True)

    # Adding footer
    st.markdown('<div class="footer-container"></div>', unsafe_allow_html=True)
    st.markdown('<div class="footer-container"></div>', unsafe_allow_html=True)

    # Footer button with link to Situation Center
    st.markdown('<div class="footer-button"><a href="https://demo.opendata.smartalmaty.kz/" target="_blank"><button>Ситуационный центр</button></a></div>', unsafe_allow_html=True)

    with st.sidebar:
        with open("data/comp.json", "r", errors='ignore') as f:
            data = json.load(f)
        st_lottie(data)

if __name__ == "__main__":
    app()
