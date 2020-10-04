from typing import Any, List

from pydantic import BaseModel


class DisplayResource(BaseModel):
    src: str
    config_width: int
    config_height: int


class Owner(BaseModel):
    id: str
    is_verified: bool
    profile_pic_url: str
    username: str


class EdgeLikedBy(BaseModel):
    count: int


class PageInfo(BaseModel):
    has_next_page: bool
    end_cursor: Any


class Owner1(BaseModel):
    id: str
    is_verified: bool
    profile_pic_url: str
    username: str


class EdgeLikedBy1(BaseModel):
    count: int


class Node(BaseModel):
    id: str
    text: str
    created_at: int
    did_report_as_spam: bool
    owner: Owner1
    viewer_has_liked: bool
    edge_liked_by: EdgeLikedBy1
    is_restricted_pending: bool


class Edge(BaseModel):
    node: Node


class EdgeThreadedComments(BaseModel):
    count: int
    page_info: PageInfo
    edges: List[Edge]


class Comment(BaseModel):
    id: str
    text: str
    created_at: int
    did_report_as_spam: bool
    owner: Owner
    viewer_has_liked: bool
    edge_liked_by: EdgeLikedBy
    is_restricted_pending: bool
    edge_threaded_comments: EdgeThreadedComments


class Post(BaseModel):
    image_url: str
    display_resources: List[DisplayResource]
    caption: str
    accessibility_caption: str
    hashtags: List[str]
    tagged_users: List
    comment_count: int
    comments: List[Comment]
