import re 

pattern= re.compile('Search this inside of this text please')

String= 'Search this inside of this text please!'

a= pattern.search(String)
b= pattern.findall(String)
c= pattern.full match(String)
d= pattern.match(String)

print(c)
