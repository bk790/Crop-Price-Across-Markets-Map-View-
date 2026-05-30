import streamlit as st
import pandas as pd
import pydeck as pdk
from deep_translator import GoogleTranslator

# ---------------------------
# Sample Crop Market Data
# ---------------------------
data = pd.DataFrame({
    "market": ["Kolar Market", "Mysore Market", "Bangalore Market", "Tumkur Market"],
    "crop": ["Rice", "Wheat", "Maize", "Millets"],
    "price_per_quintal": [2200, 2400, 1800, 2600],
    "lat": [13.1361, 12.2958, 12.9716, 13.3379],
    "lon": [78.1297, 76.6394, 77.5946, 77.1173]
})

st.title("🌾 Crop Prices Across Markets (Map View)")

# Language selection
languages = {
    "English": "en",
    "Hindi": "hi",
    "Kannada": "kn",
    "Tamil": "ta",
    "Telugu": "te"
}

lang_choice = st.selectbox("Choose Language", list(languages.keys()))
lang_code = languages[lang_choice]

translator = GoogleTranslator(source="auto", target=lang_code)

def translate(text):
    if lang_code == "en":
        return text
    return translator.translate(text)

# Translate dataframe text
data_display = data.copy()
data_display["market"] = data_display["market"].apply(translate)
data_display["crop"] = data_display["crop"].apply(translate)

st.subheader("📊 Market Prices Table")
st.dataframe(data_display)

# ---------------------------
# Map
# ---------------------------
st.subheader("🗺️ Market Price Map")

layer = pdk.Layer(
    "ScatterplotLayer",
    data=data,
    get_position='[lon, lat]',
    get_color='[0, 200, 0, 160]',
    get_radius=5000,
    pickable=True
)

view_state = pdk.ViewState(
    latitude=12.9,
    longitude=77.5,
    zoom=6,
    pitch=0
)

tooltip = {
    "html": "<b>Market:</b> {market}<br/>"
            "<b>Crop:</b> {crop}<br/>"
            "<b>Price:</b> ₹{price_per_quintal}/quintal",
    "style": {"backgroundColor": "black", "color": "white"}
}

st.pydeck_chart(pdk.Deck(
    layers=[layer],
    initial_view_state=view_state,
    tooltip=tooltip
))

# ---------------------------
# Filter Section
# ---------------------------
st.subheader("🔍 Filter")

crop_filter = st.selectbox("Select Crop", ["All"] + list(data["crop"].unique()))

filtered = data if crop_filter == "All" else data[data["crop"] == crop_filter]

st.write("Filtered Data")
st.dataframe(filtered)