import ollama

response = ollama.generate(
    model='phi3:3.8b',           # change to 'gemma' or 'gemma2' if you prefer
    prompt='Tell me the horoscope for scorpio for the following week'
)

print(response['response'])