"""Project Constants
All of the constansts used for the project including the 
spacy model.
"""

import spacy

NLP = spacy.load('en_core_web_md')

WH_WORDS = ['what', 'where', 'when', 'which',
            'who', 'whom', 'whose', 'why', 'how']

BE_WORDS = ['is', 'was', 'do', 'were', 'are']

GREETING_WORDS = ["hi", "hello", "howdy", "hey", "what's up"]

GREETING_RESPONSE = ["Hi!",
                     "Hello!",
                     "Hi, how are you today?",
                     "Hi, how can I help?",
                     "Hello, what can I do for you?"]
