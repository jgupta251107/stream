# import requests

# # ThingSpeak channel ID and API key
# channel_id = 'your_channel_id'
# api_key = 'your_api_key'

# # URL for ThingSpeak API
# url = f'https://api.thingspeak.com/channels/{channel_id}/feeds.json'

# # Parameters for the API request
# params = {
#     'api_key': api_key,
#     'results': 1  # Number of results to retrieve (change as needed)
# }

# # Send GET request to ThingSpeak API
# response = requests.get(url, params=params)

# # Check if request was successful (status code 200)
# if response.status_code == 200:
#     data = response.json()
    
#     # Check if there are any feeds in the response
#     if 'feeds' in data and len(data['feeds']) > 0:
#         # Get the latest feed
#         latest_feed = data['feeds'][0]
        
#         # Print the data
#         print('Latest Data from ThingSpeak:')
#         print('------------------------------')
#         print('Entry ID:', latest_feed['entry_id'])
#         print('Timestamp:', latest_feed['created_at'])
#         print('Field 1:', latest_feed.get('field1'))
        print('field2')
        # Add more fields as needed
        
#     else:
#         print('No feeds found in the response.')
# else:
#     print('Failed to retrieve data from ThingSpeak. Status code:', response.status_code)
