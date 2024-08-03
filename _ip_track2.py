'''imports'''

from urllib import request
import geolite2 from geolite2
import requests

def my_ip_location(my_ip):
    reader=geolite2.reader()
    location=reader.get(my_ip)
    
    #geolite database dict values and fine tunning
    a=(location['city']['name']['en'])
    b=(location['continent']['names']['en'])
    c=(location['country']['names']['en'])
    d=(location['location'])
    e=(location['postal'])
    f=(location['registered_country']['names']['en'])
    g=(location['subdivisions'][0]['names']['en'])
    
    print('''city: %s\ncontinent: %s\ncountry: %s\nlocation: %s\npostal: %s\nregistered_country: %s\nsubdivisions: %s'''%(a,b,c,d,e,f,g))
    
    
    my_ip=request.get('https://api.ipify.org').text
    
    my_ip_location(my_ip)