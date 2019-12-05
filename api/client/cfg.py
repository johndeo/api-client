"""Configuration file."""

import logging

"""Logging"""
DEFAULT_LOG_LEVEL = logging.INFO  # change to DEBUG for more detail

"""Default host"""
API_HOST = 'https://api.gro-intelligence.com'

"""BatchClient"""
ASYNC = False
MAX_QUERIES_PER_SECOND = 10

"""Requests"""
MAX_RETRIES = 4
TIMEOUT = 6000

"""GroClient smart add_data_series"""
MAX_RESULT_COMBINATION_DEPTH = 3
