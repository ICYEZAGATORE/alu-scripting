#!/usr/bin/python3
"""
Function that queries the Reddit API
and prints the titles of the first 10 hot posts listed for a given subreddit.
"""
import requests
import requests.auth

def top_ten(subreddit):
    """Prints the titles of the first 10 hot posts listed in a subreddit."""
    client_id = 'YOUR_CLIENT_ID'
    client_secret = 'YOUR_CLIENT_SECRET'
    user_agent = 'Mozilla/5.0'

    # Get an access token
    auth = requests.auth.HTTPBasicAuth(client_id, client_secret)
    data = {'grant_type': 'client_credentials'}
    headers = {'User-Agent': user_agent}
    token_response = requests.post('https://www.reddit.com/api/v1/access_token',
                                   auth=auth, data=data, headers=headers)
    if token_response.status_code != 200:
        print(None)
        return
    
    token = token_response.json().get('access_token')
    if not token:
        print(None)
        return

    # Use the token to make a request to the subreddit
    headers['Authorization'] = f'bearer {token}'
    url = f'https://oauth.reddit.com/r/{subreddit}/hot.json?limit=10'
    response = requests.get(url, headers=headers, allow_redirects=False)
    
    if response.status_code == 200:
        try:
            posts = response.json()['data']['children']
            for post in posts:
                print(post['data']['title'])
        except KeyError:
            print(None)
    else:
        print(None)

# Example usage
top_ten('python')

