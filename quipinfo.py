#!/usr/bin/python3

import os
import sys
import json
from urllib import request, error
from datetime import datetime

QUIP_ACCESS_TOKEN = os.environ.get("QUIP_ACCESS_TOKEN")
QUIP_END_POINT = "https://platform.quip.com/1/"


def get_req(url):
    req = request.Request(QUIP_END_POINT + url, headers={"Authorization": "Bearer " + QUIP_ACCESS_TOKEN})
    try:
        with request.urlopen(req) as res:
            return json.load(res)
    except error.HTTPError as e:
        print("[ERROR] {} -> {}".format(url, e))
    return None


def formatDate(ts):
    return datetime.fromtimestamp(ts//1000000).strftime("%Y-%m-%d %H:%M:%S")


def userName(user_id):
    data = get_req("users/" + user_id)
    return data["name"] if data else user_id


def getThread(thread_id):
    return get_req("threads/" + thread_id)


def showThreadInfo(thread):
    author = userName(thread["author_id"])
    print("   Thread ID:", thread["id"])
    print("         URL:", thread["link"])
    print("       Title:", thread["title"])
    print("        Type:", thread["type"])
    print("      Author:", author)
    print("Created Date:", formatDate(thread["created_usec"]))
    print("Updated Date:", formatDate(thread["updated_usec"]))
    print("    Template:", thread["is_template"])
    print("     Deleted:", thread["is_deleted"])


def main():
    if len(sys.argv) <= 1:
        print("Please enter a 12-character URL suffix.")
        exit()

    if not get_req("oauth/verify_token"):
        print("Please set QUIP_ACCESS_TOKEN environment variable. You can get the token from http://quip.com/dev/token.")
        exit()

    thread = getThread(sys.argv[1])
    if thread:
        showThreadInfo(thread["thread"])


if __name__ == "__main__":
    main()