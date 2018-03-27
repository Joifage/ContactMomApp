import configparser
import read_config


def save():
    RC = read_config

    save_tw_rec = str(RC.tw_rec)
    save_fb_rec = str(RC.fb_rec)
    save_em_rec = str(RC.em_rec)

    for letter in ['"', '[', ']', '\'']:
        if letter in save_tw_rec:
            save_tw_rec = save_tw_rec.replace(letter, "")

    for letter in ['"', '[', ']', '\'']:
        if letter in save_fb_rec:
            save_fb_rec = save_fb_rec.replace(letter, "")

    for letter in ['"', '[', ']', '\'']:
        if letter in save_em_rec:
            save_em_rec = save_em_rec.replace(letter, "")

    config = configparser.ConfigParser()
    config.read('conf.ini')
    cfgfile = open("conf.ini",
                   'w')
    config.set('twitter', 'recipients', save_tw_rec)
    config.set('facebook', 'recipients', save_fb_rec)
    config.set('email', 'recipients', save_em_rec)
    config.write(cfgfile)
    cfgfile.close()
    print("Recipients Saved")
