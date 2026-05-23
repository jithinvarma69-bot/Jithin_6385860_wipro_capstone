Feature: Positive Testing


Scenario: Positive Login Successful

Given positive user opens BigBasket website

When positive user clicks login button

And positive user enters mobile number from csv

And positive user clicks continue button

Then positive login should be successful


Scenario: Positive Pharmacy Page Opening Successful

Given positive user opens BigBasket website

When positive user clicks login button

And positive user enters mobile number from csv

And positive user clicks continue button

And positive user opens pharmacy page

Then positive pharmacy page should open successfully


Scenario: Positive Brand Filter Successful

Given positive user opens BigBasket website

When positive user clicks login button

And positive user enters mobile number from csv

And positive user clicks continue button

And positive user opens pharmacy page

And positive user applies brand filter

Then positive brand filter should apply successfully


Scenario: Positive Add Product To Basket Successful

Given positive user opens BigBasket website

When positive user clicks login button

And positive user enters mobile number from csv

And positive user clicks continue button

And positive user opens pharmacy page

And positive user adds product to basket

Then positive product should add successfully