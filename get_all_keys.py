# KEYS
# Returns all the keys in the dictionary. Order is not guaranteed. (SET ???)
# Example
# > ADD foo bar
# ) Added
# > ADD baz bang
# ) Added
# > KEYS
# 1) foo
# 2) baz

# build a dict with lists for values
# return all keys in a dictionary

my_dict1 = {}    
while True:
    def get_all_keys(k, v):
            
        my_dict1[k] = [v]
        
        print('added k: ' + k + "\n      v: " + v)
        
        
    key, value = input('Enter a key and value with a space between them: ').split()
    get_all_keys(key, value)
    print('Current Keys in Dictionary: ' + str(list(my_dict1.keys())) + '\n')
