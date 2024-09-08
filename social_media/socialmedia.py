import requestium

class SocialMediaMentions:
    def __init__(self, username, password, sid):
        self.username = username
        self.password = password
        self.sid = sid
        self.mentions = []
    
    def collect_mentions(self):
        session = requestium.Session()
        session.driver = requestium.Driver()

        # Login to Brand24
        session.driver.get("https://app.brand24.com/login")
        session.driver.find_element_by_name("username").send_keys(self.username)
        session.driver.find_element_by_name("password").send_keys(self.password)
        session.driver.find_element_by_name("login").click()

        #Navigate to mentions page
        session.driver.get("https://app.brand24.com/mentions/{self.sid}")

        # Collect mentions
        mentions_table = session.driver.find_element_by_class_name("mentions-table")
        mentions_rows = mentions_table.find_elements_by_tag_name("tr")
        for row in mentions_rows:
            mention = {
                "text": row.find_element_by_class_name("mention-text").text,
                "sentiment": row.find_element_by_class_name("sentiment").text
            }
            self.mentions.append(mention)
    
    def collate_mentions(self):
        positive_mentions = [mention for mention in self.mentions if mention["sentiment"] == "Positive"]
        negative_mentions = [mention for mention in self.mentions if mention["sentiment"] == "Negative"]
        netural_mentions = [mention for mention in self.mentions if mention["sentiment"] == "Neutral"]
        return {
            "total_mentions": len(self.mentions),
            "positive_mentions": len(positive_mentions),
            "negative_mentions": len(negative_mentions),
            "netural_mentions": len(netural_mentions)
        }

"""
username = "name.surname@example.com"
password = "password"
sid = "287321168"

mentions = SocialMediaMentions(username, password, sid)
mentions.collect_mentions()
results = mentions.collate_mentions()
print(results)

"""