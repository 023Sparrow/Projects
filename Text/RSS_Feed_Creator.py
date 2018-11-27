import feedparser

display = feedparser.parse('https://www.g-cores.com/rss')

def RssFeed(d):
    return("""The RSS Title is : {title}\nThe RSS Link is : {link}\nRSS Description is : {des}""".format(title = d.feed.title,link = d.feed.link,des
    = d.feed.description))

def RssItem(d,n):
    return """This is the No.{num} document of {rss}\nThe Title is {title}.\nThe Link is
    {link}.\nThe Description is {des}.\nThe Published is
    {pub}.\n""".format(num = n,rss = d.feed.title,title = d.entries[n].title,link =
    d.entries[n].link,des = d.entries[n].description,pub =
    d.entries[n].published)

print('please input your RSS/ATOM link:')
url = feedparser.parse(input('>>>'))
print(RssFeed(url))
print('please input the No content you want to read, or it will show anll the
articles of the rss.')
num = input('>>>')
if num:
    print(RssItem(url,num))
else:
    for num in range(1,21):
        print(RssItem(url,num))
