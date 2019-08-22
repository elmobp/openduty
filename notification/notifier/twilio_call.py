from openduty import settings

__author__ = 'deathowl'

from twilio.rest import Client

class TwilioCallNotifier:

    def __init__(self, config):
        self.__config = config

    def notify(self, notification):
        client = Client(self.__config['SID'], self.__config['token'])
        try:
            client.calls.create(
                url=settings.BASE_URL + "/twilio/%s/%s" % (notification.id, notification.user_to_notify.id),
                method="GET",
                to=notification.user_to_notify.profile.phone_number,
                from_=self.__config['phone_number'])
            print 'successfully sent the call'
        except :
            print 'failed to send the call'
