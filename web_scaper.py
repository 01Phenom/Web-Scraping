import requests
from bs4 import BeautifulSoup
import re
import pandas as pd
from requests.exceptions import Timeout, HTTPError, RequestException

# Function to extract social media links
def extract_social_media_links(soup):
    social_media = {}
    patterns = {
        'facebook': re.compile(r'facebook.com'),
        'twitter': re.compile(r'twitter.com'),
        'linkedin': re.compile(r'linkedin.com'),
        'instagram': re.compile(r'instagram.com'),
        'youtube': re.compile(r'youtube.com')
    }
    for platform, pattern in patterns.items():
        link = soup.find('a', href=pattern)
        if link and link['href']:
            social_media[platform] = link['href']
    return social_media

# Function to extract tech stack
def extract_tech_stack(soup):
    tech_stack = []
    scripts = soup.find_all('script')
    for script in scripts:
        if script.get('src'):
            src = script['src']
            if 'jquery' in src:
                tech_stack.append('jQuery')
            elif 'bootstrap' in src:
                tech_stack.append('Bootstrap')
            elif 'react' in src:
                tech_stack.append('React')
            elif 'angular' in src:
                tech_stack.append('Angular')
            elif 'vue' in src:
                tech_stack.append('Vue')
    return tech_stack

# Function to extract meta title
def extract_meta_title(soup):
    title_tag = soup.find('title')
    return title_tag.string if title_tag else ''

# Function to extract meta description
def extract_meta_description(soup):
    meta_tag = soup.find('meta', attrs={'name': 'description'})
    return meta_tag['content'] if meta_tag else ''

# Function to extract payment gateways
def extract_payment_gateways(soup):
    payment_gateways = []
    patterns = ['paypal', 'stripe', 'razorpay']
    for pattern in patterns:
        if pattern in soup.get_text().lower():
            payment_gateways.append(pattern)
    return payment_gateways

# Function to scrape a single website
def scrape_website(url):
    try:
        response = requests.get(url, timeout=30)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')

        data = {
            'url': url,
            'meta_title': extract_meta_title(soup),
            'meta_description': extract_meta_description(soup),
            'social_media_links': extract_social_media_links(soup),
            'tech_stack': extract_tech_stack(soup),
            'payment_gateways': extract_payment_gateways(soup)
        }
        return data
    except HTTPError as e:
        print(f"HTTP error scraping {url}: {e}")
    except Timeout:
        print(f"Timeout error scraping {url}")
    except RequestException as e:
        print(f"Error scraping {url}: {e}")
    return None

# Main function to scrape multiple websites and save data to CSV
def main():
    websites = [
    'https://www.apple.com',
    'https://www.microsoft.com',
    'https://www.adobe.com',
    'https://www.netflix.com',
    'https://www.reddit.com',
    'https://www.quora.com',
    'https://www.pinterest.com',
    'https://www.tumblr.com',
    'https://www.dropbox.com',
    'https://www.slack.com',
    'https://www.trello.com',
    'https://www.spotify.com',
    'https://www.airbnb.com',
    'https://www.booking.com',
    'https://www.kayak.com',
    'https://www.wikipedia.org',
    'https://www.cnn.com',
    'https://www.bbc.com',
    'https://www.nytimes.com',
    'https://www.theguardian.com',
    'https://www.bloomberg.com',
    'https://www.forbes.com',
    'https://www.techcrunch.com',
    'https://www.wired.com',
    'https://www.medium.com',
    'https://www.github.com',
    'https://www.stackoverflow.com',
    'https://www.gitlab.com',
    'https://www.bitbucket.org',
    'https://www.codecademy.com',
    'https://www.udacity.com',
    'https://www.coursera.org',
    'https://www.edx.org',
    'https://www.khanacademy.org',
    'https://www.pluralsight.com',
    'https://www.udemy.com',
    'https://www.shopify.com',
    'https://www.digitalocean.com',
    'https://www.heroku.com',
    'https://www.aws.amazon.com',
    'https://www.azure.microsoft.com',
    'https://www.salesforce.com',
    'https://www.oracle.com',
    'https://www.ibm.com',
    'https://www.samsung.com',
    'https://www.sony.com',
    'https://www.lg.com',
    'https://www.philips.com',
    'https://www.intel.com',
    'https://www.nvidia.com',
    'https://www.hp.com',
    'https://www.dell.com',
    'https://www.lenovo.com',
    'https://www.acer.com',
    'https://www.ford.com',
    'https://www.toyota.com',
    'https://www.bmw.com',
    'https://www.mercedes-benz.com',
    'https://www.audi.com',
    'https://www.nike.com',
    'https://www.puma.com',
    'https://www.underarmour.com',
    'https://www.patagonia.com',
    'https://www.northface.com'
]

    results = []
    for website in websites:
        result = scrape_website(website)
        if result:
            results.append(result)

    df = pd.DataFrame(results)
    df.to_csv('website_data.csv', index=False)

if __name__ == '__main__':
    main()
