import requests
import re
from bs4 import BeautifulSoup
from unidecode import unidecode
#import smtplib

'''
def email(receivers,price):
    sender = 'digi.ad.dado@gmail.com'
    #receivers = ['to@todomain.com']
    message = """From: From Person <digi.ad.dado@gmail.com>
    To: To Person <%s>
    Subject: digikala advertising

    Hello you use my use my program to now when yuor product is fewer than your intended price.

    now the price of your protect is %i toman. 
    let's go and buy it.
    """ %(receivers,price)
    try:
        smtpObj = smtplib.SMTP('localhost')
        smtpObj.sendmail(sender, receivers, message)         
        print ("Successfully sent email")
    except SMTPException:
        print ("Error: unable to send email")
'''



url = input('please enter url of your product page on digikala: ')
if url == '-1':
    url = 'https://www.digikala.com/product/dkp-2105089/%DA%AF%D9%88%D8%B4%DB%8C-%D9%85%D9%88%D8%A8%D8%A7%DB%8C%D9%84-%D8%B3%D8%A7%D9%85%D8%B3%D9%88%D9%86%DA%AF-%D9%85%D8%AF%D9%84-galaxy-a30s-sm-a307fnds-%D8%AF%D9%88-%D8%B3%DB%8C%D9%85-%DA%A9%D8%A7%D8%B1%D8%AA-%D8%B8%D8%B1%D9%81%DB%8C%D8%AA-64-%DA%AF%DB%8C%DA%AF%D8%A7%D8%A8%D8%A7%DB%8C%D8%AA'
    intended = '3600000'
    receivers = 'a.asgarian2@gmail.com'
else:
    intended = input('please enter intended price: ')
    receivers = input('please enter your e-mail: ')
#url = 'https://www.digikala.com/product/dkp-2105089/%DA%AF%D9%88%D8%B4%DB%8C-%D9%85%D9%88%D8%A8%D8%A7%DB%8C%D9%84-%D8%B3%D8%A7%D9%85%D8%B3%D9%88%D9%86%DA%AF-%D9%85%D8%AF%D9%84-galaxy-a30s-sm-a307fnds-%D8%AF%D9%88-%D8%B3%DB%8C%D9%85-%DA%A9%D8%A7%D8%B1%D8%AA-%D8%B8%D8%B1%D9%81%DB%8C%D8%AA-64-%DA%AF%DB%8C%DA%AF%D8%A7%D8%A8%D8%A7%DB%8C%D8%AA'
#url = 'https://www.digikala.com/product/dkp-2172577/%DA%AF%D9%88%D8%B4%DB%8C-%D9%85%D9%88%D8%A8%D8%A7%DB%8C%D9%84-%D8%B3%D8%A7%D9%85%D8%B3%D9%88%D9%86%DA%AF-%D9%85%D8%AF%D9%84-galaxy-a30s-sm-a307fnds-%D8%AF%D9%88-%D8%B3%DB%8C%D9%85-%DA%A9%D8%A7%D8%B1%D8%AA-%D8%B8%D8%B1%D9%81%DB%8C%D8%AA-128-%DA%AF%DB%8C%DA%AF%D8%A7%D8%A8%D8%A7%DB%8C%D8%AA'
try:
    json = requests.get(url)
    soup = BeautifulSoup(json.text, 'html.parser')
    prisehtml = soup.find_all('div',attrs={"class":"c-product__seller-price-raw js-price-value"})
    #print(prisehtml)
except:
    print('sorry I can not connect to digikala' )



try:
    regex = r"^.*>\n(.*)"
    test_str = (str(prisehtml))
    matches = re.finditer(regex, test_str, re.MULTILINE)
    for matchNum, match in enumerate(matches, start=1):
        for groupNum in range(0, len(match.groups())):
            groupNum = groupNum + 1
            price = match.groups()
    #print(price)
    price = unidecode(price[0])
    price = price.strip()
    print('the price of this product is %s' %(price) )
    price = price.replace(',','')
    #print(price)
except:
    print("soory digikala don't have this product")




try:
    if price <= intended:
        print('wow the price of this product is fewer than you whant \n it is good time to buy it')
        #email(receivers,price)
    else:
        print('sorry it is too expensive yet')
except:
    pass



#TODO find some server to run program evry half-hour
#TODO send e-mail to user if price <= intended (ot don't work)
#TODO make graphical interface
