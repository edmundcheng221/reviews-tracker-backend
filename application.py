import argparse
import requests
from bs4 import BeautifulSoup
import json
import math


class LendingTreeParser:

    def __init__(self, baseurl):
        self.baseurl = baseurl
        self.lst = []
        self.dictionary = {}
        self.response = requests.get(self.baseurl)

    # Code used to parse html data. Common code that can be reused.
    def common(self, tag, class_name):
        if self.response.status_code != 200:
            print("Error fetching page")
            exit()
        soup = BeautifulSoup(self.response.content, 'html.parser')
        comment_list = soup.find_all(tag, {"class": class_name})
        res = []
        for ele in comment_list:
            res.append(ele.string)
        return res

    def get_reviews_title(self):
        return self.common('p', 'reviewTitle')

    def get_reviews_comment(self):
        return self.common('p', 'reviewText')

    def get_reviews_author(self):
        if self.response.status_code != 200:
            print("Error fetching page")
            exit()
        soup = BeautifulSoup(self.response.content, 'html.parser')
        comment_list = soup.find_all('p', {"class": 'consumerName'})
        res = []
        for ele in comment_list:
            res.append(str(ele)[24:])
        res2 = []
        for ele in res:
            idx = ele.find(" ")
            res2.append(ele[0:idx])
        return res2

    def get_reviews_num_stars(self):
        if self.response.status_code != 200:
            print("Error fetching page")
            exit()
        soup = BeautifulSoup(self.response.content, 'html.parser')
        comment_list = soup.find_all('div', {"class": 'numRec'})
        res = []
        for ele in comment_list:
            res.append(str(ele)[21])
        return res

    def get_reviews_publish_date(self):
        temp = self.common('p', 'consumerReviewDate')
        dates_published = []
        for ele in temp:
            dates_published.append(ele[12::])
        return dates_published

    def get_json_object(self):
        title = reviews.get_reviews_title()
        comment = reviews.get_reviews_comment()
        author = reviews.get_reviews_author()
        stars = reviews.get_reviews_num_stars()
        date = reviews.get_reviews_publish_date()
        for num, ele in enumerate(title):
            self.dictionary['title'] = title[num]
            self.dictionary['comment'] = comment[num]
            self.dictionary['author'] = author[num]
            self.dictionary['stars'] = stars[num]
            self.dictionary['date'] = date[num]
            self.lst.append(self.dictionary)
            self.dictionary = {}
        return self.lst

    # how many reviews in total
    def num_reviews(self):
        # num 5 stars, num 4 stars, etc
        reviews_distribution = self.common('a', 'review-count-text')
        total = 0
        for ele in reviews_distribution:
            total += int(ele[1:len(ele)-1])
        return total

    def display_results(self):
        suffix = '?sort=&pid=' + str(1)
        reviews = LendingTreeParser(self.baseurl + suffix)
        a = reviews.get_json_object()
        num_reviews_per_page = len(reviews.lst)
        max_pages = math.ceil(reviews.num_reviews() / num_reviews_per_page)
        # replace 4 with max_pages + 1 if you want results from all pages
        # I only put 4 because it takes too long to run 339 pages
        for i in range(2, 4):
            suffix = '?sort=&pid=' + str(i)
            reviews = LendingTreeParser(
                self.baseurl + suffix)
            a += reviews.get_json_object()
        return json.dumps(a, indent=2)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Parse Reviews')
    parser.add_argument('baseurl', type=str,
                        help='url example: https://www.lendingtree.com/reviews/personal/first-midwest-bank/52903183')
    args = parser.parse_args()
    reviews = LendingTreeParser(args.baseurl)
    res = reviews.display_results()
    print(res)