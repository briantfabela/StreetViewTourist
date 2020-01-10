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
