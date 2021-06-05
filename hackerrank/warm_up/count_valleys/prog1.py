def countingValleys(n, s):
    level = valleys = 0
    for step in s:
        level += 1 if step == "U" else -1
        valleys += level == 0 and step == "U"
    return valleys