import requests
from plotly.graph_objs import Bar
from plotly import offline
import json

# hacker news API URL
url = "https://hacker-news.firebaseio.com/v0/topstories.json"
r = requests.get(url)

# Store json as dictionary
post_ids = r.json()
post_dicts = []

# Create another dictionary and store significant data
for post_id in post_ids[50:80]:
    url = f"https://hacker-news.firebaseio.com/v0/item/{post_id}.json"
    r2 = requests.get(url)
    post = r2.json()

    # print(f"Id: {post['id']}\n Status Code: {r2.status_code}")
    post_dict = {
        'title' : post['title'],
        'comments' : int(post['descendants']),
        'hn_link' : f"https://news.ycombinator.com/item?id={post['id']}",
        'author' : post['by']
    }

    post_dicts.append(post_dict)

# Create data for visualization
hover_texts, titles, comments = [], [], []
for post_dict in post_dicts:
    hover_text = f"{post_dict['title']} \n{post_dict['comments']}"
    title = f"<a href='{post_dict['hn_link']}'>{post_dict['author']}</a>"
    
    hover_texts.append(hover_text)
    titles.append(title)
    comments.append(post_dict['comments'])


# Visualization
data = {
    'type' : 'bar',
    'x' : titles,
    'y' : comments,
    'hovertext' : hover_texts,
    'marker' : {
        'color' : 'rgb(20, 180, 150)',
        'line' : {'width':1.5, 'color':'rgb(25, 25, 25)'}
    }
}

my_layout = {
    'title' : "Trending Hacker-News Posts",
    'xaxis' : {
        'title' : "Post Title",
        'titlefont' : {'size' : 24},
        'tickfont' : {'size' : 14}
    },
    'yaxis' : {
        'title' : "Number of comments",
        'titlefont' : {'size' : 24},
        'tickfont' : {'size' : 14}
    }
}

offline.plot({"data" : data, "layout" : my_layout}, filename='popular_hn_posts.html')