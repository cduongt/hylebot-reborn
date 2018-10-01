import json
import requests
from hylebot.config import config

class OsuApi:
    def __init__(self):
        self.api_key = config['OSU']['API_KEY']
        self.api = "https://osu.ppy.sh/api/"

    def process_message(self, message):
        if self.is_beatmap(message.content):
            return self.beatmap_info(self.is_beatmap(message.content))
        return None

    def beatmap_info(self, beatmap_id):
        query = { "k": self.api_key, "b": beatmap_id}
        r = requests.post(self.api + "/get_beatmaps", params=query)
        if len(r.json()) > 0:
            response_json = r.json()[0]
            artist_name = response_json['artist']
            song_title = response_json['title']
            mapper = response_json['creator']
            bpm = response_json['bpm']
            difficulty = response_json['difficultyrating']
            return artist_name + " - " + song_title + " by " + mapper + ", " + bpm + " BPM, " + str(round(float(difficulty), 2)) + "*"
        return None

    def user_info(self, user):
        query = { "k": self.api_key, "u": user}
        r = requests.post(self.api + "/get_user", params=query)
        response_json = r.json()[0]
        username = response_json['username']
        pp = response_json['pp_raw']
        rank = response_json['pp_rank']
        playcount = response_json['playcount']
        return "User " + username + " is rank " + rank + " with " + pp + " pp and " + playcount + " playcount." 

    def is_beatmap(self, line):
        if "osu.ppy.sh/s/" or "osu.ppy.sh/beatmapsets/" in line:
            for word in line.split():
                if "osu.ppy.sh/s/" or "osu.ppy.sh/beatmapsets/" in word:
                    return word.split("/")[-1]
        return None
