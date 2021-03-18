from modules import app
import json
def mailConfig(data):
    with open('modules/config.json') as configFile:
        config_data = json.load(configFile)
    for key, value in data.items():
        if value != "":
            config_data[key] = value
        configFile.close()

    with open('modules/config.json','w') as configFile:
        json.dump(config_data, configFile)

    app.config.update(config_data)