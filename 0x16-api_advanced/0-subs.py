#!/usr/bin/python3
"""
This script queries the Reddit API and returns the number of subscribers (not active users, total subscribers) for a given subreddit.
If the subreddit is invalid, it returns 0.
"""

import requests

def number_of_subscribers(subreddit):
    """
    Get the number of subscribers for a given subreddit.
    
    Args:
        subreddit (str): The name of the subreddit to query.

    Returns:
        int: The number of subscribers for the subreddit, or 0 if invalid.
    """
    # Define the Reddit API endpoint
    url = f'https://www.reddit.com/r/{subreddit}/about.json'

    # Set a custom User-Agent to avoid rate limits
    headers = {'User-Agent': 'Custom User Agent'}

    # Send a GET request to the Reddit API
    response = requests.get(url, headers=headers)

    # Check if the response is successful
    if response.status_code == 200:
        data = response.json()
        subscribers = data['data']['subscribers']
        return subscribers
    else:
        # Return 0 for invalid or non-existent subreddits
        return 0

if __name__ == '__main__':
    import sys
    if len(sys.argv) < 2:
        print("Please pass an argument for the subreddit to search.")
    else:
        subreddit = sys.argv[1]
        num_subscribers = number_of_subscribers(subreddit)
        print(num_subscribers)
