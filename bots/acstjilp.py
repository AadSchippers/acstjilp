#!/usr/bin/env python
# tweepy-bots/bots/autoreply.py

import tweepy
import logging
from config import create_api
import time
import datetime
import settings
import acsvaccinatieschade
import acsadviesjargon

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()


def read_inifile():
    try:
        f = open(settings.INI_FILENAME, "r")
    except FileNotFoundError:
        write_inifile("0", "1")
        f = open(settings.INI_FILENAME, "r")
    try:
        IniList = f.read().splitlines()
        try:
            ListLastRegularTweet = IniList[0].split("=")
            if ListLastRegularTweet[0] == "LastRegularTweet":
                LastRegularTweet = ListLastRegularTweet[1]
            else:
                LastRegularTweet = 0
        except Exception:
            LastRegularTweet = 0
        try:
            ListLastSinceId = IniList[1].split("=")
            if ListLastSinceId[0] == "LastSinceId":
                LastSinceId = ListLastSinceId[1]
            else:
                LastRegularTweet = 0
        except Exception:
            LastRegularTweet = 0
    except Exception:
        LastRegularTweet = 0
        LastSinceId = 1
    f.close()

    IniValues = {
        "LastRegularTweet": LastRegularTweet,
        "LastSinceId": LastSinceId,
    }

    return IniValues


def write_inifile(LastRegularTweet, LastSinceId):
    f = open(settings.INI_FILENAME, "w")
    f.write("LastRegularTweet=" + str(LastRegularTweet))
    f.write("\n")
    f.write("LastSinceId=" + str(LastSinceId))
    f.close()

    return


def check_mentions(api, since_id):
    logger.info(
        datetime.datetime.now().strftime("%Y-%m-%d %H:%M") +
        ". Retrieving mentions"
        )
    new_since_id = since_id
    for tweet in tweepy.Cursor(
        api.mentions_timeline,
        since_id=since_id
    ).items():
        new_since_id = max(tweet.id, new_since_id)

        if "#vaccinatieschade" in tweet.text.lower():
            tweet_hashag = "#VaccinatieSchade"
        elif "adviesgargon"  in tweet.text.lower():
            tweet_hashag = "#AdviesJargon"

        do_tweet(api, tweet_hashag, tweet)

    return new_since_id


def regular_tweet(api, LastRegularTweet):

    if int(LastRegularTweet) + settings.HOURS_BETWEEN_REGULAR_TWEET <= int(datetime.datetime.now().strftime("%Y%j%H")):
        LastRegularTweet = datetime.datetime.now().strftime("%Y%j%H")
        do_tweet(api, "#VaccinatieSchade", None)

    return LastRegularTweet


def do_tweet(api, tweet_hastag, tweet):
    tweet_text = None

    if tweet:
        screen_name = " @" + tweet.user.screen_name
        tweet_id = tweet.id
    else:
        screen_name = ""
        tweet_id = 0


    if tweet_hastag.lower() == "#vaccinatieschade":
        tweet_text = acsvaccinatieschade.report_vaccinatieschade(
            screen_name
            )

    elif tweet_hastag.lower() == "#adviesjargon":
        tweet_text = acsadviesjargon.report_adviesjargon(
            screen_name
            )

    if tweet_text:
        if screen_name:
            logger.info(
                datetime.datetime.now().strftime("%Y-%m-%d %H:%M") +
                ". Answering to" + screen_name
            )
        else:
            logger.info(
                datetime.datetime.now().strftime("%Y-%m-%d %H:%M") +
                ". Tweeting"
                )

        try:
            if settings.TESTING == False:
                api.update_status(
                    status=tweet_text,
                    in_reply_to_status_id=tweet_id,
                )
            logger.info(
                datetime.datetime.now().strftime("%Y-%m-%d %H:%M") +
                ". " + tweet_text
                )
        except Exception:
            logger.error(
                datetime.datetime.now().strftime("%Y-%m-%d %H:%M") +
                ". Error tweeting: " + tweet_text
                )

    return


def main():
    api = create_api()

    IniValues = read_inifile()
    since_id = int(IniValues["LastSinceId"])
    LastRegularTweet = int(IniValues["LastRegularTweet"])
    try:
        cycles = settings.CYCLES
    except Exception:
        cycles = 1
    while cycles != 0:
        if cycles > 0:
            cycles += -1
        since_id = check_mentions(
            api, since_id
            )

        LastRegularTweet = regular_tweet(api, LastRegularTweet)

        write_inifile(LastRegularTweet, since_id)

        logger.info(
            datetime.datetime.now().strftime("%Y-%m-%d %H:%M") +
            ". Waiting for " +
            str(datetime.timedelta(seconds=settings.SLEEP_TIME))            )
        if cycles == 0:
            break
        time.sleep(settings.SLEEP_TIME)


if __name__ == "__main__":
    main()
