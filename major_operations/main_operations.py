from config.knowledge_base_dictionaries import file_choices, option_choices
from elementary_beginning_operations.preliminary_operations import extracting_input
from extra_operations.verification_operations import operation_correctness


def calculator_main_functioning():
    print("Preliminary booting. Select source of file used within this programme.")

    source_of_file = extracting_input(file_choices)

    print("Selected option: " + file_choices[source_of_file]["option"])

    file_choices[source_of_file]["operation"]()

    current_score = input("Select 1st number: ")

    while True:
        selected_operation = extracting_input(option_choices)

        next_number = 0

        print("Operation selected: " + option_choices[selected_operation]["activity"])

        if selected_operation in [str(index) for index in range(1, 5)]:
            next_number = input("Select 2nd number: ")

        operation_correctness(option_choices, selected_operation, next_number)

        current_score = option_choices[selected_operation]["operation"](current_score, next_number)

        print(f" Outcome: {current_score}")
