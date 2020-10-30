N = int(input('News from how many pages you required:'))
from selenium import webdriver
News = []
Time = []
print('Page 1 is Processing')
Republic = webdriver.Chrome(executable_path='/home/aadya/0AutomationPython/chromedriver')
Republic.implicitly_wait(1000)
Republic.get('https://www.republicworld.com/india-news/general-news')

for i in range(1,13):
    text = Republic.find_element_by_xpath("/html/body/div[3]/main/div[2]/section/div[3]/div/div/div[1]/div[2]/article["+str(i)+"]/a/div[2]/div[2]/h2")
    time = Republic.find_element_by_xpath("/html/body/div[3]/main/div[2]/section/div[3]/div/div/div[1]/div[2]/article["+str(i)+"]/a/div[2]/div[1]")
    News.append(text.text)
    Time.append(time.text)
Republic.quit()

for i in range(2,N+1):
	print('Page '+str(i)+' is Processing')
	Republic = webdriver.Chrome(executable_path='/home/aadya/0AutomationPython/chromedriver')
	Republic.implicitly_wait(1000)
	Republic.get('https://www.republicworld.com/india-news/general-news/'+str(i))
	for i in range(1,13):
		text = Republic.find_element_by_xpath("/html/body/div[3]/main/div[2]/section/div[3]/div/div/div[1]/div[2]/article["+str(i)+"]/a/div[2]/div[2]/h2")
		time = Republic.find_element_by_xpath("/html/body/div[3]/main/div[2]/section/div[3]/div/div/div[1]/div[2]/article["+str(i)+"]/a/div[2]/div[1]")
		News.append(text.text)
		Time.append(time.text)
	Republic.quit()

print('Starting of CSV File creation')
import pandas as pd
s = pd.DataFrame(News,list(range(len(News))))
s.to_csv('Republic.csv')

print('All Process Completed')
print('Plesae find the file Republic.csv')