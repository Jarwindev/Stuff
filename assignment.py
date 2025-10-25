#!/usr/bin/env python

""" DV044G - LAB ASSIGNMENT 4
You find the description for the assignment in Canvas, where each detail regarding requirements is
stated. Below you find the inherent code, some of which is fully defined. You add implementation
for those functions which are needed.

Grade G:
- authenticate_user(credentials: str)
- format_username(username: list[str])
- main()

Grade VG (optional):
- None
"""

def format_username(username: list[str]) -> str:
    """Procedure to format user provided username"""

    ''' PSEUDO CODE
    FORMAT first_name letter of first name to be UPPERCASE
    FORMAT first_name letter of last_name name to be UPPERCASE
    FORMAT remaining letters as lowercase
    REPLACE empty space between first_name name and last_name name with UNDERSCORE
    RETURN formatted username as string value
    '''
    
    parts = [p.strip() for p in username]

    # First name is the first_name element, last_name is the rest joined together.
    first_name = parts[0]
    last_name = " ".join(parts[1:])

    # Capitalize first letter and make remaining lowercase for both parts.
    first_name_formatted = first_name[0].upper() + first_name[1:].lower()

    last_name = last_name.strip()
    last_name_formatted = last_name[0].upper() + last_name[1:].lower()
    return f"{first_name_formatted}_{last_name_formatted}"

def calculate_rotation_seed(password: str) -> int:
    """Procedure to calculate rotation seed for user provided password"""

    ''' PSEUDO CODE
    REPEAT for each character in password
        DETERMINE Unicode value
        MULTIPLY Unicode value by character position
        ADD result to a running total
    DIVIDE running total with password length using integer division
    RETURN calculated rotation seed as INT value
    '''

    # The total value of the characters of the password is initialized to zero.
    total = 0

    for i in range(len(password)):
        character = password[i]                  # Accesses characters by index.
        unicode_value = ord(character)           # Gets their respective Unicode value.
        position = i + 1                    # Uses 1-based indexing.
        total += unicode_value * position   # Adds the product for each character to the running total.
    
    # The rotation seed is calculated by dividing the total with the length of the password using integer division.
    rotation_seed = total // len(password)

    # The function finally returns the calculated rotation seed as an integer.
    return rotation_seed

def decrypt_password(password: str) -> str:
    """Procedure used to decrypt user provided password"""
    rot7, rot9 = 7, 9       # Rotation values. MAY NOT BE MODIFIED!!
    vowels = "AEIOUaeiou"   # MAY NOT BE MODIFIED!!
    decrypted = str()       # DO NOT MODIFY DATA TYPE
    rotation_seed = int()   # DO NOT MODIFY DATA TYPE

    ''' PSEUDO CODE
    [VG] SEND password for REORDERING by using devoted function. STORE return value in 'password'.
    REPEAT for each character in password
        DETERMINE if char IS VOWEL
        DETERMINE ROTATION KEY to use
        DETERMINE decryption value
        ADD decrypted value to decrypted string
    RETURN decrypted string value
    '''   
    
    # Reorders the password based on the rotation seed calculated by the function calculate_rotation_seed.
    rotation_seed = calculate_rotation_seed(password)
    password = reorder_password(password, rotation_seed)

    # ASCII interval ends, 33 and 126, in literals.
    ascii_min = 33
    ascii_max = 126

    # Initiated to 0, which is even.
    traversal = 0  

    for character in password:

        # Alternates between rot7 and rot9 for each character in the password, since traversal is incremented for each character.
        if traversal % 2 == 0:
            rotation_key = rot7 
        else: 
            rotation_key = rot9
        
        # Determines the Unicode value of the character,
        unicode_value = ord(character)

        # and checks if adding the rotation key would exceed the ASCII max value.
        # If it does, it wraps around to the beginning of the ASCII printable characters.
        if unicode_value + rotation_key > ascii_max:
            rotated = ascii_min + (unicode_value + rotation_key - ascii_max - 1)

        # Otherwise, it simply adds the rotation key to the Unicode value.
        else:
            rotated = unicode_value + rotation_key
        decrypted_character = chr(rotated)

        # If the original character is a vowel, it is preceded and succeeded by "0".
        # Each character gets added to the decrypted password.
        if character in vowels:
            decrypted += "0" + decrypted_character + "0"
        else:
            decrypted += decrypted_character

        # Increment traversal to alternate rotation key for next character.
        traversal += 1

    # Returns the fully decrypted password as a string.
    return decrypted

def reorder_password(password: str, rotation_seed: int) -> str:
    """Procedure used to reorder password based on rotation seed"""
    reordered = str()  # DO NOT MODIFY DATA TYPE

    ''' PSEUDO CODE
    DETERMINE reordering TYPE to use
    TYPE: 0
        REVERSE the entire password
        STORE result in variable 'reordered'
    TYPE: 1
        SWAP every second character
        STORE result in variable 'reordered'
    TYPE: 2
        DETERMINE number of positions to shift
        ROTATE password RIGHT by 'shift' positions
        STORE result in variable 'reordered'

    RETURN reordered password
    '''
    
    # Determines the type of reordering to be used based on the rotation seed modulo 3.
    reorder_type = rotation_seed % 3 

    # If the reorder type is 0, the password is simply reversed.
    if reorder_type == 0:
        reordered = password[::-1]

    # If the reorder type is 1, every second character is swapped with the previous one.
    # This is done using a while loop that iterates through the password in steps of 2.
    elif reorder_type == 1:
        reordered = ''
        i = 0
        while i < len(password) - 1:
            reordered += password[i + 1] + password[i]
            i += 2
        if i < len(password):
            reordered += password[i]

    # If the reorder type is 2, the password is rotated to the right by a number of positions determined 
    # by the rotation seed modulo the length of the password.
    else:
        shift = rotation_seed % len(password)
        reordered = password[-shift:] + password[:-shift]

    # The function finally returns the reordered password.
    return reordered

def authenticate_user(credentials: str) -> bool:
    """Procedure for validating user credentials"""
    agents = {  # Expected credentials. MAY NOT BE MODIFIED!!
        # Format: {formatted_username: [grade G decrypted, grade VG decrypted]}
        "Chevy_Chase": ["i0J0u0j0u0J0Zys0r0{", "i0J0u0j0u0J0Zys0r0{"],  # cipher: bAnanASplit
        "Dan_Aykroyd": ["i0N00h00~0[$", "[$i0N00h00~0"],                # cipher: bEauTy
        "John_Belushi": ["J0j0S%0V0w0L0", "u0N0J0j0S%0V0"]              # cipher: CaLzOnE
    }
    user_tmp = pass_tmp = str()

    """ PSEUDO CODE
    PARSE string value of 'credentials' into its components: username AND password
    SEND parsed username for FORMATTING by using devoted function. STORE return value in 'user_tmp'.
    SEND parsed password for DECRYPTION by using devoted function. STORE return value in 'pass_tmp'.
    VALIDATE that both values corresponds to expected credentials existing within dictionary 'agents'
    RETURN outcome of validation as BOOLEAN VALUE
    """

    # Finds the index of the second space in the credentials to separate username and password.
    index_cred = len(credentials) - credentials[::-1].find(" ") - 1

    # Divides the credentials into two parts: username, and password.
    password = credentials[index_cred + 1:]
    username = credentials[0:index_cred]

    # Sends the username to be formatted by using the function format_username and
    # stores the formatted username in the variable formatted_username.
    # Split the username into parts (first_name and last_name name) and pass as list to
    # format_username which expects a list of name parts.
    username_list = username.split()
    user_tmp = format_username(username_list)

    # Sends the password to be decrypted by using the function decrypt_password and
    # stores the decrypted password in the variable decrypted_password.
    pass_tmp = decrypt_password(password)

    # Validate credentials: check that the formatted username exists in the agents
    # dictionary and that the decrypted password matches one of the stored
    # accepted passwords for that user (grade G or grade VG).
    if user_tmp in agents and pass_tmp in agents[user_tmp]:
        return True
    else:
        return False


def main():
    """The main program execution."""

    PROMPT = "Enter your credentials: "  # DO NOT MODIFY CONSTANT VALUES
    credentials = str()                  # DO NOT MODIFY DATA TYPE
    is_authenticated = False             # DO NOT MODIFY DATA TYPE

    ''' PSEUDO CODE
    PROMPT user to enter their credentials
    STORE user input in variable 'credentials'
    SEND credentials for authentication and STORE return value in variable 'is_authenticated'
    PRINT SUCCESS or FAILED message

    Example input:
        joHn BElusHI CaLzOnE

    Expected output:
        Authentication successful. User may now access the system!
    
    Example input:
        joHn BElusHI calzone

    Expected output:
        Authentication failed. Program exits...
    '''

    # Prompts the user with the message "Enter your credentials: " and reads the input using input().
    # Stores the input string in the variable credentials.
    credentials = input(PROMPT)

    # Sends the credentials to be authenticated by using the function authenticate_user and
    # stores the boolean return value in the variable is_authenticated.
    is_authenticated = authenticate_user(credentials)

    if is_authenticated:
        print("Authentication successful. User may now access the system!")
    else:
        print("Authentication failed. Program exits...")

''' PSEUDO CODE
CALL function to start program execution
'''

# Calls the main function to start program execution.
if __name__ == "__main__":
    main()