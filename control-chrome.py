from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from threading import Thread, Barrier
from selenium.webdriver.common.proxy import Proxy, ProxyType

def openChrome():
    chrome_options = Options()
    chrome_options.binary_location = "D:\\GoogleChromePortable.exe"
    # chrome_options.addArguments("user-data-dir=/path/to/your/custom/profile")
    # prox = Proxy()
    # prox.proxy_type = ProxyType.MANUAL
    # prox.http_proxy = "https://PRmhTm:MMPS5X@168.81.237.128:8000"
    # prox.socks_proxy = "168.81.237.128:8000"
    # prox. = ""
    # prox.ssl_proxy = "168.81.237.128:8000"

    # capabilities = webdriver.DesiredCapabilities.CHROME
    # prox.add_to_capabilities(capabilities)
    # chrome_options.addExtensions(new File("/path/to/extension.crx"))
    # chrome_options.add_argument("--disable-extensions")
    driver = webdriver.Chrome(chrome_options=chrome_options, executable_path="C:\\Users\\NamPC\\Desktop\\Tool\\driver-106\\chromedriver.exe")
        # driver = webdriver.Chrome(desired_capabilities=capabilities,chrome_options=chrome_options, executable_path="C:\\Users\\NamPC\\Desktop\\Tool\\driver-106\\chromedriver.exe")
    driver.get("https://youtube.com")


    search = WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.NAME, 'search_query')))

    search.send_keys("python open and control chrome")       


    search_btn = WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.ID, 'search-icon-legacy')))
    search_btn.click()
    contents = WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.ID, 'contents')))

    list_title = WebDriverWait(driver, 5).until(EC.visibility_of_all_elements_located((By.CLASS_NAME, 'style-scope ytd-video-renderer')))

    # for title in list_title:
    #     print(title.text)


    # Get scroll height
    last_height = driver.execute_script("return document.body.scrollHeight")
    i = 0

    while True:
        # Scroll down to bottom
        driver.execute_script("window.scrollTo(0, arguments[0]);", i)
        i = i+100
        # Wait to load page
        time.sleep(0.5)

        # Calculate new scroll height and compare with last scroll height

openChrome()

# with concurrent.futures.ThreadPoolExecutor() as exector:
#     exector.map(openChrome(), )     


# number_of_threads = 5

# barrier = Barrier(number_of_threads)

# threads = []

# for _ in range(number_of_threads):
#     t = Thread(target=openChrome(), args=(barrier,)) 
#     t.start()
#     threads.append(t)

# for t in threads:
#     t.join()
