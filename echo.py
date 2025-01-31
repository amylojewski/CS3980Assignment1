# echo.py


def echo(text: str, repetitions: int = 3) -> str:
    """Imitate a real-world echo"""
    final_word = text.split()[-1] if text.split() else ""

    if not final_word.isalpha() and not final_word.isdigit():
        return text

    echo_lines = [
        final_word[-i:] for i in range(min(repetitions, len(final_word)), 0, -1)
    ]
    echo_lines.append(".")

    return "\n".join(echo_lines)


if __name__ == "__main__":
    text = input("Yell something at a mountain: ")
    print(echo(text))
