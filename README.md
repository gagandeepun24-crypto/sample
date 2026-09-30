# sample
first trail git repository
<br/>
author-Gagan Deep U N(VVCE)
# Palindrome Checker 🔄

A simple and efficient Python tool to check whether a given string is **not** a palindrome (or to check if it is one). It automatically handles capitalization and spaces for accurate results.

---

## 🚀 Features
* **Case-Insensitive:** Treats uppercase and lowercase letters the same (e.g., "Racecar" works).
* **Whitespace-Friendly:** Ignores spaces between words (e.g., "A man a plan a canal Panama").
* **Clean Logic:** Uses efficient Python string slicing and manipulation techniques.

---

## 💻 Code Example

```python
def is_not_palindrome(text):
    # Clean the string: remove spaces and convert to lowercase
    cleaned = "".join(text.lower().split())
    
    # Returns True if it is NOT a palindrome, False otherwise
    return cleaned != cleaned[::-1]

# Examples
print(is_not_palindrome("racecar"))  # Output: False
print(is_not_palindrome("hello"))    # Output: True

