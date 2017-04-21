'''
Created on 17-Apr-2017

@author: manoj
'''

from selenium import webdriver
import os
import csv

chromeDriver = "/home/manoj/workspace2/RedTools/test/chromedriver"
os.environ["webdriver.chrome.driver"] = chromeDriver
driver = webdriver.Chrome(chromeDriver)
driver.get("https://www.betfair.com/exchange/football/coupon?id=2")
list2 = driver.find_elements_by_xpath('//*[@data-sportid="1"]')

couponlist = []
finallist = []
for game in list2[1:]:
    coup = game.find_element_by_css_selector('span.home-team').text
    print(coup)
    couponlist.append(coup)
print(couponlist)

couponlist = [[team] for team in couponlist]
    
print('its done')


outfile = open("./footballcoupons.csv", "wb")
writer = csv.writer(outfile)
writer.writerow(["Games"])
writer.writerows(couponlist)




