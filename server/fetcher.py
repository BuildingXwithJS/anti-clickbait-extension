from trafilatura import fetch_url, extract

def getMainContent(url):
    downloaded = fetch_url(url)
    result = extract(downloaded)
    return result
