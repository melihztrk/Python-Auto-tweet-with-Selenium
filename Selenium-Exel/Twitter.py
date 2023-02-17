from selenium import webdriver
import time
from selenium.webdriver.common.by import By
import random
import requests
from bs4 import BeautifulSoup
from openpyxl import load_workbook







def trends():
  trendlist2=[]
  trendlist3=[]
  trendlist4=[]
  trendlist5=[]
  trendlist6=[]
  trendlist7=[]
  
  url2 ="https://codepedia.info/twitter-trends/united-states"
  url3 ="https://codepedia.info/twitter-trends/united-kingdom"
  url4 ="https://codepedia.info/twitter-trends/france"
  url5 ="https://codepedia.info/twitter-trends/canada"
  url6 ="https://codepedia.info/twitter-trends/germany"
  url7= "https://codepedia.info/twitter-trends/australia"

  
  response2 = requests.get(url2)
  response3 = requests.get(url3)
  response4 = requests.get(url4)
  response5 = requests.get(url5)
  response6 = requests.get(url6)
  response7 = requests.get(url7)

  
  html_icerigi2= response2.content
  html_icerigi3= response3.content
  html_icerigi4= response4.content
  html_icerigi5= response5.content
  html_icerigi6= response6.content
  html_icerigi7= response7.content
  
  soup2 = BeautifulSoup(html_icerigi2,"html.parser")
  soup3 = BeautifulSoup(html_icerigi3,"html.parser")
  soup4 = BeautifulSoup(html_icerigi4,"html.parser")
  soup5 = BeautifulSoup(html_icerigi5,"html.parser")
  soup6 = BeautifulSoup(html_icerigi6,"html.parser")
  soup7 = BeautifulSoup(html_icerigi7,"html.parser")

  

  for t2 in soup2.find_all("a",{"class": "aLnk"}):
    trendlist2.append(t2.text)
    if len(trendlist2)==10:
      break

  for t3 in soup3.find_all("a",{"class": "aLnk"}):
    trendlist3.append(t3.text)
    if len(trendlist3)==10:
      break

  for t4 in soup4.find_all("a",{"class": "aLnk"}):
    trendlist4.append(t4.text)
    if len(trendlist4)==10:
      break

  for t5 in soup5.find_all("a",{"class": "aLnk"}):
    trendlist5.append(t5.text)
    if len(trendlist5)==10:
      break

  for t6 in soup6.find_all("a",{"class": "aLnk"}):
    trendlist6.append(t6.text)
    if len(trendlist6)==10:
      break

  for t7 in soup7.find_all("a",{"class": "aLnk"}):
    trendlist7.append(t7.text)
    if len(trendlist7)==10:
      break
    global alltrend
    alltrend = trendlist2+trendlist3+trendlist4+trendlist5+trendlist6+trendlist7
def iterating_column(path,sheet_name,col):
    workbook = load_workbook(filename =path)
    sheet = workbook[sheet_name]
    global tweetsend
    tweetsend= []
    for cell in sheet[col]:
        tweetsend.append(f"{cell.value}")
    

trends()  
iterating_column("dene.xlsx",sheet_name="Sayfa1",col="A")
 


options = webdriver.ChromeOptions()
driver = webdriver.Chrome()
driver.get("https://twitter.com/i/flow/login")
time.sleep(8)
driver.find_element(By.CSS_SELECTOR, '[autocomplete="username"]').send_keys("#your username")
ileri = driver.find_element(By.CSS_SELECTOR,'[class="css-18t94o4 css-1dbjc4n r-sdzlij r-1phboty r-rs99b7 r-ywje51 r-usiww2 r-2yi16 r-1qi8awa r-1ny4l3l r-ymttw5 r-o7ynqc r-6416eg r-lrvibr r-13qz1uu"]')
ileri.click()
time.sleep(8)
driver.find_element(By.CSS_SELECTOR, '[autocomplete="current-password"').send_keys("#your password")
login = driver.find_element(By.CSS_SELECTOR,'[data-testid="LoginForm_Login_Button"]')
login.click()
time.sleep(7)
post = driver.find_element(By.CSS_SELECTOR,'[class="public-DraftStyleDefault-block public-DraftStyleDefault-ltr"]')
tweet_btn = driver.find_element(By.CSS_SELECTOR,'[data-testid="tweetButtonInline"]')
x=1
def start():
  while x < 100000:
      try:
          
          tweet_btn = driver.find_element(By.CSS_SELECTOR,'[data-testid="tweetButtonInline"]')
          post = driver.find_element(By.CSS_SELECTOR,'[class="public-DraftStyleDefault-block public-DraftStyleDefault-ltr"]')
          post.send_keys(tweetsend[x]+random.choice(alltrend)+random.choice(alltrend)+random.choice(alltrend)+str(random.randint(1, 10000)))
          time.sleep(10)
          tweet_btn.click()
          print("{}. tweet sent...".format(x))
          x += 1
          time.sleep(50)
          if x==100:
            trends()
          if x==200:
            trends()
          if x==300:
            trends()
          if x==400:
            trends()
          if x==500:
            trends()
          if x==600:
            trends()
          if x==700:
            trends()
          if x==800:
            trends()
          if x==900:
            trends()
          if x==1000:
            trends()
          
          
      except:
          print("Element not found, waiting 7 seconds")
          time.sleep(7)
        
start()
driver.quit()



