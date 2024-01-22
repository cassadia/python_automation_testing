import requests
from helper.encryption import encrypt, decrypt
from page_objects.product_page import ProductPage
from bs4 import BeautifulSoup

class ProductTest(ProductPage):
    def setUp(self):
        super().setUp()
        print("RUNNING BEFORE EACH TEST")
        self.open_page()

    def tearDown(self):
        print("RUNNING AFTER EACH TEST")
        super().tearDown()

    def test_product(self):
        self.perform_product_test("Produk (Gratis Ongkir + Kupon Diskon + Cashback)", 9)

    def test_product_voucher_pemasangan(self):
        self.perform_product_test("Voucher Pemasangan + Cashback + Garansi (Aki) Shop & Drive", 12)

    def test_product_voucher_aose(self):
        self.perform_product_test("Voucher Astra Otoservice (Pemasangan + Cashback)", 15)

    def test_product_voucher_motoquick(self):
        self.perform_product_test("Voucher Motoquick (Pemasangan + Cashback)", 18)

    def perform_product_test(self, expected_label, div_index):
        self.sleep(3)

        label_produk = self.find_element(
            f"#content-app > div > div > section > section > div:nth-child({div_index}) > div")
        print('label_produk: ', label_produk.text)

        cek_produk = self.assert_exact_text(expected_label,
                                            f"#content-app > div > div > section > section > div:nth-child({div_index}) > div")
        print('cek_produk: ', cek_produk)

        if cek_produk:
            child_produk = self.find_elements(
                f'//*[@id="content-app"]/div/div/section/section/div[{div_index + 1}]/div')

            self.scroll_to_element(f'//*[@id="content-app"]/div/div/section/section/div[{div_index + 1}]/div')

            for index, child_element in enumerate(child_produk):
                selector = child_element.get_attribute("outerHTML")
                soup = BeautifulSoup(selector, 'html.parser')
                links = soup.find_all('a', href=True)

                print('soup: ', soup)

                if links:
                    link = links[0]
                    url = self.base_url + link['href']
                    teks = link.text

                    print('teks: ', teks)

                    self.driver.get(url)

                    self.wait_for_element_visible(
                        "#content-app > div > section > section.sc-16gfu33-3.jInVLK > div.sc-1crxk01-0.hImGyb > h1")
                    self.sleep(2)
                    self.scroll_to_bottom()

                    current_url = self.get_current_url()

                    self.click("#content-app > div > section > div > button")

                    modal_text = "Tambah ke Keranjang" if "Produk" in expected_label else "Pilih Lokasi"
                    modal_element = f"#sheet-content > div > div.sc-EHOje.ffWHbE > div > div.sc-1crxk01-0.hImGyb > div.sc-1crxk01-0.imebcy > span" if "Produk" in expected_label else "body > div.ReactModalPortal > div > div > div > div.sc-1crxk01-0.ffGzzY > div > span.sc-w647qe-0.jAAZra"

                    modal_result = self.assert_exact_text(modal_text, modal_element)
                    print('modal_result: ', modal_result)

                    if modal_result:
                        self.click("#add-cart-button") if "Produk" in expected_label else self.click(
                            "body > div.ReactModalPortal > div > div > div > div.sc-1crxk01-0.cuXgWs > button.sc-1nihjkh-2.VYvtK.sc-hi7nq2-0.sc-hi7nq2-2.bnSWDy")
                        self.sleep(1)

                        if "Produk" in expected_label:
                            # test = self.wait_for_element_visible(self.notif_elem_succ_addtocart)
                            # print('test: ', test.text)
                            notif_text = self.notif_success_addtocart
                            notif_element = self.notif_elem_succ_addtocart
                        else:
                            notif_text = "Pilih Lokasi"
                            notif_element = self.notif_elem_succ_getlocation

                        if "Pilih Lokasi" in notif_text:
                            self.click(
                                '#content-app > div.sc-1crxk01-0.TStUl.sc-1p37un2-5.drQvKV > div.sc-1crxk01-0.engndw > button')
                            notif_sukses_pilihlokasi = self.wait_for_element_visible(notif_element)
                            print('notif_sukses_pilihlokasi: ', notif_sukses_pilihlokasi.text)

                            self.sleep(1)

                            print('current_url: ', current_url)
                            self.open(current_url)
                            self.sleep(2)

                            self.click(self.btn_modal_addtocart)
                            modal_tambah_keranjang = self.assert_exact_text("Tambah ke Keranjang",
                                                                            "#sheet-content > div > div.sc-EHOje.ffWHbE > div > div.sc-1crxk01-0.hImGyb > div.sc-1crxk01-0.imebcy > span")

                            if modal_tambah_keranjang:
                                self.sleep(3)

                                # check waktu booking
                                check_book = self.click(self.check_elem_book_time)
                                print('check_book: ', check_book)

                                self.click("#add-cart-button")
                                notif_sukses = self.assert_exact_text(self.notif_success_addtocart, "span > span.sc-w647qe-0.WGnpq")
                                print('notif: ', notif_sukses)

                                self.sleep(3)