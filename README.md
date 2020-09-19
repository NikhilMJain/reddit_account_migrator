# Reddit Account Migrator

Automatically migrate/copy all your subscriptions from one Reddit account to another.
 
# Usage:

## Credentials:
- Get `client_id`, `client_secret` from your old reddit account by visiting https://old.reddit.com/prefs/apps/ .Click on Create App. Use the following values.
> - name: Any name you like
> - App type: Choose the **script** option
> - description: You can leave this blank
> - about url: You can leave this blank
> - redirect url: https://reddit.com

- Copy the newly generated `client_secret` and `client_id`(the 14-character string that appears below "personal use script" on the page) 
- Replace the dummy values in the `config` file with your own newly generated values.
- Repeat this for the new account as well.

## Installation
 - Install requirements using `pip install -r requirements.txt`
 
## Run
 - Run script using `python account_migrator.py`
 