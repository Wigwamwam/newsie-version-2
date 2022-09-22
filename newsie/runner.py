import os

from newsie.query_helper import QueryHelper


LOGFILE = os.environ.get("LOGFILE", "/tmp/newsielog")

NEWS_API_KEY = os.environ.get("NEWS_API_KEY")
SLACK_BOT_TOKEN = os.environ.get("SLACK_BOT_TOKEN")
SLACK_BOT_NAME = os.environ.get("SLACK_BOT_NAME", "Newsie")
DEFAULT_SLACK_CHANNEL = os.environ.get("DEFAULT_SLACK_CHANNEL", "#news-results")

QUERIES = []


