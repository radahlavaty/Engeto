"""
project_1.py: first Engeto Online Python Academy project
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

#Welcome the user
print(40*"-")
print(f"Welcome to the app, {user_name}")
print("We have 3 texts to be analyzed.")
print(40*"-")

#Select the text_number to be analyzed
text_number = input("Enter a number btw. 1 and 3 to select: ")

#Check if the text_number is correct
if (int(text_number) < 1) and (int(text_number) > 3):
    exit("text number not in range, termination the program..")
elif not text_number.isnumeric:
    exit("text number is not a number, termination the program..")
else:
    text_number = int(text_number)

#Statistics
#Text to list preparation
selected_text = TEXTS[text_number-1]
selected_text_list = selected_text.split()

for word in selected_text_list:
    word = word.strip('.,?!-')

#Count of all words
words_amount = len(selected_text_list)
print(f"There are {words_amount} in the selected text.")

#Count of all words starting with upper case letter
words_upper_start_amount = 0
for word in selected_text_list:
    if (word[0].isnumeric() == False) and (word[0].isupper() == True):
        words_upper_start_amount += 1
print(f"There are {words_upper_start_amount} titlecase words.")

#Count of all words with only upper case letters
words_upper_all_amount = 0
for word in selected_text_list:
    if (word[0].isnumeric() == False) and (word.upper() == word):
        words_upper_all_amount += 1
print(f"There are {words_upper_all_amount} uppercase words.")

#Count of all words with only lower case letters
words_lower_all_amount = 0
for word in selected_text_list:
    if (word[0].isnumeric() == False) and (word.lower() == word):
        words_lower_all_amount += 1
print(f"There are {words_lower_all_amount} lowercase words.")

#Count of all numbers and sum
words_numbers_amount = 0
numbers_list_sum = 0
for word in selected_text_list:
    if word.isnumeric() == True:
        words_numbers_amount += 1
        numbers_list_sum += int(word)

print(f"There are {words_numbers_amount} numeric strings.")
print(f"The sum of all the numbers {numbers_list_sum}")

#Do the length words statistics
#Find max word length
length_words_dict = {}
max_length_word = 0
for word in selected_text_list:
    if len(word) > max_length_word:
        max_length_word = len(word)

#Dictionary Init
for length in range(1,max_length_word+1):
    length_words_dict[length] = 0

print(length_words_dict)

#Counting occurences for every lenght
for word in selected_text_list:
    length = len(word)
    length_words_dict[length] += 1

#Print length words statistics
print(40*"-")
print('{:}|{:^20}|{:<3} '.format("LEN","OCCURENCES","NR."))
print(40*"-")

for length in length_words_dict:
    print('{:>3}|{:<20}|{:<3} '.format(length,length_words_dict[length]*"*",length_words_dict[length]))












