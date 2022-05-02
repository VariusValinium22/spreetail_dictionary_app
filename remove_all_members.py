# eventually ALL these functions will be adding/drawing from the same {}
# instructions for each. 
# This one is: Add only an existing key to remove ALL of its values

my_dict5 = {'foo': ['bar', 'next', 'now']}    

while True:
    def remove_all_members(input_k):

        for (dict_k, dict_v) in my_dict5.items():
            if dict_k == input_k:
                dict_v.clear()                
                
            if len(dict_v) == 0:
                my_dict5.pop(dict_k) 
                print(f"\n The valueList of Key {dict_k} has been emptied. \n Key removed from dictionary.\n")                
                return                
                
    key = input('Remove ALL members: ')
    remove_all_members(key)
    

