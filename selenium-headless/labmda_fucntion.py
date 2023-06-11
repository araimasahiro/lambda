from selenium import webdriver

def lambda_handler(event, context):
    URL = "https://new.yahoo.co.jp/"

    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    options.add_argument("--disable-gpu")
    options.add_argument("--hide-scrollbars")
    options.add_argument("--single-process")
    options.add_argument("--ignore-certificate-errors")
    options.add_argument("--window-size=880x996")
    options.add_argument("--no-sandbox")
    options.add_argument("--homedir=/tmp")
    options.binary_location = "/opt/python/bin/headless-chromium"

    #ブラウザの定義
    browser = webdriver.Chrome("/opt/python/bin/chromedriver", options=options)

    browser.get(URL)
    title = browser.title
    browser.close()

    return title
