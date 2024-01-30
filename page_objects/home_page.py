from seleniumbase import BaseCase

class HomePage(BaseCase):
    btn_masuk_login = "#content-app > div > div > section > div > div.sc-ysqdlt-0.uvLpE > div:nth-child(4)"
    btn_login = "#content-app > div.sc-vswk66-0.fJiAhm > div.sc-rkmhgf-0.hWVtzq > div.sc-1crxk01-0.gVKylD > button"
    akun_username = "081296481112"
    akun_password = "Komponen1!"
    input_username = "#content-app > div.sc-vswk66-0.fJiAhm > div.sc-rkmhgf-0.hWVtzq > div.sc-1crxk01-0.gVKylD > div > div > div > input"
    input_password = "#content-app > div.sc-vswk66-0.fJiAhm > div.sc-rkmhgf-0.hWVtzq > div.sc-1crxk01-0.gVKylD > div:nth-child(2) > div > div > input"
    btn_lupa_kata_sandi = "#content-app > div.sc-vswk66-0.fJiAhm > div.sc-rkmhgf-0.hWVtzq > div.sc-1crxk01-0.gVKylD > span"
    btn_daftar_sekarang = "#modal-register > button"
    label_text_alamatEmailNoHp = "#content-app > div > div.sc-rkmhgf-0.hWVtzq > div.sc-1crxk01-0.gVKylD > div > div > span"

    # daftar customer baru
    input_daftar_nama = "#content-app > div.sc-1eqnadz-0.gBssMj > div > div:nth-child(1) > div > div > input"
    input_daftar_email = "#content-app > div.sc-1eqnadz-0.gBssMj > div > div:nth-child(2) > div > div > input"
    input_daftar_noHp = "#content-app > div.sc-1eqnadz-0.gBssMj > div > div:nth-child(4) > div > div > input"
    input_daftar_password = "#content-app > div.sc-1eqnadz-0.gBssMj > div > div:nth-child(5) > div > div > input"
    input_daftarUlang_password = "#content-app > div.sc-1eqnadz-0.gBssMj > div > div:nth-child(6) > div > div > input"
    check_datar_policy = "#content-app > div.sc-1eqnadz-0.gBssMj > div > label:nth-child(7) > div > div > div"
    label_text_daftarManual = "#content-app > div.sc-1crxk01-0.kVJwvT > span.sc-w647qe-0.fOWbCJ"

    text_daftar_nama = "im not visible"
    text_daftar_email = "visible@gmail.com"
    text_daftar_noHp = "081296234234"
    text_daftar_password = "Komponen1!"
    text_daftarUlang_password = "Komponen1!"

    btn_daftar = "#content-app > div.sc-1eqnadz-0.gBssMj > div > button"

    base_url = "https://astraotoshop.com"

    def open_page(self):
        self.open("https://astraotoshop.com")

