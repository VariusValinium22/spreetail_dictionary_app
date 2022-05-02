my_dict = {}

while True:
    def add_keys(k, v):
        if k not in my_dict:
            my_dict[k] = [v]
            print('Added')
        elif k in my_dict:
            dict_v_list = my_dict[k]
            if v not in dict_v_list:
                dict_v_list.append(v)
                print('Added')
            else:
                print('ERROR, member already exists for key')
        
    def get_all_keys():
        if len(my_dict.keys()) == 0:
            print("(empty set)")
        else:
            all_keys = my_dict.keys()
            for i, item in enumerate(all_keys,1):
                print(str(i) +')' + item)
        
    def get_members_by_key(key):
        if key in my_dict:
            all_values = my_dict.get(key)
            for i, item in enumerate(all_values,1):
                print(str(i) +')' + item)            
        elif key != my_dict:
            print("ERROR, key does not exist")

   
    def remove_member_from_key(k, v):
        if len(my_dict.keys()) == 0:
            print("ERROR, key does not exist")
        
        for (dict_k, dict_v) in my_dict.items():
            if k in my_dict:
                if dict_k == k and v in dict_v:
                    dict_v.remove(v)
                    print("Removed")
                elif dict_k == k and v not in dict_v:
                    print("ERROR, member does not exist")
        
                if len(dict_v) == 0:
                    my_dict.pop(dict_k) 
                    return
            else:
                print("ERROR, key does not exist")
    
    
    def remove_all_members(k):
        if k in my_dict:
            for (dict_k, dict_v) in my_dict.items():
                if dict_k == k:
                    dict_v.clear()
                    print("Removed")
                    
                if len(dict_v) == 0:
                    my_dict.pop(dict_k) 
                    return
        else:
            print("ERROR, key does not exist")

    def clear_dict():
            my_dict.clear()               
            print("Cleared")  

    def key_exists(k):
        if k not in my_dict:
            print("false")
        else:
            print("true")

    def member_exists(k, v):
        if k not in my_dict:
            print("false")  
        else:
            dict_v_list = my_dict[k]   
            if v in dict_v_list:        
                print("true")           
            else: print("false")

    def get_all_members():
        if len(my_dict.keys()) == 0:
            print("(empty set)")            
        else:
            # using List Comprehension
            valueList = [val for lst in my_dict.values() for val in lst]
            for i, item in enumerate(valueList,1):
                print(str(i) +') ' + item)

    def get_all_items():
        if len(my_dict.keys()) == 0:
            print("(empty set)")            
        else:
            full_list = []
            for k, v in my_dict.items():    
                value_list = v
                for i in value_list:
                    full_pair = k + ': ' + i
                    full_list.append(full_pair)

            for i, item in enumerate(full_list, 1):
                print(str(i) + ') ' + item)
    
    choice = input("").split()

    try:
        command_dict = {"ADD": add_keys, 
                        "KEYS": get_all_keys, 
                        "MEMBERS": get_members_by_key, 
                        "REMOVE": remove_member_from_key,
                        "REMOVEALL": remove_all_members,
                        "CLEAR": clear_dict,
                        "KEYEXISTS": key_exists,
                        "MEMBEREXISTS": member_exists,
                        "ALLMEMBERS": get_all_members,
                        "ITEMS": get_all_items
                        }
        if choice[0].upper() not in command_dict.keys():
            print("bad command")
        else:
            command_dict[choice[0].upper()](*choice[1:])
   
    except TypeError:
        print('too many or not enough arguments')
