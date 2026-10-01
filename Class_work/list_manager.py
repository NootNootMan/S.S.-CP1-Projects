#Surabya Satyal Shopping List Manager Period-1

item_list =[]

while True:
    actions = input("What would you like to do? (add, remove, view, exit):")
    if actions == ("add"):
        the_item_add = input("What item would you like to add?")
        item_list.append(the_item_add)
        print("Your list is below: ")
        print(*item_list)
    elif actions == ("remove"):
        the_item_remove = input("What item would you like to remove?")
        item_list.remove(the_item_remove)
        print("Your list is below: ")
        print(*item_list)
    elif actions == ("view"):
        print("Your list is below: ")
        print(*item_list)
    
    
   
    
  