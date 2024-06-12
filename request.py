from openai import OpenAI
import setting

client = OpenAI(
    api_key=setting.token,
    base_url="https://api.proxyapi.ru/openai/v1"
)

def request_gpt(text):
  chat_completion = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages= [{"role": "user", "content": text}],
    max_tokens=300
  )

  return chat_completion.choices[0].message.content