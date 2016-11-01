def words(string):
    
    my_string = string.split()
    my_dict = {}
    for item in my_string:
        if item.isdigit()==True:
            item=int(item)
        if item in my_dict:
            my_dict[item] += 1
        else:
            my_dict[item] = 1
    
    return (my_dict)
    

