def is_not_palindrome(text):
  # Clean the string: remove spaces and convert to lowercase for an accurate check
  cleaned = "".join(text.lower().split())

  # Compare the string with its reverse.
  # If they are NOT equal, it returns True (meaning it is NOT a palindrome).
  return cleaned != cleaned[::-1]


# --- Test Examples ---
print(is_not_palindrome("racecar"))  # Output: False (because it IS a palindrome)
print(is_not_palindrome("hello"))  # Output: True (because it is NOT a palindrome)
print(is_not_palindrome("A man a plan a canal Panama"))  # Output: False (it is)