import urllib.request # Library for url fetching
import lxml.html # Library for html parsing

def crawl(url, depth=3):
    if depth == 0:
        return None
    else:
        try:
            page = urllib.request.urlopen(url)
        except (urllib.request.URLError, ValueError):
            return None

        html = page.read()
        dom = lxml.html.fromstring(html)

        print("Level %d: %s" % (depth, url))

        for link in dom.xpath('//a/@href'):
            crawl(link, depth-1)

crawl('https://carterfang.wordpress.com/portfolio/')