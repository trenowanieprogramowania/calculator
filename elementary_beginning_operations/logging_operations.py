from csv import reader
from datetime import datetime
from json import dump, load

from config.constants import DATE_FORMAT


def logging_using_json_file():
    print("Welcome in the calculator!")

    user_name = input("State a name: ")

    current_time = datetime.now()

    with open('registry_files/login_dates.json', mode='r') as dictionary_registry:
        dictionary_from_json = load(dictionary_registry)

        if user_name in dictionary_from_json.keys():
            time_of_last_registry = dictionary_from_json[user_name]
            time_of_last_registry_string = datetime.strptime(time_of_last_registry, DATE_FORMAT)

            time_difference = current_time - time_of_last_registry_string

            print(f"Welcome, user {user_name}. \nLast visit: {time_difference}")

            dictionary_from_json[user_name] = current_time.strftime(DATE_FORMAT)
        else:
            print("Welcome, new user.")
            dictionary_from_json[user_name] = current_time.strftime(DATE_FORMAT)

        with open('registry_files/login_dates.json', mode='w') as dictionary_update:
            # saving given dictionary to json file
            dump(dictionary_from_json, dictionary_update)


def logging_using_csv_file():
    print("Welcome in the calculator!")

    user_name = input("State a name: ")

    current_time = datetime.now()

    with open('registry_files/login_dates.csv', mode='r') as given_csv_file:
        extracted_csv_file = reader(given_csv_file)
        dictionary_from_csv = {column[0]: column[1] for column in extracted_csv_file}

    if user_name in dictionary_from_csv.keys():
        time_of_last_registry = dictionary_from_csv[user_name]
        time_of_last_registry_string = datetime.strptime(time_of_last_registry, DATE_FORMAT)

        time_difference = current_time - time_of_last_registry_string

        print(f"Welcome, user {user_name}. \nLast visit: {time_difference}")

        dictionary_from_csv[user_name] = current_time.strftime(DATE_FORMAT)
    else:
        print("Welcome, new user.")
        dictionary_from_csv[user_name] = current_time.strftime(DATE_FORMAT)

    # saving given dictionary to csv file
    with open('registry_files/login_dates.csv', mode='w') as csv_file:
        for key, values in dictionary_from_csv.items():
            csv_file.write(f"{key},{values}\n")
