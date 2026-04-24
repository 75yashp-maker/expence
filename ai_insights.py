from groq import Groq
client = Groq(api_key="gsk_ZvvguEV06HpkWkJNQbzSWGdyb3FYcT5Pqnm9t03KzxbnwwnhpeC")

def generate_insights(df):
    summary= df.to_string()

    prompt = f"""
    analyze the following expense data and give insights:
    {summary}

    provide:
    - spending patterns
    - suggestions to save money
    """

    response = client.chat.completions.create(
        model= "openai/gpt-oss-120b",
        messages= [{"role":"user","content":prompt}]
    )
    return response.choices[0].message.content
