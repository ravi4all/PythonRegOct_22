import bs4
import urllib.request as url
path = "https://www.imdb.com/title/tt9389998/?ref_=tt_sims_tt_i_2"

response = url.urlopen(path)

page = bs4.BeautifulSoup(response,"html.parser")

title = page.find("h1")
print("Movie Name :",title.text)
rating = page.find("span", {"class" : "sc-7ab21ed2-1 jGRxWM"})
print("IMDB Rating :",rating.text)
