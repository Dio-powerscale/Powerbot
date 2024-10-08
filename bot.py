import openai

openai.api_key = 'your-api-key-here'

def get_response(prompt):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}]
    )
    return response['choices'][0]['message']['content']

if __name__ == "__main__":
    user_input = input("You: ")
    print("Bot:", get_response(user_input))
