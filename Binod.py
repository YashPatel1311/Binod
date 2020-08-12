from selenium import webdriver
import subprocess,time,sys
from selenium.webdriver.common.keys import Keys

# Number of times you want to run
n=int(input("Enter number of times you want to run: \n"))

# executing the windows batch file to open chrome
p=subprocess.Popen(r'C:\Users\Yash Patel\Desktop\python\Binod\chrome.bat',shell=True)

# Adding repo's path so that chrome web driver can be called 
# sys.path.append(r'C:\Users\Yash Patel\Desktop\Python\Binod')

# Attaching selenium to opened browser
options= webdriver.ChromeOptions()
options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
options.add_argument("--start-maximized")

driver=webdriver.Chrome(options=options)

# opening youtube
time.sleep(2)
driver.get("https://youtube.com")


if n>0:
    # Clicking the first video from recommendation
    vid1=driver.find_element_by_xpath('//*[@id="video-title"]')
    vid1.click()

i=1

while i<n:

    time.sleep(2)
    driver.execute_script("window.scrollTo(0, 720);")
    time.sleep(2)

    commentbox=driver.find_element_by_xpath('//*[@id="placeholder-area"]')
    commentbox.click()


    comment_input=driver.find_element_by_xpath('//*[@id="contenteditable-root"]')
    comment_input.send_keys('BINOD')

    webdriver.ActionChains(driver).key_down(Keys.CONTROL).key_down(Keys.ENTER).key_up(Keys.CONTROL).key_up(Keys.ENTER).perform()
    time.sleep(2)
    webdriver.ActionChains(driver).key_down(Keys.SHIFT).send_keys('n').key_up(Keys.SHIFT).perform()
    
    i+=1