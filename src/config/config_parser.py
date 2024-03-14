import logging
import configparser
import os

class Config:
    def __init__(self):
        self.config_file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "config.ini")
        self.config =  configparser.ConfigParser()
        self.config.read(self.config_file_path)
        print(self.config.sections())
        self.env = self.config["env"]["ENVIRONMENT"]
        self.logging_level = logging.INFO
        # self.config.set(self.env, "logging_level", logging.INFO) 
        # with open('self.config_file_path', 'w') as configfile:
        #     self.config.write(configfile) 
