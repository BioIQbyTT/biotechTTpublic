import streamlit as st
import pandas as pd
from modules.ai_recommender import get_top_recommendations
from modules.company_view import show_company_details
from modules.universe import load_universe

st.set_page_config(page_title="Tiny Teams Biotech", layout="wide")

st.title("🔬 Tiny Teams Biotech AI Dashboard")

tab1, tab2 = st.tabs(["🏠 Top 5 AI Picks", "📋 Full Company List"])

with tab1:
    st.subheader("Top 5 Buy Recommendations (AI-Generated)")
    top_df = get_top_recommendations()
    st.dataframe(top_df, use_container_width=True)

with tab2:
    st.subheader("Browse Biotech Universe (600+ companies)")
    universe_df = load_universe()
    selected = st.selectbox("Select a Company", universe_df["Ticker"])
    if selected:
        show_company_details(selected)

import pandas as pd

def get_top_recommendations():
    df = pd.read_csv("data/company_scores.csv")
    top5 = df.sort_values("AI_Score", ascending=False).head(5)
    return top5[["Ticker", "Company", "AI_Score"]]

import pandas as pd

def load_universe():
    df = pd.read_csv("data/company_scores.csv")
    return df

import streamlit as st
import pandas as pd

def show_company_details(ticker):
    df = pd.read_csv("data/company_scores.csv")
    row = df[df["Ticker"] == ticker].iloc[0]

    st.markdown(f"### {row['Company']} ({row['Ticker']})")
    st.metric("AI Score", row["AI_Score"])
    st.metric("Market Cap ($M)", row["MarketCap"])

    st.subheader("📢 Press Releases")
    press_df = pd.read_csv("data/press_releases.csv")
    prs = press_df[press_df["Ticker"] == ticker]
    st.dataframe(prs[["Date", "Headline"]])

    st.subheader("🧪 Trial Score")
    st.write(f"Score: {row['TrialScore']}")

    st.subheader("📅 Catalyst Events")
    st.write(f"Next Event: {row['NextCatalyst']}")

    st.subheader("💰 Valuation Benchmark")
    st.write(f"Valuation Benchmark: {row['ValuationComp']}")

Ticker,Company,AI_Score,TrialScore,NextCatalyst,ValuationComp,MarketCap
NUVL,Nuvalent,92,85,"Q3 readout","Turning Point acquisition",3000
MRUS,Merus,89,83,"ASCO 2025","Bicara comps",1800
...

streamlit run app.py
