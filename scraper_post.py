from requests import get
from bs4 import BeautifulSoup
import sys
import re
import json
from datetime import datetime


def get_post_data(url):
    page = get(url, timeout=5)
    soup = BeautifulSoup(page.content, 'html.parser')
    retext = re.findall(
        '<script type="text\/javascript">([^{]+?({.*profile_pic_url.*})[^}]+?)<\/script>', str(soup))[0][1]
    jsontext = json.loads(
        retext)['entry_data']['PostPage'][0]['graphql']['shortcode_media']
    caption = jsontext['edge_media_to_caption']['edges'][0]['node']['text']
    words = caption.split()
    hashtags = [x.strip('#') for x in words if x.startswith('#')]
    tagged_users_array = jsontext['edge_media_to_tagged_user']['edges']
    tagged_users = [x['node']['user'] for x in tagged_users_array]
    comments_array = jsontext['edge_media_to_parent_comment']['edges']
    comments = [x['node'] for x in comments_array]
    return {
        'image_url': jsontext['display_url'],
        'display_resources': jsontext['display_resources'],
        'caption': caption,
        'accessibility_caption': jsontext['accessibility_caption'],
        'hashtags': hashtags,
        'tagged_users': tagged_users,
        'comment_count': jsontext['edge_media_to_parent_comment']['count'],
        'comments': comments,
    }


if __name__ == "__main__":
    print(get_post_data("https://www.instagram.com/p/BsOGulcndj-/"))
