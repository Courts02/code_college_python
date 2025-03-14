from operator import itemgetter  # Import itemgetter to sort dictionaries by key values
import requests  # Import requests to make HTTP requests

# Make an API call to get the top stories from Hacker News and check the response.
url = "https://hacker-news.firebaseio.com/v0/topstories.json"
r = requests.get(url)
print(f"Status code: {r.status_code}")  # Print the status code to check if the request was successful

# Extract the list of top story IDs from the response.
submission_ids = r.json()   
submission_dicts = []  # Initialize an empty list to store information about each submission

# Loop through the first 30 submission IDs to get details about each story
for submission_id in submission_ids[:30]:
    # Make a new API call for each submission using its unique ID
    url = f"https://hacker-news.firebaseio.com/v0/item/{submission_id}.json"
    r = requests.get(url)
    print(f"id: {submission_id}\tstatus: {r.status_code}")  # Print each submission ID and its request status
    response_dict = r.json()  # Convert the response to a dictionary
    
    # Build a dictionary containing relevant details of the article
    submission_dict = {
        'title': response_dict['title'],  # Extract the title of the story
        'hn_link': f"https://news.ycombinator.com/item?id={submission_id}",  # Construct the discussion link
        'comments': response_dict.get('descendants', 0),  # Extract the number of comments (default to 0 if missing)
    }
    
    submission_dicts.append(submission_dict)  # Add the dictionary to the list

# Sort the list of submissions based on the number of comments in descending order
submission_dicts = sorted(submission_dicts, key=itemgetter('comments'), reverse=True)

# Loop through the sorted list and print out each article's details
for submission_dict in submission_dicts:
    print(f"\nTitle: {submission_dict['title']}")  # Print the article title
    print(f"Discussion link: {submission_dict['hn_link']}")  # Print the link to the discussion
    print(f"Comments: {submission_dict['comments']}")  # Print the number of comments

