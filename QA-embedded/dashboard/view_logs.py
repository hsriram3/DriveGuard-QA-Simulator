import streamlit as st
import json

st.title("📊 Vehicle Log Dashboard")

with open("storage/logs.json", "r") as f:
    logs = json.load(f)

st.write("### Raw Logs")
st.json(logs)

st.write("### Speeds over Time")
for log in logs:
    st.write(f"{log['timestamp']} - {log['speed']} mph")