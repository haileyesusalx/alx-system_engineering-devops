#!/usr/bin/python3
"""
This script defines a recursive function that queries the Reddit API and
returns list containing the titles of all hot articles for a given subreddit.
"""

import requests


def recurse(subreddit, hot_list=[], after=None):
    """
    Recursively fetch hot articles for a given subreddit.

    Args:
        subreddit (str): The name of the subreddit to query.
        hot_list (list, optional): The list to store hot article titles
        (default is an empty list).
        after (str, optional): A parameter used for pagination to get the next
        page of results (default is None).

    Returns:
        list: A list containing the titles of hot articles.
    """
    # Define the Reddit API endpoint for the subreddit
    url = f'https://www.reddit.com/r/{subreddit}/hot.json?' \
          f'limit=100&after={after}'

    # Set a custom User-Agent to avoid rate limits
    headers = {'User-Agent': 'Custom User Agent'}

    # Send a GET request to the Reddit API
    response = requests.get(url, headers=headers)

    # Check if the response is successful
    if response.status_code == 200:
        data = response.json()
        posts = data['data']['children']
        after = data['data']['after']

        for post in posts:
            hot_list.append(post['data']['title'])

        if after is not None:
            # Recursively call the function to get the next page
            return recurse(subreddit, hot_list, after)
        else:
            return hot_list
    else:
        # Return None for invalid or non-existent subreddits
        return None


if __name__ == '__main__':
    import sys
    if len(sys.argv) < 2:
        print("Please pass an argument for the subreddit to search.")
    else:
        subreddit = sys.argv[1]
        hot_articles = recurse(subreddit)
        if hot_articles is not None:
            print(len(hot_articles))
        else:
            print("None")
