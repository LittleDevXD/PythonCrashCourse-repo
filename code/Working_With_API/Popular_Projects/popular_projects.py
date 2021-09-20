import requests
from plotly.graph_objs import Bar
from plotly import offline

language = input('Which language project do u like to see: ')

# Call API
url = f'https://api.github.com/search/repositories?q=language:{language}&sort=stars'
header = {'Accept' : 'application/vnd.github.v3+json'}
r = requests.get(url, header)
print(f"Status Code: {r.status_code}")

# Store in json format
repo_dicts = r.json()
print(f"Repo_dicts: {repo_dicts.keys()}")

# Store all popular repositories
repositories = repo_dicts['items']

# Data need to visualize
names, hover_texts, stars = [], [], []
for repository in repositories:
    star = repository['stargazers_count']
    stars.append(int(star))

    name = f"<a href='{repository['html_url']}'>{repository['name']}</a>"
    names.append(name)

    text = f"{repository['owner']['login']}<br />{repository['description']}"
    hover_texts.append(text)

# Visualization
data = {
    'type' : 'bar',
    'x' : names,
    'y' : stars,
    'marker' : {
        'color': 'rgb(60, 100, 150)',
        'line': {'width': 1.5, 'color': 'rgb(25, 25, 25)'}
    },
    'hovertext' : hover_texts
}
    
my_layout = {
    'title' : 'Most Popular Python Projects On Github',
    'xaxis' : {
        'title' : 'Repository',
        'titlefont' : {'size' : 24},
        'tickfont' : {'size' : 14}
    },
    'yaxis' : {
        'title' : 'Number of Stars',
        'titlefont' : {'size' : 24},
        'tickfont' : {'size' : 14}
    }
}

offline.plot({'data':data, 'layout':my_layout}, filename='popular_projects.html')