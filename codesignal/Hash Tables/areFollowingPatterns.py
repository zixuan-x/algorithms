def areFollowingPatterns(strings, patterns):
    if len(strings) != len(patterns):
        return False
        
    mapping = {}
    visited = set()
    for i in range(len(strings)):
        string, pattern = strings[i], patterns[i]
        if pattern in mapping:
            if mapping[pattern] != string:
                return False
        else:
            if string in visited:
                return False
            mapping[pattern] = string
            visited.add(string)
    return True
    