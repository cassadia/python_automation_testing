import requests
from helper.encryption import encrypt,decrypt
from page_objects.home_page import HomePage

class HomeTest(HomePage):
    def setUp(self):
        # call the parent BaseCase class setup method
        super().setUp()
        print("RUNNING BEFORE EACH TEST")

        self.open_page()

    def tearDown(self):
        print("RUNNING AFTER EACH TEST")
        super().tearDown()
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
            response = requests.post('https://api.astraotoshop.com/v1/authentication-service/public/login', json=encrypted_data)
            login_data = response.json()
            print('checklogin_data: ', login_data)
            if status_code == 200:
                self.sleep(3)
            else:
                print('error')

    def test_register(self):
        self.click(self.btn_masuk_login) #klik button login
        self.sleep(2)
        self.click(self.btn_daftar_sekarang) #klik button daftar sekarang

        self.assert_exact_text("Atau daftar manual", self.label_text_daftarManual)

        self.send_keys(self.input_daftar_nama, self.text_daftar_nama)
        self.send_keys(self.input_daftar_email, self.text_daftar_email)
        self.send_keys(self.input_daftar_noHp, self.text_daftar_noHp)
        self.send_keys(self.input_daftar_password, self.text_daftar_password)
        self.send_keys(self.input_daftarUlang_password, self.text_daftarUlang_password)
        self.click(self.check_datar_policy)

        self.click(self.btn_daftar)

        self.sleep(3)