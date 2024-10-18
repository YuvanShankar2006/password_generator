import random
import streamlit as st

# Function to generate password
def create_password(numbers, capital, small, special, length):
    password = []
    characterlist = [
        'ABCDEFGHIJKLMNOPQRSTUVWXYZ',  # Uppercase
        'abcdefghijklmnopqrstuvwxyz',  # Lowercase
        '!@#$%^&*()_+-=[]{}|;:\'",.<>?/',  # Special characters
        '0123456789'  # Numbers
    ]

    for _ in range(capital):
        password.append(random.choice(characterlist[0]))
    for _ in range(small):
        password.append(random.choice(characterlist[1]))
    for _ in range(special):
        password.append(random.choice(characterlist[2]))
    for _ in range(numbers):
        password.append(random.choice(characterlist[3]))

    # Fill the remaining length with random choices from all character sets
    all_characters = ''.join(characterlist)
    while len(password) < length:
        password.append(random.choice(all_characters))

    random.shuffle(password)  # Shuffle to ensure randomness
    return ''.join(password)

# Awareness content for different platforms
awareness_content = {
    "Instagram": (
        "Creating a secure password for Instagram is essential for protecting your account from unauthorized access and potential breaches. "
        "A robust password should be at least 12 characters long and incorporate a mix of upper and lower case letters, numbers, and special symbols. "
        "Avoid easily guessable information like birthdays or common words. Additionally, consider using a password manager to generate and store complex passwords securely. "
        "Regularly updating your password and enabling two-factor authentication can further enhance your account’s security."
    ),
    "LinkedIn": (
        "Creating a secure password for your LinkedIn account is crucial, as it helps protect your professional identity and personal information. "
        "A strong password should be at least 12 characters long, incorporating a mix of uppercase and lowercase letters, numbers, and special symbols. "
        "Avoid using easily guessable details, such as your name or job title. Additionally, consider using a password manager to generate and store complex passwords securely. "
        "Regularly updating your password and enabling two-factor authentication can further enhance your account's security."
    ),
    "Google": (
        "Your Google account serves as a gateway to various services, making it vital to maintain a strong and secure password. "
        "To protect your account, create a password that is at least 12 characters long, featuring a combination of uppercase and lowercase letters, numbers, and special characters. "
        "Steer clear of using common phrases or personal information that could be easily guessed. Utilizing a password manager can help you generate and keep track of unique passwords for different accounts. "
        "Additionally, take advantage of Google's security features, such as two-step verification, to add an extra layer of protection."
    ),
    "Others": (
        "When creating passwords for other accounts, follow similar guidelines: ensure the password is at least 12 characters long, and use a combination of letters, numbers, and special symbols. "
        "Avoid personal information that could be easily guessed. A password manager can help you manage different passwords securely."
    ),
}

# Streamlit App
st.title("Yuvan's Password Generator")

# Dropdown for awareness content
platform = st.selectbox("Select a platform for which you are creating a password for:", list(awareness_content.keys()))
st.subheader(f"{platform} Password Awareness")
st.write(awareness_content[platform])

# User input for password generation
st.header("Generate a Secure Password")
length = st.number_input("Enter the desired length of the password:", min_value=12, max_value=100, value=12)
numbers = st.number_input("Enter number of numbers you need:", min_value=0, value=2)
small = st.number_input("Enter the number of small characters you need:", min_value=0, value=2)
capital = st.number_input("Enter the number of capital characters you need:", min_value=0, value=2)
special = st.number_input("Enter the number of special characters you need:", min_value=0, value=2)

if st.button("Generate Password"):
    if length < (numbers + small + capital + special):
        st.error("The password length must be greater than or equal to the total number of characters requested!")
    else:
        password = create_password(numbers, capital, small, special, length)
        st.success(f"The generated password is: **{password}**")
