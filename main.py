import re
import random
import string
import order
import responses

isGood = True

def make_order():
  global isGood
  items_list = [] #can hold multiple orders
  
  food_sel_list = [] #list for input before added to order items list
  
  order_price = 0.0
  
  order.display_menu()
  
  food_sel_list.append(input("\nWhat would you like to order?: ").lower())
  
  while isGood:
    food_sel_list.append(input("\nAnything else? type no to proceed: ").lower()) 
    for word in food_sel_list:
      if word == "no":
        isGood = False
      else:
        continue
  
  for item in range(len(order.menu)): #loops through each item in menu
    for food_sel in food_sel_list:
      if food_sel == order.menu[item]["Name"]:
        items_list.append(order.menu[item]["Name"])
        for order_choice in items_list: #each order gets price added total
          if order_choice == order.menu[item].setdefault("Name"):
              order_price += order.menu[item].setdefault("Price")
      elif food_sel == "no":
        isGood = False
          
  if len(items_list) > 0:
      order.checkout(items_list, order_price)
      

def match_message(input): #function that interprets input
  global isGood
  for phrase in responses.responses:
    resp_match = re.search(phrase, input)#searches responses dict keywords for a match with a word in input 
    if resp_match:
      print("Bot: {}".format(random.choice(responses.responses.get(phrase))))
    else:
      pass
  ord = re.search("order", input)#if input has the word order, call make_order()
  if ord:
    make_order()
  end = re.search("bye", input)
  if end:
    isGood = False

    
def receiving_response():
  global isGood
  while isGood:
    user_res = input('\nYou: ').lower()
    unpunct_user_res = user_res.translate(str.maketrans('', '', string.punctuation))
    match_message(unpunct_user_res)


def greeting():
  print("Bot: Hi I am the chatbot for Lloyd's Fried Rice Emporium. How may I assist you today?")


def main():
  greeting()
  receiving_response()


if __name__ == '__main__':
  main()