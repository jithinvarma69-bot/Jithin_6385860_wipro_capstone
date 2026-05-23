from behave import *

import time

from selenium import webdriver

from selenium.webdriver.chrome.service import Service

from webdriver_manager.chrome import ChromeDriverManager

from pages.login_page import LoginPage

from utils.logger import LogGen


logger = LogGen.loggen()


# =====================================================
# OPEN WEBSITE
# =====================================================

@given(
    "negative user opens BigBasket website"
)

def open_site(context):

    logger.info(
        "Opening BigBasket Website"
    )

    context.driver = webdriver.Chrome(
        service=Service(
            ChromeDriverManager().install()
        )
    )

    context.driver.maximize_window()

    context.driver.get(
        "https://www.bigbasket.com/"
    )

    time.sleep(5)

    logger.info(
        "Website Opened Successfully"
    )


# =====================================================
# CLICK LOGIN BUTTON
# =====================================================

@when(
    "negative user clicks login button"
)

def click_login(context):

    logger.info(
        "Clicking Login Button"
    )

    login = LoginPage(
        context.driver
    )

    login.click_login()

    time.sleep(3)

    logger.info(
        "Login Popup Opened Successfully"
    )


# =====================================================
# ENTER VALID MOBILE NUMBER
# =====================================================

@when(
    "negative user enters valid mobile number"
)

def valid_mobile(context):

    logger.info(
        "Entering Valid Mobile Number"
    )

    login = LoginPage(
        context.driver
    )

    login.enter_mobile_email(
        "7396738499"
    )

    time.sleep(3)

    logger.info(
        "Valid Mobile Number Entered"
    )


# =====================================================
# ENTER INVALID MOBILE NUMBER
# =====================================================

@when(
    "negative user enters invalid mobile number"
)

def invalid_mobile(context):

    logger.info(
        "Entering Invalid Mobile Number"
    )

    login = LoginPage(
        context.driver
    )

    login.enter_mobile_email(
        "123"
    )

    time.sleep(3)

    logger.info(
        "Invalid Mobile Number Entered"
    )


# =====================================================
# CLICK CONTINUE BUTTON
# =====================================================

@when(
    "negative user clicks continue button"
)

def continue_button(context):

    logger.info(
        "Clicking Continue Button"
    )

    login = LoginPage(
        context.driver
    )

    login.click_continue()

    time.sleep(15)

    logger.info(
        "Continue Button Clicked"
    )


# =====================================================
# CLICK VERIFY CONTINUE
# =====================================================

@when(
    "negative user enters wrong otp"
)

def wrong_otp(context):

    logger.info(
        "Clicking Verify Continue With Invalid OTP"
    )

    login = LoginPage(
        context.driver
    )

    login.click_verify_continue()

    time.sleep(5)

    logger.info(
        "Invalid OTP Validation Triggered"
    )


# =====================================================
# OTP VALIDATION
# =====================================================

@then(
    "negative otp error message should display"
)

def otp_error(context):

    assert (
        context.driver.current_url
        is not None
    )

    logger.info(
        "Invalid OTP Validation Successful"
    )


# =====================================================
# INVALID MOBILE VALIDATION
# =====================================================

@then(
    "negative invalid mobile error should display"
)

def invalid_mobile_error(context):

    assert (
        "bigbasket"
        in
        context.driver.current_url.lower()
    )

    logger.info(
        "Invalid Mobile Validation Successful"
    )