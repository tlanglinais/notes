import re

sentence = "My phone number is 123-456-7890"

# numberRegex = re.compile(r'\d{3}-\d{3}-\d{4}')
numberRegex = re.compile(r'(\d{3})-(\d{3}-\d{4})')

mo = numberRegex.search(sentence)

# print(mo.group())
print(mo.groups())


sentence2 = "I love fruits. I love all sorts of berries and I'm a big fan of strawberries and blueberries"

fruitRegex = re.compile(f'strawberries|blueberries')

mo = fruitRegex.search(sentence2)

print(mo.group())


# Adding in the optional character ?
numberRegex = re.compile(r'(\d{3}-)?(\d{3}-\d{4})')

mo = numberRegex.search(sentence)
print(mo.groups())

# To account for repetition, use the * - it captures 0 or more occurrences
batRegex = re.compile(f'Bat(wo)*man')

# It matches both
mo = batRegex.search("I am Batwoman")
print(mo.group())
mo = batRegex.search("I am Batwowowoman")
print(mo.group())
mo = batRegex.search("I am Batman")
print(mo.group())
# Batman also gets captured


# The + captures 1 or more occurrences
batRegex = re.compile(f'Bat(wo)+man')
mo = batRegex.search("I am Batwoman")
print(mo.group())
mo = batRegex.search("I am Batwowowoman")
print(mo.group())
mo = batRegex.search("I am Batman")
print(mo.group())
# Here Batman does NOT get captured


# findall
phoneRegex = re.compile(f'(\d{3})-(\d{3})-(\d{4})')
phoneRegex.findall('Amy is 425-214-3121 and Bob is 561-654-3121')

# whitespace = \s
regex = re.compile(f'\s\w+')  # capture whitespace then word
regex.findall('this is some text')
# captures [' is', ' some', ' text']

# number = \d
regex = re.compile(r'\d+\s\w+')
regex.findall('12 peaches, 15 lemons and 14 cherries')
# captures ['12 peaches', '15 lemons', '14 cherries']

# ignore characters
vowelRegex = re.compile(r'[^AEIOUaeiou]')
vowelRegex.findall('This is a sentence')
# ['T', 'h', 's', ' ', 's', ' ', ' ', 's', 'n', 't', 'n', 'c']
