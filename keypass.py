import random
import string
import os
import sys

def generate_password(length=8):
    # Define characters to be used in the password
    characters = string.ascii_letters + string.digits + string.punctuation

    # Generate the password
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def get_password_length():
    while True:
        try:
            length = int(input("Enter the length of the password: "))
            if length < 1:
                print("Invalid length. Please enter a positive integer.")
            else:
                return length
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

# Generate a password with the specified length
length = get_password_length()
password = generate_password(length)
print("Generated Password:", password)

# Wait for user input
print("Press Enter to exit, Space to generate a new password, or Backspace to clear:", end=' ')
sys.stdout.flush()

# Check user input
if os.name == 'nt':
    import msvcrt
    while True:
        key = msvcrt.getch()
        if key == b'\r':  # Enter key
            print("\nExiting...")
            # Perform any necessary cleanup or exit actions here
            break
        elif key == b' ':  # Space key
            print("\rReturning to password generation...         ")
            # Re-run the password generation step or perform any necessary actions
            length = get_password_length()
            password = generate_password(length)
            print("\033[2K\rGenerated Password:", password)
            print("Press Enter to exit, Space to generate a new password, or Backspace to clear:", end=' ')
            sys.stdout.flush()
        elif key == b'\x08':  # Backspace key
            # Clear the line and prompt for password length again
            print("\033[2K\r" + " " * 100 + "\033[1A\r", end='')
            length = get_password_length()
            password = generate_password(length)
            print("\033[2K\rGenerated Password:", password)
            print("Press Enter to exit, Space to generate a new password, or Backspace to clear:", end=' ')
            sys.stdout.flush()
else:
    import tty
    import termios
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        tty.setcbreak(sys.stdin.fileno())
        while True:
            key = ord(sys.stdin.read(1))
            if key == 13:  # Enter key
                print("\nExiting...")
                # Perform any necessary cleanup or exit actions here
                break
            elif key == 32:  # Space key
                print("\rReturning to password generation...         ")
                # Re-run the password generation step or perform any necessary actions
                length = get_password_length()
                password = generate_password(length)
                print("\033[2K\rGenerated Password:", password)
                print("Press Enter to exit, Space to generate a new password, or Backspace to clear:", end=' ')
                sys.stdout.flush()
            elif key == 127:  # Backspace key
                # Clear the line and prompt for password length again
                print("\033[2K\r" + " " * 100 + "\033[1A\r", end='')
                length = get_password_length()
                password = generate_password(length)
                print("\033[2K\rGenerated Password:", password)
                print("Press Enter to exit, Space to generate a new password, or Backspace to clear:", end=' ')
                sys.stdout.flush()
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
