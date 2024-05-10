#!/usr/bin/python3
"""Contains a function that prints the frequency of given keywords in
the titles of hot articles of a sub.
"""
import requests


def recurse(subreddit, word_list, freq={}, after=None, session=None):
    """Queries the Reddit API for the titles of all hot posts
    for a given subreddit, then parses the title and prints keyword occurrence.

    Args:
        subreddit str: subreddit to get hot posts
        word_list [str]: list of keywords
        freq {str: int}: keyword frequency dictionary
        after str: pagination
        session requests.Session: a session for persisting connection
    """

    if after:
        endpoint = "https://www.reddit.com/r/{0}/hot.json?after={1}"
        endpoint = endpoint.format(subreddit, after)
    else:
        endpoint = "https://www.reddit.com/r/{0}/hot.json".format(subreddit)

    if session is None:
        session = requests.Session()
        header = {'user-agent': 'alx-api_advanced (u/kimaita)'}
        session.headers.update(header)

    resp = session.get(endpoint, allow_redirects=False)
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

def parse_title(title, freq_dict):
    """"""
    for word in title.split():
        if word in freq_dict:
            freq_dict[word] += 1

    return freq_dict


