import requests
from bs4 import BeautifulSoup
from dateutil import parser
import queries
import datetime

URL = "http://www.education.gov.bt/"
page = requests.get(URL)

soup = BeautifulSoup(page.content, "html.parser")

tabs = soup.find_all("div", class_="tab-content")

results = tabs[0].find_all("div", class_="tab-pane")

def edu_posts():
    notifs = [];
    for result in results:
        posts = result.find_all("div", class_="pt-cv-content-item")
        for post in posts:  
            title = post.h4.text
            link = post.h4.a["href"]
            content = post.find("div", class_="pt-cv-content").contents[0]
            date = None if post.time is None else parser.parse(post.time["datetime"]).date()
            notifs.append({"title": title, "content": content, "link": link, "date": date})

    return notifs

def save_posts(cur):
    posts = edu_posts()
    for post in posts:
        if (post["date"] == None) or (post["date"] < datetime.date(2022, 1, 1)):
            continue

        cur.execute(queries.exists_sql, ("education", post["title"], post["link"]))
        if cur.fetchone() == None:
            cur.execute(queries.insert_sql, (post["title"], post["content"], post["link"], "education", post["date"], datetime.datetime.now()))
