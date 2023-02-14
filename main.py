import requests
from bs4 import BeautifulSoup
import lxml

response = requests.get("https://news.ycombinator.com/")
yc_web_page = response.text

soup = BeautifulSoup(yc_web_page, "lxml")

article_tags = soup.find_all(name="span", class_="titleline")

article_text = [tag.getText().split(" (")[0] for tag in article_tags]
article_link = [link.get("href") for link in soup.select(".titleline a")]
article_upvote = [int(vote.getText().split()[0]) for vote in soup.find_all(name="span", class_="score")]

print(article_text)
print(article_link)
print(article_upvote)

most_up_voted = max(article_upvote)
index = article_upvote.index(most_up_voted)
print(f"\n\nThe article with the most up votes is '{article_text[index]}'.\nIt's URL is {article_link[index]}.\n"
      f"It has been up voted {most_up_voted} times.")


