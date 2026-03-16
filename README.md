# Virtual Assistant

Requirements: Python 3.10+ and the 'transformers' library installed

This is a virtual assistant created to further my understanding of machine learning and llms.
Currently I'm using HuggingFace's distilgpt2 model that has been fine tuned for function calling.
As of right now, all it can do is return a function to get the weather status of any city or town in New York.

Due to the fact that distilgpt2 is an extremely small llm model, it's not 100% accurate with its recognition of non-function related queries.

To get started, download the model and change the directory location in the script to its location on your drive.
You can run the model in Ollama as normal or you can run the script with the -i flag to manually query it in the command line.


