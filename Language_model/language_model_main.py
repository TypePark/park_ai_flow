import language_model

model_chat = language_model.ModelChat()
model_chat.load_model()

input = "Hi"
response = model_chat.chat(input)
print(response)