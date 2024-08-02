#!/usr/bin/env python3
"""
    A function called filter_dataum
    returns  the log message obfuscated
    args:
        fields: a list of strings representing
        all fields to obfuscate
        redaction: a string representing
        by what the field will be obfuscated
        message: a string representing the log line
        separator: a string representing by which
        character is separating all fields
    the func should use a regex to replace
    occurrences of certain field values
    filter_dataum should be less that 5 lines
    long use re.sub to perform the substitution
"""
import re


def filter_dataum(fields, redaction, message, separator):
    """
        returns the log message obfuscated
    """
    return re.sub(rf"({'|'.join(fields)})", redaction, message)
