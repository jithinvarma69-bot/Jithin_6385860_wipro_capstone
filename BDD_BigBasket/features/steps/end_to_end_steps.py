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
    "endtoend user opens BigBasket website"
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
    "endtoend user clicks login button"
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
    "endtoend user enters mobile number from csv"
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
    "endtoend user clicks continue button"
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
# OPEN PHARMACY PAGE
# =====================================================

@when(
    "endtoend user opens pharmacy page"
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
# APPLY BRAND FILTER
# =====================================================

@when(
    "endtoend user applies brand filter"
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
# ADD PRODUCT TO BASKET
# =====================================================

@when(
    "endtoend user adds product to basket"
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
# OPEN CHECKOUT PAGE
# =====================================================

@when(
    "endtoend user opens checkout page"
)

def checkout(context):

    logger.info(
        "Opening Checkout Page"
    )

    pharmacy = PharmacyPage(
        context.driver
    )

    pharmacy.open_checkout()

    time.sleep(5)

    logger.info(
        "Checkout Page Opened Successfully"
    )


# =====================================================
# PROCEED TO PAYMENT PAGE
# =====================================================

@when(
    "endtoend user proceeds to payment page"
)

def payment(context):

    logger.info(
        "Proceeding To Payment Page"
    )

    pharmacy = PharmacyPage(
        context.driver
    )

    pharmacy.proceed_payment()

    time.sleep(5)

    logger.info(
        "Payment Page Opened Successfully"
    )


# =====================================================
# PAYMENT VALIDATION
# =====================================================

@then(
    "endtoend payment page should open successfully"
)

def payment_success(context):

    current_url = (
        context.driver.current_url.lower()
    )

    assert (
        "payment"
        in
        current_url
        or
        "checkout"
        in
        current_url
    )

    logger.info(
        "End To End Flow Completed Successfully"
    )