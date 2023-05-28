from langchain import PromptTemplate, LLMChain
from langchain.llms import GPT4All
from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler

template = """
You are a friendly chatbot assistant.

Question: {question}

Answer:"""

prompt = PromptTemplate(template=template, input_variables=["question"])

llm = GPT4All(
    model='./models/ggml-mpt-7b-chat.bin'
)

llm_chain = LLMChain(prompt=prompt, llm=llm)

query = input("Prompt: ")
response = llm_chain(query)
llm_chain(query)