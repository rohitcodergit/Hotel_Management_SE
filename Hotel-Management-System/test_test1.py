
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("http://localhost/Hotel-Management-System/")
driver.find_element(By.NAME, "Username").click()
driver.find_element(By.NAME, "Username").send_keys("Rohit Lokhande")
driver.find_element(By.NAME, "Email").click()
driver.find_element(By.NAME, "Email").send_keys("lokhanderohit2020@gmail.com")
driver.find_element(By.NAME, "Password").send_keys("123")
driver.find_element(By.NAME, "user_login_submit").click()
driver.find_element(By.XPATH,'/html/body/nav/ul/li[2]/a').click()
driver.find_element(By.XPATH, '/html/body/section[2]/div/div/div[2]/div[2]/button').click()
driver.find_element(By.XPATH, '/html/body/section[2]/div/div/div[2]/div[2]/button').click()
driver.find_element(By.NAME, "Name").click()
driver.find_element(By.NAME, "Name").send_keys("Rohit Lokhande")
driver.find_element(By.NAME, "Country").click()
driver.find_element(By.XPATH, "//option[. = 'India']").click()
driver.find_element(By.NAME, "Phone").send_keys("09307032542")
driver.find_element(By.NAME, "Email").send_keys("lokhanderohit2020@gmail.com")
driver.find_element(By.NAME, "RoomType").click()
driver.find_element(By.XPATH, "//option[. = 'DELUXE ROOM']").click()
driver.find_element(By.NAME, "Bed").click()
driver.find_element(By.XPATH, "//option[. = 'Single']").click()
driver.find_element(By.NAME, "NoofRoom").click()
driver.find_element(By.XPATH, "//option[. = '1']").click()
driver.find_element(By.NAME, "Meal").click()
driver.find_element(By.XPATH, "//option[. = 'Room only']").click()
check_in_date = "2024-04-18"
check_out_date = "2024-04-21"
driver.execute_script(f"document.getElementsByName('cin')[0].value = '{check_in_date}';")
driver.execute_script(f"document.getElementsByName('cout')[0].value = '{check_out_date}';")
driver.find_element(By.NAME, "guestdetailsubmit").click()
driver.quit()
