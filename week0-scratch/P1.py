from openai import OpenAI

client = OpenAI()

user_prompt = input("Promp: ")
system_prompt = "Limit your answer to one sentence. Pretend youre a cat."

response = client.responses.create(
    input=prompt,
    instructions=system_prompt,
    model="gpt-5"
)

print(response.output_text)
