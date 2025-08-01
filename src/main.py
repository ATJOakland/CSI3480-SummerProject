#!/usr/bin/env python3

"""
Project Name: Brute Force Demo Project
Description: Simulates a brute force attack to guess a password
Author: Andrae Taylor, Christina Carvalho, Alexander Sekulski
Date: 7/24/2025
"""

"""
The "rockyou.txt" file is a big text file of most commonly used passwords and it's used
in a lot of official places.
But it's a big file (100MB) and GitHub only allows 25MB upload so a lot had to be deleted.
"""

import time

# Constants
COMMON_PASSWORD_LIST = "../list-of-most-common-passwords/rockyou.txt"
TARGET_PASSWORD = "../secret_user_info/secret_password.txt"

def read_passwords_from_file(filename: str) -> list[str]:
    # Read all the words in the text file and adds it to the array for testing.

    try:
        # "rockyou.txt" uses latin-1 encoding so it has to be specified.
        with open(filename, "r", encoding="latin-1") as file:
            return [line.strip() for line in file]
    
    except FileNotFoundError:
        print("Error: File not found!")
        return []
    except Exception as e:
        print(f"An error occured: {e}")
        return []

def get_target(filename: str) -> str:
    # Get the target word from the secret file
    try:
        with open(filename, "r") as file:
            word = file.readline().strip()
            
            if word: # If the word isn't null/empty
                return word
            else:
                print(f"Error: File '{filename}' is empty!")
                return ""
    
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found!")
        return ""
    except Exception as e:
        print(f"An error occured: {e}")
        return ""

def main() -> None:
    start_time = time.time() # Start program run timer
    print("\nStarting Brute Force Attack...\n")

    password_list_array = read_passwords_from_file(COMMON_PASSWORD_LIST)
    target_word = get_target(TARGET_PASSWORD)

    if not target_word:
        print("\nFailed: No valid target password in password secret password file.")
        return
    
    # Loop through t
    if len(password_list_array) > 0:
        attempt = 0
        for word in password_list_array:
            attempt += 1
            print(f"{attempt}. Trying: \"{word}\"")
            
            if word == target_word:
                print(f"\nSuccess, the password word was: \"{word}\"")
                break
        else:
            print("\nFailed: The Common Password List doesn't contain the user's password.")
    
    else:
        print("\nFailed: The common password list is empty.")
    
    end_time = time.time()
    print(f"\nFinished in {end_time - start_time:.2f} seconds.\n")


if __name__ == "__main__":
    main()