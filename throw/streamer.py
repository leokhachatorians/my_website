from twython import TwythonStreamer
from django.conf import settings
from throw import models

class Streamer(TwythonStreamer):
    def __init__(self, *args, **kwargs):
        super(Streamer, self).__init__(*args, **kwargs)
        self.count = 0
        self.done = False

    def on_success(self, data):
        if 'text' in data:
            if self.count < 100:
                tweet = data['text']
                screen_name = data['user']['screen_name']
                profile_pic = data['user']['profile_image_url']
                name = data['user']['name']
                location = data['user']['location']
                mentions =  data['entities']['user_mentions']

                models.Tweets.objects.create(
                    name=name, screen_name=screen_name,
                    tweet=tweet, profile_pic=profile_pic,
                    mentions=mentions, location=location)

                self.count += 1
            else:
                self.done = True
                self.disconnect()

    def on_error(self, status_code, data):
        print(status_code, data)
        return status_code, data
