from replit import clear

def add(product_name, price_product):
  product_price[product_name] = price_product
  
def total_purchase(quantity, product_n):
  item_quantity[product_n] = quantity

def product_sequence():
  for numbers in range(length):
    sequence_dictionary[numbers] = product_list[numbers]
  
sequence_dictionary = {}

product_list = []


individual_price = []

str_i_p = ""

ask_continue_loop = True  

item_quantity = {"NAME": "QUANTITY"}

app_status = True

item = ""

ammount = 0

product_price = {"honey" : 400 , "dry fruit": 1200, "apple cider vinegar" : 280, "kashmiri saffon": 800}


while app_status == True:

  length = len(product_price)
  
  for metrial in product_price:
    
    product_list.append(metrial)
    
  product_sequence()

  product_list = []

  clear()
  
  ask = input(str(f"{sequence_dictionary}\n Enter number to pick an item\n or type 'add' to add a product\n").replace(', ',',\n '))
  
  if ask == "add":
    
    add_item_name = input("Name of the item: ")
    
    add_item_price = int(input("price of the item: ₹"))
    
    add(add_item_name, add_item_price)
    
    print(product_price)
    
  else:
    
    for numberz in range(length):
      
      if int(ask) == numberz:
        
        item = sequence_dictionary[numberz]
      
    product_quantity = int(input(f"\nhow many bottles of {item} do you want? \n"))
    
    product_quantity_string = str(product_quantity)
    
    for products in range(product_quantity):
      
      ammount += product_price[item]
      
      individual_price.append(product_price[item])
      
      str_i_p += str(product_price[item])
      
      str_i_p += " + "
      
      
      
        
  
    total_purchase(product_quantity_string, item)
    
    while ask_continue_loop == True:
      
      ask_continue = input("type 'y' to buy more products 'n' to exit :").lower()
    
      if ask_continue == "n":
        
        app_status = False
        
        ask_continue_loop = False
        
      elif ask_continue == "y":
        
        ask_continue_loop = False
        
      else:
        
        print("I didnt get that")
  
    ask_continue_loop = True
    

ask_discount = int(input("\nenter discount \n %"))

discount = ammount * ask_discount / 100

ammount_discount = ammount - discount
  
print(str(item_quantity).replace(', ',',\n '))

if ask_discount == 0:
  
  efg = str_i_p[:-2]
  
  print(f"\n{efg} = {ammount}")
  
else:
  abcd = str_i_p[:-2]
  
  print(f"\n{abcd} = {ammount}")
  
  print(f"\nafter discount ₹{ammount_discount}")
  


  

