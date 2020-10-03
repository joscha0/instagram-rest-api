from requests import get
from bs4 import BeautifulSoup
import sys
import re
import json
from datetime import datetime

URL = 'https://www.instagram.com'


def get_profile_data(username):
    url = '%s/%s/' % (URL, username)
    page = get(url, timeout=5)
    soup = BeautifulSoup(page.content, 'html.parser')
    data = soup.find_all('meta', attrs={'property': 'og:description'})
    photo = soup.find_all('meta', attrs={'property': 'og:image'})
    text = data[0].get('content').split()
    retext = re.findall(
        '<script type="text\/javascript">([^{]+?({.*profile_pic_url.*})[^}]+?)<\/script>', str(soup))[0][1]
    jsontext = json.loads(retext)['entry_data']['ProfilePage'][0]
    ig_tv_likes = 0
    ig_tv_comments = 0
    ig_tv_views = 0
    ig_tv_videos = 0
    ig_tv_list = []
    for video in jsontext['graphql']['user']['edge_felix_video_timeline']['edges']:
        ig_tv_videos += 1
        ig_tv_likes += video['node']['edge_liked_by']['count']
        ig_tv_comments += video['node']['edge_media_to_comment']['count']
        ig_tv_views += video['node']['video_view_count']
        ig_tv_list.append({
            'id': '2042452950535483363',
            'img_url': video['node']['thumbnail_src'],
            'date_posted': datetime.fromtimestamp(video['node']['taken_at_timestamp']),
            'likes': video['node']['edge_liked_by']['count'],
            'comments': video['node']['edge_media_to_comment']['count'],
            'duration': video['node']['video_duration'],
            'title': video['node']['title'],
            'caption': video['node']['edge_media_to_caption']['edges'][0]['node']['text'],
            'views': video['node']['video_view_count'],
            'link': 'https://www.instagram.com/p/' + video['node']['shortcode'],
        })
    media_likes = 0
    media_comments = 0
    media_views = 0
    media_count = 0
    media_videos = 0
    media_list = []
    for media in jsontext['graphql']['user']['edge_owner_to_timeline_media']['edges']:
        media_count += 1
        media_likes += media['node']['edge_liked_by']['count']
        media_comments += media['node']['edge_media_to_comment']['count']
        if media['node']['is_video']:
            media_videos += 1
            media_views += media['node']['video_view_count']
            media_list.append({
                'id': '2042452950535483363',
                'img_url': media['node']['thumbnail_src'],
                'date_posted': datetime.fromtimestamp(media['node']['taken_at_timestamp']),
                'likes': media['node']['edge_liked_by']['count'],
                'comments': media['node']['edge_media_to_comment']['count'],
                'type': media['node']['__typename'][5:],
                'caption': media['node']['edge_media_to_caption']['edges'][0]['node']['text'],
                'views': media['node']['video_view_count'],
                'link': 'https://www.instagram.com/p/' + media['node']['shortcode'],
            })
        else:
            media_list.append({
                'id': '2042452950535483363',
                'img_url': media['node']['thumbnail_src'],
                'date_posted': datetime.fromtimestamp(media['node']['taken_at_timestamp']),
                'likes': media['node']['edge_liked_by']['count'],
                'comments': media['node']['edge_media_to_comment']['count'],
                'type': media['node']['__typename'][5:],
                'caption': media['node']['edge_media_to_caption']['edges'][0]['node']['text'],
                'link': 'https://www.instagram.com/p/' + media['node']['shortcode'],
            })
    media_video_like_engagement = 0
    media_video_comment_engagement = 0
    if media_videos != 0:
        media_video_like_engagement = (
            ig_tv_likes / ig_tv_videos) / (ig_tv_views / ig_tv_videos)

    return {
        'name': username,
        'full_name': jsontext['graphql']['user']['full_name'],
        'bio': jsontext['graphql']['user']['biography'],
        'url': jsontext['graphql']['user']['external_url'],
        'is_business': jsontext['graphql']['user']['is_business_account'],
        'is_joined_recently': jsontext['graphql']['user']['is_joined_recently'],
        'business_category_name': jsontext['graphql']['user']['business_category_name'],
        'is_private': jsontext['graphql']['user']['is_private'],
        'is_verified': jsontext['graphql']['user']['is_verified'],
        'ig_tv_videos': jsontext['graphql']['user']['edge_felix_video_timeline']['count'],
        'highlight_reel_count': jsontext['graphql']['user']['highlight_reel_count'],
        'has_channel': jsontext['graphql']['user']['has_channel'],

        'posts': text[4],
        'followers': text[0],
        'following': text[2],
        'photo_url': photo[0].get('content'),
        'followerCount': jsontext['graphql']['user']['edge_followed_by']['count'],
        'followingCount': jsontext['graphql']['user']['edge_follow']['count'],
        'postCount': jsontext['graphql']['user']['edge_owner_to_timeline_media']['count'],

        'total_ig_tv_likes': ig_tv_likes,
        'total_ig_tv_comments': ig_tv_comments,
        'total_ig_tv_views': ig_tv_views,
        'total_ig_tv_videos': ig_tv_videos,

        'total_media_likes': media_likes,
        'total_media_comments': media_comments,
        'total_media_views': media_views,
        'total_meadia_count': media_count,

        'engagement_rate': (media_likes / media_count) / jsontext['graphql']['user']['edge_followed_by']['count'] if media_count != 0 and jsontext['graphql']['user']['edge_followed_by']['count'] != 0 else None,

        'media_list': media_list,

        'ig_tv_list': ig_tv_list,
    }


if __name__ == "__main__":
    print(get_profile_data("garyvee"))
