# ====================================================================
# ====================================================================


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Initialize WebDriver and navigate to the website
driver = webdriver.Chrome()
driver.get("http://books.toscrape.com")

try:
    # Wait for elements with class name `product_pod`
    wait = WebDriverWait(driver, 10)
    elems = wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, "product_pod")))

    # Print titles of the books
    for elem in elems:
        print(elem.find_element(By.TAG_NAME, "h3").text)

finally:
    # Close the browser
    driver.quit()



# ====================================================================
# ====================================================================


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Initialize WebDriver and navigate to the website
driver = webdriver.Chrome()
driver.get("http://books.toscrape.com")

try:
    # Wait for elements with class name `product_pod`
    wait = WebDriverWait(driver, 10)
    elems = wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, "product_pod")))

    # Print image URLs of the books
    print("Found the following book images:")
    for elem in elems:
        img = elem.find_element(By.TAG_NAME, "img")  # Locate the img tag
        img_url = img.get_attribute("src")          # Get the src attribute
        print(img_url)

finally:
    # Close the browser
    driver.quit()



# ==============================================================================
# ==============================================================================


import os
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



# add proxy
proxies = {
    "http": "http://rqmnrvak-rotate:ps7bikiydmaw@207.244.217.165:6712",
    "https": "http://rqmnrvak-rotate:ps7bikiydmaw@207.244.217.165:6712",
}



# Directory to save the images
save_dir = "book_images"
os.makedirs(save_dir, exist_ok=True)  # Create directory if it doesn't exist

# Initialize WebDriver and navigate to the website
driver = webdriver.Chrome()
driver.get("http://books.toscrape.com")

try:
    # Wait for elements with class name `product_pod`
    wait = WebDriverWait(driver, 10)
    elems = wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, "product_pod")))

    # Download and save images of the books
    print("Downloading book images:")
    for idx, elem in enumerate(elems, start=1):
        img = elem.find_element(By.TAG_NAME, "img")  # Locate the img tag
        img_url = img.get_attribute("src")    
        img_data = requests.get(img_url, proxies=proxies).content # Get the src attribute
        # img_data = requests.get(img_url).content    # Fetch the image content

        # Save the image to the specified directory
        file_name = os.path.join(save_dir, f"book_{idx}.jpg")
        with open(file_name, "wb") as img_file:
            img_file.write(img_data)
        print(f"Saved: {file_name}")

finally:
    # Close the browser
    driver.quit()
