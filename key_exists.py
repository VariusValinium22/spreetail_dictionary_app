my_dict7 = {'foo': ['bar', 'next', 'now']}   
   
while True:
    def key_exists(k):
        for key in my_dict7:
            if key == k:
                print(f"{k} is a key in this dictionary.")
            else:
                print(f"{k} is not a key in this dictionary.")
        
    key = input('Enter a key to see if it exists in this dictionary: ')
    key_exists(key)


