import requests
from helper.encryption import encrypt, decrypt
from page_objects.home_page import HomePage
from page_objects.product_page import ProductPage
from bs4 import BeautifulSoup

class BaseTest(HomePage, ProductPage):
    def setUp(self):
        super().setUp()
        print("RUNNING BEFORE EACH TEST")
        self.open_page()

    def tearDown(self):
        print("RUNNING AFTER EACH TEST")
        super().tearDown()

class HomeTest(BaseTest):
    def test_login(self):
        self.click(self.btn_masuk_login)

        self.assert_exact_text("Alamat Email atau Nomor HP", "#content-app > div > div.sc-rkmhgf-0.hWVtzq > div.sc-1crxk01-0.gVKylD > div > div > span")

        key = b'ad00bedb998b25b59e7c17e3679ffb37'
        text_to_encrypt = f'{{"username":"081296481112"}}'

        self.send_keys(self.input_username, "081296481112")
        self.click(self.btn_login)
        encrypted_data = encrypt(text_to_encrypt, key)
        response = requests.post('https://api.astraotoshop.com/v1/authentication-service/public/login/check_login_type', json=encrypted_data)
        checklogin_data = response.json()
        print('checklogin_data: ', checklogin_data)
        status_code = checklogin_data.get("status", None)
        self.sleep(2)

        if status_code == 200:
            self.send_keys(self.input_password, "Komponen1!")
            self.click(self.btn_login)
            text_to_encrypt = f'{{"username":"081296481112","password":"Komponen1!"}}'
            encrypted_data = encrypt(text_to_encrypt, key)
            response = requests.post('https://api.astraotoshop.com/v1/authentication-service/public/login',
                                     json=encrypted_data)
            login_data = response.json()
            print('checklogin_data: ', login_data)

            # Panggil method dari ProductTest
            product_test = ProductTest()
            product_test.test_product()

class ProductTest(BaseTest):
    def test_product(self):
        self.perform_product_test("Produk (Gratis Ongkir + Kupon Diskon + Cashback)", 9)

    def test_product_voucher_pemasangan(self):
        self.perform_product_test("Voucher Pemasangan + Cashback + Garansi (Aki) Shop & Drive", 12)

    def test_product_voucher_aose(self):
        self.perform_product_test("Voucher Astra Otoservice (Pemasangan + Cashback)", 15)

    def test_product_voucher_motoquick(self):
        self.perform_product_test("Voucher Motoquick (Pemasangan + Cashback)", 18)

 # Menambahkan method perform_product_test di sini untuk memastikan method ini ada dalam BaseTest
    def perform_product_test(self, expected_label, div_index):
        self.sleep(3)

        # label_produk = self.find_element(
        #     f"#content-app > div > div > section > section > div:nth-child({div_index}) > div")
        # print('label_produk: ', label_produk.text)
        #
        # cek_produk = self.assert_exact_text(expected_label,
        #                                     f"#content-app > div > div > section > section > div:nth-child({div_index}) > div")
        # print('cek_produk: ', cek_produk)