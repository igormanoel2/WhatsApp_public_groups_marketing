from bs4 import BeautifulSoup
import urllib.request
import serpscrap
import csv
import re
import io


# Scrap the google search results and return a CSV file contaning links that are somehow related to WA public groups
def google_scraper():
    keywords = ['chat.whatsapp.com/', 'chat.whatsapp.com/*', 'inurl:chat.whatsapp.com/', 'link:chat.whatsapp.com']
    config = serpscrap.Config()
    config.set('scrape_urls', True)
    config.set('num_pages_for_keyword', 100)  # 100 page per keyword
    config.set('num_results_per_page', 20)  # 20 pages per result
    scrap = serpscrap.SerpScrap()
    scrap.init(config=config.get(), keywords=keywords)
    scrap.as_csv('raw_rez')


# function to crowl all the links and find the whatsup groups insid them
def groups_links_in_link(url):
    try:
        dup_links = []
        html_page = urllib.request.urlopen(url)
        soup = BeautifulSoup(html_page, features="lxml")
        for link in soup.findAll('a', attrs={'href': re.compile("http[s]://chat.whatsapp.com/")}):
            dup_links.append(link.get('href'))
        links = list(dict.fromkeys(dup_links))

        with io.open('what_pub_groups.txt', 'a+', encoding='utf8') as f_Whatsup_groups_list:
            for clean_link in links:
                f_Whatsup_groups_list.write(clean_link + '\n')
        f_Whatsup_groups_list.close()
    except:
        return None

    # read from the CSV and extract the whatsup groups links


def groups_links_filter():
    with io.open('raw_rez.csv', 'r', encoding='utf8') as f_in:
        raw_rez = csv.reader(f_in)
        with io.open('what_pub_groups.txt', 'a+', encoding='utf8') as f_Whatsup_groups_list:
            for row in raw_rez:
                for item in row:
                    dup_urls = re.findall(
                        'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', item)
                    urls = list(dict.fromkeys(dup_urls))
                    for url in urls:
                        if re.search('http[s]://chat.whatsapp.com/', url):
                            f_Whatsup_groups_list.write(url + '\n')
                        else:
                            groups_links_in_link(url)
    f_in.close()
    f_Whatsup_groups_list.close()


# Main function
def main():
    google_scraper()
    groups_links_filter()


if __name__ == "__main__":
    main()
