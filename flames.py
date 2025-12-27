def calculate_flames(name1, name2):
    n1 = list(name1.replace(" ", "").lower())
    n2 = list(name2.replace(" ", "").lower())

    for char in n1[:]:
        if char in n2:
            n1.remove(char)
            n2.remove(char)

    count = len(n1) + len(n2)

    flames = ['Friends', 'Love', 'Affection', 'Marriage', 'Enemy', 'Siblings']
    index = 0

    while len(flames) > 1:
        index = (index + count - 1) % len(flames)
        flames.pop(index)

    return flames[0]
