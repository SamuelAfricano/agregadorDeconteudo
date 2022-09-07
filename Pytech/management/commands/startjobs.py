from django.core.management.base import BaseCommand

import feedparser
from dateutil import parser

from Pytech.models import Item

class Command(BaseCommand):
	def handle(self, *args, **options):
		feed = feedparser.parse("https://techcrunch.com/category/startups/feed/")
		post_titulo = feed.channel.title
		post_img = feed.channel.image["href"]

		for item in feed.entries:
			if not Item.objects.filter(guid=item.guid).exists():
  				episode = Item(
					titulo=item.title,
					Bio=item.description,
					link=item.link,
					imagem=post_img,
					nome=post_titulo,
					guid=item.guid,
				)
  				episode.save()