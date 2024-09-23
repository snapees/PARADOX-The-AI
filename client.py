# from openai import OpenAI
 
# # pip install openai 
# # if you saved the key under a different environment variable name, you can do something like:
# client = OpenAI(
#   api_key="sk-proj-I8tYJjqrKv2HK1qkaKKiT3BlbkFJHVx3eMicmoae84VPlrgc",
# )

# completion = client.chat.completions.create(
#   model="gpt-3.5-turbo",
#   messages=[
#     {"role": "system", "content": "You are a virtual assistant named jarvis skilled in general tasks like Alexa and Google Cloud"},
#     {"role": "user", "content": "what is coding"}
#   ]
# )

# print(completion.choices[0].message.content)


import google.generativeai as genai
genai.configure(api_key="AIzaSyCL9bYuCTUK_T4DrgkolILkIb50L51Tx94")
generation_config = {
  "temperature": 1,
  "top_p": 0.95,
  "top_k": 64,
  "max_output_tokens": 8192,
  "response_mime_type": "text/plain",
}
model = genai.GenerativeModel(
  model_name="gemini-1.5-flash",
  generation_config=generation_config,
  # safety_settings = Adjust safety settings
  # See https://ai.google.dev/gemini-api/docs/safety-settings
)
chat_session = model.start_chat(history=[])

response = chat_session.send_message("who is hritik roshan")

print(response.text)