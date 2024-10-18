# Yuvan's Password Generator

This is a simple password generator web app built using Streamlit. It generates secure passwords based on user-defined parameters like the number of capital letters, small letters, numbers, and special characters. Additionally, the app provides security awareness tips for creating strong passwords across various platforms like Instagram, LinkedIn, and Google.

## Features

- **Customizable Passwords**: Users can define the length of the password and the number of capital letters, small letters, numbers, and special characters.
- **Platform-Specific Security Awareness**: Provides password security awareness content for Instagram, LinkedIn, Google, and others to help users create strong and secure passwords.
- **Random Password Generation**: Generates a random password based on the user's preferences and ensures proper randomness by shuffling the characters.
- **User-friendly Interface**: Simple and intuitive interface built using Streamlit.

## Technologies Used

- **Python**: Main programming language used to develop the app.
- **Streamlit**: Python library used to build the web interface for the password generator.
- **Random**: Python's `random` module is used to generate random characters for the password.

## Installation

To run this project locally, follow these steps:

1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/password-generator.git
   cd password-generator
   ```

2. **Create a virtual environment (optional but recommended):**
   ```bash
   python -m venv venv
   source venv/bin/activate  # For Linux/Mac
   .\venv\Scripts\activate   # For Windows
   ```

3. **Install the required dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the app:**
   ```bash
   streamlit run app.py
   ```

The app should now be running on `http://localhost:8501/`.

## How to Use

1. Choose the platform (e.g., Instagram, LinkedIn, Google, or Others) for which you want to create a password.
2. Input the desired length and the number of capital letters, small letters, numbers, and special characters.
3. Click the "Generate Password" button to get a secure, randomly generated password.
4. If the total number of characters exceeds the chosen length, an error message will be displayed.

## File Structure

- `app.py`: Main Python file that contains the Streamlit app logic.
- `requirements.txt`: Lists the dependencies required to run the app.
- `README.md`: Project documentation file (this file).

## Contributing

Contributions are welcome! If you'd like to improve this project or report any issues, feel free to open a pull request or issue in the repository.
