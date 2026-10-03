def reverse_string(text):
    """Return the input string reversed."""
    return text[::-1]


def is_palindrome(text):
    """Check if the input string reads the same forwards and backwards."""
    cleaned = text.lower().replace(" ", "")
    return cleaned == cleaned[::-1]


def count_vowels(text):
    """Count the number of vowels in the input string."""
    vowels = "aeiouAEIOU"
    return sum(1 for char in text if char in vowels)