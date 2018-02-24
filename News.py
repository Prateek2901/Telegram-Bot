from newsapi import NewsApiClient
import json

newsapi = NewsApiClient(api_key=API_KEY)

from datetime import date,timedelta
end = str(date.today())
start = str(date.today() - timedelta(days=1))
page = 1


sources = newsapi.get_sources()


def all_News(tag):
    all_articles = newsapi.get_everything(q=tag,
                                      sources='google-news-in',
                                      #domains='bbc.co.uk,techcrunch.com',
                                      from_parameter=start,
                                      to=end,
                                      language='en',
                                      sort_by='relevancy',
                                      page=page)



    title,description,url = [],[],[]
    for i in range(0,all_articles['totalResults']):
        news = all_articles['articles'][i]
        print(news)
        title.append(news['title'])
        description.append(news['description'])
        url.append(news['url'])
    return title,description,url
