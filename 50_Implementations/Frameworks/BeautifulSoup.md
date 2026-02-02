
# BeautifulSoup

#NLP #Implementation #Python #WebScraping

---

## 1. 개요

**BeautifulSoup**는 HTML 및 XML 파일에서 데이터를 추출하기 위한 파이썬 라이브러리입니다. 웹 스크레이핑(Web Scraping) 또는 웹 크롤링(Web Crawling)을 통해 웹 페이지의 구조화된 데이터에 쉽게 접근할 수 있도록 도와줍니다. 자연어 처리(NLP) 분야에서는 웹에 존재하는 방대한 텍스트 데이터를 수집하여 [[Corpus|말뭉치]]를 구축하는 데 매우 유용하게 사용됩니다.

BeautifulSoup는 문서를 파싱(Parsing)하고, 파싱된 트리를 탐색, 검색, 수정하는 간단하고 직관적인 방법을 제공합니다. 이 문서는 `requests` 라이브러리와 함께 BeautifulSoup를 사용하는 기본적인 방법을 설명합니다.

---

## 2. 설치 및 기본 설정

### 2.1. 라이브러리 설치

BeautifulSoup와 HTML 요청을 보내기 위한 `requests` 라이브러리를 설치합니다. 또한, BeautifulSoup가 HTML을 파싱하기 위해 사용할 파서(parser)도 함께 설치해야 합니다. `lxml`은 매우 빠르고 유연하여 널리 사용됩니다.

```bash
pip install beautifulsoup4 requests lxml
```

### 2.2. 기본 사용법

웹 스크레이핑의 기본 과정은 다음과 같습니다.

1.  `requests`를 사용하여 웹 페이지의 HTML 소스 코드를 가져옵니다.
2.  가져온 HTML을 `BeautifulSoup` 객체로 변환(파싱)합니다.
3.  `BeautifulSoup` 객체가 제공하는 메서드를 사용하여 원하는 데이터를 찾고 추출합니다.

---

## 3. `requests`로 웹 페이지 가져오기

`requests` 라이브러리는 특정 URL에 HTTP 요청을 보내고 응답을 받는 기능을 수행합니다. `get()` 메서드를 사용하면 해당 URL의 HTML 콘텐츠를 가져올 수 있습니다.

```python
import requests

# 대상 URL
url = "https://example.com"

# HTTP GET 요청 보내기
response = requests.get(url)

# 응답 상태 코드 확인 (200이면 성공)
if response.status_code == 200:
    # HTML 콘텐츠 가져오기
    html_content = response.text
    # print(html_content)
else:
    print(f"Failed to retrieve the webpage. Status code: {response.status_code}")

```

---

## 4. BeautifulSoup으로 데이터 추출하기

`requests`로 가져온 HTML 콘텐츠를 BeautifulSoup 객체로 만들어 데이터를 추출할 수 있습니다.

### 4.1. BeautifulSoup 객체 생성

```python
from bs4 import BeautifulSoup

# 위에서 얻은 html_content 사용
# 'lxml' 파서를 사용하여 BeautifulSoup 객체 생성
soup = BeautifulSoup(html_content, 'lxml')
```

### 4.2. 요소 찾기 (Finding Elements)

BeautifulSoup는 HTML 태그, CSS 클래스, ID 등을 사용하여 원하는 요소를 정밀하게 찾을 수 있는 강력한 메서드를 제공합니다.

#### `find()`와 `find_all()`

-   `find(name, attrs, ...)`: 조건에 맞는 **첫 번째** 요소를 반환합니다.
-   `find_all(name, attrs, ...)`: 조건에 맞는 **모든** 요소를 리스트 형태로 반환합니다.

#### 예시: 태그 이름으로 찾기

```python
# 첫 번째 <h1> 태그 찾기
h1_tag = soup.find('h1')
print(h1_tag)
# 출력: <h1>Example Domain</h1>

# 모든 <p> 태그 찾기
p_tags = soup.find_all('p')
for p in p_tags:
    print(p)
# 출력:
# <p>This domain is for use in illustrative examples in documents. You may use this domain in literature without prior coordination or asking for permission.</p>
# <p><a href="https://www.iana.org/domains/example">More information...</a></p>
```

#### 예시: CSS 클래스(class)로 찾기

CSS 클래스로 요소를 찾을 때는 `class_` 인자를 사용합니다. (파이썬의 `class` 키워드와 충돌을 피하기 위함)

```python
# <div class="content"> ... </div> 와 같은 요소를 찾는다고 가정
# content_div = soup.find('div', class_='content')
```

#### 예시: ID로 찾기

HTML `id` 속성으로 요소를 찾을 때는 `id` 인자를 사용합니다.

```python
# <p id="main-text"> ... </p> 와 같은 요소를 찾는다고 가정
# main_text_p = soup.find('p', id='main-text')
```

#### CSS 선택자로 찾기: `select()` 및 `select_one()`

CSS 선택자(Selector)는 웹 브라우저가 HTML 요소에 스타일을 적용하기 위해 사용하는 강력한 문법입니다. BeautifulSoup는 이 선택자를 그대로 사용하여 요소를 찾을 수 있는 `select()`와 `select_one()` 메서드를 제공합니다. 이는 `find()`/`find_all()`보다 더 직관적이고 복잡한 구조를 쉽게 찾을 수 있게 해줍니다.

-   `select_one(selector)`: CSS 선택자에 해당하는 **첫 번째** 요소를 반환합니다. (`find()`와 유사)
-   `select(selector)`: CSS 선택자에 해당하는 **모든** 요소를 리스트로 반환합니다. (`find_all()`과 유사)

**주요 CSS 선택자 문법:**

-   **태그:** `p`, `div`, `a`
-   **클래스:** `.class-name` (점(.)으로 시작)
-   **ID:** `#id-name` (해시(#)로 시작)
-   **자손:** `div p` (div 안에 있는 모든 p)
-   **자식:** `ul > li` (ul 바로 아래에 있는 모든 li)
-   **속성:** `a[href]` (href 속성을 가진 모든 a)

```python
# example.com 페이지에서 a 태그를 CSS 선택자로 찾기
# <p><a href="https://www.iana.org/domains/example">More information...</a></p>
link = soup.select_one('p > a')
print(link)
# 출력: <a href="https://www.iana.org/domains/example">More information...</a>

# select는 리스트를 반환
all_links = soup.select('a')
print(all_links)
# 출력: [<a href="https://www.iana.org/domains/example">More information...</a>]
```

### 4.3. 데이터 추출하기

요소를 찾았다면, 그 안의 텍스트나 속성 값을 추출할 수 있습니다.

#### 텍스트 콘텐츠 추출: `.text` 또는 `.get_text()`

```python
h1_text = h1_tag.text
print(h1_text)
# 출력: Example Domain
```

#### 속성 값 추출: `.get('attribute_name')` 또는 `['attribute_name']`

`<a>` 태그의 `href` 속성처럼 특정 속성의 값을 가져올 수 있습니다.

```python
# find()를 사용하여 'a' 태그를 찾습니다.
a_tag = soup.find('a')

# .get() 메서드를 사용하여 href 속성 값을 가져옵니다.
link_url = a_tag.get('href')
print(link_url)
# 출력: https://www.iana.org/domains/example

# 대괄호 표기법을 사용할 수도 있습니다.
link_url_alt = a_tag['href']
print(link_url_alt)
# 출력: https://www.iana.org/domains/example
```

---

## 5. 종합 실습 예제

네이버 뉴스 기사 제목을 스크레이핑하는 간단한 예제입니다.

*주의: 웹사이트의 구조는 언제든지 변경될 수 있으며, 과도한 스크레이핑은 서버에 부하를 줄 수 있습니다. 또한, 사이트의 이용 약관(robots.txt)을 확인하여 스크레이핑이 허용되는지 확인해야 합니다.*

```python
import requests
from bs4 import BeautifulSoup

# 네이버 뉴스 IT/과학 섹션 URL
url = "https://news.naver.com/main/main.naver?mode=LSD&mid=shm&sid1=105"

# 헤더 추가 (봇 차단 방지)
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
response = requests.get(url, headers=headers)

soup = BeautifulSoup(response.text, 'lxml')

# 헤드라인 뉴스 제목을 담고 있는 CSS 선택자(selector)를 사용
# (개발자 도구를 통해 클래스 이름을 확인해야 함)
# 예시 선택자: '#section_body ul > li > dl > dt:not(.photo) > a'
# 이 선택자는 시간에 따라 변경될 수 있습니다.
headlines = soup.select('#section_body ul > li > dl > dt:not(.photo) > a')

print("네이버 IT/과학 뉴스 헤드라인:")
for i, headline in enumerate(headlines, 1):
    # .text 속성으로 텍스트만 추출하고, 양쪽 공백을 제거(strip())
    title = headline.text.strip()
    link = headline.get('href')
    print(f"{i}. {title}")
    # print(f"   - 링크: {link}")

```

이처럼 `requests`와 `BeautifulSoup`를 함께 사용하면 웹에서 원하는 텍스트 데이터를 손쉽게 수집하여 NLP 연구 및 모델 개발을 위한 자신만의 [[Corpus|말뭉치]]를 구축할 수 있습니다.
