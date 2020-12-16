import csv
import requests
from lxml import html
from time import sleep


class FacebookBot:
    def __init__(self):
        self.source = "https://www.facebook.com/"
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36"
        }


    def open_csv_file_to_get_page_names(self):
        with open('page_names.csv', 'r') as f:
            reader = csv.reader(f, delimiter=',')
            next(reader)
            page_names = [page[-1] for page in reader]

        return page_names

    
    def parse_and_get_likes(self):

        pages_with_likes = []
        
        for page in self.open_csv_file_to_get_page_names():
            page_handle = self.source+page
            print(page_handle)
            sleep(2)
            response = html.fromstring(requests.get(page_handle, headers=self.headers).text.encode('utf-8'))
            likes = int(response.xpath("//span[@id='PagesLikesCountDOMID']/span/text()")[0].replace("\u200f", "").replace(',', ''))
            print('\n', page, likes)

            pages_with_likes.append([page, likes])
        
        self.save_page_likes_in_csv(pages_with_likes)

    
    def save_page_likes_in_csv(self, pages_with_likes):

        with open('results_fb_likes.csv', 'w', newline='') as f:
            writer = csv.writer(f, delimiter=',')
            writer.writerow(['fb_page_handle', 'like_count'])
            writer.writerows(pages_with_likes)
        
        print('\n======================')
        print('LIKES SAVED SUCCESS!')
        print('======================')







bot = FacebookBot()
bot.parse_and_get_likes()
    




