import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
from scipy.interpolate import make_interp_spline

# Embedded data
speed_range = np.arange(10, 41, 1)
label_size_range = np.arange(10, 56, 1)

# Generate feasibility data
records = []
max_speed = 40
max_ramp_time_ms = 80
roller_diameter_mm = 54
gear_ratio = 2.454545454545455
steps_per_rev = 200 * 16

for speed in speed_range:
    ramp_time = (speed / max_speed) * max_ramp_time_ms
    ramp_distance = (speed * 1000 / 60) * (ramp_time / 1000)
    for label in label_size_range:
        feasible = int(label >= ramp_distance)
        records.append({
            "Speed (m/min)": speed,
            "Label Size (mm)": label,
            "Ramp Time (ms)": ramp_time,
            "Ramp Distance (mm)": ramp_distance,
            "Feasible": feasible
        })

# Create DataFrame
feas_df = pd.DataFrame.from_records(records)
pivot_table = feas_df.pivot(index="Label Size (mm)", columns="Speed (m/min)", values="Feasible")

# Streamlit UI
st.set_page_config(layout="wide")
st.title("Label Feasibility Explorer")

# Tabs for simplified interface
tab1, tab2 = st.tabs(["Line Chart", "Heatmap"])

with tab1:
    st.header("Smoothed Minimum Feasible Label Size vs Speed")
    line_df = feas_df[feas_df['Feasible'] == 1].groupby("Speed (m/min)")["Label Size (mm)"].min().reset_index()

    # Interpolate for smoother curve
    speeds = line_df["Speed (m/min)"].values
    min_labels = line_df["Label Size (mm)"].values
    speeds_smooth = np.linspace(speeds.min(), speeds.max(), 300)
    spline = make_interp_spline(speeds, min_labels, k=3)
    labels_smooth = spline(speeds_smooth)

    fig = px.line(x=speeds_smooth, y=labels_smooth, labels={'x': 'Speed (m/min)', 'y': 'Min Feasible Label Size (mm)'})
    fig.update_traces(mode='lines+markers')
    fig.update_layout(title="Smoothed Curve of Feasible Label Size vs Speed")
    st.plotly_chart(fig, use_container_width=True)

with tab2:
    st.header("Feasibility Heatmap")
    fig = px.imshow(pivot_table.values,
                    labels=dict(x="Speed (m/min)", y="Label Size (mm)", color="Feasible"),
                    x=speed_range,
                    y=label_size_range,
                    color_continuous_scale=["#FF4C4C", "#56FF56"],
                    aspect="auto")
    fig.update_layout(title="Label Feasibility Heatmap",
                      xaxis_title="Speed (m/min)",
                      yaxis_title="Label Size (mm)")
    st.plotly_chart(fig, use_container_width=True)
