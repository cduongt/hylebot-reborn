import json
import requests
from hylebot.config import config
import datetime
from datetime import timezone
import dateutil.parser


class TwitchApi:
    def __init__(self):
        self.access_token = config['TWITCH']['ACCESS_TOKEN']
        self.client_id = config['TWITCH']['CLIENT_ID']
        self.api_url = "https://api.twitch.tv/helix"
        self.user_id = "75270934"

        self.headers = {'Authorization': 'Bearer {}'.format(
            self.access_token), 'Client-Id': self.client_id}

    def get_follow_age(self, follower_username):
        follower_id = self.get_user_id(follower_username)

        if (follower_id != None):
            r = requests.get(self.api_url + "/users/follows?from_id=" +
                             follower_id + "&to_id=" + self.user_id, headers=self.headers)

            if len(r.json()) > 0:
                response_data = r.json()['data']

                if len(response_data) > 0:
                    user_follow = response_data[0]
                    follow_date = dateutil.parser.parse(
                        user_follow['followed_at'])
                    today = datetime.datetime.now(timezone.utc)

                    return follower_username + " is following Hylebus for " + str(round((today - follow_date) / datetime.timedelta(days=1))) + " days."

                else:
                    return "User is not following channel."

        return "Something is broken with Twitch."

    def get_user_id(self, username):
        r = requests.get(self.api_url + "/users?login=" +
                         username, headers=self.headers)

        if len(r.json()) > 0:
            response_data = r.json()['data'][0]

            return response_data['id']

        return None
