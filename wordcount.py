def words(string):
    ''' this function counts the frequency of occurence of words in a string .
    we first break the string into words'''
    my_string = string.split()
    my_dict={}
    for item in my_string:
        if item.isdigit()==True: #if item is digit we convert it into an int 
            item=int(item)
        if item in my_dict:
            my_dict[item] += 1 #if item already encountered increase the count
        else:
            my_dict[item] = 1 #add new idem into dictionary
    
    return (my_dict)


