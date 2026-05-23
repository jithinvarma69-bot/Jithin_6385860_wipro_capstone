import pytest
import os
import subprocess

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


# ======================================================
# DRIVER FIXTURE
# ======================================================

@pytest.fixture(scope="function")

def driver():

    driver = webdriver.Chrome(
        service=Service(
            ChromeDriverManager().install()
        )
    )

    driver.maximize_window()

    yield driver

    driver.quit()


# ======================================================
# ALLURE REPORT AFTER TEST EXECUTION
# ======================================================

def pytest_sessionfinish(session, exitstatus):

    print(
        "\nGenerating Allure Report..."
    )

    os.system(
        "allure generate allure-results -o allure-report --clean"
    )

    print(
        "\nOpening Allure Report..."
    )

    subprocess.Popen(
        [
            "allure",
            "open",
            "allure-report"
        ]
    )