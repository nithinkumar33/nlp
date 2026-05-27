from openai import OpenAI

client = OpenAI(api_key="sk-5678ijkl1234mnop5678ijkl1234mnop5678ijkl")

response = client.responses.create(
    model="gpt-4.1-mini",
    input="Explain Natural Language Processing",
    max_output_tokens=50
)

print(response.output[0].content[0].text)