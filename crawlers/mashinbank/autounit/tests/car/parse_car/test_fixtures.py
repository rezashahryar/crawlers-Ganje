# THIS IS A GENERATED FILE
# Generated by: scrapy crawl car -o res.json  # noqa: E501
import os
import unittest
from glob import glob

from scrapy_autounit.player import Player


class AutoUnit(unittest.TestCase):
    def test__car__parse_car(self):
        _dir = os.path.dirname(os.path.abspath(__file__))
        fixtures = glob(os.path.join(_dir, "*.bin"))
        for fixture in fixtures:
            player = Player.from_fixture(fixture)
            player.playback()


if __name__ == '__main__':
    unittest.main()