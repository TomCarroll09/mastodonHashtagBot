from mastodon import Mastodon

# Insert the details below
client_id = 'YOUR_CLIENT_ID'
client_secret = 'YOUR_CLIENT_SECRET'
access_token = 'YOUR_ACCESS_TOKEN'
base_url = 'https://your-mastodon-instance.com'

# Initialize the Mastodon API client
mastodon = Mastodon(
    client_id=client_id,
    client_secret=client_secret,
    access_token=access_token,
    api_base_url=base_url
)

# Change the word "hashtag" to whatever hashtag you want to boost
hashtag = 'hashtag'
results = mastodon.timeline_hashtag(hashtag)

# Boost each post found
for status in results:
    mastodon.status_reblog(status)

print(f"Boosted {len(results)} posts with #{hashtag}")
