from urllib.parse import urlparse, urlunparse

def filter_url(url):
    parsed_url = urlparse(url)
    filtered_url = parsed_url.scheme + "://" + parsed_url.netloc + parsed_url.path
    return filtered_url

# 測試範例
url1 = "https://www.instagram.com/p/C5ezb6Uhyi8/?img_index=1"
url2 = "https://www.instagram.com/p/C5nR4vwrdSv/?utm_source=ig_web_copy_link"

filtered_url1 = filter_url(url1)
filtered_url2 = filter_url(url2)

print(filtered_url1)  # Output: https://www.instagram.com/p/C5ezb6Uhyi8/
print(filtered_url2)  # Output: https://www.instagram.com/p/C5ezb6Uhyi8/
