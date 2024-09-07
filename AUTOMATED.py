import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from webdriver_manager.chrome import ChromeDriverManager

# Setup Chrome WebDriver
os.environ['PATH'] += r";D:\SELENIUM\chromedriver-win64"
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# Open the target website
driver.get("https://katalon-demo-cura.herokuapp.com/")

# Maximize the browser window (optional)
driver.maximize_window()

# Click on "Make Appointment" button
try:
    wait = WebDriverWait(driver, 10)
    make_appointment_button = wait.until(
        EC.element_to_be_clickable((By.ID, "btn-make-appointment"))
    )
    driver.execute_script("arguments[0].scrollIntoView(true);", make_appointment_button)
    make_appointment_button.click()
    print("Make Appointment button clicked successfully.")
except NoSuchElementException:
    print("Make Appointment button not found.")
    driver.quit()
    exit()
except TimeoutException:
    print("Timeout while waiting for Make Appointment button.")
    driver.quit()
    exit()

# Log in
try:
    # Wait for the username and password fields
    username_field = wait.until(EC.presence_of_element_located((By.ID, "txt-username")))
    password_field = wait.until(EC.presence_of_element_located((By.ID, "txt-password")))
    
    # Scroll into view and enter username and password
    driver.execute_script("arguments[0].scrollIntoView(true);", username_field)
    username_field.clear()
    username_field.send_keys("John Doe")  # Replace with actual username
    
    driver.execute_script("arguments[0].scrollIntoView(true);", password_field)
    password_field.clear()
    password_field.send_keys("ThisIsNotAPassword")  # Replace with actual password
    
    # Find and click the login button
    login_button = wait.until(EC.element_to_be_clickable((By.ID, "btn-login")))
    driver.execute_script("arguments[0].scrollIntoView(true);", login_button)
    login_button.click()
    print("Logged in successfully.")
except NoSuchElementException:
    print("Login elements not found.")
    driver.quit()
    exit()
except TimeoutException:
    print("Timeout while waiting for login elements.")
    driver.quit()
    exit()

# Fill the appointment form
try:
    # Wait for and scroll into view the facility dropdown
    facility_dropdown = wait.until(EC.presence_of_element_located((By.ID, "combo_facility")))
    driver.execute_script("arguments[0].scrollIntoView(true);", facility_dropdown)
    select_facility = Select(facility_dropdown)
    select_facility.select_by_visible_text("Tokyo CURA Healthcare Center")
    print("Facility selected.")
    
    # Scroll into view and check the readmission checkbox
    readmission_checkbox = wait.until(EC.element_to_be_clickable((By.ID, "chk_hospotal_readmission")))
    driver.execute_script("arguments[0].scrollIntoView(true);", readmission_checkbox)
    if not readmission_checkbox.is_selected():
        readmission_checkbox.click()
    print("Readmission checkbox checked.")
    
    # Scroll into view and select the Medicare radio button
    medicare_radio = wait.until(EC.element_to_be_clickable((By.ID, "radio_program_medicare")))
    driver.execute_script("arguments[0].scrollIntoView(true);", medicare_radio)
    medicare_radio.click()
    print("Medicare option selected.")
    
    # Scroll into view and enter visit date
    visit_date_field = wait.until(EC.presence_of_element_located((By.ID, "txt_visit_date")))
    driver.execute_script("arguments[0].scrollIntoView(true);", visit_date_field)
    visit_date_field.send_keys("20/09/2024")  # Replace with the required date
    print("Visit date entered.")
    
    # Scroll into view and enter comment
    comment_field = wait.until(EC.presence_of_element_located((By.ID, "txt_comment")))
    driver.execute_script("arguments[0].scrollIntoView(true);", comment_field)
    comment_field.send_keys("Looking forward to the appointment.")
    print("Comment entered.")
    
    # Scroll into view and click on "Book Appointment" button
    book_appointment_button = wait.until(EC.element_to_be_clickable((By.ID, "btn-book-appointment")))
    driver.execute_script("arguments[0].scrollIntoView(true);", book_appointment_button)
    book_appointment_button.click()
    print("Appointment booked successfully.")
    
except NoSuchElementException as e:
    print(f"Form elements not found: {e}")
except TimeoutException:
    print("Timeout while waiting for form elements.")
except Exception as e:
    print(f"An error occurred while booking the appointment: {e}")
finally:
    driver.quit()
