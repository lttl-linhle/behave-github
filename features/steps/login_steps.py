from behave import when, given, then

@given('the user is on the login page')
def step_impl(context):
    print("Navigating to login page")

@when('the user enters valid username "{username}" and password "{password}"')
def step_impl(context, username, password):
    print(f"Entering username: {username} and password: {password}")

@when('clicks the login button')
def step_impl(context):
    print("Clicking login button")

@then('the user should be redirected to the dashboard')
def step_impl(context):
    print("User is redirected to the dashboard")

@then('a welcome message should be displayed')
def step_impl(context):
    print("Welcome message displayed")

@when('the user enters valid username "{username}" and invalid password "{password}"')
def step_impl(context, username, password):
    print(f"Entering username: {username} and invalid password: {password}")

@then('an error message "{message}" should be displayed')
def step_impl(context, message):
    print(f"Error message displayed: {message}")

@then('the user should remain on the login page')
def step_impl(context):
    print("User remains on login page")

@when('the user leaves the username and password fields empty')
def step_impl(context):
    print("Leaving form empty")

