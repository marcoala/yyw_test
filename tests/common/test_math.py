from django.test import TestCase
from yyw_test.common.math import mean


class TestMean(TestCase):

    def test_base_usage(self):
        avg = mean(4, 4, 6, 6)
        self.assertEqual(avg, 5)
