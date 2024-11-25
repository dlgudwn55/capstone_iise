import time
import warnings
from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

warnings.filterwarnings(action='ignore')

driver = webdriver.Edge()
url = 'https://www.instagram.com'
driver.get(url)
time.sleep(1)

email = 'leehj7934'
password = 'gudwn55!'

input_li = driver.find_elements(By.TAG_NAME, 'input')
print("input_li:",input_li)
input_li[0].send_keys(email)
input_li[1].send_keys(password)
input_li[1].send_keys(Keys.RETURN)

time.sleep(5)

# 로그인 정보 저장 여부 ("나중에 하기 버튼 클릭")
btn_later1 = driver.find_element(By.CLASS_NAME, 'x1i10hfl')
btn_later1.click()
time.sleep(5)

# 알림 설정 ("나중에 하기 버튼 클릭")
# btn_later2 = driver.find_element(By.CLASS_NAME, '_a9--._a9_1')
# btn_later2.click()
# time.sleep(5)

hashtag = "여행"
driver.get(f"https://www.instagram.com/explore/tags/{hashtag}/")
time.sleep(5)

# 페이지 끝까지 스크롤
def scroll_down():
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(5)

# 게시글 설명 추출
def get_caption(link):
    driver.get(link)
    time.sleep(7)
    try:
        caption = driver.find_element(By.CSS_SELECTOR, 'h1._ap3a._aaco._aacu._aacx._aad7._aade')
        print(type(caption))
    except:
        print(type(caption))
        caption = "캡션 찾을 수 없음"
    return caption

post_links = set()

# for _ in range(1):
# scroll_down()
posts = driver.find_elements(By.XPATH, '//a[contains(@href, "/p/")]')
for post in posts:
    post_links.add(post.get_attribute('href'))

# 링크 수집 종료 후 콘솔에 표시
print(f"총 {len(post_links)}개의 게시물 URL을 수집했습니다.")

captions = []
for i, link in enumerate(post_links):
    print(link)
    caption = get_caption(link)
    if i == 0:
        print(caption)
    captions.append(caption.text)
    # captions.append(caption.text)

for i, cap in enumerate(captions):
    print(f"Post {i}: {cap}")

driver.quit()