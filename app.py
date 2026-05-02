import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import folium
from streamlit_folium import st_folium
import time

from tsp import mst_tsp
from utils import haversine

st.title("🚚 Delivery Route Optimizer ")
# INPUT
uploaded_file = st.file_uploader("Upload CSV (lat, lon)", type=["csv"])

points = []
if uploaded_file:
    df = pd.read_csv(uploaded_file)
    st.dataframe(df)
    points = list(zip(df["lat"], df["lon"]))
else:
    st.info("Enter manually")

    num = st.number_input("Number of locations", 2, 20, 5)

    for i in range(num):
        lat = st.number_input(f"City {i} Latitude", key=f"lat{i}")
        lon = st.number_input(f"City {i} Longitude", key=f"lon{i}")
        points.append((lat, lon))


# -------------------------
# DISTANCE
# -------------------------
def total_distance(route, points):
    dist = 0
    for i in range(len(route) - 1):
        dist += haversine(points[route[i]], points[route[i+1]])
    dist += haversine(points[route[-1]], points[route[0]])
    return dist


# -------------------------
# GRAPH VISUALIZATION
# -------------------------
def plot_graph(points, route):
    fig, ax = plt.subplots()

    for i, (x, y) in enumerate(points):
        ax.scatter(x, y)
        ax.text(x+0.1, y+0.1, str(i))

    for i in range(len(route) - 1):
        x1, y1 = points[route[i]]
        x2, y2 = points[route[i+1]]
        ax.plot([x1, x2], [y1, y2])

    x1, y1 = points[route[-1]]
    x2, y2 = points[route[0]]
    ax.plot([x1, x2], [y1, y2])

    st.pyplot(fig)


# -------------------------
# ANIMATION (MOVING DOT)
# -------------------------
def animate(points, route):
    placeholder = st.empty()

    for i in range(len(route)):
        fig, ax = plt.subplots()

        # points
        for idx, (x, y) in enumerate(points):
            ax.scatter(x, y)
            ax.text(x+0.1, y+0.1, str(idx))

        # full route (light)
        for j in range(len(route)-1):
            x1, y1 = points[route[j]]
            x2, y2 = points[route[j+1]]
            ax.plot([x1, x2], [y1, y2], alpha=0.3)

        # return line
        x1, y1 = points[route[-1]]
        x2, y2 = points[route[0]]
        ax.plot([x1, x2], [y1, y2], alpha=0.3)

        # moving dot 🔵
        cx, cy = points[route[i]]
        ax.scatter(cx, cy, s=200, color="red")

        ax.set_title(f"Step {i+1}/{len(route)}")

        placeholder.pyplot(fig)
        time.sleep(1)


# -------------------------
# MAP
# -------------------------
def draw_map(points, route):
    m = folium.Map(location=points[0], zoom_start=13)

    for i, (lat, lon) in enumerate(points):
        folium.Marker([lat, lon], tooltip=f"City {i}").add_to(m)

    route_points = [points[i] for i in route]
    route_points.append(route_points[0])

    folium.PolyLine(route_points, color="blue", weight=3).add_to(m)

    return m


# -------------------------
# RUN
# -------------------------
if st.button("Find Route"):
    if len(points) < 2:
        st.error("Need at least 2 points")
    else:
        route = mst_tsp(points)

        st.success("Route Generated Successfully 🚚")

        st.write("Route:", route)

        # 📏 distance
        dist = total_distance(route, points)
        st.success(f"📏 Total Distance: {dist:.2f} km")

        st.subheader("📊 Graph View")
        plot_graph(points, route)

        st.subheader("🔵 Animation")
        animate(points, route)

        st.subheader("🗺️ Map View")
        m = draw_map(points, route)
        st_folium(m, width=700, height=500)