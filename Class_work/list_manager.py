# Surabya Satyal Shopping List Manager Period-1 
item_list = [] 

while True: 
    actions = input("What would you like to do? (add, remove, view, exit): ").strip().lower() 
    
    if actions == "add": 
        the_item_add = input("What item would you like to add? ") 
        item_list.append(the_item_add) 
        print("Your list is below: ") 
        print(*item_list) 
        
    elif actions == "remove": 
        the_item_remove = input("What item would you like to remove? ") 
        if the_item_remove in item_list:
            item_list.remove(the_item_remove) 
            print("Your list is below: ") 
            print(*item_list) 
        else:
            print(f"'{the_item_remove}' is not in your shopping list!")
            
    elif actions == "view": 
        print("Your list is below: ") 
        print(*item_list) 
        
    elif actions == "exit":
        print("Goodbye!")
        break
        
    else:
        print("Invalid option, please choose add, remove, view, or exit.")

    
   
    
  
