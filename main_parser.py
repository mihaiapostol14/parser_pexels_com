from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from selenium.common.exceptions import NoSuchElementException

from config import USER_AGENT
from helper import (
    Helper,
    DriverHelper,
    ElementChecker,
    image_downloader
)

class MainParser(Helper):
    def __init__(self, user_requested_image=''):
        # Initialize Firefox options
        self.options = webdriver.FirefoxOptions()
        self.options.set_preference("general.useragent.override",
                                    USER_AGENT)  # Set custom user agent to avoid detection as a bot
        self.options.set_preference("dom.webdriver.enabled", False)  # Disable WebDriver detection
        self.options.set_preference("intl.accept_languages", 'en-us')  # Set language WebDriver
        self.options.set_preference("dom.webnotifications.enabled", False)  # Disable WebDriver notifications

        self.service = Service(executable_path='GeckoDriver/geckodriver.exe')  # Path to WebDriver

        self.driver = webdriver.Firefox(service=self.service,
                                        options=self.options)  # Create a new instance of the Firefox WebDriver with the specified options

        self.user_requested_image = user_requested_image.replace(' ', '%20')
        self.driver_helper = DriverHelper(driver=self.driver)
        self. element_checker = ElementChecker(driver=self.driver)

        self.get_item_link()



    def get_item_link(self):
        self.driver_helper.send_by_url(url=f'https://www.pexels.com/search/{self.user_requested_image}/')

        self.user_requested_image = self.user_requested_image.replace('%20', '_')
        self.create_directory(name_directory=self.user_requested_image)

        try:
                if self.element_checker.class_exists(class_name='BreakpointGrid_alwaysVisible__ECmZd'):
                    self.driver.find_element(By.CLASS_NAME,'Link_link__Ime8c').click()
        except NoSuchElementException:
            ...
        # self.driver_helper.close_driver()

        # image_downloader(
        #     filename=f'{self.user_requested_image}/{self.user_requested_image}_link.txt',
        #     dir_name=f'{self.user_requested_image}/{self.user_requested_image}_image'
        # )


def main():
    return MainParser(
        user_requested_image=input('typing your image please: ')
    )


if __name__ == '__main__':
    main()
