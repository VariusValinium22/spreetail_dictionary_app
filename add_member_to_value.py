# ADD
# Adds a member to a collection for a given key. Displays an error if the member already exists for the key.
# > ADD foo bar
# ) Added
# > ADD foo baz
# ) Added
# > ADD foo bar
# ) ERROR, member already exists for key

# Chose to use a list for the values in the dictionary
# Adding a value to a list of a given key. 
# Displays an error by comparing the input value against the valueList of the input key.
# RESEARCH: Need to either indicate the initial value added as a list [v] OR use defaultdict import 
# https://stackoverflow.com/questions/23699432/cannot-append-string-to-dictionary-key

# it seems there are two sets of data needed to keep in mind here: 
#           -dictionary variables
#           -input variables
# These were used to compare for insuring the user's input_key exists in the current dictionary and...
# to seperate the 'valueList' away into a seperate variable and compare if the input_value is in this list 
  



my_dict3 = {}    
while True: 
    def add_member_to_value(k, v):
        if k not in my_dict3:
            my_dict3[k] = [v]
            
        else:
            dict_v_list = my_dict3[k]   # capturing the 'valuelist' of the indicated key
            if v in dict_v_list:        # comparing input v with that list
                print('\n value already exists. Cannot be added. \n')
        
            else: my_dict3[k].append(v)
    
    key, value = input('Enter a key and value with a space between them \n to add to the dictionary: ').split()
    add_member_to_value(key, value)
    print('Current Dictionary: ' + str(list(my_dict3.items())) + '\n')





# my_dict3 = {}    
# while True:
#     def add_pairs(k, v):
#         if k not in my_dict3:
#             my_dict3[k] = [v]
#         elif (k, v) not in my_dict3:
#             my_dict3[k] += [v]
#         elif (k, v) in my_dict3:
#             print("Error: that value already exists in the key given.")
            
            
#     key, value = input('Enter a key and value with a space between them: ').split()
#     add_pairs(key, value)
#     print('Current Dictionary: ' + str(list(my_dict3.items())) + '\n')

#     def remove_pairs(k, v):
#         if (k, v) in my_dict3:
#             my_dict3[k] -= [v]

