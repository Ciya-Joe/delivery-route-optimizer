# delivery-route-optimizer
Delivery Route Optimizer using TSP (MST-based approach with visualization)


# 🚚 Delivery Route Optimizer using Travelling Salesman Problem (TSP)

An interactive web-based application that optimizes delivery routes using graph algorithms and real-world distance calculations. This project demonstrates how the Travelling Salesman Problem (TSP) can be applied to logistics and transportation systems.

---

## 📌 Project Overview

Efficient route planning is crucial in logistics, food delivery, and courier services.  
This project provides a solution to find the shortest possible route that visits multiple locations exactly once and returns to the starting point.

The system uses an **MST-based approximation approach** to generate a near-optimal solution with reduced computational complexity.

---

## ✨ Features

- 📂 CSV-based location input (latitude & longitude)
- 🧮 Real-world distance calculation using Haversine formula
- 📍 Optimized route generation using MST + DFS
- 📊 Graph-based visualization of route
- 🗺️ Map-based visualization (OpenStreetMap via Folium)
- 🎞️ Animated route simulation
- ⚡ Interactive web interface using Streamlit

---

## 🛠️ Tech Stack

- **Python**
- **Streamlit**
- **NetworkX**
- **Matplotlib**
- **Folium**
- **Pandas**
- **NumPy**

---

## 🧠 Methodology

1. Accept input locations (CSV or manual entry)  
2. Calculate pairwise distances using Haversine formula  
3. Construct a complete weighted graph  
4. Generate Minimum Spanning Tree (MST)  
5. Apply Depth First Search (DFS) traversal  
6. Compute optimized route and total distance  
7. Visualize results using graphs and maps  

---

## 🏗️ System Architecture

Input → Data Processing → Distance Calculation → Graph Construction → MST + DFS Optimization → Output → Visualization

---

## 📊 Sample Output

- ✔ Optimized route sequence  
- ✔ Total travel distance  
- ✔ Graph visualization  
- ✔ Interactive map view  
- ✔ Animated route traversal  

*(Add screenshots here for better presentation)*

---

## ▶️ How to Run the Project

### 1️⃣ Clone the repository
```bash
git clone https://github.com/your-username/delivery-route-optimizer.git
cd delivery-route-optimizer
