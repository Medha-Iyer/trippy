import openai

openai.api_key = "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"
# command line: export OPENAI_API_KEY = 

destination = ""
arrival_date = ""
arrival_time = ""
departure_date = ""
departure_time = ""
transport = ""
budget = ""
travel_style = ""
meals = ""

messages = []
messages.append({"role": "system", "content": "You are a travel assistant..."})
messages.append({"role": "assistant", "content": "Hello, I’m Trippy! Where are you traveling to?"})

# messages.append({"role": "assistant", "content": reply})
# messages.append({"role": "user", "content": })
# messages.append({"role": "system", "content": ""})

# print("\n" + reply + "\n")

def reply(message_list):
    response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=message_list)
    return response["choices"][0]["message"]["content"]