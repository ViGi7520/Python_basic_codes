""" Mad Libs Generator """


# story 1
def p_story1():
    print("************************")
    print ("Zoo")
    print("************************")
    print (f"Today I went to the zoo. I saw a(n) {adjective1} {noun1} jumping up and down on its tree. " \
             f"He {verb_p1} {adverb1} through the large tunnel that led to its {adjective2} {noun2}. " \
             f"I got some peanuts and passed them through the cage to a gigantic gray {noun3} towering above my head. " \
             f"Feeding that animal mademe hungry. " \
             f"I went to get a {adjective3} scoop of ice cream. " \
             f"It filled my stomach. Afterwards I had to {verb1} {adverb2} to catch our bus." \
             f"When I got home I {verb_p2} my mom for a {adjective4} day at the zoo.")
    print("************************")

#story 2
def p_story2():
    print("************************")
    print ("Jungle")
    print("************************")
    print (f"I walk through the color jungle. I take out my {adjective1} canteen. "
           f"There's a {adjective2} parrot with a {adjective3} {noun1} in his mouth right there in front "
           f"of me in the {adjective4} trees! I gaze at his {adjective1} {noun2}. "
           f"A sudden sound awakes me from my daydream! "
           f"A panther’s {verb1} in front of my head! I {verb2} his {adjective2} breath. I remember I have a packet of {noun3} "
           f"that makes go into a deep slumber! I {verb1} it away from me in front of the {noun1}. Yes he's eating it! "
           f"I {verb2} away through the {adjective3} jungle. "
           f"I meet my parents at the tent. Phew! It’s been an exciting day in the jungle. ")
    print("************************")

# All the questions that the program asks the user
print("Select story. ")
print("1. Zoo")
print("2. Jungle")
print("3. story")
print("4. story")
print("Type 'quit' to exit")
print("  ")

run = True

while run:
    choice = input("Enter story number: ")
    if choice in ('1', '2', '3', '4'):

        noun1 = 'monkey'
        noun2 = 'cat'
        noun3 = 'elephant'
        adjective1 = 'naughty'
        adjective2 = 'fat'
        adjective3 = 'big'
        adjective4 = 'amazing'
        verb1 = 'run'
        verb2 = 'jump'
        adverb1 = 'blind'
        adverb2 = 'fast'
        verb_p1 = 'slided'
        verb_p2 = 'told'
        """
        noun1 = input("Choose a noun: ")
        noun2 = input("Choose a noun: ")
        noun3 = input("Choose a noun: ")
        adjective1 = input("Choose an adjective: ")
        adjective2 = input("Choose an adjective: ")
        adjective3 = input("Choose an adjective: ")
        adjective4 = input("Choose an adjective: ")
        verb1 = input("Choose a verb: ")
        verb2 = input("Choose a verb: ")
        adverb1 = input("Choose a adverb: ")
        adverb2 = input("Choose a adverb: ")
        verb_p1 = input("Choose a verb in past tense: ")
        verb_p2 = input("Choose a verb in past tense: ")
        """

        if choice == '1':
            print("Zoo Story selected")
            print(p_story1())
        elif choice == '2':
            print("Jungle Story selected")
            print(p_story2())
        elif choice == '3':
            print("story 3")
        elif choice == '4':
            print("story 4")

    else:
        if choice == "quit":
            print("Quiting")
            run = False