#!/usr/bin/env python3
"""
This module defines a function that returns the log msg obfuscated
"""
import os
import re
import logging
import mysql.connector
from typing import List


def filter_datum(fields: List[str], redaction: str,
                 message: str, separator: str) -> str:
    """
    Function returns masked log msg, uses a regex to replace
    occurrences of certain field values and uses re.sub to
    perform the substitution with a single regex.
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


PII_FIELDS = ("name", "email", "phone", "ssn", "password")


def get_logger() -> logging.Logger:
    """
    creates and configures a logger for user_data with
    PII redaction
    """
    logger = logging.getLogger("user_data")  # name logger
    logger.setLevel(logging.INFO)  # set level
    logger.propagate = False  # disable propagation
    handler = logging.streamHandler()  # create handler
    # formatter to redact PIIs
    formatter = RedactingFormatter(fields=list(PII_FIELDS))
    handler.setFormatter(formatter)
    logger.addHandler(handler)  # add handler, logger
    return logger


def get_db() -> mysql.connector.connection.MySQLConnection:
    """
    Connects to MySQL db using env variables and returns
    a MySQLConnection object
    """
    username = os.getenv("PERSONAL_DATA_DB_USERNAME", "root")
    password = os.getenv("PERSONAL_DATA_DB_PASSWORD", "")
    host = os.getenv("PERSONAL_DATA_DB_HOST", "localhost")
    db_name = os.getenv("PERSONAL_DATA_DB_NAME")

    return mysql.connector.connect(
        user=username,
        password=password,
        host=host,
        database=db_name
    )


def main() -> None:
    """
    obtain a db connection using get_db (I)
    retrieve all rows in the users table (II)
    display each row under a filtered format (III)
    """
    # I
    db = get_db()
    logger = get_logger()
    # II
    cursor = db.cursor(dictionary=True)
    cursor.execute("SELECT * FROM users;")
    for row in cursor:
        # III
        message = "; ".join(f"{key}={value}" for key, value in row.items())
        logger.info(message)
    cursor.close()
    db.close()

    if __name__ == "__main__":
        main()


class RedactingFormatter(logging.Formatter):
    """ Redacting Formatter class
        """

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[str]):
        """
        instantiate
        """
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        """
        called when a log record's formatted into a str
        """
        record.msg = filter_datum(self.fields, self.REDACTION,
                                  record.msg, self.SEPARATOR)
        return super().format(record)
