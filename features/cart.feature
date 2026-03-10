Feature: Shopping Cart functionality
  As a customer
  I want to be able to add, remove, and purchase items
  So that I can buy products online

  @TO-22
  Scenario: Add a single item to the cart
    Given the user is logged in
    And the user is on a product page for "Wireless Mouse"
    When the user clicks "Add to Cart"
    Then the shopping cart icon should show 1 item
    And a success message "Item added to cart" should be displayed

  @TO-23
  Scenario: Remove an item from the cart
    Given the user is logged in
    And the user has "Wireless Mouse" in their cart
    When the user goes to the cart page
    And clicks "Remove" on the "Wireless Mouse" item
    Then the shopping cart should be empty
    And a message "Cart is empty" should be displayed

  @TO-24
  Scenario: Checkout with items in the cart
    Given the user has "Keyboard" in their cart
    And the user is on the checkout page
    When the user enters shipping information
    And clicks "Place Order"
    Then the order should be confirmed
    And the user should receive an order number
