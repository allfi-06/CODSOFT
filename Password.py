import random
import string

# Prompt user to input desired length of the password
password_length = int(input("Enter the desired length of the password: "))

# Prompt user to input complexity of the password
print("Choose the complexity of the password:")
print("1. Lowercase letters only")
print("2. Uppercase letters only")
print("3. Mixed case letters (both lowercase and uppercase)")
print("4. Letters and digits")
print("5. Letters, digits, and special characters")
complexity = int(input("Enter your choice (1/2/3/4/5): "))

# Define character sets based on complexity choice
if complexity == 1:
    chars = string.ascii_lowercase
elif complexity == 2:
    chars = string.ascii_uppercase
elif complexity == 3:
    chars = string.ascii_letters
elif complexity == 4:
    chars = string.ascii_letters + string.digits
elif complexity == 5:
    chars = string.ascii_letters + string.digits + string.punctuation
else:
    print("Invalid complexity choice!")
    exit()

# Generate the password
password = ''.join(random.choice(chars) for _ in range(password_length))

# Print the generated password
print(f"Generated password: {password}")
