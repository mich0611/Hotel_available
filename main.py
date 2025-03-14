from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from webdriver_manager.chrome import ChromeDriverManager
import time
from datetime import datetime

class WebAgent():

    def __init__(self):
        # Tsugi-Tsugi login page
        self.url = 'https://m.tsugitsugi.com/login?next=%2Fplan%2Fselect'  
        self.username = 'michaelchen0611@gmail.com'
        self.password = 'HaveFun2!'

    def setup_driver(self):
        # Set up Chrome options to ignore SSL errors
        chrome_options = Options()
        chrome_options.add_argument('--ignore-certificate-errors')
        chrome_options.add_argument('--ignore-ssl-errors')
        
        # Initialize driver with options
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
        return driver
    
    def return_area_value(self, area_dict, area_name = "伊豆"):
        for key in area_dict.keys():
            if area_name in key:
                return key, area_dict[key]
        return None
    
    # def traverse_hotels(self, driver):
    #         # Find buttons with exact class "btn btn-primary px-4" and text "資訊", excluding those with "ms-2"
    #         buttons = WebDriverWait(driver, 10).until(
    #             EC.presence_of_all_elements_located((
    #                 By.XPATH, 
    #                 "//button[@class='btn btn-primary px-4' and contains(text(), '資訊') and not(contains(@class, 'ms-2'))]"
    #             ))
    #         )
    #         num_buttons = len(buttons)
    #         print(f"Found {num_buttons} buttons to traverse")

    #         original_window = driver.current_window_handle
    #         try:
    #             button = buttons[0]  # Get only the first button
    #             print("Clicking first button")
                
    #             # Scroll to the button and click it
    #             ActionChains(driver).move_to_element(button).click().perform()
    #             time.sleep(3)  # Wait for page to load
    #             print(f'driver current handlers: {len(driver.window_handles)}')
                
    #             confirm_button = WebDriverWait(driver, 10).until(
    #                 EC.element_to_be_clickable((
    #                     By.XPATH, 
    #                     "//button[contains(@class, 'btn btn-primary btn-next px-5') and contains(text(), '確認、預訂空房')]"
    #                 ))
    #             )
    #             print("Found '確認、預訂空房' button")
                
    #             # Scroll to and click the "確認、預訂空房" button
    #             ActionChains(driver).move_to_element(confirm_button).click().perform()
    #             print("Clicked '確認、預訂空房' button")
    #             time.sleep(3)  # Wait for the next action or page load

    #             # Optional: Check the new URL after clicking
    #             print(f"After clicking '確認、預訂空房', current URL: {driver.current_url}")

    #             # Scrape availability from the calendar
    #             print("Scraping availability for March 1, 2025 to April 1, 2025")
    #             grid_cells = WebDriverWait(driver, 10).until(
    #                 EC.presence_of_all_elements_located((
    #                     By.XPATH, 
    #                     "//div[@role='gridcell' and contains(@class, 'ngb-dp-day')]"
    #                 ))
    #             )

    #             availability_data = {}
    #             start_date = datetime(2025, 3, 1)
    #             end_date = datetime(2025, 4, 1)

    #             for cell in grid_cells:
    #                 try:
    #                     # Get the date from aria-label (e.g., "13-3-2025")
    #                     aria_label = cell.get_attribute("aria-label")  # Format: DD-MM-YYYY
    #                     if not aria_label:
    #                         continue
    #                     day, month, year = map(int, aria_label.split("-"))
    #                     current_date = datetime(year, month, day)

    #                     # Filter dates within the range
    #                     if start_date <= current_date <= end_date:
    #                         # Extract day number
    #                         day_number = cell.find_element(By.XPATH, ".//div[1]").text.strip()
                            
    #                         # Extract availability symbol
    #                         availability_span = cell.find_element(By.XPATH, ".//div[2]//span")
    #                         availability = availability_span.text.strip()

    #                         # Store the data
    #                         date_str = current_date.strftime("%Y-%m-%d")
    #                         availability_data[date_str] = "Available" if availability == "〇" else "Not Available"
    #                         print(f"Date: {date_str}, Availability: {availability_data[date_str]}")
    #                 except Exception as cell_error:
    #                     print(f"Error processing grid cell: {cell_error}")
    #                     continue

    #             return availability_data  # Optional: return the data for further use

    #         except Exception as button_error:
    #             print(f"Error processing first button: {button_error}")   


    def traverse_hotels(self, driver):
            # Find buttons with exact class "btn btn-primary px-4" and text "資訊", excluding those with "ms-2"
            buttons = WebDriverWait(driver, 10).until(
                EC.presence_of_all_elements_located((
                    By.XPATH, 
                    "//button[@class='btn btn-primary px-4' and contains(text(), '資訊') and not(contains(@class, 'ms-2'))]"
                ))
            )
            num_buttons = len(buttons)
            print(f"Found {num_buttons} buttons to traverse")

            original_window = driver.current_window_handle
            try:
                button = buttons[0]  # Get only the first button
                print("Clicking first button")
                
                # Scroll to the button and click it
                ActionChains(driver).move_to_element(button).click().perform()
                time.sleep(3)  # Wait for page to load
                print(f'driver current handlers: {len(driver.window_handles)}')
                
                confirm_button = WebDriverWait(driver, 10).until(
                    EC.element_to_be_clickable((
                        By.XPATH, 
                        "//button[contains(@class, 'btn btn-primary btn-next px-5') and contains(text(), '確認、預訂空房')]"
                    ))
                )
                print("Found '確認、預訂空房' button")
                
                # Scroll to and click the "確認、預訂空房" button
                ActionChains(driver).move_to_element(confirm_button).click().perform()
                print("Clicked '確認、預訂空房' button")
                time.sleep(3)  # Wait for the next action or page load

                # Optional: Check the new URL after clicking
                print(f"After clicking '確認、預訂空房', current URL: {driver.current_url}")

                # Scrape availability from the calendar
                print("Scraping availability for March 1, 2025 to April 1, 2025")
                grid_cells = WebDriverWait(driver, 10).until(
                    EC.presence_of_all_elements_located((
                        By.XPATH, 
                        "//div[contains(@class, 'ngb-dp-content')]//div[@role='gridcell' and contains(@class, 'ngb-dp-day')]"
                    ))
                )

                availability_data = {}
                start_date = datetime(2025, 3, 1)
                end_date = datetime(2025, 4, 30)

                for cell in grid_cells:
                    try:
                        # Get the date from aria-label (e.g., "13-3-2025")
                        aria_label = cell.get_attribute("aria-label")  # Format: DD-MM-YYYY
                        if not aria_label:
                            continue
                        day, month, year = map(int, aria_label.split("-"))
                        current_date = datetime(year, month, day)

                        # Filter dates within the range
                        if start_date <= current_date <= end_date:
                            # Skip hidden cells
                            if "hidden" in cell.get_attribute("class"):
                                continue

                            # Extract day number
                            day_number_elem = cell.find_elements(By.XPATH, ".//div[1]")
                            day_number = day_number_elem[0].text.strip() if day_number_elem else None
                            if not day_number:
                                continue
                            
                            # Extract availability symbol
                            availability_span = cell.find_elements(By.XPATH, ".//div[2]//span")
                            if availability_span:
                                availability = availability_span[0].text.strip()
                            else:
                                availability = None  # Handle cases like "-" or no span

                            # Interpret availability
                            if availability == "〇":
                                status = "Available"
                            elif availability == "×":
                                status = "Not Available"
                            elif availability == "-" or availability is None:
                                status = "Unknown"
                            else:
                                status = "Unexpected"

                            # Store the data
                            date_str = current_date.strftime("%Y-%m-%d")
                            availability_data[date_str] = status
                            print(f"Date: {date_str}, Day: {day_number}, Availability: {status}")

                    except Exception as cell_error:
                        print(f"Error processing grid cell with aria-label '{aria_label}': {cell_error}")
                        continue

                return availability_data  # Optional: return the data for further use

            except Exception as button_error:
                print(f"Error processing first button: {button_error}")

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
                
            # Wait for the login button to be clickable and click it
            login_button = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.CLASS_NAME, "btn-next"))
            )
            # Scroll into view and click using ActionChains as a fallback
            ActionChains(driver).move_to_element(login_button).click().perform()
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

            area_dict = {}
            for option in select.options:
                value = option.get_attribute("value")
                text = option.text
                area_dict[text] = value
                print(f"value: {value}, text: {text}")
            
            area_name, key = self.return_area_value(area_dict)

            # Select "首都圈（東京）" by value
            select.select_by_value(key)
            print(f"Selected {area_name}")

            # Locate and click the Search button
            search_button = driver.find_element(By.CLASS_NAME, "blue_btn_ht")
            search_button.click()
            print("Clicked Search button")
            # driver.refresh()
            time.sleep(3)  # Wait to observe the result
            
            self.traverse_hotels(driver)
                
        except Exception as e:
            print(f"An error occurred: {e}")
        
        finally:
            # Close the browser window and quit the driver
            driver.quit()
            print("Browser closed")

if __name__ == "__main__":
    web_agent = WebAgent()
    web_agent.access_website()