text  = 'mybird crs 2020'
numbers = []
for word in text.split():
    if word.isdigit():
        numbers.append(word)
print(numbers)