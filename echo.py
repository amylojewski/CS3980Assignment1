# echo.py


def echo(text: str, repetitions: int = 3) -> str:
    """Imitate a real-world echo"""

    # Split the text by spaces and get the last word (final word).
    # If the text is empty, it returns an empty string as the final word.
    final_word = text.split()[-1] if text.split() else ""

    # If the final word is neither alphabetic nor numeric, return the original text.
    if not final_word.isalpha() and not final_word.isdigit():
        return text

    # Create a list of "echo" lines. Each line contains a substring of the final word,
    # starting from the last character and reducing by one character with each line.
    echo_lines = [
        final_word[-i:] for i in range(min(repetitions, len(final_word)), 0, -1)
    ]

    # Add a period (".") at the end of the echo lines to simulate the ending of the echo.
    echo_lines.append(".")

    # Join the list of echo lines into a single string with line breaks between them.
    return "\n".join(echo_lines)


# Main program execution
if __name__ == "__main__":
    # Prompt the user to enter some text (simulating yelling at a mountain)
    text = input("Yell something at a mountain: ")

    # Call the echo function and print the result (imitating the echo effect)
    print(echo(text))
