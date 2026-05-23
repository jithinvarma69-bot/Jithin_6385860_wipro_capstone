Feature: Negative Testing


Scenario: Negative Wrong OTP

Given negative user opens BigBasket website

When negative user clicks login button

And negative user enters valid mobile number

And negative user clicks continue button

And negative user enters wrong otp

Then negative otp error message should display


Scenario: Negative Invalid Mobile Number

Given negative user opens BigBasket website

When negative user clicks login button

And negative user enters invalid mobile number

And negative user clicks continue button

Then negative invalid mobile error should display