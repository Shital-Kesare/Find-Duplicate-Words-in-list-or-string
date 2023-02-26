def Find_Duplicate_Words_in_list(anylist):
    try:
        Unique_list = []
        Duplicate_list = []
        
        for i in anylist:
            if i not in Unique_list:
                Unique_list.append(i)
            else:
                Duplicate_list.append(i)
        return Duplicate_list
    except:
        return 'an exception occured'
    
mylist = [5, 3, 5, 2, 1, 6, 6, 4]

Find_Duplicate_Words_in_list(mylist)