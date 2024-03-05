# LangChain Definitions Generator

## LangChain
Langchain is an open-source framework that enables developers working with artificial intelligence to combine large language models like GPT-4 with external data sources.

## Prompt 
A prompt for a language model is a set of instructions or input provided by a user to guide the model's response, helping it understand the context and generate relevant and coherent language-based output, such as answering questions, completing sentences, or engaging in a conversation.

## Ollama
Ollama allows you to run open-source large language models, such as Llama 2, locally. It bundles model weights, configuration, and data into a single package, defined by a Modelfile. It optimizes setup and configuration details, including GPU usage.

## Setup
- [Download](https://ollama.com/download) and install Ollama onto the available supported platforms 
- Fetch available LLM model via ollama pull <name-of-model>
    * View a list of available models via the model library
    * e.g., for Llama-7b: ollama pull llama2
- This will download the default tagged version of the model. Typically, the default points to the latest, smallest sized-parameter model.
On Mac, the models will be download to ~/.ollama/models

On Linux (or WSL), the models will be stored at /usr/share/ollama/.ollama/models

- Specify the exact version of the model of interest as such ollama pull vicuna:13b-v1.5-16k-q4_0
- To view all pulled models, use ollama list
- To chat directly with a model from the command line, use ollama run <name-of-model>
- View the Ollama documentation for more commands. Run ollama help in the terminal to see available commands too.

## Llama 2
Llama 2 is released by Meta Platforms, Inc. This model is trained on 2 trillion tokens, and by default supports a context length of 4096. Llama 2 Chat models are fine-tuned on over 1 million human annotations, and are made for chat.

## Output parsers
Output parsers are responsible for taking the output of an LLM and transforming it to a more suitable format. This is very useful when you are using LLMs to generate any form of structured data.

Besides having a large collection of different types of output parsers, one distinguishing benefit of LangChain OutputParsers is that many of them support streaming.

- **String output parser**: The StringOutputParser takes language model output (either an entire response or as a stream) and converts it into a string. This is useful for standardizing chat model and LLM output.

## LCEL 
LCEL makes it easy to build complex chains from basic components, and supports out of the box functionality such as streaming, parallelism, and logging.
Basic example: **prompt + model + output parser**

## Chain 
Chains refer to sequences of calls - whether to an LLM, a tool, or a data preprocessing step. The primary supported way to do this is with LCEL.
- **Chains that are built with LCEL.** In this case, LangChain offers a higher-level constructor method. However, all that is being done under the hood is constructing a chain with LCEL.
- **[Legacy] Chains** constructed by subclassing from a legacy Chain class. These chains do not use LCEL under the hood but are rather standalone classes.  

## Interface 
To make it as easy as possible to create custom chains, we’ve implemented a “Runnable” protocol. The Runnable protocol is implemented for most components. This is a standard interface, which makes it easy to define custom chains as well as invoke them in a standard way. The standard interface includes:

* **stream:** stream back chunks of the response
* **invoke:** call the chain on an input
* **batch:** call the chain on a list of inputs

These also have corresponding async methods:

* **astream:** stream back chunks of the response async
* **ainvoke:** call the chain on an input async
* **abatch:** call the chain on a list of inputs async
* **astream_log:** stream back intermediate steps as they happen, in addition to the final response
* **astream_events:** beta stream events as they happen in the chain (introduced in langchain-core 0.1.14)

To see the full documentation, including details on the tools used and their usage, please refer to [LangChain Documentation](https://python.langchain.com/docs/).

