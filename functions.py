def get_summ(one, two, delimiter='&'):
    one = str(one)
    two = str(two)
    three = delimiter.join((one, two))
    return three.upper()

print(get_summ('Learn', 'Python'))