# Python 3.7.1 - Briant J. Fabela (12/26/2019)

from selenium import webdriver # selenium v3.141.0

# for 'explicit' wait implementation
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from PIL import Image # PIL v7.0.0
from os import path

def main():
    # xpaths
    xpaths = dict( # this will lets us use an object-like struture in our code
        searchField = '//*[@id="searchboxinput"]',
        searchButton = '//*[@id="searchbox-searchbutton"]',
        photosButton = '//*[@id="pane"]/div/div[1]/div/div/div[1]/div[1]/button',
        titleCard = '/html/body/jsl/div[3]/div[9]/div[12]/div[1]',
        backButton = '//*[@id="pane"]/div/div[1]/div/div/div[2]/button[1]'
    )

    t = Tourist("https://www.google.com/maps", xpaths, 'adds.txt')
    t.tour()

def crop_img(img, left, top, right, bottom, name, stamp='_cropped', ext="png"):
    """Crops and saves a PIL.Image.Image Object"""

    w, h = img.size # get the window size dimensions (window dimensions)
    result = img.crop((left, top, w-right, h-bottom))
    result.save(path.join('pictures', name+stamp+'.'+ext)) # save in /pictures
    img.close()
    result.close() # close both objects

def read_addresses(txt_file_path):
    '''Returns a text file of addresses as a python list'''

    addresses = open(txt_file_path) # file should have an address per line
    return [line.strip('\n') for line in addresses] # returns addresses as list

class Tourist:
    ''' A Tourist uses the selenium driver to visit a list of addresses'''

    def __init__(self, url, xpaths, addresses_txt_file_path):
        self.url = url
        self.xpaths = xpaths # xpath dictionary
        self.locations = read_addresses(addresses_txt_file_path)
        self.driver_fp = r'chromedriver_win32/chromedriver_v79.exe'

    def wait_and_click(self, driver, xpath, timeout_limit=10):
        '''Waits for button visibility and attempts to click until timeout'''
    
        wait = WebDriverWait(driver, timeout_limit).until(
            EC.visibility_of_element_located((By.XPATH, xpath))
        ) # will wait, or timeout if button not found

        button = driver.find_element_by_xpath(xpath)
        button.click()

    def tour(self, max_window=True, dims=(1080,800)):
        '''Opens the webridriver using Selenium.

        After opening the driver it begins parsing thru self.locations and
        taking screenshots of each location in Google Streetview.
        '''

        driver = webdriver.Chrome(self.driver_fp)

        # set window size and go to url
        if max_window: 
            driver.maximize_window()
        else:
            driver.set_window_size(*dims)
        driver.get(self.url)

        for loc in self.locations:
            field = driver.find_element_by_xpath(self.xpaths['searchField'])
            field.send_keys(loc) # type in location

            '''
            field_button = driver.find_element_by_xpath(self.xpaths['searchButton'])
            field_button.click() # click search button'''

            self.wait_and_click(driver, self.xpaths['searchField'])

            # implementation of an explicit wait while content loads
            wait = WebDriverWait(driver, 10).until(
                EC.visibility_of_element_located((By.XPATH, self.xpaths['photosButton']))
            ) # 'visibility_of_element' seems to throw out far less TimeoutExceptions
            
            photosButton = driver.find_element_by_xpath(self.xpaths['photosButton'])
            photosButton.click()

            wait = WebDriverWait(driver, 10).until( # wait until the streetview loads
                EC.visibility_of_element_located((By.XPATH, self.xpaths['titleCard']))
            )

            # take screen capture
            driver.save_screenshot(path.join('pictures', 'temp_screenshot.png'))
            img = Image.open(r'pictures/temp_screenshot.png')
            crop_img(img, 410, 0, 0, 0, loc)
            print(loc, "successfully screencaptured")

            back_button = driver.find_element_by_xpath(self.xpaths['backButton'])
            back_button.click() # click back button

            wait = WebDriverWait(driver, 10).until( # searchField needs some time to load
                EC.visibility_of_element_located((By.XPATH, self.xpaths['searchField']))
            )

            field.clear()
        
        print("Tour has ended.")

if __name__ == "__main__":
    main()