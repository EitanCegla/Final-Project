from selenium import webdriver
driver = webdriver.Chrome(executable_path='C:/Users/Eitan_Cegla/Desktop/Eitan/DevOps/Class 3/chromedriver.exe')
driver.get("http://192.168.99.100:5000")
con_txt = driver.find_element_by_tag_name("body")
print(con_txt.text)
