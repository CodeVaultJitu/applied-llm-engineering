import ollama

response = ollama.generate(
    model='phi3:3.8b',           
    prompt='Explain recursion in one sentence'
)

print(response['response'])

#built