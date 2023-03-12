'''
Based on Value , we need to find out how many keys are present under dictionary with similar value.

'''
#Who has 'iphone' mobiles 
users = {'kiran':'vivo','Madhu':'iphone','Sunil':'redmi','Usha':'iphone','Siddu':'vivo','deepak':'oneplux','giri':'pixel','chandra':'iphone'}
iphone_users = [x[0] for x in users.items() if(x[1]=='iphone')]
print(iphone_users)
