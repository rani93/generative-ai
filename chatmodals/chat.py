from dotenv import load_dotenv

load_dotenv()

from langchain.chat_models import init_chat_model

model = init_chat_model("mistral-small-latest", model_provider="mistralai")
response = model.invoke("What is the capital of France?")
print(response)