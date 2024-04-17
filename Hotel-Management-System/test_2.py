import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("http://localhost/Hotel-Management-System/")
driver.set_window_size(1366, 738)
driver.find_element(By.XPATH, '/html/body/section[2]/div[2]/div[1]/div/div[2]').click()
driver.find_element(By.NAME, "Emp_Email").click()
driver.find_element(By.NAME, "Emp_Email").send_keys("Admin@gmail.com")
driver.find_element(By.NAME, "Emp_Password").send_keys("1234")
driver.find_element(By.NAME, "Emp_login_submit").click()
driver.find_element(By.CSS_SELECTOR, ".pagebtn:nth-child(3)").click()
driver.switch_to.frame(1)
