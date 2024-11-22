import time
from selenium.webdriver.remote.webdriver import WebDriver

def infinite_scroll(driver: WebDriver, pause_time=2, max_scrolls=50):
    """
    Scrolls to the bottom of the page repeatedly to load dynamic content.

    :param driver: Selenium WebDriver instance.
    :param pause_time: Time to wait after each scroll (in seconds).
    :param max_scrolls: Maximum number of scroll attempts.
    """
    try:
        last_height = driver.execute_script("return document.body.scrollHeight")

        for i in range(max_scrolls):
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(pause_time)

            new_height = driver.execute_script("return document.body.scrollHeight")
            if new_height == last_height:
                print(f"Scrolling stopped. No more content after {i+1} scrolls.")
                break
            last_height = new_height

    except Exception as e:
        print(f"Error during infinite scroll: {e}")
