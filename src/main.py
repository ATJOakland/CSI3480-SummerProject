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

def main() -> None:
    word = input("Enter a word: ")

    print(f"You entered : {word}")

if __name__ == "__main__":
    main()
