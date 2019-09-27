from teachme.userinput import UserInput


class Chat:
    def __init__(self, chatty: bool = True):
        if chatty:
            print("Hello! \n"
                  + "Call the method teachme.Chat.start_chat()"
                  + " to start a conversation.")

    def start_chat(self) -> None:
        """Initialize chat with user
        """
        print("Ok, lets talk... \n"
              + "Feel free to start, by typing something. \n"
              + "Type quit when you are done.")
        user_chat = ''
        while user_chat.lower() != 'quit':
            user_chat = input("> ")
            if user_chat.lower() != 'quit':
                self.create_response(user_chat)

    def create_response(self, user_chat: str) -> None:
        """Create Response to User Input
        """
        userinput = UserInput(user_chat)
        if userinput.user_question():
            print("Is that a question?")
        else:
            print(f"Sounds like, {user_chat}")
