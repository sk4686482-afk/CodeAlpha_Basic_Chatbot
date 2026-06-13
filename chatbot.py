def start_chatbot():
    print("Welcome to Simple Chatbot")
    print("Available inputs: hello, how are you, bye\n")

    while True:
        user_input = input("You: ").strip().lower()

        if user_input == 'hello':
            print("Chatbot: Hi!")
        
        elif user_input == 'how are you':
            print("Chatbot: I'm fine, thanks!")
        
        elif user_input == 'bye':
            print("Chatbot: Goodbye!")
            break
            
        else:
            print("Chatbot: Please use standard inputs.")

start_chatbot()