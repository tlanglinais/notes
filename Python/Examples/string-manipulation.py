# Escape characters
sent = "This is a \n sentence"
print(sent)
# This is a
# sentence

# The r character before a string denotes a "raw" string
rawSent = r"This is a \n sentence"
print(rawSent)
# This is a \n sentence


# Check if word is/isn't in sentence
sent = "Hello World"
'Hello' in sent
# True
'Hello hi' not in sent
# True


# Upper, lower, isUpper, isLower
sent = "I love blueberries"

# Note: upper and lower do not re-assign!
sent.upper()
sent.lower()
sent.islower()
sent.isupper()

# Other similar methods
sent.isalnum
sent.isalpha()
sent.isascii()
sent.isdecimal()
sent.isdigit()
sent.isidentifier
sent.isnumeric()
# there are many more

# Starts with / Ends with
sent = "Ruby is walking the dog"
sent.startswith("Ruby")  # True
sent.endswith("dog")  # True


# Split
