*** Settings ***
Documentation    This Test Suite contains web tests for the calculator app

Library  ../keywords/common.py
Library  ../keywords/calculator.py

Suite Teardown  Close all screens

*** Variables ***


*** Test Cases ***
Validate typed number
    When Launch application
    And Type number  3
    Then Validate typed number is  3

Clear screen
    When Press delete button
    Then Verify screen is clean

Type all numbers on screen
    When Type all numbers
    Then Verify numbers on screen are  0123456789