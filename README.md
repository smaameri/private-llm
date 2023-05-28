# Private LLM's on local and in the cloud with LangChain, GPT4All and Cerebrium

## Summary
Provided here are a few python scripts for interacting with your own locally hosted GPT4All LLM model using Langchain.
There is also a script for interacting with your cloud hosted LLM's using Cerebrium and Langchain
The scripts increase in complexity and features, as follows:

`local-llm.py` Interact with a local GPT4All model.

`local-llm-chain.py` Interact with a local GPT4All model using Prompt Templates.

`cloud-llm.py` Interact with a cloud hosted LLM model. The model is deployed and hosted on the Cerebrium platform.

I wrote an article which explores some of the concepts here, as well as walks through building each of the scripts.
[Can read that here](https://medium.com/@ssmaameri/building-a-multi-document-reader-and-chatbot-with-langchain-and-chatgpt-d1864d47e339)


## Getting started
Clone the repository, set up the virtual environment, and install the required packages

```
git clone git@github.com:smaameri/private-llm.git
cd private-llm
mkdir models
python3 -m venv .venv
. .venv/bin/activate
pip install -r requirements.txt
```

## Store your Cerebirum API key
To use the cloud-llm.py script that interacts with an LLM deployed on Cerebrium, you will need to setup your public Cerebrium
API Key.

Copy the example env file

`cp .env.example .env`

Now copy your public Cerebrium API key into the `.env` file, and save the file. It should send up looking something like

`CEREBRIUMAI_API_KEY=public-`

## Start chatting
To start interacting with a local-llm, you can download the GPT4All LLM from here https://gpt4all.io/index.html, and
add the downloaded model to the projects `/models` directory.

Now kick off the local-llm-chain.py script to start interacting with it.
```python
python3 local-llm-py.py
```

Could it be better? Try tweaking the prompts to get a better chatbot style assistant. Interested in using a local LLM
to read and interact with documents? Combine the concepts here with the project I created on building a [document reader
and chatbot](https://github.com/smaameri/multi-doc-chatbot).