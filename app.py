
import streamlit as st
import pandas as pd
import plotly.express as px
import pickle
from pathlib import Path
from prophet import Prophet
from utils import box_vertices, rotate_vertices, plot_box

BASE = Path(__file__).resolve().parent.parent
DATA_PATH = BASE / "data" / "settlement_log.csv"
MODEL_PATH = BASE / "models" / "prophet_model.pkl"

st.set_page_config(layout="wide", page_title="Settlement & Tilt Dashboard")

@st.cache_data(ttl=300)
def load_data():
    if DATA_PATH.exists():
        df = pd.read_csv(DATA_PATH, parse_dates=['timestamp']).sort_values('timestamp')
        return df
    else:
        return pd.DataFrame()

st.title("Real-Time Settlement & Tilt Monitoring Dashboard")

df = load_data()

if df.empty:
    st.warning("No data found. Please run data_generator.py first.")
else:
    st.subheader("Latest readings")
    st.dataframe(df.tail(10))

    # Settlement over time plot
    fig1 = px.line(df, x='timestamp', y='settlement_mm', title='Settlement Over Time')
    st.plotly_chart(fig1, use_container_width=True)

    # Tilt over time plot
    fig2 = px.line(df, x='timestamp', y=['tilt_x_deg', 'tilt_y_deg'], title='Tilt Over Time')
    st.plotly_chart(fig2, use_container_width=True)

    # Forecast settlement using Prophet
    if MODEL_PATH.exists():
        model = pickle.load(open(MODEL_PATH, "rb"))
        df_prophet = df.rename(columns={"timestamp": "ds", "settlement_mm": "y"})
        future = model.make_future_dataframe(periods=24)  # forecast next 24 hours
        forecast = model.predict(future)
        fig3 = px.line(forecast, x='ds', y='yhat', title='Settlement Forecast (Next 24 hours)')
        st.plotly_chart(fig3, use_container_width=True)
    else:
        st.warning("Prophet model not found. Please run train_models.py to create it.")

    # 3D building tilt visualization (using last recorded tilt)
    last = df.iloc[-1]
    verts = box_vertices(width=10, depth=10, height=30)
    tilted_verts = rotate_vertices(verts, last['tilt_x_deg']*10, last['tilt_y_deg']*10)  # scale tilt for visibility
    st.subheader("3D Building Tilt Visualization")
    fig4 = plot_box(tilted_verts)
    st.plotly_chart(fig4, use_container_width=True, height=500)
=======
import streamlit as st
import pandas as pd
import plotly.express as px
import pickle
from pathlib import Path
from prophet import Prophet
from utils import box_vertices, rotate_vertices, plot_box

BASE = Path(__file__).resolve().parent.parent
DATA_PATH = BASE / "data" / "settlement_log.csv"
MODEL_PATH = BASE / "models" / "prophet_model.pkl"

st.set_page_config(layout="wide", page_title="Settlement & Tilt Dashboard")

@st.cache_data(ttl=300)
def load_data():
    if DATA_PATH.exists():
        df = pd.read_csv(DATA_PATH, parse_dates=['timestamp']).sort_values('timestamp')
        return df
    else:
        return pd.DataFrame()

st.title("Real-Time Settlement & Tilt Monitoring Dashboard")

df = load_data()

if df.empty:
    st.warning("No data found. Please run data_generator.py first.")
else:
    st.subheader("Latest readings")
    st.dataframe(df.tail(10))

    # Settlement over time plot
    fig1 = px.line(df, x='timestamp', y='settlement_mm', title='Settlement Over Time')
    st.plotly_chart(fig1, use_container_width=True)

    # Tilt over time plot
    fig2 = px.line(df, x='timestamp', y=['tilt_x_deg', 'tilt_y_deg'], title='Tilt Over Time')
    st.plotly_chart(fig2, use_container_width=True)

    # Forecast settlement using Prophet
    if MODEL_PATH.exists():
        model = pickle.load(open(MODEL_PATH, "rb"))
        df_prophet = df.rename(columns={"timestamp": "ds", "settlement_mm": "y"})
        future = model.make_future_dataframe(periods=24)  # forecast next 24 hours
        forecast = model.predict(future)
        fig3 = px.line(forecast, x='ds', y='yhat', title='Settlement Forecast (Next 24 hours)')
        st.plotly_chart(fig3, use_container_width=True)
    else:
        st.warning("Prophet model not found. Please run train_models.py to create it.")

    # 3D building tilt visualization (using last recorded tilt)
    last = df.iloc[-1]
    verts = box_vertices(width=10, depth=10, height=30)
    tilted_verts = rotate_vertices(verts, last['tilt_x_deg']*10, last['tilt_y_deg']*10)  # scale tilt for visibility
    st.subheader("3D Building Tilt Visualization")
    fig4 = plot_box(tilted_verts)
    st.plotly_chart(fig4, use_container_width=True, height=500)
>>>>>>> ff6ed34b7f408d0d84bd0ff98a752dc382751fb8
