import configparser

config = configparser.ConfigParser()


TW = 'twitter'
FB = 'facebook'
EM = 'email'

tw_rec = []
fb_rec = []
em_rec = []


try:
    config.read('conf.ini')
    tw_ck = config[TW]['consumer_key']
    tw_cs = config[TW]['consumer_secret']
    tw_atk = config[TW]['access_token_key']
    tw_ats = config[TW]['access_token_secret']
    tw_rec = config[TW]['recipients']

    fb_u = config[FB]['username']
    fb_p = config[FB]['password']
    fb_rec = config[FB]['recipients']

    em_sm = config[EM]['smtp_server']
    em_po = config[EM]['port']
    em_e = config[EM]['email']
    em_pa = config[EM]['pass']
    em_rec = config[EM]['recipients']

    tw_rec = tw_rec.split(', ')
    fb_rec = fb_rec.split(', ')
    em_rec = em_rec.split(', ')

except Exception as e:
    print(e)