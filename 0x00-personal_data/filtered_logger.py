#!/usr/bin/env python3
"""
This module defines a function that returns the log msg obfuscated
"""
import re
import logging


def filter_datum(fields, redaction, message, separator):
    """
    Function returns obfuscated log msg, uses a regex to replace occurrences of certain field values and uses re.sub to perform the substitution with a single regex.
    Args:
        fields: a list of strings representing all fields to obfuscate
        redaction: a string representing by what the field will be obfuscated
        message: a string representing the log line
        separator: a string representing by which character is separating all
        fields in the log line (message)
    Returns:
        obfuscated log message
    """
    for field in fields:
        message = re.sub(rf"{field}=.*?{separator}", f"{field}={redaction}{separator}", message)
    return message

    pattern = r'({})=.+?(?={}|$)'.format('|'.join(fields), separator)
    return re.sub(pattern, lambda m: f"{m.group(1)}={redaction}", message)

class RedactingFormatter(logging.Formatter):
    """ Redacting Formatter class
        """

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self):
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        msg = super().format(record)
        return filter_datum(self.fields, self.REDACTION, msg, self.SEPARATOR)
