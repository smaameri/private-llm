import os
from dotenv import load_dotenv
from langchain import PromptTemplate, LLMChain
from langchain.llms import CerebriumAI

load_dotenv('.env')

template = """
You are a friendly chatbot assistant.

Question: {question}

Answer:"""

prompt = PromptTemplate(template=template, input_variables=["question"])

llm = CerebriumAI(endpoint_url="https://run.cerebrium.ai/gpt4-all-webhook/predict")

llm_chain = LLMChain(prompt=prompt, llm=llm)

green = "\033[0;32m"
white = "\033[0;39m"

while True:
    query = input(f"{green}Prompt: ")
    if query == "exit" or query == "quit" or query == "q":
        print('Exiting')
        break
    if query == '':
        continue
    response = llm_chain(query)
    print(f"{white}Answer: " + response['text'])

