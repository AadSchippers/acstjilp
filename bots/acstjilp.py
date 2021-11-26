#!/usr/bin/env python
# tweepy-bots/bots/autoreply.py

import tweepy
import logging
from config import create_api
import time
import acsvaccinatieschade
import acsadviesjargon

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()


def check_mentions(api, keywords, since_id):
    logger.info("Retrieving mentions")
    new_since_id = since_id
    for tweet in tweepy.Cursor(
        api.mentions_timeline,
        since_id=since_id
    ).items():
        new_since_id = max(tweet.id, new_since_id)

        tweet_text = None

        if '#vaccinatieschade' in tweet.text.lower():
            tweet_text = acsvaccinatieschade.report_vaccinatieschade(
                tweet.user.name
                )

        elif '#adviesjargon' in tweet.text.lower(tweet.user.name):
            tweet_text = acsadviesjargon.report_adviesjargon()

        if tweet_text:
            logger.info(f"Answering to {tweet.user.name}")

            try:
                api.update_status(
                    status=tweet_text,
                    in_reply_to_status_id=tweet.id,
                )
            except:
                pass

    return new_since_id


def main():
    api = create_api()
    try:
        f = open("last_since_id.txt", "r")
    except:
        f = open("last_since_id.txt", "w")
        f.close()
        f = open("last_since_id.txt", "r")
    try:
        since_id = int(f.read())
    except:
        since_id = 1
    f.close()
    while True:
        since_id = check_mentions(
            api, ["#vaccinatieschade", "#adviesjargon"], since_id
            )
        f = open("last_since_id.txt", "w")
        f.write(str(since_id))
        f.close()

        logger.info("Waiting...")
        time.sleep(60)


if __name__ == "__main__":
    main()
