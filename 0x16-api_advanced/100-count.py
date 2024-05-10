#!/usr/bin/python3
"""Contains a function that prints the frequency of given keywords in
the titles of hot articles of a sub.
"""
import requests


def count_words(subreddit, word_list, freq=None, after=None, session=None):
    """Queries the Reddit API for the titles of all hot posts
    for a given subreddit, then parses the title and prints keyword occurrence.

    Args:
        subreddit str: subreddit to get hot posts
        word_list [str]: list of keywords
        freq {str: int}: keyword frequency dictionary
        after str: pagination
        session requests.Session: a session for persisting connection

    Returns:
        frequency dictionary or None if subreddit invalid
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

        if freq is None:
            word_list = [word.lower() for word in word_list]
            freq = dict.fromkeys(word_list, 0)

        for post in posts:
            parse_title(post.get('data').get('title').lower(), freq)

        if next:
            return count_words(subreddit, word_list, freq, next, session)

        for w in sorted(freq.items(), reverse=True, key=lambda x: x[1]):
            if w[1]:
                print("{}: {}".format(w[0], w[1]))

        return freq
    except Exception:
        return None


def parse_title(title, freq_dict):
    """Counts the occurences of keywords in a sentence,
    updating a frequency dictionary
    """
    for word in title.split():
        if word in freq_dict:
            freq_dict[word] += 1
