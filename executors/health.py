import requests
from bs4 import BeautifulSoup
from dateutil import parser
import queries
import datetime

URL = "https://www.moh.gov.bt/"
page = requests.get(URL)

soup = BeautifulSoup(page.content, "html.parser")

news_section = soup.find("div", class_="news-section")

tabs = news_section.find_all("div", class_="tab-pane")

def health_posts():
    notifs = [];
    for tab in tabs:
        posts = tab.find_all("div", class_="news-post")
        for post in posts:
                title = post.h4.text
                link = post.a["href"]
                content = post.p.text
                post_date = post.find("div", class_="news-date").contents[2].strip()
                date = None if post_date == '' else parser.parse(post_date).date()
                notifs.append({"title": title, "content": content, "link": link, "date": date})
    
    return notifs

def save_posts(cur):
    posts = health_posts()
    for post in posts:
        if (post["date"] == None) or (post["date"] < datetime.date(2022, 1, 1)):
            continue

        cur.execute(queries.exists_sql, ("health", post["title"], post["link"]))
        if cur.fetchone() == None:
            cur.execute(queries.insert_sql, (post["title"], post["content"], post["link"], "health", post["date"], datetime.datetime.now()))
