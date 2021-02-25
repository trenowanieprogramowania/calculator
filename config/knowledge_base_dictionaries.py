from elementary_beginning_operations.background_operations import addition, subtraction, multiplication, division,\
    nullification, terminating_programme
from elementary_beginning_operations.logging_operations import logging_using_json_file, logging_using_csv_file

option_choices = {"1": {"operation": addition, "option": "adding to current score", "forbidden": [],
                        "activity": "addition"},
                  "2": {"operation": subtraction, "option": "subtracting from current score", "forbidden": [],
                        "activity": "subtraction"},
                  "3": {"operation": multiplication, "option": "multiplying current score", "forbidden": [],
                        "activity": "multiplication"},
                  "4": {"operation": division, "option": "dividing current score", "forbidden": [0.],
                        "activity": "division"},
                  "5": {"operation": nullification, "option": "making current score equal to 0", "forbidden": [],
                        "activity": "nullification"},
                  "6": {"operation": terminating_programme, "option": "exiting programme", "forbidden": [],
                        "activity": "exit"}}

file_choices = {"1": {"operation": logging_using_json_file, "option": "using json file as registry source",
                      "forbidden": []},
                "2": {"operation": logging_using_csv_file, "option": "using csv file as registry source",
                      "forbidden": []}}
