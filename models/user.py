from typing import List, Optional
from pydantic import BaseModel


class MediaListItem(BaseModel):
    id: str
    img_url: str
    date_posted: str
    likes: int
    comments: int
    type: str
    caption: str
    views: Optional[int] = None
    link: str


class IgTvListItem(BaseModel):
    id: str
    img_url: str
    date_posted: str
    likes: int
    comments: int
    duration: float
    title: str
    caption: str
    views: int
    link: str


class User(BaseModel):
    name: str
    full_name: str
    bio: str
    url: str
    is_business: bool
    is_joined_recently: bool
    business_category_name: str
    is_private: bool
    is_verified: bool
    ig_tv_videos: int
    highlight_reel_count: int
    has_channel: bool
    posts: str
    followers: str
    following: str
    photo_url: str
    followerCount: int
    followingCount: int
    postCount: int
    total_ig_tv_likes: int
    total_ig_tv_comments: int
    total_ig_tv_views: int
    total_ig_tv_videos: int
    total_media_likes: int
    total_media_comments: int
    total_media_views: int
    total_meadia_count: int
    engagement_rate: float
    media_list: List[MediaListItem]
    ig_tv_list: List[IgTvListItem]
