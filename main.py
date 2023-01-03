import re
#use dictionary in the future, but can't right now because I want the responses to be able to be used for other input conditions
responses = ['Good Bye.\n', 
             'I\'m sorry. I can\'t help you with that.\n',
             'Okay. Go ahead.\n',
             'We sell our signature Premium Fried Rice and other plates I recommend are the Dragon Fried Rice and the Omurice.\n',
             'Please email our customer service department through lloydsfriedriceemporium@gmail.com for further assistance or call 800-588-2300.\n',
             'We have locations in Round Rock, Pflugerville, Austin, and Georgetown.\n',
             'Our store hours are 8am-9pm everyday.\n'
            ]

def match_message(input): #function that interprets input
  
  if 'no' in input:
    print('Bot: {}'.format(responses[0]))#.format() is used for easier insertion
    isGood = False #breaks loop
  elif 'yes' in input:
    print('Bot: {}'.format(responses[2]))
    receiving_response()#reiterates input function
  elif 'menu' in input:
    print('Bot: {}'.format(responses[3]))
    receiving_response()
  elif 'refund' in input:
    print('Bot: {}'.format(responses[4]))
    receiving_response()
  elif 'location' in input:
    print('Bot: {}'.format(responses[5]))
    receiving_response()
  elif 'time' in input:
    print('Bot: {}'.format(responses[6]))
    receiving_response()
  else:
    print('Bot: {}'.format(responses[1]))
    receiving_response()
    
def get_response(user_input): #function that receives user input 
  split_input = re.split(r"\s+", user_input.lower()) #processes user_input and splits into list by every iteration of space
  processed_input = [re.sub(r'[^\w\s]', '', item) for item in split_input] #processes each item in split_input and removes non-alphanumeric characters
  
  return match_message(processed_input)#inserts split, alphanumeric input as parameter for match_message

def receiving_response():
  get_response(input('You: '))

def greeting():
  print("Bot: Hi I am the chatbot for Lloyd's Fried Rice Emporium. How may I assist you today?\n")

def main():
  greeting()
  receiving_response()

if __name__ == '__main__':
  main()
  
