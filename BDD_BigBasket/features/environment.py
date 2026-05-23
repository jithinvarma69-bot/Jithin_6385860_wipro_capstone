import os

from datetime import datetime

import allure


# =====================================================
# BEFORE SCENARIO
# =====================================================

def before_scenario(context, scenario):

    print(
        f"\nStarting Scenario: {scenario.name}"
    )


# =====================================================
# AFTER EVERY STEP
# =====================================================

def after_step(context, step):

    try:

        if hasattr(context, "driver"):

            # =========================================
            # CREATE SCREENSHOT FOLDER
            # =========================================

            if not os.path.exists(
                "screenshots"
            ):

                os.makedirs(
                    "screenshots"
                )

            # =========================================
            # SCREENSHOT FILE NAME
            # =========================================

            screenshot_name = (
                f"screenshots/"
                f"{step.name}_"
                f"{datetime.now().strftime('%Y%m%d_%H%M%S')}.png"
            )

            # =========================================
            # SAVE SCREENSHOT
            # =========================================

            context.driver.save_screenshot(
                screenshot_name
            )

            # =========================================
            # ATTACH TO ALLURE REPORT
            # =========================================

            allure.attach.file(
                screenshot_name,
                name=step.name,
                attachment_type=allure.attachment_type.PNG
            )

    except Exception as e:

        print(
            f"Screenshot Error: {e}"
        )


# =====================================================
# AFTER SCENARIO
# =====================================================

def after_scenario(context, scenario):

    print(
        f"\nCompleted Scenario: {scenario.name}"
    )

    try:

        if hasattr(context, "driver"):

            context.driver.quit()

    except:

        pass