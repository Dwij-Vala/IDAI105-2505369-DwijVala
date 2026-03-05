import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
from sklearn.ensemble import IsolationForest

from mlxtend.frequent_patterns import apriori, association_rules

import folium
from streamlit_folium import st_folium

# ----------------------------------------------------
# PAGE CONFIG
# ----------------------------------------------------

st.set_page_config(
    page_title="SmartCharging Analytics",
    layout="wide"
)

st.title("⚡ SmartCharging Analytics Dashboard")
st.caption("Data Mining Project – EV Charging Behavior Analysis")

# ----------------------------------------------------
# FILE UPLOAD
# ----------------------------------------------------

st.sidebar.header("Upload Dataset")

uploaded_file = st.sidebar.file_uploader(
    "Upload EV Charging Dataset (CSV)",
    type=["csv"]
)

if uploaded_file is None:
    st.info("Please upload your EV charging dataset.")
    st.stop()

df = pd.read_csv(uploaded_file)

# ----------------------------------------------------
# FILTERS
# ----------------------------------------------------

st.sidebar.header("Filters")

numeric_columns = df.select_dtypes(include=np.number).columns

if len(numeric_columns) > 0:

    selected_column = st.sidebar.selectbox(
        "Select numeric column to filter",
        numeric_columns
    )

    min_val = float(df[selected_column].min())
    max_val = float(df[selected_column].max())

    selected_range = st.sidebar.slider(
        "Range",
        min_val,
        max_val,
        (min_val, max_val)
    )

    df = df[
        (df[selected_column] >= selected_range[0]) &
        (df[selected_column] <= selected_range[1])
    ]

# ----------------------------------------------------
# DASHBOARD TABS
# ----------------------------------------------------

tab1, tab2, tab3, tab4, tab5 = st.tabs([
    "📊 Overview",
    "📈 Data Analysis",
    "🔍 Clustering & Anomalies",
    "🔗 Association Rules",
    "🗺 Map & Insights"
])

# ----------------------------------------------------
# OVERVIEW TAB
# ----------------------------------------------------

with tab1:

    st.subheader("Dataset Preview")

    st.dataframe(df.head())

    col1, col2, col3 = st.columns(3)

    if "Usage Stats (avg users/day)" in df.columns:
        avg_usage = df["Usage Stats (avg users/day)"].mean()
        col1.metric("Average Daily Users", round(avg_usage,2))

    if "Cost (USD/kWh)" in df.columns:
        avg_cost = df["Cost (USD/kWh)"].mean()
        col2.metric("Average Charging Cost", round(avg_cost,2))

    col3.metric("Total Stations", len(df))

# ----------------------------------------------------
# DATA ANALYSIS TAB
# ----------------------------------------------------

with tab2:

    st.subheader("Exploratory Data Analysis")

    if "Usage Stats (avg users/day)" in df.columns:

        fig = px.histogram(
            df,
            x="Usage Stats (avg users/day)",
            title="Usage Distribution"
        )

        st.plotly_chart(fig, use_container_width=True)

    if "Cost (USD/kWh)" in df.columns and "Usage Stats (avg users/day)" in df.columns:

        fig = px.scatter(
            df,
            x="Cost (USD/kWh)",
            y="Usage Stats (avg users/day)",
            title="Cost vs Usage"
        )

        st.plotly_chart(fig, use_container_width=True)

    numeric_cols = df.select_dtypes(include=np.number).columns

    if len(numeric_cols) > 0:

        st.subheader("Correlation Heatmap")

        fig, ax = plt.subplots(figsize=(10,6))
        sns.heatmap(df[numeric_cols].corr(), cmap="coolwarm", ax=ax)

        st.pyplot(fig)

# ----------------------------------------------------
# CLUSTERING + ANOMALY TAB
# ----------------------------------------------------

with tab3:

    st.subheader("Clustering Analysis")

    cluster_features = []

    for col in [
        "Usage Stats (avg users/day)",
        "Cost (USD/kWh)",
        "Charging Capacity (kW)",
        "Distance to City (km)"
    ]:
        if col in df.columns:
            cluster_features.append(col)

    if len(cluster_features) >= 2:

        X = df[cluster_features]

        scaler = StandardScaler()
        X_scaled = scaler.fit_transform(X)

        kmeans = KMeans(n_clusters=3, random_state=42)

        df["Cluster"] = kmeans.fit_predict(X_scaled)

        fig = px.scatter(
            df,
            x=cluster_features[0],
            y=cluster_features[1],
            color="Cluster",
            title="Cluster Visualization"
        )

        st.plotly_chart(fig, use_container_width=True)

    else:
        st.warning("Not enough columns available for clustering")

    st.subheader("Anomaly Detection")

    if len(cluster_features) >= 2:

        model = IsolationForest(contamination=0.05)

        df["Anomaly"] = model.fit_predict(df[cluster_features])

        anomalies = df[df["Anomaly"] == -1]

        st.write("Detected Anomalies")

        st.dataframe(anomalies)

# ----------------------------------------------------
# ASSOCIATION RULES TAB
# ----------------------------------------------------

with tab4:

    st.subheader("Association Rule Mining")

    categorical_df = df.select_dtypes(include="object")

    if not categorical_df.empty:

        binary_df = pd.get_dummies(categorical_df)

        freq_items = apriori(binary_df, min_support=0.1, use_colnames=True)

        if not freq_items.empty:

            rules = association_rules(
                freq_items,
                metric="confidence",
                min_threshold=0.5
            )

            st.dataframe(rules.head(20))

        else:
            st.info("No association rules found")

    else:
        st.info("Dataset has no categorical columns for rule mining")

# ----------------------------------------------------
# MAP + INSIGHTS TAB
# ----------------------------------------------------

with tab5:

    st.subheader("Charging Station Map")

    if "Latitude" in df.columns and "Longitude" in df.columns:

        m = folium.Map(
            location=[df["Latitude"].mean(), df["Longitude"].mean()],
            zoom_start=5
        )

        for _, row in df.iterrows():

            popup_text = f"""
            Station ID: {row.get('Station ID','N/A')} <br>
            Usage: {row.get('Usage Stats (avg users/day)','N/A')} <br>
            Cost: {row.get('Cost (USD/kWh)','N/A')}
            """

            folium.CircleMarker(
                location=[row["Latitude"], row["Longitude"]],
                radius=6,
                popup=popup_text,
                color="blue",
                fill=True
            ).add_to(m)

        st_folium(m, width=900)

    else:
        st.warning("Latitude and Longitude columns are required for map")

    st.subheader("Top Stations")

    if "Usage Stats (avg users/day)" in df.columns:

        top = df.sort_values(
            by="Usage Stats (avg users/day)",
            ascending=False
        ).head(10)

        st.dataframe(top)

    st.subheader("Recommendations")

    st.markdown("""
    - Expand EV stations in high demand areas  
    - Install fast chargers where usage is highest  
    - Reduce charging cost in low demand stations  
    - Monitor anomaly stations for maintenance issues  
    """)

# ----------------------------------------------------
# DOWNLOAD DATA
# ----------------------------------------------------

st.header("Download Processed Data")

csv = df.to_csv(index=False).encode("utf-8")

st.download_button(
    "Download Dataset",
    data=csv,
    file_name="ev_analysis.csv",
    mime="text/csv"
)