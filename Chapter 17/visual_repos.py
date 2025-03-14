import requests  # Import the requests library to make API calls
import plotly.express as px  # Import Plotly Express for data visualization

# Make an API call to GitHub and check the response.
url = "https://api.github.com/search/repositories"
url += "?q=language:python+sort:stars+stars:>10000"  # Search for Python repositories with more than 10,000 stars, sorted by stars

headers = {"Accept": "application/vnd.github.v3+json"}  # Set headers to specify GitHub API version
r = requests.get(url, headers=headers)  # Send GET request to GitHub API
print(f"Status code: {r.status_code}")  # Print the status code to check if the request was successful

# Process overall results.
response_dict = r.json()  # Convert API response to JSON format
print(f"Complete results: {not response_dict['incomplete_results']}")  # Check if the results are complete

# Extract repository information.
repo_dicts = response_dict['items']  # Get the list of repositories
repo_links, stars, hover_texts = [], [], []  # Initialize lists to store repository links, star counts, and hover texts

for repo_dict in repo_dicts:
    # Turn repository names into clickable links.
    repo_name = repo_dict['name']  # Get the repository name
    repo_url = repo_dict['html_url']  # Get the repository URL
    repo_link = f"<a href='{repo_url}'>{repo_name}</a>"  # Create an HTML link for the repository
    repo_links.append(repo_link)  # Add the link to the list

    stars.append(repo_dict['stargazers_count'])  # Add the number of stars to the list

    # Build hover texts with repository owner and description.
    owner = repo_dict['owner']['login']  # Get the repository owner's username
    description = repo_dict['description']  # Get the repository description
    hover_text = f"{owner}<br />{description}"  # Create a hover text with owner and description
    hover_texts.append(hover_text)  # Add hover text to the list

# Create a bar chart visualization.
title = "Most-Starred Python Projects on GitHub"  # Set the chart title
labels = {'x': 'Repository', 'y': 'Stars'}  # Set axis labels
fig = px.bar(x=repo_links, y=stars, title=title, labels=labels, hover_name=hover_texts)  # Generate the bar chart

# Customize the layout.
fig.update_layout(title_font_size=28, xaxis_title_font_size=20, yaxis_title_font_size=20)

# Customize the bar chart appearance.
fig.update_traces(marker_color='SteelBlue', marker_opacity=0.6)

fig.show()  # Display the visualization

