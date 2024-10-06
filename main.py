import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin


# تابعی برای بررسی وضعیت فعال بودن لینک
def is_link_active(url):
    try:
        response = requests.head(url, timeout=5)
        return response.status_code == 200
    except requests.RequestException:
        return False


# تابع برای جمع‌آوری لینک‌ها از یک صفحه
def collect_links(url):
    # ارسال درخواست به سایت
    response = requests.get(url)

    # تجزیه HTML با BeautifulSoup
    soup = BeautifulSoup(response.text, 'html.parser')

    # جمع‌آوری تمام لینک‌های موجود در صفحه
    links = set()
    for link in soup.find_all('a', href=True):
        full_url = urljoin(url, link['href'])
        links.add(full_url)

    return links


# وب‌سایتی که می‌خواهید بررسی کنید
website_url = 'https://sisno.ir'

# جمع‌آوری لینک‌ها
all_links = collect_links(website_url)

# فیلتر کردن لینک‌های فعال
active_links = [link for link in all_links if is_link_active(link)]

# نمایش لینک‌های فعال
for link in active_links:
    print(link)
