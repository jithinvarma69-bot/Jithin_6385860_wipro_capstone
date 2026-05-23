# BigBasket Automation Testing Framework

---

# Project Title

## BigBasket Automation Framework Using Selenium Python BDD

---

# Project Overview

BigBasket Automation Framework is a complete automation testing framework developed using Selenium WebDriver with Python for automating and validating the BigBasket web application.

This framework is designed using industry-level automation concepts such as:

- Selenium Automation
- Behave BDD Framework
- Page Object Model (POM)
- Data Driven Testing
- Positive Testing
- Negative Testing
- End To End Testing
- Logging
- Allure Reporting

The framework automates multiple user workflows of the BigBasket application and validates different functionalities such as:

- Login functionality
- Pharmacy page validation
- Brand filter validation
- Add to basket functionality
- Checkout flow
- Payment page navigation
- Invalid mobile validation
- Invalid OTP validation

---

# Main Objective Of The Project

The main objective of this project is:

- Automate BigBasket web application testing
- Reduce manual testing effort
- Validate application workflows automatically
- Improve execution speed
- Implement reusable automation framework
- Implement BDD Data Driven Testing
- Generate execution logs
- Generate Allure reports
- Follow industry automation standards

---

# Technologies Used

| Technology | Purpose |
|------------|----------|
| Python | Programming Language |
| Selenium WebDriver | Browser Automation |
| Behave | BDD Framework |
| Pytest | Test Execution |
| Allure Reports | Reporting |
| WebDriver Manager | Driver Management |
| CSV | Data Driven Testing |
| Logging | Execution Logs |

---

# Framework Design Pattern

## Page Object Model (POM)

This framework follows the Page Object Model design pattern.

Advantages:

- Better code reusability
- Easy maintenance
- Less code duplication
- Better framework structure
- Centralized web element management

Separate page classes are created for:

- Login Page
- Pharmacy Page
- Base Page

---

# Framework Architecture

``` id="arch001"
Project_BigBasket/

│
├── .venv/
│
├── allure-report/
│
├── allure-results/
│
├── config/
│   └── config.properties
│
├── data/
│   └── login_data.csv
│
├── features/
│   ├── positive.feature
│   ├── negative.feature
│   ├── end_to_end.feature
│   │
│   ├── environment.py
│   │
│   └── steps/
│       ├── positive_steps.py
│       ├── negative_steps.py
│       └── end_to_end_steps.py
│
├── logs/
│   └── automation.log
│
├── pages/
│   ├── __init__.py
│   ├── base_page.py
│   ├── login_page.py
│   └── pharmacy_page.py
│
├── screenshots/
│
├── tests/
│   ├── __init__.py
│   ├── test_1_end_to_end.py
│   ├── test_2_positive.py
│   └── test_3_negative.py
│
├── utils/
│   ├── config_reader.py
│   ├── csv_reader.py
│   ├── excel_reader.py
│   ├── logger.py
│   └── screenshot_util.py
│
└── README.md