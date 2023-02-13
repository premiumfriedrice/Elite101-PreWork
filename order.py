import random
isGood = True


ordered = [
]
menu = [
  {"Name":"special fried rice", "Price":13.99, "MenuIndex":1},
  {"Name":"dragon fried rice", "Price":10.99, "MenuIndex":2},
  {"Name":"omurice", "Price":9.99, "MenuIndex":3}
]

def address():
  print("\nPlease enter an address: ")
  
  try: 
    building_num = int(input("Building: "))
  except:
    building_num = 0
  
  try:
    street = input("Street: ")
  except:
    street = "Street"
    
  try:
    city = str(input("City: "))
  except:
    city = "City"

  try:
    state = str(input("State: "))
  except:
    state = "State"
    
  try:
    zip = int(input("ZIP: "))
  except:
    zip = 00000
  
  given_address = "{0} {1} {2}, {3} {4}".format(building_num, street, city, state, zip)

  print(given_address)
  
  return given_address

  
def display_menu():
  print("\n **MENU**")
  for item in menu:
    print('--------------------')
    for key, value in item.items():
      print('{0}\t\t{1}'.format(key, value))
  print('--------------------')


#def make_order():
  #global isGood
  #items_list = []

  #order_price = 0.0
  
  #display_menu()
  
  #food_sel = input("\nWhat would you like to order?: ")

  #for item in range(len(menu)):
    #if food_sel == menu[item]["Name"]:
      #items_list.append(menu[item]["Name"])
      #ordered_item = food_sel
    
      #for order_choice in items_list:
        #if ordered_item == menu[item].setdefault("Name"):
          #order_price += menu[item].setdefault("Price")
 
  #checkout_choice = input("\nWould you like to proceed to checkout? ").lower()
  #if checkout_choice == "yes":
   #checkout(items_list, order_price)
  #elif checkout_choice == "no":
    #food_sel = input("What else would you like to order?: ")
    #print(items_list, order_price)
  

def checkout(req_items, n_price): #prints receipt and lets customer know about order progress
  
  branch = "Round Rock"

  delivery_address = address()
  
  order_num = random.randint(1, 1000)

  status = "In Progress"
    
  if status == "In Progress":
    new_order = Order(order_num, status, req_items, n_price, delivery_address, branch) #new Order object
    ordered.append(new_order.details())
    for order in ordered: #prints receipt
      print('\n--------------------')
      for key, value in order.items():
        print('{0}\t\t{1}'.format(key, value))
    print('--------------------')

  
class Order:
  def __init__(self, order_num, status, items, price, delivery_address, branch):
    self.order_num = random.randint(1, 1000)
    self.status = str(status)
    self.items = str(items)
    self.price = float(price)
    self.delivery_address = delivery_address
    self.branch = str(branch)

  def details(self):
    return {
      "OrderID":self.order_num,
      "Status":self.status,
      "Items":self.items,
      "Price":self.price,
      "Address":self.delivery_address,
      "Branch":self.branch
           }