import os
from datetime import datetime

from rfeed import Item, Feed


def generate_feed(json_list):
    items = []
    for json_item in json_list:
        level = json_item.get('level') or 'INFO'
        item = Item(
            title=json_item.get('_line'),
            link='https://app.logdna.com/',
            pubDate=datetime.now(),
            author=json_item.get('container'),
            description=level
        )
        items.append(item)
    feed = Feed(
        title="LogDNA RSS Feed",
        link=os.environ.get('RSS_LINK'),
        description='LogDNA RSS Feed for Rainmeter widgets.',
        lastBuildDate=datetime.now(),
        items=items
    )

    return feed.rss()
