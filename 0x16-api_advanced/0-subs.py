#!/usr/bin/python3
import requests


def number_of_subscribers(subreddit):
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
