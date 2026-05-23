import allure
import pytest
import time

from pages.login_page import LoginPage
from utils.logger import LogGen


logger = LogGen.loggen()


# ======================================================
# SCREENSHOT FUNCTION
# ======================================================

def take_screenshot(driver, name):

    time.sleep(2)

    screenshot_name = f"{name}.png"

    driver.save_screenshot(
        screenshot_name
    )

    allure.attach.file(
        screenshot_name,
        name=name,
        attachment_type=
        allure.attachment_type.PNG
    )


# ======================================================
# NEGATIVE TEST CASE 1
# INVALID MOBILE NUMBER
# ======================================================

@allure.feature(
    "BigBasket Negative Testing"
)

@allure.story(
    "Invalid Mobile Number Validation"
)

@allure.severity(
    allure.severity_level.CRITICAL
)

@pytest.mark.order(1)

def test_invalid_phone(driver):

    login = LoginPage(driver)

    logger.info(
        "===== INVALID MOBILE TEST STARTED ====="
    )

    # ==================================================
    # OPEN WEBSITE
    # ==================================================

    login.open_bigbasket()

    time.sleep(5)

    take_screenshot(
        driver,
        "homepage_opened"
    )

    # ASSERTION
    assert (
        "bigbasket"
        in
        driver.current_url.lower()
    )

    logger.info(
        "Homepage Opened Successfully"
    )

    # ==================================================
    # CLICK LOGIN
    # ==================================================

    login.click_login()

    time.sleep(3)

    take_screenshot(
        driver,
        "login_popup_opened"
    )

    # ASSERTION
    assert (
        driver.current_url
        is not None
    )

    logger.info(
        "Login Popup Opened Successfully"
    )

    # ==================================================
    # ENTER INVALID MOBILE NUMBER
    # ==================================================

    invalid_mobile = "123"

    login.enter_mobile_email(
        invalid_mobile
    )

    time.sleep(3)

    take_screenshot(
        driver,
        "invalid_mobile_entered"
    )

    # ASSERTION
    assert (
        len(invalid_mobile) < 10
    )

    logger.info(
        "Invalid Mobile Number Entered"
    )

    # ==================================================
    # CLICK CONTINUE
    # ==================================================

    login.click_continue()

    time.sleep(5)

    take_screenshot(
        driver,
        "invalid_mobile_validation"
    )

    # ASSERTION
    assert (
        "bigbasket"
        in
        driver.current_url.lower()
    )

    logger.info(
        "Invalid Mobile Validation Successful"
    )

    logger.info(
        "===== INVALID MOBILE TEST PASSED ====="
    )


# ======================================================
# NEGATIVE TEST CASE 2
# INVALID OTP
# ======================================================

@allure.feature(
    "BigBasket Negative Testing"
)

@allure.story(
    "Invalid OTP Validation"
)

@allure.severity(
    allure.severity_level.CRITICAL
)

@pytest.mark.order(2)

def test_invalid_otp(driver):

    login = LoginPage(driver)

    logger.info(
        "===== INVALID OTP TEST STARTED ====="
    )

    # ==================================================
    # OPEN WEBSITE
    # ==================================================

    login.open_bigbasket()

    time.sleep(5)

    take_screenshot(
        driver,
        "otp_homepage"
    )

    # ASSERTION
    assert (
        "bigbasket"
        in
        driver.current_url.lower()
    )

    logger.info(
        "Homepage Opened Successfully"
    )

    # ==================================================
    # CLICK LOGIN
    # ==================================================

    login.click_login()

    time.sleep(3)

    take_screenshot(
        driver,
        "otp_login_popup"
    )

    # ASSERTION
    assert (
        driver.current_url
        is not None
    )

    logger.info(
        "Login Popup Opened Successfully"
    )

    # ==================================================
    # ENTER VALID MOBILE NUMBER
    # ==================================================

    valid_mobile = "7396738499"

    login.enter_mobile_email(
        valid_mobile
    )

    time.sleep(3)

    take_screenshot(
        driver,
        "valid_mobile_entered"
    )

    # ASSERTION
    assert (
        len(valid_mobile) == 10
    )

    logger.info(
        "Valid Mobile Number Entered"
    )

    # ==================================================
    # CLICK CONTINUE
    # ==================================================

    login.click_continue()

    time.sleep(15)

    take_screenshot(
        driver,
        "otp_screen"
    )

    # ASSERTION
    assert (
        driver.current_url
        is not None
    )

    logger.info(
        "OTP Screen Opened Successfully"
    )

    # ==================================================
    # CLICK VERIFY CONTINUE
    # ==================================================

    login.click_verify_continue()

    time.sleep(5)

    take_screenshot(
        driver,
        "invalid_otp_validation"
    )

    # ASSERTION
    assert (
        driver.current_url
        is not None
    )

    logger.info(
        "Invalid OTP Validation Successful"
    )

    logger.info(
        "===== INVALID OTP TEST PASSED ====="
    )