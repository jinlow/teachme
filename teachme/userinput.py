"""Process User Input
"""
import random
import spacy
from spacy.symbols import AUX
from teachme import constants

nlp = spacy.load('en_core_web_sm')

class UserInput:
    """Process User Input
    Methods for processing and extracting meaning from user input
    """

    def __init__(self, user_input: str):
        self.nlp_input = nlp(user_input)

    def user_question(self) -> bool:
        """Is Input a quesion?
        A simply grammer to determine if the input is a question.
        """
        # Initialize token indexes
        wh_i = -1
        q_i = -1
        # Loop through tokens
        for tok in self.nlp_input:
            if tok.head == tok:
                root_i = tok.i
            if tok.lower_ in constants.WH_WORDS:
                wh_i = tok.i
            if (tok.lower_ in constants.BE_WORDS) and tok.i == 0:
                q_i = tok.i
                root_i -= 1
            elif tok.dep == AUX:
                q_i = AUX
        return (q_i > root_i) | (wh_i == 0)

    def get_tense(self) -> bool:
        """Return tense of Input
        """
        dtl = []
        for tok in self.nlp_input:
            if tok.tag_ in ['VBD', 'VBN']:
                dtl.append('PAST')
            elif tok.tag_ in ['VBG', 'VBP', 'VBZ']:
                dtl.append('PRESENT')
            else:
                dtl.append('UKNOWN')
        if 'PAST' in dtl:
            doc_tense = 'PAST'
        elif 'PRESENT' in dtl:
            doc_tense = 'PRESENT'
        else:
            doc_tense = 'UNKNOWN'
        return doc_tense

    def question_response(self) -> None:
        """Resonpd to Questions
        Formulate a response question
        """

    def greeting_check(self) -> bool:
        """Check for Greeting
        Test if the user input is a greeting and create response.
        """
        greeting = [tok.lower_ in constants.GREETING_WORDS for tok in self.nlp_input]
        return any(greeting)

    def proc_userinput(self) -> None:
        """Process User Input
        Using the methods in the UserInput class process the incoming
        chats.
        """
        self.greeting_check()
        if self.user_question():
            print("Is this a question?")
        elif self.greeting_check():
            print(random.choice(constants.GREETING_RESPONSE))
        else:
            print(f"Sounds like, {self.nlp_input}")
