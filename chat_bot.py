import openai

openai.api_key = "YOUR API KEY HERE"
MODEL = "text-davinci-003"

def prompt(conversation_history=None, user_input=None):
    return f"""
As an advanced chatbot, your primary goal is to assist users to the best of your ability.
This may involve answering questions, providing helpful information, or completing tasks based on user input. In order to effectively assist users, it is important to be detailed and thorough in your responses.
Use examples and evidence to support your points and justify your recommendations or solutions.

{conversation_history}

User: {user_input}
Chatbot:"""

def get_response(prompt):
    return openai.Completion.create(
        engine=MODEL,
        prompt=prompt,
        max_tokens=2048,
        n=1,
        stop=None,
        temperature=0.5,
    )['choices'][0]['text'].strip()

def main():
    conversation_history = ""
    while True:
        user_input = input("> ")
        if user_input == 'exit':
            break
        chatbot_response = get_response(
            prompt(
                conversation_history=conversation_history,
                user_input=user_input
            )
        )
        print(f'Chatbot: {chatbot_response}')
        conversation_history += f'User: {user_input}\nChatbot: {chatbot_response}\n'

if __name__ == '__main__':
    main()