import requests

from plotly.graph_objs import Bar
from plotly import offline

url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
headers = {'Accept': 'application/vnd.github.v3+json'}
r = requests.get(url, headers = headers)
print(f'Status code: {r.status_code}')

response_dict = r.json()

print(f"Total repositories: {response_dict['total_count']}")
repo_dicts = response_dict['items']
print(f'Repositories returned: {len(repo_dicts)}')

stars, labels, repo_links = [], [], []

for repo_dict in repo_dicts:
	repo_name = repo_dict['name']
	stars.append(repo_dict['stargazers_count'])

	owner = repo_dict['owner']['login']
	description = repo_dict['description']
	label = f"{owner}<br />{description}"
	labels.append(label)

	repo_link = f"<a href='{repo_dict['html_url']}'>{repo_name}</a>"
	repo_links.append(repo_link)
'''
	print("\n\n")
	print(f"Name: {repo_dict['name']}")
	print(f"Owner: {repo_dict['owner']['login']}")
	print(f"Stars: {repo_dict['stargazers_count']}")
	print(f"Repository: {repo_dict['html_url']}")
	print(f"Created: {repo_dict['created_at']}")
	print(f"Updated: {repo_dict['updated_at']}")
	print(f"Description: {repo_dict['description']}")
'''

data = [{
	'type': 'bar',
	'x': repo_links,
	'y': stars,
	'hovertext': labels,
	'marker': {
		'color': 'rgb(60, 100, 150)',
		'line': {'width': 1.5, 'color': 'rgb(25, 25, 25)'}
	},
}]

layout = {
	'title': 'Python Github Projects',
	'xaxis': {
		'title': 'Repository',
		'titlefont': {'size': 24},
		'tickfont': {'size': 14}
	},
	'yaxis': {'title': 'Stars',	
			'titlefont': {'size': 24},
			'tickfont': {'size': 14}
	},
}

fig = {'data': data, 'layout': layout}
offline.plot(fig)



