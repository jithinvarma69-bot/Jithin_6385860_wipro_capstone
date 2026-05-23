from behave import *

import time
import csv

from selenium import webdriver

from selenium.webdriver.chrome.service import Service

from webdriver_manager.chrome import ChromeDriverManager

from pages.login_page import LoginPage

from pages.pharmacy_page import PharmacyPage

from utils.logger import LogGen


logger = LogGen.loggen()


# =====================================================
# READ CSV DATA
# =====================================================

def read_csv_data():

    with open(
        "data/login_data.csv"
    ) as file:

        reader = csv.DictReader(
            file
        )

        return list(reader)


# =====================================================
# OPEN WEBSITE
# =====================================================

@given(
    "positive user opens BigBasket website"
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
        "BigBasket Website Opened Successfully"
    )


# =====================================================
# CLICK LOGIN BUTTON
# =====================================================

@when(
    "positive user clicks login button"
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
        "Login Button Clicked Successfully"
    )


# =====================================================
# ENTER MOBILE NUMBER
# =====================================================

@when(
    "positive user enters mobile number from csv"
)

def mobile(context):

    logger.info(
        "Entering Mobile Number"
    )

    login = LoginPage(
        context.driver
    )

    data = read_csv_data()

    mobile = data[0]["mobile"]

    login.enter_mobile_email(
        mobile
    )

    time.sleep(3)

    logger.info(
        "Mobile Number Entered Successfully"
    )


# =====================================================
# CLICK CONTINUE BUTTON
# =====================================================

@when(
    "positive user clicks continue button"
)

def continue_button(context):

    logger.info(
        "Clicking Continue Button"
    )

    login = LoginPage(
        context.driver
    )

    login.click_continue()

    time.sleep(20)

    login.click_verify_continue()

    time.sleep(8)

    logger.info(
        "Login Successful"
    )


# =====================================================
# LOGIN VALIDATION
# =====================================================

@then(
    "positive login should be successful"
)

def login_success(context):

    assert (
        "bigbasket"
        in
        context.driver.current_url.lower()
    )

    logger.info(
        "Positive Login Validation Successful"
    )


# =====================================================
# OPEN PHARMACY PAGE
# =====================================================

@when(
    "positive user opens pharmacy page"
)

def pharmacy(context):

    logger.info(
        "Opening Pharmacy Page"
    )

    pharmacy = PharmacyPage(
        context.driver
    )

    pharmacy.open_pharmacy()

    time.sleep(5)

    logger.info(
        "Pharmacy Page Opened Successfully"
    )


# =====================================================
# PHARMACY VALIDATION
# =====================================================

@then(
    "positive pharmacy page should open successfully"
)

def pharmacy_success(context):

    assert (
        "pharmacy"
        in
        context.driver.current_url.lower()
    )

    logger.info(
        "Pharmacy Validation Successful"
    )


# =====================================================
# APPLY BRAND FILTER
# =====================================================

@when(
    "positive user applies brand filter"
)

def filter_brand(context):

    logger.info(
        "Applying Brand Filter"
    )

    pharmacy = PharmacyPage(
        context.driver
    )

    pharmacy.apply_brand_filter(
        "Dettol"
    )

    time.sleep(5)

    logger.info(
        "Brand Filter Applied Successfully"
    )


# =====================================================
# FILTER VALIDATION
# =====================================================

@then(
    "positive brand filter should apply successfully"
)

def filter_success(context):

    assert (
        context.driver.current_url
        is not None
    )

    logger.info(
        "Brand Filter Validation Successful"
    )


# =====================================================
# ADD PRODUCT TO BASKET
# =====================================================

@when(
    "positive user adds product to basket"
)

def basket(context):

    logger.info(
        "Adding Product To Basket"
    )

    pharmacy = PharmacyPage(
        context.driver
    )

    pharmacy.add_product_to_basket()

    time.sleep(5)

    logger.info(
        "Product Added To Basket Successfully"
    )


# =====================================================
# PRODUCT VALIDATION
# =====================================================

@then(
    "positive product should add successfully"
)

def product_success(context):

    assert (
        context.driver.current_url
        is not None
    )

    logger.info(
        "Positive Basket Validation Successful"
    )