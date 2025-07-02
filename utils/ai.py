import os
import google.generativeai as genai

# Configure with secure API key
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

def natural_to_sql(prompt):
    model = genai.GenerativeModel("gemini-pro")
    system_prompt = '''
You are an expert data analyst. Convert the following natural language question into a SQL query for a SQLite database with a table called 'employees' having columns:
- id (int)
- name (text)
- department (text)
- salary (int)
- join_date (text: YYYY-MM-DD)

Only return the SQL query without explanation.
'''
    full_prompt = f"{system_prompt.strip()}\n{prompt.strip()}"
    response = model.generate_content(full_prompt)
    return response.text.strip()
