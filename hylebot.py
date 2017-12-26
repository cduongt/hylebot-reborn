import hylebot.core

def main():
    TWITCH_SERVER = "irc.twitch.tv"
    TWITCH_PORT = 6667
    TWITCH_NICKNAME = "Hylebot"
    TWITCH_OAUTH = open("oauth.txt", "r").read()
    TWITCH_CHANNEL = ["Hylebot"]

    twitch_bot = hylebot.core.HyleServer("twitch", TWITCH_SERVER, TWITCH_PORT, TWITCH_NICKNAME, TWITCH_CHANNEL, TWITCH_OAUTH)
    twitch_bot.connect()

if __name__ == "__main__":
    main()