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
import random
import customtkinter as ctk
from tkinter import simpledialog, messagebox

# Constants
COMMON_PASSWORD_LIST = "./small-password-list/smallpasswordlist.txt" #Changed from rockyou file path to secret_password path
TARGET_PASSWORD = "./secret_user_info/secret_password.txt"

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

def get_password(user):
    # Returns the password of the specified user called. Each password increases in complexity.
    user_passwords = {"user1":"password", "user2":"password123", "user3":"password123456" }
    return user_passwords.get(user, None) # Returns None if username isnt found

def perform_2fa(root_window) -> bool:
    """
    Performs 2FA by generating a random 4-digit number and asking user to input it.
    Returns True if user enters correct number, False if they cancel or enter wrong number.
    """

    # Generate random 4-digit number
    random_number = random.randint(1000, 9999)

    # Ask user to input the number
    user_input = simpledialog.askstring(
        "2FA Verification", 
        f"Please type {random_number}:", 
        parent=root_window
    )

    # Check if user cancelled or entered wrong number
    if user_input is None:  # User cancelled
        return False

    try:
        if int(user_input) == random_number:
            return True

        else:
            messagebox.showerror("2FA Failed", "Incorrect number entered!", parent=root_window)
            return False

    except ValueError:
        messagebox.showerror("2FA Failed", "Please enter a valid number!", parent=root_window)
        return False


def user_interface():
    root = ctk.CTk() # Initializes the User Interface window
    ctk.set_appearance_mode("dark")
    root.title("Brute Force Attack")
    root.geometry("500x500")
    frame = ctk.CTkFrame(master=root, width=500, height=500) #Sets a frame in the window to utalize a grid for label & button placement
    frame.place(relx=.5, rely=.5, anchor="center", bordermode = 'outside') #places the frame in the center of the window

    #Creates a checkbox for 2FA option
    twoFACheckbox = ctk.CTkCheckBox(frame, border_color = "black", text="Enable 2FA", font=("Arial", 20), text_color="white")
    twoFACheckbox.grid(column = 0, row = 0, pady = (20,5), padx = 125)

    #Creates a dropdown list to select the user
    optionmenu = ctk.CTkOptionMenu(frame, font=("Arial", 20), fg_color = "black", button_color = "black", values=["user1", "user2", "user3"])
    optionmenu.grid(column = 0, row = 1, pady = 5, padx = 10)

    #Creates a button called "Start Attack" and places it on the grid. Runs the main function to start the attack
    startAttackButton = ctk.CTkButton(frame, text="Start Attack", font=("Arial", 24), text_color="white", fg_color="black", width=20, command=lambda: main(elements, twoFACheckbox, root))
    startAttackButton.grid(column = 0, row = 2, pady = (5,20), padx = 10)

    #Creates a label called "attemptNumber" and places it on the grid. Will be updated with the current attempt number.
    attemptNumberLabel = ctk.CTkLabel(frame, text="--", font=("Arial", 24), text_color="white")
    attemptNumberLabel.grid(column = 0, row = 3, pady = 3, padx = 3)

    #Creates a label called "passwordAttempt" and places it on the grid. Will be updated with the current password attempt.
    passwordAttemptLabel = ctk.CTkLabel(frame, text="--", font=("Arial", 24), text_color="white")
    passwordAttemptLabel.grid(column = 0, row = 4, pady = 3, padx = 3)
    
    #Creates a label called "elapsedTime" and places it on the grid. Will be updated with the current elapsed time.
    elapsedTimeLabel = ctk.CTkLabel(frame, text="00:00", font=("Arial", 24), text_color="white")
    elapsedTimeLabel.grid(column = 0, row = 5, pady = 3, padx = 3)

    #Creates a label called "passwordDetected" and places it on the grid. Will be updated to say if the password was found or not.
    passwordDetectedLabel = ctk.CTkLabel(frame, text="Click \"Start Attack\"", font=("Arial", 24), text_color="white")
    passwordDetectedLabel.grid(column = 0, row = 6, pady = (20,5), padx = 3)

    #Creates a button called "Test login". 
    startAttackButton = ctk.CTkButton(frame, text="Test Login", font=("Arial", 24), text_color="white", fg_color="black", width=20, command=lambda: login_page(root, frame))
    startAttackButton.grid(column = 0, row = 7, pady = (5,20), padx = 10)

    elements = [elapsedTimeLabel, attemptNumberLabel, passwordAttemptLabel, passwordDetectedLabel, optionmenu] #Array of all the elements to pass to main to update them as the program runs

    root.mainloop() #Runs the user interface

def login_page(root, frame):
    frame.place_forget() # Hides the user_interface frame

    login_frame = ctk.CTkFrame(master=root, width=500, height=500) #Sets a frame in the window to utalize a grid for label & button placement
    login_frame.place(relx=.5, rely=.5, anchor="center", bordermode = 'outside') #places the frame in the center of the window

    #Creates a button that calls the "hide_login_page" function to switch to the main user interface
    back_button = ctk.CTkButton(login_frame, text="Back", font=("Arial", 24), text_color="white", fg_color="black", width=20, command=lambda: hide_login_page(frame, login_frame))
    back_button.grid(column = 0, row = 0, pady = 10, padx = 10, columnspan = 2)

    #Creates a username label and places it on the grid
    username_label = ctk.CTkLabel(login_frame, text="Username: ", font=("Arial", 24), text_color="white")
    username_label.grid(column = 0, row = 1, pady = 10, padx = 10)

    #Creates a username text box for the user to enter a username
    username_text_box = ctk.CTkEntry(login_frame, placeholder_text="Enter username")
    username_text_box.grid(column = 1, row = 1, pady = 10, padx = (0,10))

    #Creates a password label and places it on the grid
    password_label = ctk.CTkLabel(login_frame, text="Password: ", font=("Arial", 24), text_color="white")
    password_label.grid(column = 0, row = 2, pady = 10, padx = 10)

    #Creates a password text box for the user to enter a password
    password_text_box = ctk.CTkEntry(login_frame, placeholder_text="Enter password")
    password_text_box.grid(column = 1, row = 2, pady = 10, padx = (0,10))

    #Creates a label that will pdate depending on if the login was a success
    login_success = ctk.CTkLabel(login_frame, text=" ", font=("Arial", 24), text_color="white")
    login_success.grid(column = 0, row = 3, pady = 10, padx = 10, columnspan = 2)

    #Creates a login button to run the "test_login" function to test if the inputted username and password work
    login_button = ctk.CTkButton(login_frame, text="Login", font=("Arial", 24), text_color="white", fg_color="black", width=20, command=lambda: test_login(username_text_box, password_text_box, login_success))
    login_button.grid(column = 0, row = 4, pady = 10, padx = 10, columnspan = 2)

def hide_login_page(frame, login_frame):
    #Hides the login page and places the main user interface page
    login_frame.place_forget()
    frame.place(relx=.5, rely=.5, anchor="center", bordermode = 'outside')

def test_login(username_text_box, password_text_box, login_success):
    username = username_text_box.get() #Gets the username from the username text box
    test_password = password_text_box.get() #Gets the password from the password text box
    actual_password = get_password(username) #Gets the actual password of the target user
    
    #Changes the login_sucess label depending on if the right username and password were entered
    if test_password == actual_password:
        login_success.configure(text_color = "green", text="Login success!")
    else:
        login_success.configure(text_color = "red", text="Login failed.")

def main(elements, twofa_checkbox, root_window) -> None:
    start_time = time.time() # Start program run timer
    print("\nStarting Brute Force Attack...\n")   
    
    #Assigns the corresponding labels from the labels array
    elapsedTimeLabel = elements[0]
    attemptNumberLabel = elements[1]
    passwordAttemptLabel = elements[2]
    passwordDetectedLabel = elements[3]
    optionmenu = elements[4]

    password_list_array = read_passwords_from_file(COMMON_PASSWORD_LIST)
    target_user = optionmenu.get() #Gets the current user selected from the dropdown list
    target_word = get_password(target_user) #Gets the password from the target user
    passwordDetectedLabel.configure(text_color = "white", text="Running Attack...")

    if not target_word:
        print("\nFailed: No valid target password in password secret password file.")
        passwordDetectedLabel.configure(text_color = "red", text="No valid password in file") #Updates passwordDetectedLabel
        return
    
    # Loop through passwords
    if len(password_list_array) > 0:
        attempt = 0
        for word in password_list_array:
            attempt += 1
            print(f"{attempt}. Trying: \"{word}\"")            
            attemptNumberLabel.configure(text=f"Attempt: #{attempt} ") #Updates attemptNumberLabel
            passwordAttemptLabel.configure(text=f"Password: {word}") #Updates passwordAttemptLabel

            end_time = time.time()
            elapsed_time = round(end_time - start_time, 2)
            print(f"Time: {elapsed_time} seconds.")
            elapsedTimeLabel.configure(text=f"{elapsed_time} s") #updates elapsedTimeLabel
            
            root_window.update()  # Refresh UI to show current attempt

            # Check if 2FA is enabled
            if twofa_checkbox.get():
                print("2FA enabled - requesting verification...")

                if not perform_2fa(root_window):
                    print("2FA verification failed or cancelled. Stopping attack.")
                    passwordDetectedLabel.configure(text_color = "red", text="Attack cancelled (2FA failed)")
                    return

            if word == target_word:
                print(f"\nSuccess, the password word was: \"{word}\"")
                passwordDetectedLabel.configure(text_color = "green", text="Password found!") #updates passwordDetectedLabel
                break
        else:
            print("\nFailed: The Common Password List doesn't contain the user's password.")
            passwordDetectedLabel.configure(text_color = "red", text="Password was not found") #updates passwordDetectedLabel
    
    else:
        print("\nFailed: The common password list is empty.")
        passwordDetectedLabel.configure(text_color = "red", text="Password list was empty") #updates passwordDetectedLabel

if __name__ == "__main__":
    #main()
    user_interface() #Temporarily until we move things around to the UI instead of being in the terminal