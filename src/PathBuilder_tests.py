import unittest
from urllib.parse import urlparse, parse_qs

from helpers.PathBuilder import get_stats_path 

class PathBuilderTests(unittest.TestCase):

    def test_GetStatsPath_WithYear_ReturnsExpected(self):
        statsId = str(5)
        expectedPath = 'https://www.pgatour.com/api/stats-download?timePeriod=THROUGH_EVENT&statsId=' + statsId + '&tourCode=R&year=2024'
        path = get_stats_path(statsId = statsId)
        self.assertEqual(path, expectedPath)

    def test_GetStatsPath_ReturnsQuery(self):
        statsId = str(7)
        expectedQuery = 'timePeriod=THROUGH_EVENT&statsId=7&tourCode=R&year=2024'
        path = get_stats_path(statsId = statsId)
        query = urlparse(path).query
        print(query)
        self.assertEqual(query, expectedQuery)

if __name__ == '__main__':
    unittest.main()