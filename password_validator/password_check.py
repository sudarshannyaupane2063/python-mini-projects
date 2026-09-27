#password validator function

def password():
    while True:
        n = input("Enter your password for validation: ")
        valid = True
        if len(n)<8:
            print("Password required at least 8 characters!")
            valid = False

        space_check = any(char.isspace() for char in n)
        if space_check:
            print("Enter password without space!")
            valid = False

        upper_check = any(char.isupper() for char in n)
        if not upper_check:
            print("Password required at least one uppercase!")
            valid = False

        lower_check = any(char.islower() for char in n)
        if not lower_check:
            print("Password required at least one lowercase!")
            valid = False

        number_check = any(char.isdigit() for char in n)
        if not number_check:
            print("Password required at least one number!")
            valid = False

        special_check = any(not char.isalnum() for char in n)
        if not special_check:
            print("Password required at least one special character!")
            valid = False

        if valid:
            print("Password validated successfully.")
            break

password()
