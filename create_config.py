import os
import configparser

FB = 'facebook'


def does_config_exist():
    exist_conf = os.path.isfile('./conf.ini')
    if exist_conf is True:
        print("Ini Found: True")
    else:
        print("Ini Found: False.. Generating")
        config = configparser.ConfigParser()
        config['twitter'] = {'consumer_key': 'None',
                             'consumer_secret': 'None',
                             'access_token_key': 'None',
                             'access_token_secret': 'None',
                             'recipients': 'None'}
        config[FB] = {'username': 'None',
                      'password': 'None',
                      'recipients': 'None'}
        config['email'] = {'smtp_server': "smtp.gmail.com",
                           'port': "587",
                           'email': 'None',
                           'pass': 'None',
                           'recipients': 'None'}
        with open('conf.ini', 'w') as configfile1:
            config.write(configfile1)
            configfile1.close()


does_config_exist()

