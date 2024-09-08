import requests
from bs4 import BeautifulSoup
import json

class PageEngagement:
    def __init__(self, page_url):
        self.page_url = page_url
        self.engagement_data = {}

    def get_facebook_data(self):
        #Get facebook data using Facebook Graph API
        access_token = "YOUR_FACEBOOK_ACCESS_TOKEN"
        api_url = f"https://graph.facebook.com/v13.0/?id={self.page_url}&fields=engagement&access_token={access_token}"
        response = requests.get(api_url)
        data = json.loads(response.text)
        self.engagement_data["facebook"] = {
            "likes": data["engagement"]["likes"],
            "shares": data["engagement"]["shares"],
            "comments": data["engagement"]["comments"]
        }

    def get_twitter_data(self):
        # Get Twitter data using Twitter API
        api_url = f"https://cdn.api.twitter.com/1/urls/count.json?url={self.page_url}"
        response = requests.get(api_url)
        data = json.loads(response.text)
        self.engagement_data["twitter"] = {
            "tweets": data["count"]
        }

    def get_linkedin_data(self):
        # Get LinkedIn data using LinkedIn API
        api_url = f"https://www.linkedin.com/countserv/count/share?url={self.page_url}"
        response = requests.get(api_url)
        data = json.loads(response.text)
        self.engagement_data["linkedin"] = {
            "shares": data["count"]
        }

    def get_tiktok_data(self):
        # Get TikTok data using TikTok API
        api_url = f"https://api.tiktok.com/v1/share/share_count?url={self.page_url}"
        response = requests.get(api_url)
        data = json.loads(response.text)
        self.engagement_data["tiktok"] = {
            "shares": data["share_count"]
        }

    def get_instagram_data(self):
        # Get Instagram data using Instagram API
        access_token = "YOUR_INSTAGRAM_ACCESS_TOKEN"
        api_url = f"https://graph.instagram.com/v13.0/{self.page_url}?fields=engagement&access_token={access_token}"
        response = requests.get(api_url)
        data = json.loads(response.text)
        self.engagement_data["instagram"] = {
            "likes": data["engagement"]["likes"],
            "comments": data["engagement"]["comments"]
        }

    def calculate_engagement_rate(self):
        # Calculate engagement rate based on Facebook data
        if "facebook" in self.engagement_data:
            likes = self.engagement_data["facebook"]["likes"]
            shares = self.engagement_data["facebook"]["shares"]
            comments = self.engagement_data["facebook"]["comments"]
            engagement_rate = (likes + shares + comments) / (likes + shares + comments + 100) * 100
            self.engagement_data["engagement_rate"] = engagement_rate

    def get_page_data(self):
        # Get page data using BeautifulSoup
        response = requests.get(self.page_url)
        soup = BeautifulSoup(response.text, "html.parser")
        self.engagement_data["page_data"] = {
            "title": soup.title.text,
            "description": soup.find("meta", attrs={"name": "description"}).attrs["content"]
        }

    def assess_page(self):
        self.get_facebook_data()
        self.get_twitter_data()
        self.get_linkedin_data()
        self.get_tiktok_data()
        self.get_instagram_data()
        self.calculate_engagement_rate()
        self.get_page_data()
        return self.engagement_data

"""
# Example usage
page_url = "https://example.com"
engagement = PageEngagement(page_url)
data = engagement.assess_page()
print(data)
"""