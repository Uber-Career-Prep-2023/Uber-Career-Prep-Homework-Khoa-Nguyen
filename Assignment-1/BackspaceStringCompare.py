# Stacks
def backspace(string: str) -> str:
    stack = []
    for i in string:
        if i == "#":
            try:
                stack.pop()

            except:
                pass

        else:
            stack.append(i)

    return "".join(stack)


def backspace_string_compare(string_1: str, string_2: str) -> bool:
    string_1 = backspace(string_1)
    string_2 = backspace(string_2)
    return string_1 == string_2


input1_s1 = "abcde"
input1_s2 = "abcde"
print(backspace_string_compare(input1_s1, input1_s2))  # Expected = True

input2_s1 = "#Uber Career Prep"
input2_s2 = "u#Uber Careee#r Prep"
print(backspace_string_compare(input2_s1, input2_s2))  # Expected = True

input3_s1 = "abcdef###xyz"
input3_s2 = "abcw#xyz"
print(backspace_string_compare(input3_s1, input3_s2))  # Expected = True

input4_s1 = "abcdef###xyz"
input4_s2 = "abcdefxyz###"
print(backspace_string_compare(input4_s1, input4_s2))  # Expected = False

# Time Complexity O(n)
# Space Complexity O(n)
# 30 ish minutes