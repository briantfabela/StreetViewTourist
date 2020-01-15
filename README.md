# StreetViewTourist
Screengrabs an address in google streetview using Selenium on a Chrome webdriver and processes the screengrabs with PIL. 

**SampleWorkflow.py** details the process step-by-step.

### For your consideration:
This is most useful for residential addresses. Commercial and public venues that have dedicated photo albums may require you to use different XPaths to access *Street View*. As of the latest release of **SampleWorkflow.py** the behavior has not been tested for anything other than residential addresses.

### Recommendations:
Consider utilizing a loop for iteration through a list, dict, etc. of addresses for more effective automation. Depending on your driver/OS and behavior of the browser this scipt is subject to break. Use wait functions and try/except statements to counter this.

Chrome webdriver download page: (different versions and OS options)
https://chromedriver.chromium.org/home

### Please consider Google Map/Earth's *Terms of Service and Fair Use* when using of any data acquired.
https://www.google.com/permissions/geoguidelines/

#### What Addresses work? Formats, etc.
***4123 W 14th St Yuma, AZ 85364*** works pefectly. As do most residential addressses in this format:
{St num} {St name} {city},{State} {zip}

Some commercial venues also work fine such as ***Walgreens Pharmacy 4th Ave Yuma, AZ*** or uniquely named local businesses like ***Ricky's Other Place***. But commercial chains do require a unique St name and City in order for the google algorithms to take you directly to the store at the address you are referencing. If there were two Walgreens along 4th Ave, the serach result would not yield a unique location. As of now, the first result in that screen is selected; as it is *often* the most relevant result. Example: https://www.google.com/maps/search/Circle+K+4th+ave/@32.7100013,-114.633314,4927m/data=!3m2!1e3!4b1

However, most businesses have pictures and NOT streetview as their default image. This is problematic for this script because sometimes the pictures from the albums are bad photos, indoor photos (rarely good), or corporate-type placeholders like a logo or something straight out of Getty Images. TODOs might include identifying a DOM element that most usually yields a streetview for businesses, schools, MHRV Parks, parks, gov't offices, etc. However, differentiating between residential addresses and business loactions might prove challenging. Maybe the existance of that element would be the telling factor?

#### Recent Changes:
- Improvements in common error handling
- WebDirver is now a Tourist class attribute 'self.driver'
- Ability to handle search results; currently now selecting the first (usually most relevant) result
- Implemented time.sleep as an alternative to explicit waits to circumvent complex exception handling
