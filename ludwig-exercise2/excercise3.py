def in_range(value1, value2):
    rangeObject = range(value1, value2)
    length = len(rangeObject)
    if length > 10:
        return True
    else:
        return False

print(in_range(10,19))