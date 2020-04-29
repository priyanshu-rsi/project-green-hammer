import pkg_resources
pkg_resources.require("PyYAML==5.3.1")
import yaml
print("Using yaml version: ", yaml.__version__)
from os import path

class ConfigHelper:
    def __init__(self):
        print("Inited ConfigHelper")
        self.configPath = "config.yml"
        
        #Create file if it doesn't exists(failsafe)
        if not path.exists('userconfig.yml'):
            file = open('userconfig.yml', 'w+')
            file.close()

    def read(self, key=False):
        print("Reading config")
        sendBack = False
        with open(r'userconfig.yml') as configFile:
            config = yaml.load(configFile, Loader=yaml.FullLoader)
            sendBack = config
        if key:
            for index,item in enumerate(config):
                for cKey in item:
                    if cKey == key: #Found the parent config key
                        sendBack = item[key]
        print(sendBack)
        return sendBack

    def write(self, key, value): # Creates the key if it doesn't exists, update if it does
        config = self.read()
        config = config if config != None else []
        print("Writing config")
        i = 0
        processed = False
        for index,item in enumerate(config):

            for cKey in item:
                if cKey == key: #Found the parent config key
                    config[index][cKey] = value
                    processed = True
            i=i+1
        if not processed:
            d = {}
            d[key] = value
            config.append(d)
        with open(r'userconfig.yml', 'w') as file:
            userconfig = yaml.dump(config, file)
        return True

    def delete(self, key):
        print("Delete config item")
        config = self.read()
        config = config if config != None else []
        print("Writing config")
        i = 0
        processed = False
        for index,item in enumerate(config):

            for cKey in item:
                if cKey == key: #Found the parent config key
                    del config[index]
                    processed = True
        with open(r'userconfig.yml', 'w') as file:
            userconfig = yaml.dump(config, file)
        return True


# app =   ConfigHelper()
# app.write("sample", {"this": "complex object", "isa" : "object", "is": "the"})
# app.read("sample")
# app.delete("sample")