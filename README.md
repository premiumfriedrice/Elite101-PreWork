# Elite101-PreWork

# Introduction 
The chatbot is a simple chatbot that indentifies a keyword, and matches a response that I set it to. 

# Theme & Usage
The theme of the chatbot is to be a virtual assistant of my fictional fried rice emporium.

# Breakdown
The code first greets you, and then asks how it can help and presents an input which belongs to the receiving_response() function.
When you input, the input first passes through the get_response() function where it is processed for easier use. The code utilises the functions of regex. The re.split function which I set to split the input at every iteration of a blank space, and then passes through the re.sub function which eliminates any punctuation.

After the code is finished processing, it is set as a parameter of match_message() where it is decided how the chatbot should respond to the input. The match_message() function scans the input list for any keywords, and if found, a set of coditional statements are used to match the response to the keyword. The responses are sourced from a list of responses that I have typed, and are then matched to the keyword that was indentified. 

The program runs continuously until the user decides to quit by inputing "no". 

# Sources
here are the sources I used to create this chatbot.
https://docs.google.com/document/d/19SNXkOv7qeXkeEC8hsTcsIxoxYdmCM5ykaRLbKB5yt0/edit?usp=sharing
