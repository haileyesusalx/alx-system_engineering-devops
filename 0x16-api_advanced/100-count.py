#!/usr/bin/python3
"""
This script defines a recursive function that queries the Reddit API, parses
the title of all hot articles, and prints a sorted count of given keywords.
"""

import requests


def count_words(subreddit, word_list, after=None, count_dict=None):
    """
    Recursively count keywords in the titles of hot articles for a given
    subreddit.

    Args:
        subreddit (str): The name of the subreddit to query.
        word_list (list): A list of keywords to count.
        after (str, optional): A parameter used for pagination
        (default is None).
        count_dict (dict, optional): A dictionary to store word counts
        (default is None).
    """
    if count_dict is None:
        count_dict = {}

    if after is None:
        url = f'https://www.reddit.com/r/{subreddit}/hot.json?limit=100'
    else:
        url = f'https://www.reddit.com/r/{subreddit}/hot.json?' \
              f'limit=100&after={after}'

    headers = {'User-Agent': 'Custom User Agent'}

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        data = response.json()
        posts = data['data']['children']
        after = data['data']['after']

        for post in posts:
            title = post['data']['title'].lower()
            for word in word_list:
                if f' {word} ' in f' {title} ':
                    if word in count_dict:
                        count_dict[word] += title.count(word)
                    else:
                        count_dict[word] = title.count(word)

        if after is not None:
            return count_words(subreddit, word_list, after, count_dict)
        else:
            sorted_counts = sorted(count_dict.items(),
                                   key=lambda x: (-x[1], x[0]))
            for word, count in sorted_counts:
                print(f"{word}: {count}")
    else:
        print()


if __name__ == '__main__':
    import sys
    if len(sys.argv) < 3:
        print("Usage: {} <subreddit> <list of keywords>".format(sys.argv[0]))
        print("Ex: {} programming 'python java javascript'".
              format(sys.argv[0]))
    else:
        subreddit = sys.argv[1]
        words = [x.lower() for x in sys.argv[2].split()]
        count_words(subreddit, words)
