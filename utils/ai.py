import google.generativeai as genai

genai.configure(api_key="AIzaSyCT6eoTg9vCs6y0NudVlBDAwDbx9cPHj34")

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
    response = model.generate_content([system_prompt, prompt])
    return response.text.strip()
