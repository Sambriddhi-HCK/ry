temperature = int (input ('Enter the temperature: '))
humidity = int (input ('Enter the humidity: '))
if temperature >= 85 and humidity > 60: 
    print ('muggy day today') 
elif temperature >= 85: 
    print ('warm, but not muggy today') 
elif temperature >= 65: 
    print ('pleasant today') 
elif temperature <= 45: 
    print ('cold today') 
else: 
    print ('cool today')
