my_dict = {'foo': ['bar', 'next', 'now'], 'boo': ['far', 'bext', 'bow']}    
while True: 
    def member_exists(k, v):
        if k not in my_dict:
            print(f"\nThe key '{k}' is not in this dictionary. Please check your entry. \n")
            
        else:
            dict_v_list = my_dict[k]   
            if v in dict_v_list:        
                print("true")
        
            else: print("false")
    
    key, value = input("Enter a key and value with a space between them \n to find them in this dictionary: ").split()
    member_exists(key, value)
    print('Current Dictionary: ' + str(list(my_dict.items())) + '\n')
    

