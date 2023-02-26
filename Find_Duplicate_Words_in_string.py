def Find_Duplicate_Words_in_string(anystr):
    try:    
        Unique_list = []
        Duplicate_list = []

        for i in anystr.split():
            if i not in Unique_list:
                Unique_list.append(i)
            else:
                Duplicate_list.append(i)
        return Duplicate_list
    except:
        return 'an exception occured'
        


text = 'the dog is the best dog'

Find_Duplicate_Words_in_string(text)