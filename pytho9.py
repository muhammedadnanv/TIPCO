import requests

def get_user_posts(username):
    url = f"https://www.instagram.com/rifa_fathima__817/?__a=1"
    response = requests.get(url)
    data = response.json()
    posts = data["graphql"]["user"]["edge_owner_to_timeline_media"]["edges"]
    return posts

def report_user_posts(username):
    posts = get_user_posts(username)
    for post in posts:
        post_id = post["node"]["id"]
        post_url = f"https://www.instagram.com/p/{post_id}/"
        likes = post["node"]["edge_liked_by"]["count"]
        comments = post["node"]["edge_media_to_comment"]["count"]
        print(f"Post URL: {post_url}")
        print(f"Likes: {likes}")
        print(f"Comments: {comments}")
        print("")

# Example usage
report_user_posts("instagram")
