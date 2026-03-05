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

# Project Overview

This project analyzes Electric Vehicle (EV) charging station data using **data mining techniques** to uncover usage patterns, station performance, and abnormal behaviors.

The goal is to use artificial intelligence and data analytics techniques to help improve EV charging infrastructure and decision-making for charging station providers.

The project applies several data mining methods including:

* Data preprocessing
* Exploratory data analysis (EDA)
* Clustering analysis
* Association rule mining
* Anomaly detection
* Interactive dashboard visualization using Streamlit

---

# Dataset Description

The dataset contains information about EV charging stations including:

* Station ID
* Latitude and Longitude
* Charger Type
* Charging Capacity
* Charging Cost (USD/kWh)
* Distance to City
* Usage Statistics (Average users per day)
* Station Operator
* Renewable Energy Source
* Reviews / Ratings

This data helps analyze station demand, efficiency, and usage patterns.

---

# Data Preprocessing

Before analysis, the dataset was cleaned and prepared.

The preprocessing steps include:

* Handling missing values
* Filtering dataset values using user controls
* Scaling numerical data using **StandardScaler**
* Converting categorical variables into binary variables for association rule mining

These steps ensure the dataset is ready for machine learning analysis.

---

# Exploratory Data Analysis (EDA)

Several visualizations were created to better understand the dataset.

Examples include:

* Histogram showing EV charging demand distribution
* Scatter plot comparing charging cost and station usage
* Correlation heatmap for numerical features

EDA helps identify trends, patterns, and relationships in the data.

---

# Clustering Analysis

The **K-Means clustering algorithm** was used to group EV charging stations based on usage patterns.

Features used for clustering:

* Average users per day
* Charging cost
* Charging capacity
* Distance to city

This clustering identifies groups of stations such as:

* High demand stations
* Moderate demand stations
* Low usage stations

These insights help understand different station usage behaviors.

---

# Anomaly Detection

**Isolation Forest** was used to detect unusual or abnormal stations.

Anomalies may represent:

* Stations with unusually high demand
* Stations with extremely low usage
* Possible technical issues
* Potential data errors

Detecting anomalies helps improve monitoring and maintenance of charging infrastructure.

---

# Association Rule Mining

Association rule mining was implemented using the **Apriori algorithm**.

This technique identifies relationships between station characteristics.

Example insights include:

* Certain charger types may correlate with higher usage
* Renewable energy stations may attract more users

The algorithm evaluates rules using:

* Support
* Confidence
* Lift

---

# Streamlit Dashboard Features

The project includes a fully interactive **Streamlit dashboard**.

Main features include:

* Dataset preview
* Interactive filtering
* Exploratory data visualizations
* Clustering analysis
* Anomaly detection
* Association rule mining
* Interactive EV charging station map
* Station ranking and insights
* Download processed dataset

The dashboard allows users to explore EV charging patterns interactively.

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

This project uses several Python libraries:

* Streamlit
* Pandas
* NumPy
* Matplotlib
* Seaborn
* Plotly
* Scikit-learn
* MLxtend
* Folium

These tools support data analysis, machine learning, and interactive visualization.

---

# Key Insights

Some key insights obtained from the analysis include:

* Certain charging stations show significantly higher demand.
* Charging cost influences the number of users.
* Geographic location plays a major role in charging demand.
* Some stations show abnormal patterns requiring further investigation.

These insights can support better EV infrastructure planning.

---

# References

Data Visualization Resources
https://www.data-to-viz.com/

K-Means Clustering Explanation
https://neptune.ai/blog/k-means-clustering

Association Rule Mining Guide
https://www.analyticsvidhya.com/blog/2021/10/a-comprehensive-guide-on-market-basket-analysis/

Anomaly Detection Techniques
https://www.datacamp.com/courses/anomaly-detection-in-python
