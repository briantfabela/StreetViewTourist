# Python 3.7.5 - Briant J. Fabela (12/26/2019)


from selenium import webdriver
# setting up chrome driver is a hassle so im working with a local copy for win
driver = webdriver.Chrome(r'chromedriver_win32/chromedriver_v79.exe')

# for 'explicit' wait implementation
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# for image cropping, drawing, and processing
from PIL import Image, ImageDraw

# url path for google maps
googleMapsUrl = 'https://www.google.com/maps'

# xpaths
xpaths = dict(
    searchField = '//*[@id="searchboxinput"]',
    searchButton = '//*[@id="searchbox-searchbutton"]',
    photosButton = '//*[@id="pane"]/div/div[1]/div/div/div[13]/div[1]/button',
    titleCard = '/html/body/jsl/div[3]/div[9]/div[12]/div[1]'
)

# lets test automating a search
loc = '1969 S. Madison Ave YUMA AZ'

driver.get(googleMapsUrl) # go to page

driver.maximize_window() # max the window

field = driver.find_element_by_xpath(xpaths['searchField']) # find search field
field.send_keys(loc) # type on search field

fieldButton = driver.find_element_by_xpath(xpaths['searchButton']) # button
fieldButton.click() # click search button

# the page needs some time to load here while the button loads
# waits up to 10 seconds, making attempts every half second, until timeout
wait = WebDriverWait(driver, 10).until( # wait until 'Photos' button is located
    EC.presence_of_element_located((By.XPATH, xpaths['photosButton']))
)

# once button is found click it
photosButton = driver.find_element_by_xpath(xpaths['photosButton'])
photosButton.click() # Usually yields streetview. sometimes storefront picture

# wait for streetviewto load using the visibility of the titlecard as proxy
wait = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.XPATH, xpaths['titleCard']))
)

driver.save_screenshot('screenshot.png') # placeholder name until processing

# now lets edit this image using PIL
# dimensions for use with a 2560 x 1440 monitor; adjust as needed

img = Image.open('screenshot.png') # lets load our screenshot

# crop
w, h = img.size # get screengrab's dimensions
result = img.crop((410, 0, w, h)) # crop the left 410px

'''
# draw rectangles to cover widgets, you can skip this if you dont mind them
rectangles = [ # drawn based on two point coords (x, y)
    [(40,40), (200, 200)]
    #[(0, 0), (200, 125)],
    #[(0, h-165), (175, h)]
]

for rect in rectangles: # draw all rectangles
    overlay = ImageDraw.Draw(img)
    overlay.rectangle(rect, fill='black')
    print(rect, "drawn")
'''

result.save('test.png')
img.close()