# Virtual Assistant

Requirements: Python 3.10+ and the 'transformers' library installed
Requirement: Download the fine-tuned model here: https://drive.google.com/drive/folders/1Lg8hKOMpYRGObOzHGmqXQEUMj9bL_jh6?usp=sharing

This is a virtual assistant created to further my understanding of machine learning and llms.
Currently I'm using HuggingFace's distilgpt2 model that has been fine tuned for function calling.
As of right now, all it can do is return a function to get the weather status of any city or town in New York.

Due to distilgpt2 being an extremely small model, it's not 100% accurate with its recognition of non-function related queries.
Notably the data this model was fine tuned on was procedurally generated, this also adds to the inaccuracy of its language processing.

To get started, download the model and change the directory location in the script to its location on your drive.
Calling the model in ollama would work, however it works best nested into a program.


