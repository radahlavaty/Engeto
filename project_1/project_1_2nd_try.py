"""
project_1_2nd_try.py: first Engeto Online Python Academy project
author: Radek Hlavatý
email: rada.hlavaty@gmail.com
discord: radhead#2491
"""
#Import
from task_template import TEXTS
from registered_users import registered_users

#User information input
user_name = input("username:")
password = input("password:")

#Check if the user is registered
if user_name not in registered_users:
    exit("unregistered user, termination the program..")
elif registered_users[user_name] != password:
    exit("incorrect password for registered user, termination the program..")

text_amount = len(TEXTS)
#Welcome the user
print(40*"-")
print(f"Welcome to the app, {user_name}")
print(f"We have {text_amount} texts to be analyzed.")
print(40*"-")

#Select the text_number to be analyzed
text_number = input(f"Enter a number btw. 1 and {text_amount} to select: ")
print(40*"-")

#Check if the text_number is correct
if (int(text_number) < 1) or (int(text_number) > text_amount):
    exit("text number not in range, termination the program..")
elif not text_number.isnumeric:
    exit("text number is not a number, termination the program..")
else:
    text_number = int(text_number)

#Statistics
#Text to list preparation
selected_text = TEXTS[text_number-1]
selected_text_base = selected_text.split()
selected_text_list = []

for word in selected_text_base:
    word = word.strip('.,?!-')
    selected_text_list.append(word)
    
#Counting variables init
words_upper_start_amount = 0
words_upper_all_amount = 0
words_lower_all_amount = 0
words_numbers_amount = 0
numbers_list_sum = 0
length_words_dict = {}

#Count of all words
words_amount = len(selected_text_list)

#Counting words statistics
for word in selected_text_list:
    if not word[0].isnumeric():
        #Count of all words starting with upper case letter
        if word[0].isupper():
            words_upper_start_amount += 1
        #Count of all words with only upper case letters
        if word.upper() == word:
            words_upper_all_amount += 1
        #Count of all words with only lower case letters
        if word.lower() == word:
            words_lower_all_amount += 1
    #Count of all numbers and sum
    if word.isnumeric():
        words_numbers_amount += 1
        numbers_list_sum += int(word)
    #adding length words statistics into dictionary
    length_words_dict[len(word)] = length_words_dict.get(len(word),0) + 1 

#Printing words statistics
print(f"There are {words_amount} words in the selected text.")
print(f"There are {words_upper_start_amount} titlecase words.")
print(f"There are {words_upper_all_amount} uppercase words.")
print(f"There are {words_lower_all_amount} lowercase words.")
print(f"There are {words_numbers_amount} numeric strings.")
print(f"The sum of all the numbers {numbers_list_sum}")

#Print length words statistics
print(40*"-")
print('{:}|{:^25}|{:<3} '.format("LEN","OCCURENCES","NR."))
print(40*"-")

for length in dict(sorted(length_words_dict.items())):
    print('{:>3}|{:<25}|{:<3} '.format(length,length_words_dict[length]*"*",length_words_dict[length]))












