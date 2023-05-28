from langchain.llms import GPT4All

llm = GPT4All(model='./models/ggml-gpt4all-j-v1.3-groovy.bin')

llm("""
You are a friendly chatbot assistant.

Question: Where is Paris?

Answer:""")
