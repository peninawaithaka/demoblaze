Feature: User login

    Background:
        Given the user navigates to the login page

    Scenario: Successful login with valid credentials
        When the user enters valid credentials
        Then the user is directed to their logged in home page

    # Scenario: Failed login with invalid credentails
    #     When the user enter invalid credentials
    #     Then an error message is displayed