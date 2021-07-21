import requests
import json

from plotly.graph_objs import Bar
from plotly import offline

url = 'https://api.github.com/search/repositories?q=language:C&sort=stars'
headers = {'Accept': 'application/vnd.github.v3+json'}

r = requests.get(url, headers=headers)
print(f"Status code: {r.status_code}")

response = r.json()
repo_dicts = response['items']

stars, labels, repo_links = [], [], []

for repo_dict in repo_dicts:
	repo_name = repo_dict['name']
	repo_desc = repo_dict['description']
	label = f"{repo_name}<br />{repo_desc}"
	repo_link = f"<a href='{repo_dict['html_url']}'>{repo_name}</a>"

	stars.append(repo_dict['stargazers_count'])
	labels.append(label)
	repo_links.append(repo_link)

data = [{
		'type': 'bar',
		'x': repo_links,
		'y': stars,
		'hovertext': labels,
		'marker': {
			'color': 'rgb(255, 0, 0)',
			'line': {'width': 1.5, 'color': 'rgb(255, 255, 255)'}
		},
}]

layout = {
		'title': 'Github C Projects',
		'xaxis': {
			'title': 'Repository',
			'titlefont': {'size': 24},
			'tickfont': {'size': 14},
		},
		'yaxis': {
			'title': 'Stars count',
			'titlefont': {'size': 24},
			'tickfont': {'size': 14},
		},
}

fig = {'data': data, 'layout': layout}
offline.plot(fig, filename='c_repos.html')




