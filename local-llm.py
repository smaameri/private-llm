from langchain.llms import GPT4All

llm = GPT4All(model='./models/ggml-mpt-7b-chat.bin')

llm("""
You are a friendly chatbot assistant.

Question: Where is Paris?

Answer:""")
