import requests
from bs4 import BeautifulSoup
from dateutil import parser
import queries
import datetime

URL = "https://www.mohca.gov.bt/"
page = requests.get(URL)

soup = BeautifulSoup(page.content, "html.parser")

content = soup.find(id="content")

articles = content.find_all("article")

def culture_posts():
    notifs = [];
    for article in articles:
        title = article.h2.text.strip()
        link = article.h2.a["href"]
        content = article.p.contents[0]
        post_date = article.find("time", class_="published")["datetime"]
        date = None if post_date == '' else parser.parse(post_date).date()
        notifs.append({"title": title, "content": content, "link": link, "date": date})
    
    return notifs

def save_posts(cur):
    posts = culture_posts()
    for post in posts:
        if (post["date"] == None) or (post["date"] < datetime.date(2022, 1, 1)):
            continue

        cur.execute(queries.exists_sql, ("culture", post["title"], post["link"]))
        if cur.fetchone() == None:
            cur.execute(queries.insert_sql, (post["title"], post["content"], post["link"], "culture", post["date"], datetime.datetime.now()))
