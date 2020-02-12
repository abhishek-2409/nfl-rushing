from django.test import TestCase, Client
from nflrushing.models import Player
from nflrushing.views import index
from django.urls import reverse, resolve

class TestModels(TestCase):

    # def testInitialFailTest(self):
    #     assert 1==2

    def setUp(self):
        self.player1=Player()
        self.player1.player = "John Doe"
        self.player1.team = 'ABC'
        self.player1.pos = 'XYZ'
        self.player1.att = 21
        self.player1.att_g = 2.1
        self.player1.yds = 12
        self.player1.avg = 1.2
        self.player1.yds_g = 2.2
        self.player1.td = 10
        self.player1.lng = '85'
        self.player1.fst = 10
        self.player1.fst_pc = 29
        self.player1.rush20p = 14
        self.player1.rush40p = 10
        self.player1.fum = 5
        self.player1.save()


    def testEntryPlayer(self):
        test_player=Player.objects.get(player="John Doe")
        self.assertEqual(test_player, self.player1)

    def testStringRep(self):
        self.assertEqual(str(self.player1), self.player1.player)
        self.assertEqual(str(self.player1), "John Doe")

class TestUrls(TestCase):

    def testIndexURL(self):
        url = reverse('home')
        self.assertEquals(resolve(url).func, index)

class TestView(TestCase):

    def testIndex(self):
        client = Client()
        response = client.get(reverse('home'))

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response,'index.html')



