"""
Date Created: 27/07/2021
@Author: Orlando Avila
Description: Manage the diferent type of logs
"""

from robot.api import logger

#Colors
SUCCESS_GREEN = "#006400"
FAIL_RED = "#ff0000"
WARNIG_YELLOW="#d8870b"

def log_pass(log_info):
    formatted_message = _format_message(log_info, SUCCESS_GREEN)
    logger.info(formatted_message, html=True)

def log_fail(log_info):
    formatted_message = _format_message(log_info, FAIL_RED)
    logger.error(formatted_message, html=True)
    #Improvement -> Add screenshot of screen in error
    raise AssertionError("Ending test...")

def log_fail_exit(log_info):
    formatted_message = _format_message(log_info, FAIL_RED)
    logger.error(formatted_message, html=True)
    raise AssertionError("Ending test...")

def log_warning(log_info):
    formatted_message = _format_message(log_info, WARNIG_YELLOW)
    logger.warn(formatted_message, html=True)

def log_info(log_info):
    logger.info(log_info, html=False)

def _format_message(message, message_color):
    return f'<div style="color: {message_color};">{message}</div>'