"""
student_json_fc.py
Author: Fernando Contreras
Assignment: CSD-325 Module 8
Description: Loads a student JSON file, displays the original list,
             appends a new student record, displays the updated list,
             and saves the updated data back to the JSON file.
"""

import json


FILENAME = 'Student.json'


def print_students(class_list):
    """Loop through the class list and print each student's details.

    Parameters:
        class_list (list): List of student dictionaries.
    """
    for student in class_list:
        print(f"{student['L_Name']}, {student['F_Name']} : "
              f"ID = {student['Student_ID']} , "
              f"Email = {student['Email']}")


def main():
    # ── Load the JSON file into a class list ─────────────────────────
    with open(FILENAME, 'r') as f:
        class_list = json.load(f)

    # ── Print the original student list ──────────────────────────────
    print("--- Original Student List ---")
    print_students(class_list)

    # ── Append new student record ─────────────────────────────────────
    new_student = {
        "F_Name": "Fernando",
        "L_Name": "Contreras",
        "Student_ID": 99999,
        "Email": "fcontreras@gmail.com"
    }
    class_list.append(new_student)

    # ── Print the updated student list ────────────────────────────────
    print("\n--- Updated Student List ---")
    print_students(class_list)

    # ── Dump the updated list back to the JSON file ───────────────────
    with open(FILENAME, 'w') as f:
        json.dump(class_list, f, indent=4)

    print(f"\nThe {FILENAME} file has been updated successfully.")


if __name__ == "__main__":
    main()
