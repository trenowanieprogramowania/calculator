def extracting_input(knowledge_base_dictionary: dict):
    entry_text = ""

    for current_key, in knowledge_base_dictionary.keys():
        entry_text += str(current_key) + " " + str(knowledge_base_dictionary[current_key]["option"]) + "\n"

    choice = input("Available options: \n" + entry_text)

    try:
        if knowledge_base_dictionary[choice]:
            pass
    except KeyError as e:
        print("Undefined argument selected. Select again.")  # info level
        print("Error message: ", e)  # debug level

        choice = False
    except Exception as e:
        print("Unidentified error emerged: ")
        print("Error message: " + str(e) + "\nTry again.")

        choice = False

    return choice
