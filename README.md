# AI SQL Assistant (Streamlit App)

This app allows users to log in and interact with a sample database using natural language. It uses Google Gemini to convert queries into SQL and displays the results with graphs and insights.

## Features
- Secure user login
- Natural language to SQL conversion
- Data visualizations
- Sample employee database (SQLite)

## Run Locally

```bash
pip install -r requirements.txt
python database/create_sample_db.py
streamlit run app.py
```

## Environment Variables

Create a `.streamlit/secrets.toml` file (not committed):

```toml
GOOGLE_API_KEY = "your-google-api-key"
```

For Streamlit Cloud, set this in **Settings > Secrets** as:

```toml
GOOGLE_API_KEY = "your-google-api-key"
```
