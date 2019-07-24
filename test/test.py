import requests
import unittest


class ServerTest(unittest.TestCase):
    def test(self):
        r = requests.get('http://localhost:50000')
        
        self.assertEqual(r.status_code, 200)


if __name__ == '__main__':
    unittest.main()
