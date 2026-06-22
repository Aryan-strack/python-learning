 # String Transformation Methods

# 1. upper() - Converts all characters in a string to uppercase.

name = "Aryan"
print(name.upper())  # ARYAN

# 2. lower() - Converts all characters in a string to lowercase.
print(name.lower())  # aryan

# 3. title() - Converts the first character of each word to uppercase and the rest to lowercase.
print(name.title())  # Aryan


# 4. strip() - Removes leading and trailing whitespace from a string.
message = "   Hello, World!   "
print(message.strip())  # "Hello, World!"

# Replace Method

# 5. replace() - Replaces occurrences of a specified substring with another substring.

greeting = "Hello, World!"
new_greeting = greeting.replace("World", "Python")
print(new_greeting)  # "Hello, Python!"

# Split Method

# 6. split() - Splits a string into a list of substrings based on a specified delimiter.

sentence = "Hello, how are you?"
words = sentence.split()  # Default delimiter is whitespace
print(words)  # ['Hello,', 'how', 'are', 'you?']

# 7. join() - Joins a list of strings into a single string using a specified delimiter.
word_list = ['Hello', 'World']
joined_string = ' '.join(word_list)  # Join with a space
print(joined_string)  # "Hello World"