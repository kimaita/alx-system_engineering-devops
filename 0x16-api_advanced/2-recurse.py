#!/usr/bin/python3
"""Contains a function that returns a list of the titles of a sub's hot posts.
"""
import requests


def recurse(subreddit, hot_list=[], after=None, session=None):
    """Queries the Reddit API for the titles of all hot posts
    for a given subreddit.

    Args:
        subreddit (str): subreddit to get hot posts
        after (str): pagination
    """
    header = {'user-agent': 'alx-api_advanced (u/kimaita)'}

    if after:
        endpoint = "https://www.reddit.com/r/{0}/hot.json?after={1}"
        endpoint = endpoint.format(subreddit, after)
    else:
        endpoint = "https://www.reddit.com/r/{0}/hot.json".format(subreddit)

    if session is None:
        session = requests.Session()

    resp = session.get(endpoint, headers=header, allow_redirects=False)
    try:
        resp_data = resp.json().get('data')
        next = resp_data.get('after')
        posts = resp_data.get('children')
        hot_list += [post.get('data').get('title') for post in posts]
        if next:
            return recurse(subreddit, hot_list, next, session)
        return hot_list
    except Exception:
        return None
