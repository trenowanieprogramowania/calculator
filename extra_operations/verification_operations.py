def operation_correctness(input_knowledge_base: dict, selected_operation, second_number):
    if float(second_number) in input_knowledge_base[selected_operation]["forbidden"]:
        print("Impossible operation. Exiting calculator.")

        while second_number == "0":
            second_number = input("Select 2nd number: ")
