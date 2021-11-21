# Sentence convertor is program based on exercise on Udemy.com
# It takes user input and turn it into sentence by capitalizing the first letter and adding punctuation.

def sentence_maker(phrase):                                                 # Function that capitalize the first letter and add interpunction
    interrogatives = ('how', 'why', 'what', 'who', 'where')                 # Tuple of specific words that indicate question
    capitalized = phrase.capitalize()
    
    if phrase.startswith(interrogatives) == True:
        return '{}?'.format(capitalized)
    else:
        return '{}.'.format(capitalized)
        
phrases = []

user_input = ''

while True:
    user_input = input('Say something: [to end type \end] ')                # While loop is set to restart again unless the \end expression is entered.
    if user_input == '\end':
        break
    
    else:
        phrases.append(sentence_maker(user_input))                          # Everything that user inputs is processed by function sentence_maker and appended to the list called phrases.

print(' '.join(phrases))                                                    # Using a method join() will create a string with all the user's capitalized phrases with punctuation.
