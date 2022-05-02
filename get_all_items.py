# same code as return_all_members but with a return of .items() instead of .values()

my_dict10 = {'foo': ['bar', 'next', 'now'], 'fee': ['car', 'mext', 'mow']}    
while True: 
    def get_all_items():
        if len(my_dict10.keys()) == 0:
            print(f"\nThe dictionary is currently empty.\n")
                
        else:
            dict_v_list = my_dict10.items()   
            print(f"\nALL the pairs of every key in this dictionary is:\n  {dict_v_list}\n")
        
    key = input("Hit enter to see all pairs of this dictionary.")
    get_all_items()