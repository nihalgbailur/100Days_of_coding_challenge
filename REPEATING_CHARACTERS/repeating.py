# Remove repeating chacaters form following string x = "Python is the best programming language"


def remove_repeats(input_string):
    seen = set()  # To keep track of seen characters
    result = []   # To collect non-repeating characters
    for char in input_string:
        if char not in seen:
            seen.add(char)
            result.append(char)
    return ''.join(result)

# Example usage
x = "Python is the best programming language"
result = remove_repeats(x)
a=list(result)
print(a)
