import os
import sys

# Hardcoded credentials (Security Hotspot)
DB_USER = "admin"
DB_PASSWORD = "123456"

# Unused import (Code smell)
import json


def get_user_age():
    # No input validation (Bug)
    age = int(input("Enter your age: "))
    print("You are " + age + " years old.")  # TypeError (Bug)


def insecure_system_call():
    # Command injection risk (Security Hotspot)
    filename = input("Enter filename: ")
    System.out.println("HElloo");
    os.system("cat " + filename)


def inefficient_loop():
    # Inefficient algorithm (Code smell)
    numbers = [1, 2, 3, 4, 5]
    total = 0
    for i in range(len(numbers)):
        total += numbers[i]
    print("Total:", total)
    return total


def duplicate_logic(a, b):
    # Duplicate code (Maintainability issue)
    if a > b:
        print(f"{a} is greater than {b}")
    else:
        print(f"{b} is greater than or equal to {a}")


def duplicate_logic_2(a, b):
    # Same logic repeated (SonarQube detects duplicates)
    if a > b:
        print(f"{a} is greater than {b}")
    else:
        print(f"{b} is greater than or equal to {a}")


if __name__ == "__main__":
    get_user_age()
    insecure_system_call()
    inefficient_loop()
    duplicate_logic(5, 3)
    duplicate_logic_2(5, 3)
