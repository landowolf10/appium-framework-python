*** Settings ***
Documentation    This test suite contains app tests for the login page

Library  ../keywords/common.py
Library  ../keywords/login.py

Suite Teardown  Close all screens

*** Variables ***


*** Test Cases ***
Validate login page
    When Launch application
    And Validate title  Login
    Then User is on login page