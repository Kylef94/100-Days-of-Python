from bs4 import BeautifulSoup as bs
import requests
import lxml

response = requests.get('https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/')
web_page = response.text

soup = bs(web_page, "html.parser")
titles = soup.find_all(name="h3", class_="title")
title_list = []
for title in titles:
    title_list.append(title.getText())

print(title_list)
with open('100 best films of all time.txt', 'w', encoding='utf-8') as f:
    for title in title_list:
        f.write('%s\n' % title)
    print('done')



# response = requests.get("https://news.ycombinator.com/news")
# yc_web_page = response.text
#
# soup = bs(yc_web_page, "html.parser")
# articles = soup.find_all(class_='titleline')
# article_texts = []
# article_links = []
#
# for article_tag in articles:
#     link = article_tag.a['href']
#     article_links.append(link)
#
#     text = article_tag.getText()
#     article_texts.append(text)
#
#
# article_scores = [int(score.getText().split()[0]) for score in soup.find_all(name='span',class_='score')]
# highest_score = max(article_scores)
# highest_score_index = article_scores.index(highest_score)
# print(highest_score)
# print(article_texts[highest_score_index])
# print(article_links[highest_score_index])
# print(article_scores[highest_score_index])

# with open('website.html', encoding='utf8') as f:
#     contents = f.read()
#
#
# soup = bs(contents, 'html.parser')
# print(soup.prettify())