def zadanie(string):

    output = 0
    template = []
    check_rep = []
    
    for s in string:
        S = s.capitalize()
        template.append(S)
    
    for s in string:
        S = s.capitalize()
        template.remove(S)
        #check if already counted
        if S not in check_rep:
            check_rep.append(S)
            #check if occurs more than once
            if S in template:
                    output += 1
            
    print(output)
