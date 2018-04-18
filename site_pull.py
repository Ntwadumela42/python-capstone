"""Working on modifying, doesn't work with most sites"""


from collections import Counter
import bs4
from inflection import titleize
import requests



from bs4 import BeautifulSoup

def title_generator(links):  #Takes the raw html data http://www.dailysmarty.com/posts/installing-and-working-with-pipenv
    titles = []

    def post_formatter(url):
        
            url = url.split('/')[-1]   #splits by /, selects last item
            url = url.replace('-', ' ')  #replaces - with spaces
            url = titleize(url)   #Only use of inflection
            titles.append(url)


    for link in links:
        post_formatter(link["href"])


    return titles


page = requests.get('http://www.cnn.com')
soup = BeautifulSoup(page.content, 'html.parser')
links = soup.find_all('a')
titles = title_generator(links)

# for title in titles:
#   title_list = []
#   title_list str(titles)
  
print(Counter(titles))



###Counter({'': 25, 'Videos': 7, 'Vr': 5, 'Cnn': 5, 'Culture': 4, '?Utm Source=Cnn.Com&Utm Medium=Referral&Utm Campaign=Navbar': 4, 'Us': 3, 'World': 3, 'Politics': 3, 'Money.Cnn.Com': 3, 'Opinions': 3, 'Health': 3, 'Entertainment': 3, 'Technology': 3, 'Style': 3, 'Travel': 3, 'Bleacherreport.Com': 3, 'Go2': 3, 'Crime And Justice': 2, 'Energy And Environment': 2, 'Extreme Weather': 2, 'Space Science': 2, 'Africa': 2, 'Americas': 2, 'Asia': 2, 'Europe': 2, 'Middle East': 2, 'President Donald Trump 45': 2, 'Congress Capitol Hill': 2, 'Us Security': 2, 'Supreme Court Nine': 2, 'Trumpmerica': 2, 'Election': 2, 'Opinion Politics': 2, 'Opinion Social Issues': 2, 'Food Diet': 2, 'Fitness Excercise': 2, 'Wellness': 2, 'Parenting': 2, 'Vital Signs': 2, 'Celebrities': 2, 'Movies': 2, 'Tv Shows': 2, 'Media': 2, 'Business': 2, 'Gadgets': 2, 'Future': 2, 'Startups': 2, 'Arts': 2, 'Design': 2, 'Fashion': 2, 'Architecture': 2, 'Luxury': 2, 'Autos': 2, 'Destinations': 2, 'Food And Drink': 2, 'Play': 2, 'Stay': 2, 'Nfl': 2, 'College Football': 2, 'Nba': 2, 'Mlb': 2, 'World Football': 2, 'Winter Olympics 2018': 2, 'Digital Studios': 2, 'Digital Shorts': 2, 'Hln': 2, 'All Shows': 2, 'How To Watch Vr': 2, 'Vr Archives': 2, 'More': 2, 'Photos': 2, 'Cnn Longform': 2, 'Cnn Investigations': 2, 'Profiles': 2, 'Cnn Leadership': 2, 'Subscription': 2, 'Search Jobs?Org Ids=1174&Ac=19299': 2, 'Www.Turner.Com': 1, 'Terms': 1, 'Privacy': 1, 'Accessibility': 1, '#': 1, 'About': 1, 'Tours.Cnn.Com': 1, 'Store.Cnn.Com': 1, 'Newsletters': 1, 'Transcripts': 1, 'Collection': 1, 'Cnnnewsource.Com': 1})
