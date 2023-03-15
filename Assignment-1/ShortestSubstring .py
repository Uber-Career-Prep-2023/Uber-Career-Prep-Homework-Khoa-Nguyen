def shortest_sub_string(string: str, target: str) -> int:
    hashmap = {}
    for n, i in enumerate(string):
        if i in target:
            hashmap[n] = i

    lst2 = list(hashmap.values())
    lst = list(hashmap.keys())
    print(lst)

    for i in range(0,len(lst)):
        print(lst2[i:len(lst2)])

    l = lst[0]
    r = lst[0]








print(shortest_sub_string("abracadabra", "abc")) # expected = 4

print(shortest_sub_string("zxycbaabcdwxyzzxwdcbxyzabccbazyx", "zzyzx")) # expected = 10

print(shortest_sub_string("dog", "god")) # expected = 3

# 40 min limit