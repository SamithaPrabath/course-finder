from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

chrome_options = Options()
# chrome_options.add_argument('--headless') 

driver = webdriver.Chrome('chromedriver.exe', options=chrome_options)

url = 'https://www.topjobs.lk/applicant/vacancybyfunctionalarea.jsp?FA=SDQ&jst=OPEN'

driver.get(url)

table_rows = driver.find_elements(By.XPATH, '//table//tr')

for row in table_rows:
    try:

        # Wait for the new window to open
        driver.execute_script("arguments[0].click();", row)
        wait = WebDriverWait(driver, 10)
        new_window = wait.until(EC.new_window_is_opened)

        # Switch to the new window
        driver.switch_to.window(new_window)

        # Get the URL of the new window
        time.sleep(2)
        new_window_url = driver.current_url
        # print("New Window URL:", new_window_url)

        # Close the new window
        driver.close()

        # Switch back to the original window
        driver.switch_to.window(driver.window_handles[0])
    except Exception as e:
        print("Error:", str(e))
    
    
# table_rows = driver.find_elements_by_xpath('//table//tr')
# for row in table_rows:
#     h2_elements = row.find_elements_by_xpath('.//span')
#     for h2 in h2_elements:
#         print(h2.text)

driver.quit()
