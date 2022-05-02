my_dict9 = {}    
while True: 
    def get_all_members():
        if len(my_dict9.keys()) == 0:
            print(f"\nThe dictionary is currently empty.\n")
                
        else:
            dict_v_list = my_dict9.values()   
            print(f"\nALL the values of every key in this dictionary is:\n  {dict_v_list}\n")
        
    key = input("Hit enter to see all values of this dictionary.")
    get_all_members()
    