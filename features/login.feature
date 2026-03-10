Feature: User Login
  As a registered user
  I want to be able to login to the system
  So that I can access my account

  Scenario: Successful login with valid credentials
    Given the user is on the login page
    When the user enters valid username "testuser" and password "password123"
    And clicks the login button
    Then the user should be redirected to the dashboard
    And a welcome message should be displayed

  Scenario: Failed login with invalid password
    Given the user is on the login page
    When the user enters valid username "testuser" and invalid password "wrongpass"
    And clicks the login button
    Then an error message "Invalid credentials" should be displayed
    And the user should remain on the login page

  Scenario: Failed login with empty credentials
    Given the user is on the login page
    When the user leaves the username and password fields empty
    And clicks the login button
    Then an error message "Username and password are required" should be displayed
