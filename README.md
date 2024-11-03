# Yollama

## what is this ?

This repo holds the code for helper functions for Ollama with Langchain.

## prerequisites

This has been tested on a Ubuntu 24 server. You'll need:

- Ollama installed
- the Ollama models you'll need to install are:

```python
default_llm_model_name = "llama3.1"
default_long_context_llm_model_name = "mistral-nemo"
default_sql_llm_model_name = "qwen2.5-coder"
```

The `num_ctx` parameter is the size of the context window used to generate the next token, here we use values for a 20GB VRAM GPU.

- Python 3 with `venv` and `pip` installed

## basic usage

`pip install yollama`

### `get_llm()`

1st parameter is the use case (`Literal["default", "long-context", "sql"]`), which determines the model and context size.

2nd parameter is a boolean to determine if the LLM should return a JSON object or a string.

```python
from yollama import get_llm

llm = get_llm()

# invoke default model (Llama3.1) in JSON mode
print(llm.invoke({"input_query": some_user_input}))
```

```python
# invoke Mistral-Nemo model in text mode with some lengthy context
print(get_llm("long-context", False).invoke({"document": some_big_text}))
```

```python
# invoke Qwen2.5-Coder model in text mode, to get a raw SQL query
print(get_llm("sql", False).invoke({"query": "create a SQL query to get the latest headlines"}))
```

## philosophy

### fully local models

I've decided to let go of OpenAI to:

- preserve my privacy
- save money

As local models are getting better and better, I'm confident that I'll be able to have a greater experience in the future, even with my small 20GB VRAM GPU. 🤔 Of course, it's not fast, but hey everything comes with tradeoffs right? 💪

## contributions guidelines

🤝 I haven't made up my mind on contribution guidelines yet. I guess we'll update them as you contribute!