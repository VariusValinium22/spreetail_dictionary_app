import os
# looking to incorporate this code into the above code...might keep it apart and retrieve these functions from one main menu/file
# want to be make entries to the dict and then look them up. This can be accomplished with a 'go back to menu' and then choose '3-Add members'
while True:
    def get_all_keys():
        print("ADD foo bar")
        my_dict['foo'] = 'bar'
        print("Added")
        print("ADD baz bang")
        my_dict['baz'] = 'bang'
        print("Added")        
            
        keyValues = my_dict.keys()
        for i, item in enumerate(keyValues,1):
            print(str(i) +')' + item)
    
    def get_value_list(): 
        my_dict = {}
        print("ADD foo bar")
        my_dict['foo'] = ['bar']
        print("ADD foo baz")
        my_dict['foo'].append('baz')
        print("MEMBERS foo")
        keyValues = my_dict.get('foo')

        for i, item in enumerate(keyValues,1):
                print(str(i) +')' + item)

        if 'bad' not in keyValues:
            print("MEMBERS bad")
            print("ERROR, key does not exist.")       

    def add_member_to_value():
        my_dict = {}
        print("ADD foo bar")
        my_dict['foo'] = ['bar']
        print("Added")
        print("ADD foo baz")
        my_dict['foo'].append('baz')
        print("Added")
        print("ADD foo bar")
        
        dict_v_list = my_dict['foo']   
        if 'bar' in dict_v_list:
            print('ERROR, member already exists for key')
    
        else: my_dict['foo'].append('bar')

    def remove_member_from_key(): 
        print("ADD foo bar")
        my_dict['foo'] = ['bar']
        
        print("Added")
        print("ADD foo baz")
        my_dict['foo'].append('baz')
        
        print("REMOVE foo bar")
        for k, v in my_dict.items():
            v.remove('bar')
        print("Removed")
        
        print('REMOVE foo bar')
        for k, v in my_dict.items():
            if 'bar' in v:
                v.remove('bar')
            else:
                print('ERROR, member does not exist')
                
        print("KEYS")
        keyValues = my_dict.keys()
        for i, item in enumerate(keyValues,1):
            print(str(i) +')' + item)
        print('REMOVE foo baz')
        for k, v in my_dict.items():
            if 'baz' in v:
                v.remove('baz')
            else:
                print('ERROR, member does not exist')
        print("Removed")
                
        print("KEYS")
        for k, v in my_dict.items():
            keyValues = my_dict.items()    
            if len(v) == 0:
                print("empty set")
                      
        print('REMOVE boom pow')
        for k, v in my_dict.items():
            if 'boom' in my_dict.items():
                v.remove('pow')
            else: 
                print("ERROR, key does not exist")

    def remove_all_members(): 
        print("ADD foo bar")
        my_dict['foo'] = ['bar']
        
        print("Added")
        print("ADD foo baz")
        my_dict['foo'].append('baz')
        print("Added")
        print("KEYS")
        keyValues = my_dict.keys()
        for i, item in enumerate(keyValues,1):
            print(str(i) +')' + item)
        
        print("REMOVEALL foo")
        my_dict.pop('foo')
        print("Removed")        
        
        print("KEYS")
        if len(my_dict) == 0:
                print("(empty set)")
        else:
            print(my_dict.keys())
        
        print("REMOVEALL foo")
        
        remove_key = my_dict.pop("foo", None)
    
        if remove_key != None:
            print("Removed")
        else:
            print("ERROR, key does not exist")

    def remove_dict(): 
        print("ADD foo bar")
        my_dict['foo'] = ['bar']
        print("Added")
        
        print("ADD bang zip")
        my_dict['bang'] = ['zip']
        print("Added")
        
        print("KEYS")
        if len(my_dict) == 0:
            print("(empty set)")
        else:
            keyValues = my_dict.keys()
            for i, item in enumerate(keyValues,1):
                print(str(i) +')' + item)
        
        print("CLEAR")
        my_dict.clear()               
        print("Cleared")
        
        print("KEYS")
        if len(my_dict) == 0:
            print("(empty set)")
        else:
            keyValues = my_dict.keys()
            for i, item in enumerate(keyValues,1):
                print(str(i) +')' + item)
        
        print("CLEAR")
        my_dict.clear()               
        print("Cleared")
        
        print("KEYS")
        if len(my_dict) == 0:
            print("(empty set)")
        else:
            keyValues = my_dict.keys()
            for i, item in enumerate(keyValues,1):
                print(str(i) +')' + item)

    def key_exists(): 
        print("KEYEXISTS foo")
        if len(my_dict) == 0:
            print("False")
        else:
            print("True")        
        
        print("ADD foo bar")
        my_dict['foo'] = ['bar']
        print("Added")
        
        print("KEYEXISTS foo")
        if len(my_dict) == 0:
            print("False")
        else:
            print("True")

    print(" ------------------------------------------------------------------------------")
    print(" --                      Dictionary of Lists MENU                            --")
    print(" -- 1. return all keys in the dictionary                                     --")
    print(" -- 2. return the collection of strings for the given key                    --")
    print(" -- 3. add a member to a collection of a given key                           --")
    print(" -- 4. Removes a member from a key.                                          --")
    print(" -- 5. Remove all members for a key and remove the key from the dictionary.  --")
    print(" -- 6. Removes all keys and all members from the dictionary.                 --")
    print(" -- 7. Returns whether a key exists or not.                                  --")
    print(" -- 8. Returns whether a member exists within a key.                         --")
    print(" -- 9. Returns all the members in the dictionary                             --")
    print(" --10. Returns all keys in the dictionary and all of their members.          --")
    print(" --11. Exit this program                                                     --")
    print(" ------------------------------------------------------------------------------")

    choice = input("Please choose a number: ")

    my_dict = {}
    if choice == '1':
        get_all_keys()
    if choice == '2':
        get_value_list()    
    if choice == '3':
        add_member_to_value()    
    if choice == '4':
        remove_member_from_key()
        my_dict = {}
    if choice == '5':
        remove_all_members()
        my_dict = {}
    if choice == '6':
        remove_dict()
        my_dict = {}
    if choice == '7':
        key_exists()
        my_dict = {}
    if choice == '8':
        get_value_list()
        my_dict = {}
    if choice == '9':
        get_value_list()
        my_dict = {}
    if choice == '10':
        get_value_list()
    if choice == '11':
        print('Have a nice day!')
        os.system('clear')
        break
        







