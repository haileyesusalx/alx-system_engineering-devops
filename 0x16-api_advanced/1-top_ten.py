#!/usr/bin/python3
"""
This script queries the Reddit API and prints the titles of the first 10 hot
posts listed for a given subreddit.
"""

import requests


def top_ten(subreddit):
    """
    Print the titles of the first 10 hot posts for a given subreddit.

    Args:
        subreddit (str): The name of the subreddit to query.
    """
    # Define the Reddit API endpoint for the subreddit
    url = f'https://www.reddit.com/r/{subreddit}/hot.json?limit=10'

    # Set a custom User-Agent to avoid rate limits
    headers = {'User-Agent': 'Custom User Agent'}

    # Send a GET request to the Reddit API
    response = requests.get(url, headers=headers)

    # Check if the response is successful
    if response.status_code == 200:
        data = response.json()
        posts = data['data']['children']

        # Print the titles of the first 10 posts
        for post in posts:
            print(post['data']['title'])
    else:
        # Print None for invalid or non-existent subreddits
        print(None)


if __name__ == '__main__':
    import sys
    if len(sys.argv) < 2:
        print("Please pass an argument for the subreddit to search.")
    else:
        subreddit = sys.argv[1]
        top_ten(subreddit)
