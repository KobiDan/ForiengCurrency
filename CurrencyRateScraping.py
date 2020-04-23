import requests,bs4
from datetime import datetime

r = requests.get('https://www.boi.org.il/currency.xml')
soup = bs4.BeautifulSoup(r.text , features="html.parser")
country = soup.select('country')
currency = soup.select('currencycode')
rate = soup.select('rate')
date = soup.select('last_update')
change = soup.select('change')
filename = date[0].getText()
filename = filename.split('-')
year , month ,day = int(filename[0]), int(filename[1]), int(filename[2])

filename = datetime(year,month,day).strftime('%d.%m.%Y')

print(filename)


file = open(str(filename)+'.txt','w')
for i in range(len(country)):
        if i ==0:
                print(' Country        Currency      Rate          Change')
                file.write('|   Country    |Currency|   Rate    | Change |\n----------------------------------------------\n')
        print('|',country[i].getText() ,' '*(14-len(country[i].getText())),
              '|  ' ,currency[i].getText() ,' '*(5-len(currency[i].getText())) ,
              '|  ' ,rate[i].getText() , ' '*(9-len(rate[i].getText())) ,
              '|  ' ,change[i].getText(),' '*(6-len(change[i].getText())),'|' )
        file.write('|'+country[i].getText() +' '*(14-len(country[i].getText()))+
              '|  ' +currency[i].getText() +' '*(6-len(currency[i].getText())) +
              '|  ' +rate[i].getText() + ' '*(9-len(rate[i].getText())) +
              '|  ' +change[i].getText()+' '*(6-len(change[i].getText()))+'|' +'\n' )
