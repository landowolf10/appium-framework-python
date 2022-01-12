*** Settings ***
Documentation    This test suite contains app tests for the login page

Library  ../keywords/common.py
Library  ../keywords/create_user.py

Suite Teardown  Close all screens

*** Variables ***


*** Test Cases ***
Validate register screen
    When Launch application
    And Click create user button
    Then Validate title  Registro
    And User is on register screen

Verify registration with empty boxes
    When User is on register screen
    And Click register button
    Then Verify popup title is  Campos vacíos
    And Validate popup message is  Favor de llenar todos los campos.
    And Click accept popup button
    Then Verify popup visibility is  False