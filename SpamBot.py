# Run First - pip install python-twitter
# pip install fbchat

import twitter
import os
import fbchat
import smtplib
import importlib
import time
import read_config
import save_config
import create_config

RC = read_config
t = time.strftime("%d-%m-%Y %H:%M:%S", time.gmtime())
# Twitter API keys
api = twitter.Api(consumer_key=RC.tw_ck,
                  consumer_secret=RC.tw_cs,
                  access_token_key=RC.tw_atk,
                  access_token_secret=RC.tw_ats)

# FB Details
username = RC.fb_u
password = RC.fb_p

create_config.does_config_exist()

choice = ""

while choice != "e":
    count_tw = 0
    count_fb = 0
    count_em = 0
    for idx, entry in enumerate(RC.tw_rec):
        count_tw += 1
    for idx, entry in enumerate(RC.fb_rec):
        count_fb += 1
    for idx, entry in enumerate(RC.em_rec):
        count_em += 1
    os.system('cls')
    print("Joifs Spammy Social Media App")
    print("\n    Recipients List: \n")
    print(format("\tTwitter:", '<15'), "Set:", count_tw)
    print("\t¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯")
    for person in RC.tw_rec:
        print("\t", person)
    print(format("\n\tFB: ", '<15'), "Set:", count_fb)
    print("\t¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯")
    for person in RC.fb_rec:
        print("\t", person)
    print(format("\n\tEmail: ", '<15'), "Set:", count_em)
    print("\t¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯")
    for person in RC.em_rec:
        print("\t", person)
    print("""
            a = add recipient
            d = delete recipient  
            r = read recipients from file
            s = save list
            
            go = send message
            reset = reset recipients
            
            e = exit
    """)
    choice = input("Select a function: ").lower()
    if choice == "a":
        platform = 'None'
        while platform >= '0' or platform <= '3':
            print("""   
            1. Twitter
            2. Facebook
            3. Mail
                        
            0. Back""")
            platform = input("\nSelect Platform: ")
            if platform == "1":
                user = input("Enter handle: ")
                RC.tw_rec.append(user)
                break
            elif platform == "2":
                user = input("Enter handle: ")
                RC.fb_rec.append(user)
                break
            elif platform == "3":
                user = input("Enter handle: ")
                RC.em_rec.append(user)
                break
            elif platform == "0":
                break
            else:
                print("Invalid Selection")
    elif choice == "d":
        platform = 'None'
        while platform >= '0' or platform <= '3':
            print("""
            1. Twitter
            2. Facebook
            3. Mail
                        
             0. Back""")
            platform = input("\nSelect Platform: ")
            if platform == "1":
                user = input("Type user to remove?: ")
                if user in RC.tw_rec:
                    RC.tw_rec.remove(user)
                    break
                else:
                    print(user, "isn't in the recipient list.")
            elif platform == "2":
                user = input("Type user to remove?: ")
                if user in RC.fb_rec:
                    RC.fb_rec.remove(user)
                    break
                else:
                    print(user, "isn't in the recipient list.")
            elif platform == "3":
                user = input("Type user to remove?: ")
                if user in RC.em_rec:
                    RC.em_rec.remove(user)
                else:
                    print(user, "isn't in the recipient list.")
            elif platform == "0":
                break
            else:
                print("Invalid Selection")
    elif choice == "r":
        importlib.reload(read_config)
    elif choice == "s":
        save_config.save()
    elif choice == "go":
        msg = input("Enter message to send: ")
        print("Sending Message: ", msg)
        print("To: ", RC.tw_rec, RC.fb_rec, RC.em_rec)
        if count_tw > 0:
            print("\nTwitter..")
            for person in RC.tw_rec:
                try:
                    send_msg = api.PostDirectMessage(msg, user_id=None, screen_name=person)
                    print("Twitter message sent to:", person)
                    print("[" + t + "] : Message: [" + msg + "] recipient: [" + person + "]", file=open("log.txt", "a"))
                except Exception as e:
                    print(e)
        if count_fb > 0:
            print("\nFacebook..")
            client = fbchat.Client(username, password)
            for person in RC.fb_rec:
                try:
                    friends = client.searchForUsers(person)  # return a list of names
                    friend = friends[0]
                    sent = client.send(fbchat.models.Message(text=msg), thread_id=friend.uid)
                    if sent:
                        print("FB Message sent to:", person)
                        print("[" + t + "] : Message: [" + msg + "] recipient: [" + person + "]", file=open("log.txt", "a"))
                except Exception as e:
                    print(e)
        if count_em > 0:
            print("\nEmail..")
            for person in RC.em_rec:
                try:
                    server = smtplib.SMTP(RC.em_sm, RC.em_po)
                    server.starttls()
                    server.login(RC.em_e, RC.em_pa)
                    server.sendmail(RC.em_e, person, msg)
                    server.quit()
                    print("Sent:", person)
                    print("[" + t + "] : Message: [" + msg + "] recipient: [" + person + "]", file=open("log.txt", "a"))
                except Exception as e:
                    print(e)
            print("Messages Sent, press enter to continue")
            input()
    elif choice == "reset":
        RC.tw_rec = []
        RC.fb_rec = []
        RC.em_rec = []
    elif choice == "e":
        print("Goodbye")
    else:
        print("Invalid Selection")
