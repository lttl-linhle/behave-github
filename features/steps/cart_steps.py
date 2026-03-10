from behave import given, when, then

@given('the user is logged in')
def step_impl(context):
    print("User is logged in")

@given('the user is on a product page for "{product}"')
def step_impl(context, product):
    print(f"Viewing product: {product}")

@when('the user clicks "Add to Cart"')
def step_impl(context):
    print("Clicking Add to Cart")

@then('the shopping cart icon should show {count:d} item')
def step_impl(context, count):
    print(f"Cart shows {count} item(s)")

@then('a success message "{message}" should be displayed')
def step_impl(context, message):
    print(f"Success message: {message}")

@given('the user has "{product}" in their cart')
def step_impl(context, product):
    print(f"User has {product} in cart")

@given('the user is on the checkout page')
def step_impl(context):
    print("User is on the checkout page")

@when('the user goes to the cart page')
def step_impl(context):
    print("Navigating to cart page")

@when('clicks "Remove" on the "{product}" item')
def step_impl(context, product):
    print(f"Removing {product} from cart")

@then('the shopping cart should be empty')
def step_impl(context):
    print("Cart is now empty")

@then('a message "{message}" should be displayed')
def step_impl(context, message):
    print(f"Message displayed: {message}")

@when('the user enters shipping information')
def step_impl(context):
    print("Entering shipping info")

@when('clicks "Place Order"')
def step_impl(context):
    print("Clicking Place Order")

@then('the order should be confirmed')
def step_impl(context):
    print("Order confirmed")

@then('the user should receive an order number')
def step_impl(context):
    print("Order number received")

