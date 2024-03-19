import json
import time
import os
clear = lambda: os.system("cls")

def show_inventory():
  with open("inventory.json","r") as file:
    inventory = json.load(file)
  print(inventory)
    
def update_inventory(current_item):
  inventory= []
  with open("inventory.json","r") as file:
    inventory = json.load(file) 
  inventory.append(current_item["item_name"])  
  with open("inventory.json","w") as file:
    json.dump(inventory,file) 

def show_item(item_choice:int, menu_choice:str, item_data:dict):
  current_item = item_data[menu_choice][item_choice - 1]
  print("")
  print(current_item["item_name"])
  print("")
  print(f"Description: {current_item["visual_description"]}")
  print("")
  print(f"Lore: {current_item["flavour_text"]}")
  print("")
  print(f"Stats: +{current_item["stats"]}")
  print("")
  print(f"Cost: {current_item["cost"]["gold"]} gold {current_item["cost"]["silver"]} silver")
  purchase_choice = input("do you want to buy it? [y/n] ").lower()
  
  if purchase_choice == "y":
    print("thank you for your purchase.")
    update_inventory(current_item) 
  else:  
    main() 

def show_menu(menu_choice): 
  with open("itemData.json","r") as file:
    item_data = json.load(file)
  
  try:
    menu= [(item["item_name"], item["cost"]) for item in item_data[menu_choice]]
  except:
    print("Please enter either: [foods, drinks, specials]")
    main()
    
  for index,(item_name, cost) in enumerate(menu):
    gold = cost["gold"]
    silver = cost["silver"]
    print(f"{index +1}) {item_name}: {gold} gold {silver} silver")
  
  item_choice = int(input(f"Selecet the number that sounds appealing [1 - {len(item_data[menu_choice])}]: "))
  
  if item_choice > len(item_data[menu_choice]):
    print("Please sellect a valid order number.")
    show_menu(menu_choice)  
  show_item(item_choice, menu_choice,  item_data, )
    
def main():
  
  print("Welcome to the Black Tavern")
  print("Inventory")
  print("Foods")
  print("Drinks")
  print("Specials")
  menu_choice = input("What would you like open? ").lower()
  if menu_choice == "inventory":
    show_inventory()
  else:
    show_menu(menu_choice)
  
if __name__ == "__main__":
  main()
