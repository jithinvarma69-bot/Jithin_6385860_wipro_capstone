import os
from datetime import datetime


class ScreenshotUtil:

    @staticmethod
    def take_screenshot(driver, file_name):

        base_dir = os.path.dirname(os.path.dirname(__file__))

        screenshot_dir = os.path.join(base_dir, "screenshots")

        if not os.path.exists(screenshot_dir):
            os.makedirs(screenshot_dir)

        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

        screenshot_path = os.path.join(
            screenshot_dir,
            f"{file_name}_{timestamp}.png"
        )

        driver.save_screenshot(screenshot_path)

        print(f"Screenshot saved at: {screenshot_path}")

        return screenshot_path