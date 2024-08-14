from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import time

# Set up Chrome options
chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")

# Initialize the WebDriver with Chrome options
driver = webdriver.Chrome(options=chrome_options)

try:
    # Open the IUCN Red List website
    driver.get("https://www.iucnredlist.org/")

    # Find the search box element using the class attribute
    search_box = driver.find_element("css selector", "input.search.search--site")

    # Type the search query "Lynx rufus" and hit Enter
    search_box.send_keys("Coyote")
    search_box.send_keys(Keys.RETURN)

    # Wait for the search results to load
    time.sleep(3)

    # Find and click on the first 'View' link with the class "link--faux"
    view_link = driver.find_element("css selector", "a.link--faux")
    view_link.click()

    # Wait for the species page to load after clicking the link
    time.sleep(3)

    # Find the h1 element with the class "headline_title"
    headline = driver.find_element("css selector", "h1.headline__title")
    headline_text = headline.text

    # Find and click the download button with the specified class
    download_button = driver.find_element("name", "download_search_results")
    download_button.click()

    # Wait for the download options to appear
    time.sleep(4)

    # Find all 'link--download' buttons
    download_buttons = driver.find_elements("css selector", "a.link--download")
    if download_buttons:
        # Get the href attribute of the first download button
        first_href = download_buttons[0].get_attribute("href")
    else:
        first_href = None
        print("No download buttons found.")

    # Create a dictionary with the headline and first href
    result = {
        "headline": headline_text,
        "first_download_href": first_href
    }

    # Print the dictionary
    print(result)

finally:
    # Close the browser
    driver.quit()
    print("Browser closed.")
