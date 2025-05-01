#!/usr/bin/env python3
"""
This module defines a function that returns the log msg obfuscated
"""
import re


def filter_datum(fields, redaction, message, separator):
    """
    Function returns masked log msg, uses a regex to replace occurrences of certain
    field values and uses re.sub to perform the substitution with a single regex.
    Args:
        fields: a list of strings representing all fields to obfuscate
        redaction: a string representing by what the field will be obfuscated
        message: a string representing the log line
        separator: a string representing by which character is separating all
        fields in the log line (message)
    Returns:
        obfuscated log message
    """
    pattern = f'({"|".join(fields)})=[^{separator}]+'
    return re.sub(pattern, lambda m: f"{m.group(1)}={redaction}", message)