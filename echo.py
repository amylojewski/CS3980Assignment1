# echo.py


def echo(text: str, repetitions: int = 3) -> str:
    """Imitate a real-world echo"""
    words = text.split()
    final_word = words[-1] if words else ""

    echo_lines = [final_word[i:] for i in range(min(repetitions, len(final_word)))]
    echo_lines.append(".")

    return "\n".join(echo_lines)


if __name__ == "__main__":
    text = input("Yell something at a mountain: ")
    print(echo(text))
