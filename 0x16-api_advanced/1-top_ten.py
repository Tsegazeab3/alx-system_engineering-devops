#!/usr/bin/python3
"""
Script to print hot posts on a given Reddit subreddit.
"""

import requests

def top_ten(subreddit):
    """Print the titles of the 10 hottest posts on a given subreddit."""
    url = f"https://www.reddit.com/r/{subreddit}/hot/.json"

    headers = {
        "User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/your_reddit_username)"
    }

    response = requests.get(url, headers=headers, allow_redirects=False)

    # Check if the status code indicates an invalid subreddit
    if response.status_code != 200:
        print("None")
        return

    try:
        data = response.json().get("data", {}).get("children", [])
        if not data:
            print("None")
            return

        # Extract the titles of the first 10 posts
        top_10_posts = "\n".join(post.get("data", {}).get("title", "No title") for post in data[:10])
        print(top_10_posts)

    except ValueError:  # Handle JSON decoding errors
        print("None")

