def checkAnagram(s, t):
    if len(s) != len(t):
        return False
    
    if sorted(s) == sorted(t):
        return True
    return False


print checkAnagram("geeksforgeeks", "forgeeksgees")