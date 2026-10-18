from collections import deque


def is_palindrome(text: str) -> bool:
    """Повертає True, якщо рядок є паліндромом (без урахування регістру та пробілів)."""
    chars = deque(ch for ch in text.lower() if not ch.isspace())

    # Порівнюємо символи з обох кінців. Для непарної довжини
    # середній символ залишається в черзі і не потребує перевірки.
    while len(chars) > 1:
        if chars.popleft() != chars.pop():
            return False
    return True


if __name__ == "__main__":
    examples = [
        "А роза упала на лапу Азора",  # непарна кількість символів
        "Abba",                        # парна кількість символів
        "Never odd or even",
        "Was it a car or a cat I saw",
        "level",
        "Python",
        "ab",
        "a",
        "",
    ]
    for example in examples:
        print(f"{example!r}: {is_palindrome(example)}")
