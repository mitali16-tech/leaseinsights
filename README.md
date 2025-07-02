# AI SQL Assistant (Streamlit App)

This app allows users to log in and interact with a sample database using natural language. It uses OpenAI (or Google Gemini via API) to convert queries into SQL and displays the results with graphs and insights.

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

## Replace API Key
Edit `utils/ai.py` and replace `"your-google-api-key"` with your actual key.

## Example Questions
- What is the average salary per department?
- Show employees who joined after 2021.
- Who earns more than 65000?
