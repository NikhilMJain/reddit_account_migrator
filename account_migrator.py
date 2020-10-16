import pathlib
from configparser import ConfigParser

from praw import Reddit

CONFIG_PATH = '{}/config'.format(pathlib.Path(__file__).parent.absolute())


class AccountMigrator(object):
    def execute(self, old_account, new_account):
        subreddit_list = self._get_subcribed_subreddits_list(old_account)
        self._subcribe_to_subreddits(subreddit_list, new_account)

    def _get_subcribed_subreddits_list(self, old_account):
        print('Fetching all subreddits...')
        reddit = Reddit(user_agent='Migrator', **old_account)
        return [sub.display_name for sub in reddit.user.subreddits(limit=None)]

    def _subcribe_to_subreddits(self, subreddit_list, new_account):
        reddit = Reddit(user_agent='Migrator', **new_account)
        for sub in subreddit_list:
            print('Subscribing to {}'.format(sub))
            reddit.subreddit(sub).subscribe()
        print('Subscribed to all subreddits on the new account!')


if __name__ == '__main__':
    config = ConfigParser()
    config.read(CONFIG_PATH)
    old_account = dict(config.items('old'))
    new_account = dict(config.items('new'))
    AccountMigrator().execute(old_account, new_account)

