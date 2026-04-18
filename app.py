import streamlit as st
import pandas as pd
st.set_page_config(page_title="CET Cutoff Analyzer", layout="centered")
st.title("🎓 CET Cutoff Analyzer (3 Years)")
df = pd.read_csv("data.csv")
st.sidebar.header("Filter Options")
college = st.sidebar.selectbox(
    "Select College",
    sorted(df["College"].unique())
)
course = st.sidebar.selectbox(
    "Select Branch",
    sorted(df["Course"].unique())
)
filtered = df[
    (df["College"] == college) &
    (df["Course"] == course)
]

result = filtered.sort_values(by="Year", ascending=False).head(3)

st.subheader(f"📊 Cutoff for {college} - {course}")
st.dataframe(result, use_container_width=True)

st.subheader("📈 Cutoff Trend")
chart_data = result.sort_values("Year")
st.line_chart(chart_data.set_index("Year")["Cutoff"])

st.download_button(
    "📥 Download CSV",
    result.to_csv(index=False),
    "cutoff_result.csv",
    "text/csv"
)

if result.empty:
    st.warning("No data found for selected filters")
