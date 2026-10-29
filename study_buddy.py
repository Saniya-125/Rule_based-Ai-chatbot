# +++++++++rule based ai python chatbot+++++++++
import datetime
import time

name=input("Enter your name: ")
presentHour = datetime.datetime.now().hour
if 5 <= presentHour <= 11:
    print("Good Morning",name)
elif 11<= presentHour <=17:
    print("Good afternoon",name)
elif 17<=presentHour <=20:
    print("Good evening",name)
else:
    print("Good night",name)

print("Namaste! Welcome to your study_buddy bot ")
print("You can ask me basic Questions and as much as rou can and type bye to exit the chat")

#Chatbot memory creation[dictionary of responses]


responses={
    "Hello":"Welcome to tito,your personalised ai study buddy.",
    "How are you?":"I'm fine thankyou",
    "who are you":"I'm tito you smart study buddy",
    "motivate me":"Keep going .Every bug of your project makes you a better developer.",
    "happy":"Great to hear that.",
    "What is variable":"A variable is a named memory location to store data.The values can be changed.",
    "What is function":"A reusable block of code desined to perform specific task.",
    "Keywords":"Reserved words with predefined meaning that cannot be used as identifiers.",
    "Comments":"Notes in the code for explanation thay are ignored by compilers.",
    "Arrays":"A collection of elements of the same data type stored in contiguous memory.",
    "Pointers":"Variables that store the momory address of another variables.",
    "Pillars of Object oriented programming":"Thera are 4 pillars in object oriented programming.",
    "class":"A blueprint or template ued to create individual objects.",
    "object":"An instance of a class containing data attributes and methods.",
    "inheritance":"A mechnism where a child class acquires properties from a parent class.",
    "polymorphism":"The ability of a function or object to exist mulyiple times.",
    "abstraction":"Hiding complex implementation details and showing only essential features.",
    "encapsulation":"Bundling data and methods into a single unit while restricting direct access.",
}

# method function to get response of chat bot
def getResponeOfBot(userQuestion):
    userQuestion=userQuestion.lower()
    for eachKey in responses:
        if eachKey in userQuestion:
            return responses[eachKey]

    return "not able to tell that .Im in learning mode"        


# Take user input

while True:
    userInput=input("Please ask your Question: ")
    reply= getResponeOfBot(userInput)
    print("tito's response:-->",reply)

    if "bye" in  userInput.lower():
        break
