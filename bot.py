import os
import openai

# Set your OpenAI API key from an environment variable
openai.api_key = os.getenv("OPENAI_API_KEY")

def get_response(prompt):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",  # Change this to your desired model
        messages=[
            {"role": "user", "content": prompt}
        ]
    )
    return response.choices[0].message['content']

def main():
    print("Welcome to the Power Scaling Bot! Type 'exit' to quit.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            print("Goodbye!")
            break
        response = get_response(user_input)
        print("Bot:", response)

if __name__ == "__main__":
    main()
