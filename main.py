from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from webdriver_manager.chrome import ChromeDriverManager
import time

class WebAgent():

    def __init__(self):
        # Tsugi-Tsugi login page
        self.url = 'https://m.tsugitsugi.com/login?next=%2Fplan%2Fselect'  
        self.username = ''
        self.password = ''

    def setup_driver(self):
        # Set up Chrome options to ignore SSL errors
        chrome_options = Options()
        chrome_options.add_argument('--ignore-certificate-errors')
        chrome_options.add_argument('--ignore-ssl-errors')
        
        # Initialize driver with options
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
        return driver

    def access_website(self):
        # Initialize the driver
        driver = self.setup_driver()
        
        try:
            # Open the login page
            driver.get(self.url)
            print(f"Successfully opened {self.url}")
            
            # Wait for page to load
            time.sleep(2)
            
            # Find username (email) field by ID and enter username
            username_field = driver.find_element(By.ID, "exampleFormControlInput1")
            username_field.send_keys(self.username)
            print("Entered username")
            
            # Find password field by ID and enter password
            password_field = driver.find_element(By.ID, "exampleFormControlInput2")
            password_field.send_keys(self.password)
            print("Entered password")
                
            # Find and click the login button by class name or XPath
            login_button = driver.find_element(By.CLASS_NAME, "btn-next")  # Using unique class
            login_button.click()
            print("Clicked login button")
            
            # Wait to observe the result
            time.sleep(5)

            # Click the <a> element
            link_element = driver.find_element(By.XPATH, "//a[@href='/']")
            link_element.click()
            print("Clicked the link")
            time.sleep(5)  # Wait to observe the result

            # Locate the <select> element by formcontrolname (or class if preferred)
            select_element = driver.find_element(By.XPATH, "//select[@formcontrolname='area']")
            # Alternative: select_element = driver.find_element(By.CLASS_NAME, "form-select")
            
            # Create a Select object
            select = Select(select_element)
            
            # Select "首都圈（東京）" by value
            select.select_by_value("4")
            print("Selected 首都圈（東京） by value")

            # Locate and click the Search button
            search_button = driver.find_element(By.CLASS_NAME, "blue_btn_ht")
            search_button.click()
            print("Clicked Search button")
            # driver.refresh()
            time.sleep(8)  # Wait to observe the result

                
        except Exception as e:
            print(f"An error occurred: {e}")
        
        finally:
            # Close the browser window and quit the driver
            driver.quit()
            print("Browser closed")

if __name__ == "__main__":
    web_agent = WebAgent()
    web_agent.access_website()