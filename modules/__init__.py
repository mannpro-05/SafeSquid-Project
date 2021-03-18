from flask import Flask
import logging
import json

logging.basicConfig(filename='record.log', level=logging.DEBUG)
with open('modules/config.json') as configFile:
    config_data = json.load(configFile)
app = Flask(__name__)
app.secret_key = "5791628bb0b13ce0c676dfde280ba245"
app.config.update(config_data)

from modules import routes