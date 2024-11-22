from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from selenium.common.exceptions import NoSuchElementException

from config import USER_AGENT
from helper import (
    Helper,
    DriverHelper,
    ElementChecker
)


class ParserItemInfo(Helper):
    def __init__(self,source_file=''):
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

        self.source_file = source_file
        self.driver_helper = DriverHelper(driver=self.driver)
        self.element_checker = ElementChecker(driver=self.driver)

        self.iter_by_item()




    def iter_by_item(self):
        with open(file=self.source_file, mode='r') as file:
            source = file.read()
            for url in source.split():
                self.random_pause_code(start=1, stop=4)
                self.driver_helper.send_by_url(url=url)
                self.get_image()


    def get_image(self):
        self.random_pause_code(start=1, stop=4)

        self.driver.execute_script("arguments[0].scrollIntoView();", self.driver.find_element(By.TAG_NAME, 'img'))

        try:
            if self.element_checker.tag_exists(tag_name='img'):
                self.driver.find_element(By.TAG_NAME, 'img').click()
                self.random_pause_code(start=1, stop=4)
                image_link = self.driver.find_element(By.TAG_NAME, 'img').get_attribute('src')


                self.crate_file(
                    filename=f"{self.source_file.split('/')[0]}/{self.source_file.split('/')[0]}_image_link.txt",
                    mode='a',
                    data=image_link
                )
                self.driver_helper.close_driver()

        except NoSuchElementException:
            self.driver_helper.close_driver()


def main():
    return ParserItemInfo(
        source_file='mario/super_car/super_car_image_page_links.txt'
    )


if __name__ == '__main__':
    main()
