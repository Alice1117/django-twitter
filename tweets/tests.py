from django.test import TestCase
from django.contrib.auth.models import User
from tweets.models import Tweet
from datetime import timedelta
from utils.time_helpers import utc_now

# Create your tests here.
class TweetTests(TestCase):
    def test_hours_to_now(self):
        alice = User.objects.create_user(username='alice')
        tweet = Tweet.objects.create(user=alice, content='alice loves Rui!')
        tweet.created_at = utc_now() - timedelta(hours=10)
        tweet.save()
        self.assertEqual(tweet.hours_to_now/3600, 10)
