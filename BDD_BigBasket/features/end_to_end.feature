Feature: End To End Testing


Scenario: Complete BigBasket Flow

Given endtoend user opens BigBasket website

When endtoend user clicks login button

And endtoend user enters mobile number from csv

And endtoend user clicks continue button

And endtoend user opens pharmacy page

And endtoend user applies brand filter

And endtoend user adds product to basket

And endtoend user opens checkout page

And endtoend user proceeds to payment page

Then endtoend payment page should open successfully