import streamlit as st
from utils.auth import login, check_login
from utils.ai import natural_to_sql
from utils.db import run_query
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="AI SQL Assistant", layout="wide")

if not check_login():
    login()
    st.stop()

st.title("🤖 AI SQL Assistant")
st.write(f"Welcome, **{st.session_state.user}**!")

prompt = st.text_area("Ask a question about your data:", height=100)
if st.button("Get Insights"):
    with st.spinner("Thinking..."):
        sql = natural_to_sql(prompt)
        st.code(sql, language='sql')

        result = run_query(sql)

        if isinstance(result, str) and result.startswith("Error"):
            st.error(result)
        else:
            st.dataframe(result)

            if "salary" in result.columns:
                fig = px.histogram(result, x="salary", title="Salary Distribution")
                st.plotly_chart(fig)

            if "department" in result.columns:
                fig = px.bar(result, x="department", y="salary", title="Salary by Department")
                st.plotly_chart(fig)
