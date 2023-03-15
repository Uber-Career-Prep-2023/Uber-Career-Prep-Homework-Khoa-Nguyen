# Two arrays/strings increment/decrement hashmap counts
def hashing(string: str) -> dict:
    hashmap = {}
    for i in string:
        if i in hashmap:
            hashmap[i] = hashmap[i]+1
        else:
            hashmap[i] = 1

    return hashmap

def k_anagrams(s1: str, s2: str, k: int) -> bool:
    if len(s1) != len(s2):
        return False
    else:
        hash1 = hashing(s1)
        hash2 = hashing(s2)
        if hash1 == hash2:  
            return True

        counter = 0
        for i in hash1:
            if i in hash2:
                if hash1[i] > hash2[i]:
                    counter += hash1[i]-hash2[i]

                elif hash1[i] < hash2[i]:
                    counter += hash2[i]-hash1[i]

            else:
                counter += hash1[i]

    return counter <= k







print(k_anagrams("apple", "peach", 1))  # Expected = False

print(k_anagrams("apple", "peach", 2))  # Expected = True

print(k_anagrams("cat", "dog", 3))  # Expected = True

print(k_anagrams("debit curd", "bad credit", 1))  # Expected = True

print(k_anagrams("baseball", "basketball", 2))  # Expected = False

# Time Complexity O(n)
# Space Complexity O(n)
# 35 ish minutes