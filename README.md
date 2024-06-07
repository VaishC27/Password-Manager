# Password-Manager
This Python script is a Password Manager application that uses the Tkinter library for the graphical user interface (GUI). 
It uses the previously built password generator project for generating secure passwords. 
Other Functionalities include copying them to the clipboard, and saving them along with the associated website and email/username to a file. 
Below is a brief explanation of the code:

### Libraries Imported:
1. **Tkinter:** For creating the GUI.
2. **Messagebox:** For displaying popup messages.
3. **Random (randint, choice, shuffle):** For generating random passwords.
4. **Pyperclip:** For copying the generated password to the clipboard.

### Password Generation (`generate_pswd` function):
- **Character Sets:** Lists of letters, numbers, and symbols used for password generation.
- **Password Components:** Randomly selects a set number of letters, symbols, and numbers.
- **Shuffle and Combine:** Shuffles the selected characters and combines them into a final password.
- **Insert and Copy:** Inserts the generated password into the password entry field and copies it to the clipboard.

### Saving Passwords (`save` function):
- **Data Retrieval:** Retrieves the website, email, and password from the input fields.
- **Validation:** Checks if any fields are empty and displays a message if so.
- **Confirmation:** Asks for user confirmation before saving the details.
- **File Writing:** Appends the website, email, and password to a file (`data.txt`) and clears the input fields.

### GUI Setup:
- **Window Setup:** Creates the main application window with a title and padding.
- **Canvas and Image:** Displays a logo image using a canvas widget.
- **Labels and Entries:** Creates input fields for the website, email/username, and password with corresponding labels.
- **Buttons:** Adds buttons for generating passwords and saving the details. Each button is linked to its respective function (`generate_pswd` and `save`).

### Main Loop:
- **Main Loop:** Starts the Tkinter event loop to run the application.

This script provides a functional password manager with an intuitive interface for generating and storing passwords securely.
