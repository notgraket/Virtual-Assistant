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
    """Match responses to functions if possible"""
    if "(" in response:
        try:
            eval(response)
        except:
            print(response)
    else:
        print(response)



# Callable functions for the model

def get_weather(city, state):
    """Get the weather data for the city in a given state"""
    url = f"https://geocoding-api.open-meteo.com/v1/search?name={city}&count=3&language=en&format=json&countryCode=US"
    responses = requests.get(url).json()

    for response in responses['results']:
        if response['admin1'] == state and response['name'] == city:
            break
    
    lat, long = response['latitude'], response['longitude']
    weather_url = f"https://api.open-meteo.com/v1/forecast?latitude={lat}2&longitude={long}&hourly=temperature_2m&current=temperature_2m,rain,wind_speed_10m&wind_speed_unit=mph&temperature_unit=fahrenheit&precipitation_unit=inch"
    responses = requests.get(weather_url).json()
    temperature = responses['current']['temperature_2m']

    print(f"It's currently {temperature} degrees in {city}")
    
    


# Running the script outright will run this
def main():
    print("Enter 'end' to exit")
    end = False
    while not end:
        user_input = input("Query: ")
        if (user_input == "end"): 
            return
        response = query(user_input)
        map_response(response)

if __name__ == "__main__":
    main()
