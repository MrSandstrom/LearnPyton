def tokenize(lines):
    lines_length = len(lines)
    return_array = []

    #print("No lines {}".format(lines_length))

    # test 1
    if (lines_length == 0):
        return return_array
    
    # test 2
    if (lines_length == 1):
        if len(lines[0]) == 0:
            return return_array
    
    # test 3
    if (lines_length == 1):
        data = lines[0]
        #print ("Data='{}'".format(data))
        data = data.strip()
        #print ("Data='{}'".format(data))
    
        if len(data) == 0:
            return return_array

        
    # test4
    if (lines_length == 1):
        tokens = lines[0].split()
        #print ("Before: {}".format(tokens))
        new_tokens = []

        for token in tokens:
            new_tokens.append(token.lower())
        
        #print ("After: {}".format(new_tokens))
        
        return new_tokens
        
        

       
        
    

    
    