# string_utils.py

def concatenate_strings(str1, str2):
    """Return the concatenation of two strings."""
    return str1 + str2

def reverse_string(s):
    """Return the reversed version of the input string."""
    return s[::-1]

def to_uppercase(s):
    """Convert the input string to uppercase."""
    return s.upper()

def capitalize_words(s):
    """Capitalize the first letter of each word in the input string."""
    return ' '.join(word.capitalize() for word in s.split())
