import streamlit as st
import requests

API_KEY = "14a03d89cabbd7f6529b416e8005d054"
BASE_URL = f"https://api.openweathermap.org/data/2.5/weather?appid={API_KEY}&units=metric"

st.set_page_config(
    page_title="Weather Forecast App",
    page_icon="☀️"
)

st.title("☀️ Weather Forecast App")
st.markdown("This app will take a city name as input and display real-time weather data.")
st.markdown("---")


city = st.text_input("Enter City Name:", placeholder="e.g. New York")

if st.button("Get Weather"):
    if city:
        try:
            
            final_url = f"{BASE_URL}&q={city}"
            
            
            response = requests.get(final_url)
            data = response.json()
            
    
            if data['cod'] == 200:
                
                main_data = data['main']
                weather_desc = data['weather'][0]['description']
                
                st.subheader(f"Weather in {city.title()}")
                st.write(f"**Temperature:** {main_data['temp']} °C")
                st.write(f"**Feels Like:** {main_data['feels_like']} °C")
                st.write(f"**Humidity:** {main_data['humidity']}%")
                st.write(f"**Condition:** {weather_desc.title()}")
            else:
                st.error(f"⚠️ City not found. Please check spelling.")

        except requests.exceptions.RequestException as e:
            st.error(f"❌ An error occurred during the API request: {e}")
            
    else:
        st.warning("Please enter a city name.")