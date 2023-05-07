
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from pathlib import Path
import matplotlib.pyplot as plt

source1 = "https://www.flipkart.com/apple-iphone-xs-space-grey-64-gb/p/itmf944ees7rprte?pid=MOBF944E5FTGHNCR&lid=LSTMOBF944E5FTGHNCRAH33S3&marketplace=FLIPKART&srno=s_1_2&otracker=search&otracker1=search&fm=SEARCH&iid=3bdbc1fe-fb28-4b87-b9dd-5cfa9bca72f7.MOBF944E5FTGHNCR.SEARCH&ppt=sp&ppn=sp&ssid=dh4th365ow0000001584871616021&qH=0b3f45b266a97d70"
source2 = "https://www.amazon.in/Apple-iPhone-128GB-Space-Black/dp/B0BDJ22G36/ref=sr_1_1_sspa?crid=1FXH6QQGC4Q4J&th=1"


# create a webdriver object for chrome-option and configure
wait_imp = 10
CO = webdriver.ChromeOptions()
CO.add_experimental_option('useAutomationExtension', False)
CO.add_argument('--ignore-certificate-errors')
CO.add_argument('--start-maximized')
wd = webdriver.Chrome()

print ("*************************************************************************** \n")
print("                     Starting Program, Please wait ..... \n")

print ("Connecting to Flipkart")
wd.get(source1)
wd.implicitly_wait(wait_imp)
f_price = wd.find_element("xpath", '/html/body/div[1]/div/div[3]/div[1]/div[2]/div[2]/div/div[3]/div[1]/div/div')


pr_name = wd.find_element("xpath", '/html/body/div[1]/div/div[3]/div[1]/div[2]/div[2]/div/div[1]/h1/span')
product = pr_name.text
r_price = f_price.text
# print (r_price[1:])
print (" ---> Successfully retrieved the price from Flipkart \n")
time.sleep(2)

print("Connecting to Amazon")
wd.get(source2)
wd.implicitly_wait(wait_imp)
# a_price = wd.find_element_by_id("priceblock_ourprice")
a_price =  wd.find_element("xpath", '/html/body/div[4]/div[2]/div[3]/div[12]/div[14]/div[3]/div[1]/span[2]/span[2]/span[2]')
raw_p = a_price.text
# print (raw_p[2:8])
print (" ---> Successfully retrieved the price from Amazon \n")
time.sleep(2)



# Final display
print ("#------------------------------------------------------------------------#")
print ("Price for [{}] on all websites, Prices are in INR \n".format(product))
print("Price available at Flipkart is: "+r_price[1:])
print("  Price available at Amazon is: "+raw_p[2:8])


new_string = r_price
 
emp_str = ""
for m in new_string:
    if m.isdigit():
        emp_str = emp_str + m
print("Find numbers from string:",emp_str) 

new_string1 = raw_p


emp_str1 = ""
for m in new_string1:
    if m.isdigit():
        emp_str1 = emp_str1 + m
print("Find numbers from string:",emp_str1) 




aa=int(emp_str)
bb=int(emp_str1)


print(aa)

language = ['flipkart', 'amazon']
students = [aa,bb]

plt.bar(language, students)

plt.show()






