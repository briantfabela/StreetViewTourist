# Python 3.7.5 - Briant J. Fabela (12/26/2019)

from selenium import webdriver
# setting up chrome driver is a hassle so im working with a local copy for win
driver = webdriver.Chrome(r'chromedriver_win32/chromedriver_v79.exe')

# For 'explicit' wait implementation
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# url path for google maps
googleMapsUrl = 'https://www.google.com/maps'

# xpaths
xpaths = dict(
    searchField = '//*[@id="searchboxinput"]',
    searchButton = '//*[@id="searchbox-searchbutton"]',
    photosButton = '//*[@id="pane"]/div/div[1]/div/div/div[13]/div[1]/button'
)

# lets test automating a search
loc = '1969 S. Madison Ave YUMA AZ'

driver.get(googleMapsUrl) # go to page

field = driver.find_element_by_xpath(xpaths['searchField']) # find search field
field.send_keys(loc) # type on search field

fieldButton = driver.find_element_by_xpath(xpaths['searchButton']) # button
fieldButton.click() # click search button

# the page needs some time to load here while the button loads
# waits up to 10 seconds, making attempts every half second, until timeout
wait = WebDriverWait(driver, 10).until( # wait until 'Photos' button is located
    EC.presence_of_element_located((By.XPATH, xpaths['photosButton'])))

# once button is found click it
photosButton = driver.find_element_by_xpath(xpaths['photosButton'])
photosButton.click() # Usually yields streetview. sometimes storefront picture

driver.maximize_window() # max the window