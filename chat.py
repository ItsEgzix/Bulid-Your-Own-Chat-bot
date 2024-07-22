import os

import google.generativeai as genai

genai.configure(api_key="your API Key")


generation_config = {
  "temperature": 1,
  "top_p": 0.95,
  "top_k": 64,
  "max_output_tokens": 8192,
  "response_mime_type": "text/plain",
}
  # safety_settings = Adjust safety settings
  # See https://ai.google.dev/gemini-api/docs/safety-settings
model = genai.GenerativeModel(
  model_name="gemini-1.5-pro",
  generation_config=generation_config,
  safety_settings = [
    {"category": "HARM_CATEGORY_HARASSMENT", "threshold": "BLOCK_NONE"},
    {"category": "HARM_CATEGORY_HATE_SPEECH", "threshold": "BLOCK_NONE"},
    {"category": "HARM_CATEGORY_SEXUALLY_EXPLICIT", "threshold": "BLOCK_NONE"},
    {"category": "HARM_CATEGORY_DANGEROUS_CONTENT", "threshold": "BLOCK_NONE"},
  ]

)

chat_session = model.start_chat(
  history=[
    {
      "role": "user",
      "parts": [
        "You are _Name_, an __ explain__",
      ],
    },
    {
      "role": "model",
      "parts": [
        "--customize the chatbot respose--",
      ],
    },
  ]
)

# response = chat_session.send_message("Who are you?")
# print(response.text)

