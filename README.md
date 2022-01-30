# notif-scraper

Scrap content of different websites and list it in a single page.


Setting up the environment:
  1) Create a virtual environment to run python and install dependencies (pip install virtualenv and python3 -m venv env)
  2) Install the dependencies written in requirements.txt (pip install -r requirements.txt)
  3) And done


Write the scrapers under executors directory:
1) Create a file for a single for website 
2) Write a function inside it which returns an array in the following format: [{"title": title, "content": content, "link": link, "date": date}]
3) Call the function inside main.py
