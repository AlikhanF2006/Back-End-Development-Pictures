"""Application package."""
from flask import Flask

app = Flask(__name__)

from backend import routes  # noqa: E402,F401
