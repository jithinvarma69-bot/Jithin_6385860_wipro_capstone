from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


class LoginPage:

    # LOCATORS

    LOGIN_BUTTON = (
        By.XPATH,
        "//button[contains(.,'Login')]"
    )

    MOBILE_INPUT = (
        By.XPATH,
        "//input[@placeholder='Enter Phone number/ Email Id']"
    )

    CONTINUE_BUTTON = (
        By.XPATH,
        "//button[contains(.,'Continue')]"
    )

    VERIFY_BUTTON = (
        By.XPATH,
        "//button[contains(.,'Continue')]"
    )

    INVALID_MOBILE_POPUP = (
        By.XPATH,
        "//*[contains(text(),'valid mobile number')]"
    )

    INVALID_OTP_POPUP = (
        By.XPATH,
        "//*[contains(text(),'OTP')]"
    )

    # CONSTRUCTOR

    def __init__(self, driver):

        self.driver = driver

        self.wait = WebDriverWait(
            driver,
            20
        )

    # OPEN WEBSITE

    def open_bigbasket(self):

        self.driver.get(
            "https://www.bigbasket.com"
        )

    # CLICK LOGIN

    def click_login(self):

        time.sleep(5)

        login_btn = self.wait.until(
            EC.presence_of_element_located(
                self.LOGIN_BUTTON
            )
        )

        self.driver.execute_script(
            "arguments[0].click();",
            login_btn
        )

    # ENTER MOBILE NUMBER

    def enter_mobile_email(self, mobile):

        time.sleep(3)

        mobile_box = self.wait.until(
            EC.presence_of_element_located(
                self.MOBILE_INPUT
            )
        )

        mobile_box.clear()

        mobile_box.send_keys(mobile)

    # CLICK CONTINUE

    def click_continue(self):

        time.sleep(2)

        continue_btn = self.wait.until(
            EC.presence_of_element_located(
                self.CONTINUE_BUTTON
            )
        )

        self.driver.execute_script(
            "arguments[0].click();",
            continue_btn
        )

    # CLICK VERIFY CONTINUE

    def click_verify_continue(self):

        time.sleep(3)

        verify = self.wait.until(
            EC.presence_of_element_located(
                self.VERIFY_BUTTON
            )
        )

        self.driver.execute_script(
            "arguments[0].click();",
            verify
        )

    # INVALID MOBILE POPUP

    def get_invalid_mobile_popup(self):

        return self.wait.until(
            EC.presence_of_element_located(
                self.INVALID_MOBILE_POPUP
            )
        )

    # INVALID OTP POPUP

    def get_invalid_otp_popup(self):

        return self.wait.until(
            EC.presence_of_element_located(
                self.INVALID_OTP_POPUP
            )
        )