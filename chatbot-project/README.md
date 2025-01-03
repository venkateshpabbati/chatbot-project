# Chatbot Project

This project is a simple chatbot that greets users, tells the current time, and shares jokes. It utilizes the 'facebook/bart-large-mnli' model for processing user input.

## Features

- **Greeting**: The chatbot can greet users with a friendly message.
- **Time**: The chatbot can tell the current time in a user-friendly format.
- **Jokes**: The chatbot can share random jokes to entertain users.

## Project Structure

```
chatbot-project
├── src
│   ├── main.py          # Entry point of the application
│   ├── chatbot          # Package containing chatbot functionalities
│   │   ├── __init__.py  # Initializes the chatbot package
│   │   ├── greet.py     # Module for greeting users
│   │   ├── time.py      # Module for telling the current time
│   │   └── jokes.py     # Module for telling jokes
│   └── models           # Package for loading models
│       └── __init__.py  # Initializes the models package
├── requirements.txt     # Lists project dependencies
└── README.md            # Documentation for the project
```

## Setup Instructions

1. Clone the repository:
   ```
   git clone <repository-url>
   cd chatbot-project
   ```

2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

3. Run the chatbot:
   ```
   python src/main.py
   ```

## Usage Examples

- To greet the user, simply start the chatbot.
- To get the current time, ask the chatbot "What time is it?"
- To hear a joke, ask the chatbot "Tell me a joke."

## License

This project is licensed under the MIT License.