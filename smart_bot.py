from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import pandas as pd
  
df = pd.read_csv('/Users/pranav_m/Documents/EY Smart Testing/testdata.csv')
driver = webdriver.Chrome('/Users/pranav_m/Documents/EY Smart Testing/chromedriver')

driver.get('https://www.sigfig.com/site/#/signup?next=%2Flanding')
result=[]
time.sleep(1)

for i in df.index:
    
    entry = df.loc[i]

    name_find =  driver.find_element_by_name("username")
    name_find.send_keys(entry['username'])

    email_find =  driver.find_element_by_name("email")
    email_find.send_keys(entry['email'])

    password_find =  driver.find_element_by_name("password")
    password_find.send_keys(entry['password'])

    time.sleep(2)

    submit_find = driver.find_element_by_xpath("/html/body/div[2]/content-wrapper/div/div/div/signup/div/div/form/button")
    submit_find.click()

    expected_string = "https://www.sigfig.com/f/#/plan/signup"
    actual_string = driver.current_url
    
    if (expected_string == actual_string){
        result.append("Passed")
	} 
    else{
		result.append("Failed")
	}

df['result'] = result

driver.close()

    
    
    
    
    
    
    username_find.clear()
    email_find.clear()
    password_find.clear()username_find.clear()








