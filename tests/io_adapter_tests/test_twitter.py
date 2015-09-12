from unittest import TestCase
from chatterbot.adapters.io import TwitterAdapter


class TwitterAdapterTests(TestCase):

    def setUp(self):
        adapter = TwitterAdapter(
            consumer_key="blahblahblah",
            consumer_secret="nullvoidnullvoidnullvoid"
        )

