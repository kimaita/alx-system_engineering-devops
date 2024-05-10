#!/usr/bin/python3
"""Contains a function that prints the first 10 hot posts for a sub.
"""
import requests


def top_ten(subreddit):
    """Queries the Reddit API for the first 10 hot posts for a given subreddit
    and prints the titles.

    Args:
        subreddit (str): subreddit to get hot posts
    """
    endpoint = "https://www.reddit.com/r/{0}/hot.json?limit={1}"
    endpoint = endpoint.format(subreddit, 10)
    header = {'user-agent': 'alx-api_advanced (u/kimaita)'}
    resp = requests.get(endpoint, headers=header, allow_redirects=False)
    try:
        resp_json = resp.json()
        posts = resp_json['data'].get('children', None)
        for post in posts:
            print(post['data'].get('title'))
    except Exception:
        print(None)
