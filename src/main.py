def main():
    import time
    from chatbot.greet import greet_user
    from chatbot.time import tell_time
    from chatbot.jokes import tell_joke

    print(greet_user())
    
    while True:
        user_input = input("How can I assist you? (type 'exit' to quit) ").strip().lower()
        
        if user_input == 'exit':
            print("Goodbye!")
            break
        elif 'time' in user_input:
            print(tell_time())
        elif 'joke' in user_input:
            print(tell_joke())
        else:
            print("I'm sorry, I can only tell the time or tell jokes.")

if __name__ == "__main__":
    main()