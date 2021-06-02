import re

# Steps
    # - Read potential-contacts
    # - Create functions to find emails
    # - Create functions to find numbers

def read_potential_contacts():
    with open('./assets/potential-contacts.txt','r') as data:
        read = data.read()
    # print(read)
    return read
    # pass

not_duplicate = []
def get_mails():
    check_mails = r'([a-zA-Z0-9._-]+@[a-zA-Z0-9._-]+\.[a-zA-Z0-9_-]+)'
    read = read_potential_contacts()

    get_all_mails = re.findall(check_mails, read)
    get_all_mails.sort()
    # print(get_all_mails)

    with open("solved_mails.txt", "w") as writing:
        for i in get_all_mails:
            if i not in not_duplicate:
                writing.write(f"{str(i)}\n")
            not_duplicate.append(i)

not_duplicate2 = []
def get_numbers():

    phone_numbers = r'([+]*[(][0-9]{1,5}[)][-\s/0-9]*)'
    read = read_potential_contacts()

    get_all_numbers = re.findall(phone_numbers, read)
    print(get_all_numbers)
    # get_all_numbers.sort()
    
    with open("phone_numbers.txt", "w") as writing:
        for i in get_all_numbers:
            if i not in not_duplicate2:
                writing.write(f"{str(i)}\n")
            not_duplicate2.append(i)



# read_potential_contacts()
# get_mails()
get_numbers()