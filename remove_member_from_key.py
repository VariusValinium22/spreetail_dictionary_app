# REMOVE
# Removes a member from a key. 
# If the last member is removed from the key, the key is removed from the dictionary. 
# If the key or member does not exist, displays an error.

# comparing again the dictionary data to input data.
# implementing .remove function to remove the specified listValue
# implementing .pop on the key to remove the empty key:value pair from the dictionary

my_dict4 = {'foo': ['bar', 'next', 'now']}    

while True:
    def remove_member_from_key(k, v):

        for (dict_k, dict_v) in my_dict4.items():
            if dict_k == k:
                dict_v.remove(v)                
            elif dict_k != k:
                print("That key doesn't exist in this dictionary")

            if len(dict_v) == 0:
                my_dict4.pop(dict_k) 
                print(f"\n The valueList of Key {dict_k} has been emptied. \n Key removed from dictionary.\n")                
                return                
                
    key, value = input('Remove a member: ').split()
    remove_member_from_key(key, value)
    print(my_dict4)