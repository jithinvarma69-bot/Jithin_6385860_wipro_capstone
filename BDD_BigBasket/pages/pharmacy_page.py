from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


class PharmacyPage:

    def __init__(self, driver):

        self.driver = driver

        self.wait = WebDriverWait(
            driver,
            20
        )

    # =================================================
    # REUSABLE JS CLICK
    # =================================================

    def js_click(self, xpath):

        element = self.wait.until(
            EC.presence_of_element_located(
                (By.XPATH, xpath)
            )
        )

        self.driver.execute_script(
            "arguments[0].scrollIntoView({behavior:'smooth', block:'center'});",
            element
        )

        time.sleep(1)

        self.driver.execute_script(
            "arguments[0].click();",
            element
        )

    # =================================================
    # SELECT BRAND FILTER
    # =================================================

    def select_brand(self, brand):

        try:

            brand_checkbox = self.wait.until(
                EC.presence_of_element_located(
                    (
                        By.XPATH,
                        f"//label[contains(.,'{brand}')]"
                    )
                )
            )

            self.driver.execute_script(
                "arguments[0].scrollIntoView();",
                brand_checkbox
            )

            time.sleep(2)

            self.driver.execute_script(
                "arguments[0].click();",
                brand_checkbox
            )

            print(
                f"{brand} brand selected"
            )

            time.sleep(3)

        except Exception as e:

            print(
                f"Brand filter failed: {e}"
            )

    # =================================================
    # SELECT PRICE FILTER
    # =================================================

    def select_price_filter(
            self,
            min_price,
            max_price
    ):

        try:

            time.sleep(5)

            price_checkbox = self.wait.until(
                EC.presence_of_element_located(
                    (
                        By.XPATH,
                        f"//*[contains(text(),'Rs {min_price} to Rs {max_price}')]"
                    )
                )
            )

            self.driver.execute_script(
                "arguments[0].scrollIntoView();",
                price_checkbox
            )

            time.sleep(2)

            self.driver.execute_script(
                "arguments[0].click();",
                price_checkbox
            )

            print(
                f"Price filter selected: Rs {min_price} to Rs {max_price}"
            )

            time.sleep(3)

        except Exception as e:

            print(
                f"Price filter failed: {e}"
            )

    # =================================================
    # SELECT RATING FILTER
    # =================================================

    def select_rating_filter(
            self,
            rating
    ):

        try:

            rating_checkbox = self.wait.until(
                EC.presence_of_element_located(
                    (
                        By.XPATH,
                        "(//input[@type='checkbox'])[1]"
                    )
                )
            )

            self.driver.execute_script(
                "arguments[0].scrollIntoView();",
                rating_checkbox
            )

            time.sleep(2)

            self.driver.execute_script(
                "arguments[0].click();",
                rating_checkbox
            )

            print(
                f"{rating} Star Rating Selected"
            )

            time.sleep(3)

        except Exception as e:

            print(
                f"Rating filter failed: {e}"
            )

    # =================================================
    # ADD PRODUCT TO BASKET
    # =================================================

    def add_to_basket(self):

        try:

            add_button = self.wait.until(
                EC.presence_of_element_located(
                    (
                        By.XPATH,
                        "//button[contains(text(),'Add')]"
                    )
                )
            )

            self.driver.execute_script(
                "arguments[0].scrollIntoView();",
                add_button
            )

            time.sleep(2)

            self.driver.execute_script(
                "arguments[0].click();",
                add_button
            )

            print(
                "Product added to basket"
            )

            time.sleep(3)

        except Exception as e:

            print(
                f"Add to basket failed: {e}"
            )

    # =================================================
    # INCREASE QUANTITY
    # =================================================

    def increase_quantity(self):

        try:

            plus_button = self.wait.until(
                EC.presence_of_element_located(
                    (
                        By.XPATH,
                        "//button[contains(@class,'increment')]"
                    )
                )
            )

            self.driver.execute_script(
                "arguments[0].click();",
                plus_button
            )

            print(
                "Quantity increased"
            )

            time.sleep(3)

        except Exception as e:

            print(
                f"Quantity increase failed: {e}"
            )

    # =================================================
    # OPEN BASKET
    # =================================================

    def open_basket(self):

        try:

            basket = self.wait.until(
                EC.presence_of_element_located(
                    (
                        By.XPATH,
                        "//span[contains(text(),'item') or contains(text(),'Item')]"
                    )
                )
            )

            self.driver.execute_script(
                "arguments[0].click();",
                basket
            )

            print(
                "Basket opened"
            )

            time.sleep(3)

        except Exception as e:

            print(
                f"Basket open failed: {e}"
            )

    # =================================================
    # CHECKOUT
    # =================================================

    def click_checkout(self):

        try:

            checkout = self.wait.until(
                EC.presence_of_element_located(
                    (
                        By.XPATH,
                        "//button[contains(text(),'Checkout')]"
                    )
                )
            )

            self.driver.execute_script(
                "arguments[0].click();",
                checkout
            )

            print(
                "Checkout opened"
            )

            time.sleep(3)

        except Exception as e:

            print(
                f"Checkout failed: {e}"
            )

    # =================================================
    # OPEN PHARMACY PAGE
    # =================================================

    def open_pharmacy(self):

        self.driver.get(
            "https://www.bigbasket.com/cl/pharmacy-wellness/"
        )

    # =================================================
    # SEARCH PRODUCT
    # =================================================

    def search_product(self, product):

        search = self.driver.find_element(
            By.XPATH,
            "//input[@placeholder='Search for Products...']"
        )

        search.send_keys(product)

        time.sleep(3)

    # =================================================
    # APPLY BRAND FILTER
    # =================================================

    def apply_brand_filter(self, brand):

        brand_filter = self.driver.find_element(
            By.XPATH,
            "//span[contains(text(),'Brand')]"
        )

        self.driver.execute_script(
            "arguments[0].scrollIntoView();",
            brand_filter
        )

        time.sleep(2)

        self.driver.execute_script(
            "arguments[0].click();",
            brand_filter
        )

        time.sleep(3)

    # =================================================
    # ADD PRODUCT TO BASKET
    # =================================================

    def add_product_to_basket(self):

        add_button = self.driver.find_element(
            By.XPATH,
            "(//button[contains(text(),'Add')])[1]"
        )

        self.driver.execute_script(
            "arguments[0].scrollIntoView();",
            add_button
        )

        time.sleep(2)

        self.driver.execute_script(
            "arguments[0].click();",
            add_button
        )

        time.sleep(3)

    # =================================================
    # OPEN CHECKOUT PAGE
    # =================================================

    def open_checkout(self):

        self.driver.get(
            "https://www.bigbasket.com/basket/"
        )

        time.sleep(5)

    # =================================================
    # PROCEED TO PAYMENT PAGE
    # =================================================

    def proceed_payment(self):

        checkout = self.driver.find_element(
            By.XPATH,
            "//button[contains(text(),'Checkout')]"
        )

        self.driver.execute_script(
            "arguments[0].click();",
            checkout
        )

        time.sleep(5)
