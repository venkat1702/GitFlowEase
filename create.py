from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import pyperclip
import time
import os
#user credentials
userid='#userid'
password='#userpassword'

repository=input("Enter name of the repository: ")

driver=webdriver.Firefox()
driver.get('https://github.com/login')

user=driver.find_element_by_id('login_field')
user.send_keys(userid)
user_pw=driver.find_element_by_id('password')
user_pw.send_keys(password)
signin=driver.find_element_by_xpath('//*[@id="login"]/form/div[4]/input[9]')
signin.submit()
time.sleep(3)
new_repo=driver.find_element_by_xpath('//*[@id="repos-container"]/h2/a')
new_repo.click()
repo_name=driver.find_element_by_xpath('//*[@id="repository_name"]')
repo_name.send_keys(repository)
read_me=driver.find_element_by_xpath('//*[@id="repository_auto_init"]')
read_me.click()
create_repo=driver.find_element_by_xpath('//*[@id="new_repository"]/div[4]/button')
create_repo.submit()
time.sleep(5)
clone_repo=driver.find_element_by_xpath('/html/body/div[4]/div/main/div[3]/div/div[2]/div[1]/div[2]/span/get-repo/details/summary')
clone_repo.click()
cr_copy=driver.find_element_by_xpath('/html/body/div[4]/div/main/div[3]/div/div[2]/div[1]/div[2]/span/get-repo/details/div/div/div[1]/div/div[1]/div/div/clipboard-copy')
cr_copy.click()
git_url=pyperclip.paste()

os.system('git init')
os.system('touch README.md')
os.system('git add .')
os.system('git status')
os.system('git commit -m "Initial commit"')
os.system('git remote add origin '+git_url)
os.system('git push -f origin master')

print(repository+" repository created !!!")

