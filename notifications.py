import secret_settings
import settings

from event_model import Event
import datetime

today = datetime.datetime.now()
import requests


def check_event_dates():
    e = Event(settings.HOST, settings.TEST_DB)
    events = e.get_all_events()
    for event in events:

        # day1 = datetime.datetime.now()
        # day2 = ('2016-10-28 10:32:45')
        #
        # day2 = datetime.datetime(*time.strptime(day2, "%Y-%m-%d %H:%M:%S")[:6])
        # print(abs(day2 - day1).seconds)

        d0 = today
        d1 = datetime.datetime(today.year, event['date'].month, event['date'].day)

        delta = d1 - d0

        if str(delta.days) in "721":
            bot_message = f"friendly reminder its {event['name']} {event['type']} in {delta.days}" + (f"days" if delta.days > 1 else "day")
            bot_send_notifications(bot_message)

        elif delta.days == 0:
            bot_message = f"friendly reminder its {event['name']} {event['type']}" +(" is TOMORROW" if delta.seconds/3600 > 0 else "TODAY")
            bot_send_notifications(bot_message)
            print(delta.seconds/3600)


def bot_send_notifications(bot_message):
    print(f"bot message =---{bot_message}")
    ### Send text message
    bot_token = secret_settings.BOT_TOKEN
    bot_chatID = '757815786'
    send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatID + '&parse_mode=Markdown&text=' + bot_message

    requests.get(send_text)
def send_notifications():
    pass


# bot_send_notifications("hello my friend")
check_event_dates()
