# cmd 창에 chcp 65001 실행
import re, requests, csv
from bs4 import BeautifulSoup
from time import sleep

def reviews_info(div):
    review_text = div.find("div", "a-row review-data").span.text
    review_author = div.find("a", "a-size-base a-link-normal author").text
    review_stars = div.find("div", "a-row").a.text
    on_review_date = div.find('span', 'a-size-base a-color-secondary review-date').text
    review_date = [x.strip() for x in re.sub("on ", "", on_review_date).split(",")]
    return { "review_text" : review_text, "review_author" : review_author, "review_stars" : review_stars, "review_date": review_date }

base_url = "https://www.amazon.com/Overwatch-Collectors-PC/product-reviews/B017L187X2/ref=cm_cr_dp_see_all_summary?ie=UTF8&showViewpoints=1&sortBy=helpful&pageNumber="

reviews = []
NUM_PAGES = 8

for page_num in range(1, NUM_PAGES + 1):
    print("souping page", page_num, ",", len(reviews), "의 data를 수집")
    url = base_url + str(page_num)
    soup = BeautifulSoup(requests.get(url).text, 'lxml') # 아마존은 lxml이 답이다
    for div in soup('div', 'a-section review'):
        reviews.append(reviews_info(div))
        sleep(30)
###################################################
# Save dict data
keys = reviews[0].keys()
with open('amazon_overwatch_review.csv', 'w', encoding="utf-8") as f:
    dict_writer = csv.DictWriter(f, delimiter=',', lineterminator='\n', fieldnames=keys)
    dict_writer.writeheader()
    dict_writer.writerows(reviews)
