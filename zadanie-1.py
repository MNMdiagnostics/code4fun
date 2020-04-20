def zadanie(string):
    #first element - capital at even
    first = []
    counter = 0
    for s in string:
        if int(counter) % 2 == 0:
            first.append(s)
            counter += 1
        else:
            capital = s.capitalize()
            first.append(capital)
            counter += 1
    separator = ''
    first = separator.join(first)
    
    #second element - capital at odd
    second = []
    counter = 0
    for s in string:
        if int(counter) % 2 != 0:
            second.append(s)
            counter += 1
        else:
            capital = s.capitalize()
            second.append(capital)
            counter += 1
    second = separator.join(second)
    
    #merge and print
    output = [first, second]
    print(output)
