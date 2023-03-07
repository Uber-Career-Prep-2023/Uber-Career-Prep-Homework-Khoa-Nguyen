def reverse_vowels(string: str) -> str:
    string = list(string)

    vowels = {"a", "e", "i", "o", "u", "A", "E", "I", "O", "U"}

    counter = 0
    reverse_string = [i for i in string[::-1] if i in vowels]

    for n, i in enumerate(string):
        if i in vowels:
            string[n] = reverse_string[counter]
            counter += 1

    string = "".join(string)

    return string


input1 = "Uber Career Prep"
print(reverse_vowels(input1))  # expected = "eber Ceraer PrUp"

input2 = "xyz"
print(reverse_vowels(input2))  # expected = "xyz"

input3 = "flamingo"
print(reverse_vowels(input3))  # expected = "flominga"

# Time Complexity = O(n)
# Space Complexity = O(n)
