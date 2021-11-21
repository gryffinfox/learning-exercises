# This program is an avatar maker exercise from a book Learn how to code
# Program asks how do you want your avatar and if you don't provide answer
# it will choose the default option.


def get_attribute(query, default):                              # Definition of a function that will take query and default obtion as parameters.
    question = query + ' ['+ default + ']? '
    answer = input(question)                                    # User is asked about his or hers choice with user input.
    
    if (answer == ''):                                          # If they don't reply, default obtion is used.
        answer = default
        
    print('You chose', answer)
    return answer

gender = get_attribute('What gender', 'female')    
hair = get_attribute('Which hair color', 'brown')
hair_length = get_attribute('What hair length', 'short')
eye = get_attribute('What eye color', 'blue')
glasses = get_attribute('Has glasses', 'no')
beard = get_attribute('Has beard', 'no')

print('\nThis is how your avatar looks like:'
    '\nGender:', gender,
    '\nHair:', hair,
    '\nHair length:', hair_length,
    '\nEye color:', eye,
    '\nGlasses:', glasses,
    '\nBeard:', beard)
