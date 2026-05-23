import allure
import pytest
import time

from pages.login_page import LoginPage
from pages.pharmacy_page import PharmacyPage
from utils.logger import LogGen


logger = LogGen.loggen()


# ======================================================
# SCREENSHOT FUNCTION
# ======================================================

def take_screenshot(driver, name):

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
# COMMON LOGIN FLOW
# ======================================================

def login_flow(driver):

    logger.info(
        "Starting Login Flow"
    )

    login = LoginPage(driver)

    login.open_bigbasket()

    time.sleep(5)

    # ASSERTION
    assert (
        "bigbasket"
        in
        driver.current_url.lower()
    )

    take_screenshot(
        driver,
        "homepage"
    )

    logger.info(
        "Homepage Opened Successfully"
    )

    login.click_login()

    time.sleep(3)

    take_screenshot(
        driver,
        "login_popup"
    )

    # ASSERTION
    assert (
        driver.current_url
        is not None
    )

    logger.info(
        "Login Popup Opened Successfully"
    )

    login.enter_mobile_email(
        "7396738499"
    )

    time.sleep(3)

    take_screenshot(
        driver,
        "mobile_entered"
    )

    # ASSERTION
    assert (
        driver.current_url
        is not None
    )

    logger.info(
        "Mobile Number Entered Successfully"
    )

    login.click_continue()

    time.sleep(20)

    login.click_verify_continue()

    time.sleep(8)

    take_screenshot(
        driver,
        "login_success"
    )

    # ASSERTION
    assert (
        "bigbasket"
        in
        driver.current_url.lower()
    )

    logger.info(
        "Login Successful"
    )


# ======================================================
# POSITIVE TEST CASE 1
# BRAND FILTER
# ======================================================

@allure.feature(
    "Positive Testing"
)

@allure.story(
    "Brand Filter Working"
)

@pytest.mark.order(1)

def test_brand_filter(driver):

    logger.info(
        "Starting Brand Filter Test"
    )

    login_flow(driver)

    pharmacy = PharmacyPage(driver)

    driver.get(
        "https://www.bigbasket.com/cl/pharmacy-wellness/"
    )

    time.sleep(5)

    take_screenshot(
        driver,
        "pharmacy_page"
    )

    # ASSERTION
    assert (
        "pharmacy"
        in
        driver.current_url.lower()
    )

    logger.info(
        "Pharmacy Page Opened Successfully"
    )

    pharmacy.select_brand(
        "Dettol"
    )

    time.sleep(5)

    take_screenshot(
        driver,
        "brand_filter"
    )

    # ASSERTION
    assert (
        driver.current_url
        is not None
    )

    logger.info(
        "Brand Filter Working Successfully"
    )


# ======================================================
# POSITIVE TEST CASE 2
# PRICE FILTER
# ======================================================

@allure.feature(
    "Positive Testing"
)

@allure.story(
    "Price Filter Working"
)

@pytest.mark.order(2)

def test_price_filter(driver):

    logger.info(
        "Starting Price Filter Test"
    )

    login_flow(driver)

    pharmacy = PharmacyPage(driver)

    driver.get(
        "https://www.bigbasket.com/cl/pharmacy-wellness/"
    )

    time.sleep(5)

    # ASSERTION
    assert (
        "pharmacy"
        in
        driver.current_url.lower()
    )

    logger.info(
        "Pharmacy Page Opened Successfully"
    )

    pharmacy.select_price_filter(
        "300",
        "500"
    )

    time.sleep(5)

    take_screenshot(
        driver,
        "price_filter"
    )

    # ASSERTION
    assert (
        driver.current_url
        is not None
    )

    logger.info(
        "Price Filter Working Successfully"
    )


# ======================================================
# POSITIVE TEST CASE 3
# ADD TO BASKET
# ======================================================

@allure.feature(
    "Positive Testing"
)

@allure.story(
    "Add Product To Basket"
)

@pytest.mark.order(3)

def test_add_to_basket(driver):

    logger.info(
        "Starting Add To Basket Test"
    )

    login_flow(driver)

    pharmacy = PharmacyPage(driver)

    driver.get(
        "https://www.bigbasket.com/cl/pharmacy-wellness/"
    )

    time.sleep(5)

    # ASSERTION
    assert (
        "pharmacy"
        in
        driver.current_url.lower()
    )

    logger.info(
        "Pharmacy Page Opened Successfully"
    )

    pharmacy.add_to_basket()

    time.sleep(5)

    take_screenshot(
        driver,
        "product_added"
    )

    # ASSERTION
    assert (
        driver.current_url
        is not None
    )

    logger.info(
        "Product Added Successfully"
    )


# ======================================================
# POSITIVE TEST CASE 4
# OPEN BASKET
# ======================================================

@allure.feature(
    "Positive Testing"
)

@allure.story(
    "Basket Opening Successful"
)

@pytest.mark.order(4)

def test_open_basket(driver):

    logger.info(
        "Starting Open Basket Test"
    )

    login_flow(driver)

    pharmacy = PharmacyPage(driver)

    driver.get(
        "https://www.bigbasket.com/cl/pharmacy-wellness/"
    )

    time.sleep(5)

    # ASSERTION
    assert (
        "pharmacy"
        in
        driver.current_url.lower()
    )

    logger.info(
        "Pharmacy Page Opened Successfully"
    )

    pharmacy.add_to_basket()

    time.sleep(5)

    # ASSERTION
    assert (
        driver.current_url
        is not None
    )

    logger.info(
        "Product Added Successfully"
    )

    pharmacy.open_basket()

    time.sleep(5)

    take_screenshot(
        driver,
        "basket_opened"
    )

    # ASSERTION
    assert (
        driver.current_url
        is not None
    )

    logger.info(
        "Basket Opened Successfully"
    )