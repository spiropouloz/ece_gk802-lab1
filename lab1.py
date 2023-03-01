##---------##
##Marios Spyropoulos
##up1072763 - HMTY
##ECE_GK802 - Lab1
##---------##

import requests
import datetime

def more(text):
    count = 0
    for line in text.split('\n'):
        print(line)
        count += 1
        if count % 30 == 0:
            reply = input('Show more (y/n)? ')
            if reply == 'n':
                break

#Erwthma 1
url = input("Insert URL: ") 

response = requests.get(url)

##Erwthma 2
html = response.text
more(html)


#Erwthma 3
print("\n------------- HEADERS -------------")  
for key, value in response.headers.items():
    print(key, ':', value)


#Erwthma 4
print('\n------------- Web Server uses: ',response.headers.get('server'),'-------------') #Erwthma 4(a)

cookies = response.cookies
if len(cookies.items()):  
    print("\n------------- COOKIES: YES -------------") #Erwthma 4(b)
    
    for cookie in cookies:
        print(cookie.name,"expires at", datetime.datetime.fromtimestamp(cookie.expires)) #Erwthma 4(c)
    
else:
    print("\n------------- COOKIES: NO -------------\n")


