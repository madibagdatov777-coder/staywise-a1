
import streamlit as st
import pandas as pd
from urllib.parse import quote

st.set_page_config(
    page_title="StayWise AI",
    page_icon="🌍",
    layout="wide"
)

hotels = [
    ["ibis budget Paris Porte de Montmartre","Paris","France","Europe",55,7.2],
    ["Generator Paris","Paris","France","Europe",65,8.0],
    ["easyHotel London Victoria","London","United Kingdom","Europe",75,7.1],
    ["Premier Inn London City","London","United Kingdom","Europe",95,8.4],
    ["a&o Berlin Mitte","Berlin","Germany","Europe",35,7.5],
    ["ibis budget Berlin Alexanderplatz","Berlin","Germany","Europe",60,7.8],
    ["Motel One Amsterdam","Amsterdam","Netherlands","Europe",105,8.5],
    ["MEININGER Amsterdam City West","Amsterdam","Netherlands","Europe",70,8.1],
    ["Hostel One Prague","Prague","Czech Republic","Europe",30,8.8],
    ["B&B Hotel Roma San Lorenzo","Rome","Italy","Europe",65,7.9],
    ["Ostello Bello Milano","Milan","Italy","Europe",40,9.0],
    ["Hotel Lisboa","Lisbon","Portugal","Europe",55,8.0],
    ["Safestay Barcelona Passeig de Gracia","Barcelona","Spain","Europe",45,8.1],
    ["Atenea Barcelona","Barcelona","Spain","Europe",75,8.3],
    ["Citybox Oslo","Oslo","Norway","Europe",85,8.2],
    ["Scandic Go Stockholm","Stockholm","Sweden","Europe",90,8.0],
    ["Danhostel Copenhagen City","Copenhagen","Denmark","Europe",45,8.0],
    ["Maverick City Lodge","Budapest","Hungary","Europe",35,8.7],
    ["Hotel Fortuna","Krakow","Poland","Europe",40,8.1],
    ["Hotel Cosmos","Athens","Greece","Europe",45,8.0],
    ["Hotel Boss","Singapore","Singapore","Asia",75,7.8],
    ["YOTEL Singapore Orchard Road","Singapore","Singapore","Asia",100,8.2],
    ["The Pod Boutique Capsule Hotel","Singapore","Singapore","Asia",55,8.0],
    ["Lub d Bangkok Siam","Bangkok","Thailand","Asia",30,8.5],
    ["ibis Bangkok Riverside","Bangkok","Thailand","Asia",45,8.1],
    ["Red Planet Bangkok Asoke","Bangkok","Thailand","Asia",28,7.7],
    ["The Millennials Kyoto","Kyoto","Japan","Asia",45,8.8],
    ["Sakura Hotel Ikebukuro","Tokyo","Japan","Asia",50,8.0],
    ["Hotel Mystays Asakusa","Tokyo","Japan","Asia",55,7.9],
    ["Nine Tree Hotel Myeongdong","Seoul","South Korea","Asia",65,8.3],
    ["Toyoko Inn Seoul Dongdaemun","Seoul","South Korea","Asia",55,8.1],
    ["Zostel Mumbai","Mumbai","India","Asia",18,8.2],
    ["Bloomrooms @ New Delhi Railway Station","New Delhi","India","Asia",30,8.0],
    ["The Hosteller Goa","Goa","India","Asia",20,8.4],
    ["Citymax Hotel Bur Dubai","Dubai","UAE","Asia",50,7.5],
    ["Rove Downtown","Dubai","UAE","Asia",95,8.8],
    ["Wanderlust Hostel","Kuala Lumpur","Malaysia","Asia",18,8.0],
    ["The Chow Kit Hotel","Kuala Lumpur","Malaysia","Asia",40,8.3],
    ["Khaosan Tokyo Origami","Tokyo","Japan","Asia",35,8.5],
    ["Hotel 81 Chinatown","Singapore","Singapore","Asia",65,7.4],
    ["Pod 51 Hotel","New York","USA","North America",100,7.8],
    ["HI New York City Hostel","New York","USA","North America",55,8.5],
    ["Freehand Chicago","Chicago","USA","North America",75,8.0],
    ["Samesun Vancouver","Vancouver","Canada","North America",45,8.1],
    ["HI Toronto Hostel","Toronto","Canada","North America",40,8.0],
    ["Selina Cancun Laguna","Cancun","Mexico","North America",45,7.8],
    ["Hotel M Montreal","Montreal","Canada","North America",50,8.5],
    ["Viajero Miami","Miami","USA","North America",60,8.2],
    ["Che Lagarto Hostel","Rio de Janeiro","Brazil","South America",25,8.0],
    ["Viajero Buenos Aires Hostel","Buenos Aires","Argentina","South America",30,8.7]
]

df = pd.DataFrame(
    hotels,
    columns=["Hotel","City","Country","Continent","Price","Rating"]
)

st.markdown("""
<style>
.stApp {
    background: #0b1120;
    color: #f1f5f9;
}
header {visibility: hidden;}
.block-container {
    padding-top: 2rem;
    max-width: 1250px;
}
.hero {
    padding: 35px;
    border-radius: 22px;
    background: linear-gradient(120deg,#172554,#312e81,#164e63);
    margin-bottom: 25px;
}
.hero h1 {
    font-size: 43px;
    color: white;
    margin-bottom: 8px;
}
.hero p {color:#cbd5e1;font-size:17px;}
.hotel {
    background: #172033;
    border: 1px solid #29364d;
    border-radius: 15px;
    padding: 20px;
    margin-bottom: 17px;
}
.hotel h3 {color:#ffffff;font-size:19px;}
.price {color:#38bdf8;font-size:25px;font-weight:700;}
.info {color:#aab7cc;font-size:14px;}
.stButton button {
    background: #2563eb;
    color: white;
    border-radius: 9px;
    border: none;
}
</style>
""", unsafe_allow_html=True)

st.markdown("""
<div class="hero">
    <h1>🌍 StayWise AI</h1>
    <p>Find affordable hotels anywhere in the world.</p>
    <p>Discover 50 hotel options across multiple countries.</p>
</div>
""", unsafe_allow_html=True)

st.subheader("🔎 Find your hotel")

col1, col2, col3 = st.columns(3)

with col1:
    continents = ["All"] + sorted(df["Continent"].unique().tolist())
    continent = st.selectbox("Continent", continents)

with col2:
    countries = ["All"] + sorted(df["Country"].unique().tolist())
    country = st.selectbox("Country", countries)

with col3:
    city_search = st.text_input("City or hotel", placeholder="Enter city or hotel name")

col4, col5 = st.columns(2)

with col4:
    max_price = st.slider("Maximum price per night ($)", 10, 200, 100)

with col5:
    min_rating = st.slider("Minimum rating", 0.0, 10.0, 0.0, 0.5)

sort_option = st.selectbox(
    "Sort hotels",
    ["Cheapest first", "Most expensive first", "Highest rating"]
)

filtered = df.copy()

if continent != "All":
    filtered = filtered[filtered["Continent"] == continent]

if country != "All":
    filtered = filtered[filtered["Country"] == country]

if city_search:
    filtered = filtered[
        filtered["City"].str.contains(city_search, case=False, na=False) |
        filtered["Hotel"].str.contains(city_search, case=False, na=False)
    ]

filtered = filtered[
    (filtered["Price"] <= max_price) &
    (filtered["Rating"] >= min_rating)
]

if sort_option == "Cheapest first":
    filtered = filtered.sort_values("Price")
elif sort_option == "Most expensive first":
    filtered = filtered.sort_values("Price", ascending=False)
else:
    filtered = filtered.sort_values("Rating", ascending=False)

st.divider()

m1, m2, m3 = st.columns(3)

m1.metric("Hotels found", len(filtered))
m2.metric("Countries", filtered["Country"].nunique())
m3.metric(
    "Lowest price",
    f"${filtered['Price'].min()}" if not filtered.empty else "—"
)

st.subheader("🏨 Available hotel options")

if filtered.empty:
    st.warning("No hotels found. Change your filters.")
else:
    for start in range(0, len(filtered), 2):
        cols = st.columns(2)

        for j, (_, hotel) in enumerate(filtered.iloc[start:start+2].iterrows()):
            booking_url = (
                "https://www.google.com/travel/search?q=" +
                quote(f"{hotel['Hotel']} {hotel['City']} hotel")
            )

            with cols[j]:
                st.markdown(f"""
                <div class="hotel">
                    <h3>🏨 {hotel['Hotel']}</h3>
                    <div class="info">
                        📍 {hotel['City']}, {hotel['Country']}<br>
                        🌎 {hotel['Continent']}<br>
                        ⭐ Rating: {hotel['Rating']}/10
                    </div>
                    <br>
                    <div class="price">${hotel['Price']} / night</div>
                    <div class="info">Indicative demo price</div>
                </div>
                """, unsafe_allow_html=True)

                st.link_button(
                    "🔎 Find and book",
                    booking_url,
                    use_container_width=True
                )

st.divider()

st.caption(
    "StayWise AI © 2026 | Worldwide hotel discovery. "
    "Demo catalog: prices and ratings are illustrative, "
    "not live booking offers."
)
