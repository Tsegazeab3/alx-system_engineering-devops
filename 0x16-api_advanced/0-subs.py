#!/usr/bin/python3
"""
Script that queries subscribers on a given Reddit subreddit.
"""
import requests


def number_of_subscribers(subreddit):
    """Return the total number of subscribers on a given subreddit."""

    url = "https://www.reddit.com/r/{subreddit}/about.json"
    headers = {"User-Agent": "requests"}

    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code != 200:
        return 0
    data = response.json().get("data")
    subscribers = data.get('subscribers')
    return subscribers
