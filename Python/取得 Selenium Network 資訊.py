import json

from selenium import webdriver
from selenium.webdriver import DesiredCapabilities
from selenium_utilities import getChromeDriver

def process_browser_log_entry(entry):
    response = json.loads(entry['message'])['message']
    return response

caps = DesiredCapabilities.CHROME
caps['goog:loggingPrefs'] = {'performance': 'ALL'}
options = webdriver.ChromeOptions()
options.add_argument('--lang=en-US')
options.add_argument('--ignore-ssl-errors')
options.add_argument('--mute-audio')
options.add_argument("--start-maximized")
driver = webdriver.Chrome(executable_path=getChromeDriver(), options=options,desired_capabilities=caps)
driver.get('https://www.google.com/recaptcha/api2/demo')
while True:
    browser_log = driver.get_log('performance')
    events = [process_browser_log_entry(entry) for entry in browser_log]
    events = [event for event in events if 'Network.response' in event['method']]
    
    # 拿 R
    for i in events:
        if "userverify" in str(i):
            print(driver.execute_cdp_cmd('Network.getResponseBody', {'requestId': events[0]["params"]["requestId"]}))
