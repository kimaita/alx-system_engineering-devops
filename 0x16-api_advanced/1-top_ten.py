#!/usr/bin/python3
"""Contains a function that prints the first 10 hot posts in a subreddit."""

import requests


def top_ten(subreddit):
    """Queries the Reddit API and prints the titles of the first 10 hot posts
    listed for a given subreddit.

    Args:
    subreddit (str): subreddit to get hot posts.
    """

    url = "https://www.reddit.com/r/{}/hot.json?count=10".format(subreddit)
    headers = {"user-agent": "alx-api_advanced (u/kimaita)"}
    resp = requests.get(url, headers=headers)
    try:
        resp_json = resp.json()
        posts = resp_json["data"].get("children")
        if not posts:
            print(None)
        else:
            for post in posts:
                print(post["data"].get("title"))
    except Exception:
        print(None)
