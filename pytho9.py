import requests

def get_user_posts(username):
    url = f"https://www.instagram.com/{username}/?__a=1"
    response = requests.get(url)
    data = response.json()
    posts = data['graphql']['user']['edge_owner_to_timeline_media']['edges']
    return posts

def get_user_followers(username):
    url = f"https://www.instagram.com/{username}/?__a=1"
    response = requests.get(url)
    data = response.json()
    followers = data['graphql']['user']['edge_followed_by']['count']
    return followers

def get_user_following(username):
    url = f"https://www.instagram.com/{username}/?__a=1"
    response = requests.get(url)
    data = response.json()
    following = data['graphql']['user']['edge_follow']['count']
    return following

def get_user_info(rifa_fathima__817):
    url = f"https://www.instagram.com/{username}/?__a=1"
    response = requests.get(url)
    data = response.json()
    user_info = {
        'username': data['graphql']['user']['username'],
        'full_name': data['graphql']['user']['full_name'],
        'biography': data['graphql']['user']['biography'],
        'followers': data['graphql']['user']['edge_followed_by']['count'],
        'following': data['graphql']['user']['edge_follow']['count'],
        'posts': data['graphql']['user']['edge_owner_to_timeline_media']['count']
    }
    return user_info

# Example usage
username = 'example_user'
user_posts = get_user_posts(username)
user_followers = get_user_followers(username)
user_following = get_user_following(username)
user_info = get_user_info(username)

print(f"Username: {user_info['username']}")
print(f"Full Name: {user_info['full_name']}")
print(f"Biography: {user_info['biography']}")
print(f"Followers: {user_info['followers']}")
print(f"Following: {user_info['following']}")
print(f"Posts: {user_info['posts']}")

