# Get a response to the input text 'I would like to book a flight.'
response = bot.get_response('I have a complaint.')

print("Bot Response:", response)
name=input("Enter Your Name: ")
print("Welcome to the Bot Service! Let me know how can I help you?")
while True:
    request=input(name+':')
    if request=='Bye' or request =='bye':
        print('Bot: Bye')
        break
    else:
        response=bot.get_response(request)
        print('Bot:',response)
        
        
        
               
