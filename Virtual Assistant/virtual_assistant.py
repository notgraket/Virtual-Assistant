# Nicolas Sepello
# Interactive Script for the Virtual Assistant

from transformers import AutoTokenizer, AutoModelForCausalLM
import requests

model_location = r"H:\Models\distilgpt2-finetuned" # Change to your model's install location
tokenizer = AutoTokenizer.from_pretrained(model_location)
model = AutoModelForCausalLM.from_pretrained(model_location)


def query(prompt : str):
    """Returns a valid function given your prompt or a 'I don't know' response"""
    inputs = tokenizer(prompt, return_tensors = "pt")
    outputs = model.generate(**inputs, max_length=128, do_sample=True, top_p=0.95, temperature=0.65, pad_token_id=tokenizer.eos_token_id)
    response = tokenizer.decode(outputs[0], skip_special_tokens=True)
    return response.split("Assistant: ")[-1].strip() # get only the last output


def map_response(response : str):
    """Dynamically match responses to functions if possible"""
    if "(" in response:
        eval(response)
    else:
        print(response)



# Callable functions for the model

def get_weather(city, state):
    """Get the weather data for the city in a given state"""
    print("called get_weather")


# If you run the script without -i this will run
def main():
    end = False
    while not end:
        user_input = input("Query: ")
        response = query(user_input)
        map_response(response)



if __name__ == "__main__":
    main()
