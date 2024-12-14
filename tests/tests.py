import unittest
from urllib.parse import urlparse, parse_qsl
from path_builder import get_stats_path 

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
        self.assertEqual(query, expectedQuery)
        
    def test_GetStatsPath_ReturnsExpected_in_Query(self):
        statsId = str(12345)
        path = get_stats_path(statsId = statsId)
        query_dict = path_to_query_dict(path)
        self.assertEqual(query_dict['statsId'], statsId)

def path_to_query_dict(path: str):
    query = urlparse(path).query
    return dict(parse_qsl(query))

if __name__ == '__main__':
    unittest.main()