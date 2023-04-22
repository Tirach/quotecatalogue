# Import the necessary module(s).
import json
import textwrap


# This function repeatedly prompts for input until an integer of at least 1 is entered.
def input_int(prompt):
    while True:
        error_message, min_value = 'Invalid input.\n', 1
        try:
            number = int(input(prompt))

            if min_value is not None and number < min_value:
                print('Value below minimum.\n')
                continue

            return number

        except ValueError:
            print(error_message)


# This function repeatedly prompts for input until something other than whitespace is entered.
def input_something(prompt):
    while True:
        user_input = input(prompt)
        user_input = user_input.strip()

        if user_input == '':
            continue
        else:
            return str(user_input)


# This function opens "data.txt" in write mode and writes data_list to it in JSON format.
def save_data(data_list):
    save_my_stuff = open('data.txt', 'w')
    json.dump(data_list, save_my_stuff, indent=4)
    save_my_stuff.close()


# Attempt to open data.txt and read the data into a "data" variable.
# If the file does not exist or does not contain JSON data, set "data" to an empty list instead.
# This is the only time that the program should need to read anything from the file.
try:
    read_data = open('data.txt', 'r')
    data = json.load(read_data)
    read_data.close()

except FileNotFoundError:
    data = list()

# Print welcome message, then enter the endless loop which prompts the user for a choice.
print('Welcome to the "Quote Catalogue" Admin Program.')

while True:
    print('\nChoose [a]dd, [l]ist, [s]earch, [v]iew, [d]elete or [q]uit.')
    choice = input('> ').lower()

    if choice == 'a':
        # Add a new quote.
        data_dict = dict()

        data_dict['quote'] = input_something('Enter a quote: ')
        data_dict['year'] = input_something(
            'Enter the year. If not known, specify with [u]nknown: ')
        data_dict['author'] = input_something('Enter the author: ').title()

        if data_dict['year'] == 'u':
            data_dict['year'] = 'Unknown'

        data_dict['likes'] = 0
        data_dict['loves'] = 0

        data.append(data_dict)

        save_data(data)

        print('\nQuote added!')

    elif choice == 'l':
        # List the current quotes.
        if not data:
            print('\nNo quotes saved! Use choice [a] to add quotes.')
        else:
            for index, key in enumerate(data):
                print(f'\n{index + 1}) "{textwrap.shorten(key["quote"], width=40, placeholder="...").capitalize()}" -'
                      f' {key["author"].title()}, {key["year"]}')

    elif choice == 's':
        # Search the current quotes.
        if not data:
            print('\nNo quotes saved! Use choice [a] to add quotes.')
        else:
            search = input_something('Enter a search term: ').lower()
            search_result = False

            for index, key in enumerate(data):

                if search in key['quote'].casefold() or search in key['author'].casefold():
                    print(f'\n Search results: \n{index + 1}) "{textwrap.shorten(key["quote"], width=40, placeholder="...").capitalize()}" -'
                          f' {key["author"].title()}, {key["year"]}')
                    search_result = True

            if search_result == False:
                print('\nNo quotes matching search parameters.')

    elif choice == 'v':
        # View a quote.
        if not data:
            print('\nNo quotes saved! Use choice [a] to add quotes.')
        else:
            v_lookup = input_int(
                '\nEnter an integer equal to or greater than 1: ') - 1
            try:
                print(f'\n"{data[v_lookup]["quote"]}" \n\t-'
                      f' {data[v_lookup]["author"].title()}, {data[v_lookup]["year"]}.\n'
                      f' This quote has received {data[v_lookup]["likes"]} likes and {data[v_lookup]["loves"]} loves.\n')
            except IndexError:
                print('\nInvalid index number.')

    elif choice == 'd':
        # Delete a quote.
        if not data:
            print(
                '\nNo quotes saved! Use choice [a] to add quotes, so you can delete them, you monster.')
        else:
            d_lookup = input_int(
                '\nEnter an integer equal to or greater than 1: \n') - 1
            try:
                del data[d_lookup]
                save_data(data)
                print('\nQuote deleted!')
            except IndexError:
                print('\nNo quote found at this index.')

    elif choice == 'q':
        # End the program.
        print('\nGoodbye!\n')
        break

    else:
        # Print "invalid choice" message.
        print('\nInvalid choice! Please try again.\n')
