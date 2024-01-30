from seleniumbase import BaseCase
from test.test_home import HomeTest
from test.test_product import ProductTest

class TestSuite(BaseCase):
    def run_login_test(self):
        login_test = HomeTest.test_login()
        login_test.run_test()

    def run_product_test(self):
        product_test = ProductTest.test_product_voucher_pemasangan()
        product_test.test_run()

    def test_full_suite(self):
        self.run_login_test()
        self.run_product_test()

if __name__ == "__main__":
    suite = TestSuite("TestSuite")
    suite.run_test()
