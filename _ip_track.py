'''imports'''
import pygeoip
import requests


my_ip_addr= requests.get('https://api.ipify.org').text
gip=pygeoip.GeoIp('GeoliteCity.dat')
res=gip.record_by_addr(my_ip_addr)

for key, val in res.items():
    print(f'{key} : {val} ')