import requests  # this allows us to access the web without opening the browser
from bs4 import BeautifulSoup  # web scrapping library
import pprint

res = requests.get('https://news.ycombinator.com/news')

soup = BeautifulSoup(res.text, 'html.parser')
# this lets bs know that it's html and we want it to go through the tags
links = soup.select('.storylink')
subtext = soup.select('.subtext')


def sort_stories_by_votes(hackernews_list):
    return sorted(hackernews_list, key=lambda k: k['votes'], reverse=True)


def create_custom_hackernews(links, subtext):
    hackernews = []
    for index, item in enumerate(links):

        title = item.getText()
        href = item.get('href', None)
        vote = subtext[index].select('.score')

        if len(vote):
            points = int(vote[0].getText().replace(' points', ''))

            if points > 99:
                hackernews.append(
                    {'title': title, 'link': href, 'votes': points})
    return sort_stories_by_votes(hackernews)


# print(create_custom_hackernews(links, votes))
pprint.pprint(create_custom_hackernews(links, subtext))
