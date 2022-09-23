import os
from dotenv import load_dotenv
from pathlib import Path

dotenv_path = Path('/.env')
load_dotenv(dotenv_path=dotenv_path)


from newsie.query_helper import QueryHelper


LOGFILE = os.environ.get("LOGFILE", "/tmp/newsielog")

NEWS_API_KEY = os.getenv("NEWS_API_KEY")
SLACK_BOT_TOKEN = os.getenv("SLACK_BOT_TOKEN")
SLACK_BOT_NAME = os.environ.get("SLACK_BOT_NAME", "Newsie")
DEFAULT_SLACK_CHANNEL = os.environ.get("DEFAULT_SLACK_CHANNEL", "#news-results")

# Pytz timezone string. You can see a full list here:
# https://gist.github.com/heyalexej/8bf688fd67d7199be4a1682b3eec7568
# or by calling pytz.all_timezones
TIMEZONE = "America/New_York"

# Valid 2 letter The 2-letter ISO 3166-1 code (lowercase).
# E.g. "us" for USA. Defaults to all.
COUNTRY_CODE = "us"

# Query objects for us to use in our application

QUERIES = [

    QueryHelper(
        name="Finance News",
        query="stock market",
        language="en"
    ),

    QueryHelper(
        name="Science News",
        category="science",
        slack_channel="#science",
        language="en"
    ),

]
