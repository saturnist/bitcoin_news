import praw


def reddit_search(sub, start):
    """
    looks at subreddit posts on a given date
    Args:
        sub: string for subreddit
        start: list of integers representing unix epochs

    Returns:
        dictionary of reddit submissions with title as key and url as value

    """
    blacklist = ['reddit.com', 'redd.it', 'i.reddituploads.com', 'imgur.com', 'youtube.com', '.gif', '.png', '.jpg']
    results = {}
    reddit = praw.Reddit()
    subreddit = reddit.subreddit(sub)

    for d in start:
        for b in subreddit.submissions(d, d + 86400):
            if any(reddit_url in b.url for reddit_url in blacklist):
                continue
            else:
                results[b.title] = b.url

    return results
