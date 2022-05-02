# MEMBERS
# Returns the collection of strings(LIST ???) for the given key. Return order is not guaranteed. Returns an error if the key does not exists.
# Example:
# > ADD foo bar
# > ADD foo baz
# > MEMBERS foo
# 1) bar
# 2) baz
# > MEMBERS bad
# ) ERROR, key does not exist

# using the key to return the valueList from user's input_key

my_dict2 = {"foo": ["bar","baz"]}

while True:
    
    def get_value_list(key):    
        if key in my_dict2:
            keyValues = my_dict2.get(key)
            print(keyValues)
            print('\n')
            
        elif key != my_dict2:
            print("ERROR, key does not exist. Please try again. \n")

    choice = input("Enter a key to find it in the dictionary: ")
    get_value_list(choice)

    # key, value = input('Enter a key and value with a space between them \n to add to the dictionary: ').split()
    # findValue(key, value)
    # print('Current Dictionary: ' + str(list(my_dict2.items())) + '\n')


# my_dict3 = {}    
# while True: 
#     def add_pairs(k, v):
#         if k not in my_dict3:
#             my_dict3[k] = [v]
            
#         else:
#             dict_v_list = my_dict3[k]   # capturing the 'valuelist' of the indicated key
#             if v in dict_v_list:        # comparing input v with that list
#                 print('\n value already exists. Cannot be added. \n')
        
#             else: my_dict3[k].append(v)
    
#     key, value = input('Enter a key and value with a space between them \n to add to the dictionary: ').split()
#     add_pairs(key, value)
#     print('Current Dictionary: ' + str(list(my_dict3.items())) + '\n')


# ------------------------------------------------------
# --         Dictionary of Lists MENU                 --
# -- 1. return all keys in the dictionary             --
# -- 2. return value of specified key                 --
# -- 3. add members to list of specified key          --
# -- 4. remove member from list of specified key      --
# -- 5. remove ALL member of a list of specified key  --
# -- 6. clear the dictionary's content                --
# -- 7. see if a key exists in this dictionary        --
# -- 8. see if a member exists in this dictionary     --
# -- 9. remove member from list of specified key      --
# --10. remove member from list of specified key      --
# ------------------------------------------------------