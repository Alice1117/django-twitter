from rest_framework.test import APIClient
from testing.testcases import TestCase
from tweets.models import Tweet

TWEET_LIST_API = '/api/tweets/'
TWEET_CREATE_API = '/api/tweets/'

class TweetApiTests(TestCase):

    def setUp(self):
        self.anonymous_client = APIClient()

        self.user1 = self.create_user('user3', 'user3@jiuzhang.com')
        self.tweets1 = [
            self.create_tweet(self.user1)
            for i in range(3)
        ]
        self.user1_client = APIClient()
        self.user1_client.force_authenticate(self.user1)

        self.user2 = self.create_user('user4', 'user4@jiuzhang.com')
        self.tweets2 = [
            self.create_tweet(self.user2)
            for i in range(2)
        ]

        print("setUp has completed.")

    def test_list_api(self):
        print("test_list_api")

        response = self.anonymous_client.get(TWEET_LIST_API)
        self.assertEqual(response.status_code, 404)

        #normal request
        print("test_list_api_2")
        response = self.anonymous_client.get(TWEET_LIST_API, {'user_id': self.user1.id})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data['tweets']), 3)
        response = self.anonymous_client.get(TWEET_LIST_API, {'user_id': self.user2.id})
        self.assertEqual(len(response.data['tweets']), 2)

        print("test_list_api_3")
        #check the order
        self.assertEqual(response.data['tweets'][0]['id'], self.tweets2[1].id)
        self.assertEqual(response.data['tweets'][1]['id'], self.tweets2[0].id)

    # def test_create_api(self):
    #     print("test_create_api")
    #     #user has to login
    #     response = self.anonymous_client.post(TWEET_LIST_API)
    #     self.assertEqual(response.status_code, 403)
    #
    #     #content cannot be null
    #     response = self.user1_client.post(TWEET_CREATE_API)
    #     self.assertEqual(response.status_code, 400)
    #
    #     #content cannot be too short
    #     response = self.user1_client.post(TWEET_CREATE_API, {'content': '1'})
    #     self.assertEqual(response.status_code, 400)
    #
    #     #content cannot be long
    #     response = self.user1_client.post(TWEET_CREATE_API, {
    #         'content': '0' * 141
    #     })
    #     self.assertEqual((response.status_code, 400))
    #
    #     #Happy path
    #     tweets_count = Tweet.objects.count()
    #     response = self.user1_client.post(TWEET_CREATE_API, {
    #         'content': 'Hello world, this is my first tweet!'
    #     })
    #     self.assertEqual((response.status_code, 201))
    #     print('print: ' + response.data['user'])
    #     self.assertEqual((response.data['user']['id'],self.user1.id))
    #     self.assertEqual(Tweet.objects.count(), tweets_count + 1)