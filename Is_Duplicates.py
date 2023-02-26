def Is_Duplicates(anylist):
    try:
        set_list = set(anylist)
        if len(anylist) != len(set_list):
            print('Length of List: ',len(anylist),'\n','Length of Set: ',len(set_list),'\n','Duplicates found in list')
        else:
            print('No Duplicates found in list')
    except:
        return 'an exception occured'
mylist = [5, 3, 5, 2, 1, 6, 6, 4]

Is_Duplicates(mylist)