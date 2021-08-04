
# ----COMMON IMPORTS - STARTS
from typing import List
# ----COMMON IMPORTS - ENDS


# Used to store the parsed input data of contacts and to print data to output.
# You are not obliged to work with this class while processing the contacts in your code.
# This is only used by the readInputFromConsole() and printOutputToConsole() 
# functions to take or return contacts data from your code.
class ContactData:
    def __init__(self) -> None:
        self.name: str = None
        self.birth_date: str = None
        self.phone_numbers: List[str] = []
        self.last_update_time: int = 0


# ----INPUT PARSING - STARTS
# Reads the contacts input data from the console and returns to your code.
# This function also converts special input 'empty' to empty string.
# 
# !!!!! Note !!!!!
# Changing the code inside this function is not recommended, 
# as it may impact the output of your program.
# 
# Example Input:
# 3
# alice
# 05-06-2000
# 3
# 12345678 empty (022)-2456-7890
# 5
# Bob Parson
# empty
# 1
# 56728192
# 10
# Alice Weasley
# empty
# 2
# 12345678 98765432
# 20
def read_console_input() -> List[ContactData]:
    contacts_input_list = []
    num_of_contacts = int(input())
    for i in range(num_of_contacts):
        contact = ContactData()

        contact.name = input()

        birth_date_output = input()
        contact.birth_date = birth_date_output \
            if birth_date_output != "empty" else ""
        
        num_of_phones = int(input())
        phone_numbers_input = input()
        if num_of_phones > 0:
            phone_numbers_input = phone_numbers_input.split(" ")
            for phone in phone_numbers_input:
                contact.phone_numbers.append(phone if phone != "empty" else "")

        contact.last_update_time = int(input())

        contacts_input_list.append(contact)

    return contacts_input_list
# ----INPUT PARSING - ENDS

# ----OUTPUT PRINTING - STARTS
# Takes the merged contacts data from your code and prints it to console in required format.
# It takes care of printing the output in correct format and in correct order.
# Also prints empty strings as special output 'empty'.
# 
# !!!!! Note !!!!!
# Changing the code inside this function is not recommended, 
# as it may impact the output of your program.
# 
# Example Output:
# Alice Weasley
# 05-06-2000
# empty 12345678 (022)-2456-7890 98765432
# 20
# Bob Parson
# empty
# 56728192
# 10
# 
def print_output_to_console(merged_contacts: List[ContactData]):
    merged_contacts.sort(key=lambda x: x.name)
    for contact_data in merged_contacts:
        print(contact_data.name)
        print(contact_data.birth_date if contact_data.birth_date != "" else "empty")

        phone_numbers_output = ""
        if contact_data.phone_numbers:
            contact_data.phone_numbers.sort()
        for phone in contact_data.phone_numbers:
            phone_numbers_output = phone_numbers_output + \
                (phone if phone != "" else "empty") + " "
        if phone_numbers_output:
            phone_numbers_output = phone_numbers_output[:-1]
        print(phone_numbers_output)

        print(contact_data.last_update_time)
# ----OUTPUT PRINTING - ENDS


contacts_input: List['ContactData'] = read_console_input()

merged_contacts: List['ContactData'] = []

# code start

# helper functions
def merge_duplicates(list_index, contact_numbers):
    merged_number = contact_numbers[list_index[0]]
    # print('in function')
    # create contacts list from indexes
    list_contacts = []
    for i in list_index:
        list_contacts.append(contact_numbers[i])
    
    # print(list_contacts[0].last_update_time)

    list_contacts.sort(key=lambda x: x.last_update_time)
    list_contacts.reverse()
    # print(list_contacts[0].last_update_time)

    merged_number.name = list_contacts[0].name
    merged_number.last_update_time = list_contacts[0].last_update_time

    # for dob
    for i in list_contacts:
        if i.birth_date != '':
          merged_number.birth_date  = i.birth_date
          break

    final_phone_numbers = []
    # for phone numbers
    for i in list_contacts:
        for j in i.phone_numbers:
            if not (j in final_phone_numbers):
                final_phone_numbers.append(j)

    merged_number.phone_numbers = final_phone_numbers
    return merged_number
    # return merged_number

# initializations
num_contacts = len(contacts_input)
duplicate_contacts_indexes = [-1] * num_contacts
merge_contacts_indexes = [[] for i in range(num_contacts)]

# find duplicates
for i in range(num_contacts):
    for j in range(i+1, num_contacts):
        flag = False
        for num1 in (contacts_input[i].phone_numbers):
            for num2 in (contacts_input[j].phone_numbers):
                if num1 != '' and num2 != '' and num1 == num2:
                    if duplicate_contacts_indexes[i] == -1:
                        duplicate_contacts_indexes[i] = duplicate_contacts_indexes[j] = i
                    else:
                        duplicate_contacts_indexes[j] = duplicate_contacts_indexes[i]
                    flag = True     
            if flag == True:
                break

# print(duplicate_contacts_indexes)

# push non duplicates and make list of duplicates
for i in range(num_contacts):
    if duplicate_contacts_indexes[i] == -1:
        merged_contacts.append(contacts_input[i])
    else:
        merge_contacts_indexes[duplicate_contacts_indexes[i]].append(i)

# print(merge_contacts_indexes)

# merge duplicates
for i in range(num_contacts):
    if len(merge_contacts_indexes[i]) != 0:
        merged_contacts.append(merge_duplicates(merge_contacts_indexes[i], contacts_input))

# WRITE YOUR CODE HERE. You may also create your own functions and import 
# additional packages as required.

print_output_to_console(merged_contacts)

# sample input
# 3
# Amar P
# 23-05-1997
# 2
# 8888888888 9999999999
# 12
# Akbar
# 03-07-2000
# 1
# 1234567890
# 25
# Anthony G
# 27-12-1989
# 1
# 28719283
# 10

# sample output

# Akbar
# 03-07-2000
# 1234567890
# 25
# Amar P
# 23-05-1997
# 8888888888 9999999999
# 12
# Anthony G
# 27-12-1989
# 28719283
# 10
