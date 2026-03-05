# ⚡ SmartCharging Analytics – EV Charging Behavior Analysis

## Student Information

**Student Name:** Dwij Vala 

**Student ID:** 2505369 

**CRS:** Artificial Intelligence 

**Course:** Data Mining 

**School:** Udgam School for Children 

---

# Project Title

**Mining the Future: SmartCharging Analytics – Uncovering EV Behavior Patterns**

---

# Streamlit Application

The project is deployed as an interactive web application using **Streamlit Cloud**.

### Live Application Link

https://ev-charging-analytics.streamlit.app/

This dashboard allows users to explore EV charging data, visualize usage patterns, detect anomalies, and understand charging behavior across stations.

---

# Project Scope and Objectives

Electric vehicles are becoming increasingly popular worldwide, making efficient charging infrastructure critical. This project analyzes EV charging station data to identify patterns in station usage and operational performance.

### Objectives

* Understand EV charging demand patterns
* Analyze relationships between charging cost and station usage
* Identify groups of charging stations with similar behavior using clustering
* Detect unusual charging stations through anomaly detection
* Discover hidden relationships between station characteristics using association rule mining
* Present insights through an interactive Streamlit dashboard

---

# Dataset Description

The dataset used in this project contains detailed information about EV charging stations, including:

* Station ID
* Latitude and Longitude
* Charger Type
* Charging Capacity (kW)
* Cost (USD/kWh)
* Distance to City (km)
* Average Usage Statistics (Users per Day)
* Station Operator
* Renewable Energy Source
* Reviews / Ratings

These variables help analyze station demand, operational efficiency, and charging behavior.

---

# Data Preparation and Preprocessing

Before performing analysis, the dataset was cleaned and prepared.

### Steps Performed

* Handling missing values
* Filtering and validating dataset entries
* Scaling numerical features using **StandardScaler**
* Converting categorical variables to binary values for association rule mining

These preprocessing steps ensure that the dataset is suitable for machine learning algorithms and data mining techniques.

---

# Exploratory Data Analysis (EDA)

Exploratory Data Analysis was performed to understand trends and relationships within the dataset.

### Visualizations Created

* Histogram of charging station demand
* Scatter plot of charging cost vs usage
* Correlation heatmap of numerical variables

EDA helps reveal patterns and insights before applying advanced machine learning techniques.

---

# Clustering Analysis

The **K-Means clustering algorithm** was used to group charging stations based on similar usage characteristics.

### Features Used for Clustering

* Usage statistics (average users per day)
* Charging cost
* Charging capacity
* Distance to city

### Insights from Clustering

The algorithm identified different groups of stations such as:

* High demand charging stations
* Medium usage stations
* Low demand stations

This segmentation helps understand station utilization patterns.

---

# Anomaly Detection

The **Isolation Forest algorithm** was applied to detect abnormal charging stations.

### Possible Anomalies

* Stations with unusually high demand
* Stations with extremely low usage
* Possible technical or operational issues

Anomaly detection helps identify potential problems within the charging network.

---

# Association Rule Mining

Association rule mining was performed using the **Apriori algorithm** to identify relationships between station characteristics.

### Metrics Used

* Support
* Confidence
* Lift

### Example Insights

* Certain charger types may correlate with higher demand
* Stations with renewable energy may attract more users

Association rules help uncover hidden relationships within the dataset.

---

# Streamlit Dashboard Features

The Streamlit application provides an interactive interface for exploring the analysis.

### Dashboard Features

* Dataset preview
* Interactive filters
* Exploratory data visualizations
* Clustering analysis
* Anomaly detection
* Association rule mining
* Interactive EV charging station map
* Station ranking and insights
* Download processed dataset

The dashboard enables users to explore EV charging patterns dynamically.

---

# Repository Structure

```
IDAI105-2505369-DwijVala
│
├── ev_charging_analytics_app.py
├── requirements.txt
├── EV_Charging_Stations.csv
├── README.md
```

---

# Technologies Used

This project was implemented using the following technologies:

* Python
* Streamlit
* Pandas
* NumPy
* Matplotlib
* Seaborn
* Plotly
* Scikit-learn
* MLxtend
* Folium

These tools enable data analysis, machine learning, and interactive visualization.

---

# Key Insights

Key findings from the analysis include:

* Some charging stations experience significantly higher usage compared to others.
* Charging cost can influence user demand.
* Geographic location plays an important role in station utilization.
* Certain stations show unusual behavior that may require further investigation.

These insights can help optimize EV charging infrastructure planning.

---

# References

Data Visualization Resources
https://www.data-to-viz.com/

K-Means Clustering Guide
https://neptune.ai/blog/k-means-clustering

Association Rule Mining Guide
https://www.analyticsvidhya.com/blog/2021/10/a-comprehensive-guide-on-market-basket-analysis/

Anomaly Detection Techniques
https://www.datacamp.com/courses/anomaly-detection-in-python
