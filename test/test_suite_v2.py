# project_name/tests/test_suite.py
import unittest
from pythonProject.test.test_home import HomeTest
from pythonProject.test.test_product import ProductTest

class FullTestSuite(unittest.TestCase):
    def setUp(self):
        self.home_test = HomeTest()
        self.product_test = ProductTest()

    def tearDown(self):
        pass

    def test_full_suite(self):
        # Jalankan skenario login
        self.home_test.setUp()
        self.home_test.test_login()
        self.home_test.tearDown()

        # Jalankan skenario produk
        self.product_test.setUp()
        self.product_test.test_product()
        self.product_test.tearDown()

if __name__ == '__main__':
    # Jalankan test suite
    unittest.TextTestRunner(verbosity=2).run(unittest.TestLoader().loadTestsFromTestCase(FullTestSuite))