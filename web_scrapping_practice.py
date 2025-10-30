''' web scrapping practice'''
from bs4 import BeautifulSoup
import requests
import pandas as pd

# url
URL = "https://www.opencodez.com"
response = requests.get (URL, timeout=10)

# html parser
soup = BeautifulSoup (response.content, "html.parser")

# scrap
main_title = soup.find ('h1', attrs= {'class':'image-logo'}).find('img')['alt']
latest_page = int (soup.find_all ('a', attrs= {'class':'inactive'})[-1]['href'].split('/')[-1])
title_all_list = []
book_img_all_list = []
print (f"\nWeb site Title is :'{main_title}'\n")
for p in range (1, (latest_page)+1):
    URL = "https://www.opencodez.com/page/{}".format(p)
    response = requests.get (URL , timeout=10)
    soup = BeautifulSoup (response.content, "html.parser")

#books_title and image link
    latest_post = soup. find ('div', attrs= {'class':'latest-section'})
    title_all = latest_post.findAll ('h2', attrs= {'class':'title'})
    book_img_all = latest_post.findAll ('div' , attrs= {'class':'featured-thumbnail'})

    each_list_lenght = [len (title_all), len (book_img_all)]
    if len( set( each_list_lenght)) == 1:
        for i in range (0 , each_list_lenght[0]):
            title_all_list.append (title_all[i].find ('a').get_text())
            book_img_all_list.append (book_img_all[i].find ('img')['src'])
        print (f"\nscrap page {p} is finished!")
    else:
        print ("\nsorry! we have missing value!!")

df = pd.DataFrame (list(zip(title_all_list, book_img_all_list)), columns= ['Title', 'ImageLink'])
print (df)

df.to_csv ("Opencodes_Posts.csv", index= False)
