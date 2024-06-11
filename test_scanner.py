import unittest
from scanner.scanner import scan_url_for_open_redirect

class TestScanner(unittest.TestCase):
    def test_scan_url_for_open_redirect(self):
        # Test cases for the scan_url_for_open_redirect function
        # You can define your test cases here
        # Example:
        result = scan_url_for_open_redirect("https://example.com")
        self.assertIsNone(result)  # Replace this with your assertion

if __name__ == '__main__':
    unittest.main()

