import requests
from helper.encryption import encrypt,decrypt
from page_objects.home_page import HomePage
from bs4 import BeautifulSoup

class ProductTest(HomePage):
    def setUp(self):
        # call the parent BaseCase class setup method
        super().setUp()
        print("RUNNING BEFORE EACH TEST")

        self.open_page()

    def tearDown(self):
        print("RUNNING AFTER EACH TEST")
        super().tearDown()
    # def test_product_sukucadang(self):
        # self.sleep(3)
        # produk = self.find_elements("#content-app > div > div > section > section > div.sc-1sdj1hu-0.dPPxkl > div")
        # content-app > div > div > section > section > div.sc-1sdj1hu-0.dPPxkl > div
        # content-app > div > div > section > section > div.sc-1sdj1hu-0.dPPxkl > div
        # content-app > div > div > section > section > div.sc-1sdj1hu-0.ePucrc > div > div:nth-child(1)
        # content-app > div > div > section > section > div.sc-1sdj1hu-0.ePucrc > div > div:nth-child(2)
        # content-app > div > div > section > section > div.sc-1sdj1hu-0.ePucrc > div > div:nth-child(3)

        # content-app > div > div > section > section > div:nth-child(9)
        # content-app > div > div > section > section > div:nth-child(9) > div > span
        # content-app > div > div > section > section > div.sc-1sdj1hu-0.ePucrc
        # content-app > div > div > section > section > div.sc-1sdj1hu-0.ePucrc > div > div:nth-child(1)
        # content-app > div > div > section > section > div.sc-1sdj1hu-0.ePucrc > div > div:nth-child(2)
        # content-app > div > div > section > section > div.sc-1sdj1hu-0.ePucrc > div > div:nth-child(3)

        # content-app > div > div > section > section > div:nth-child(12)

        # for i, request in enumerate(produk, start=1):
        #     locator_a = f"#content-app > div > div > section > section > div.sc-1sdj1hu-0.ePucrc > div > div:nth-child({i}) > a"
        #     link_elemen = self.find_element(locator_a)
        #     url_produk = link_elemen.get_attribute("href")
        #     print(f"URL produk ke-{i}: {url_produk}")
        #     print(f"HTML produk ke-{i}: {request.get_attribute('outerHTML')}")
        #
        #     html_content = f"""{request.get_attribute('outerHTML')}"""
        #
        #     soup = BeautifulSoup(html_content, 'html.parser')
        #
        #     links = soup.find_all('a', href=True)
        #
        #     for link in links:
        #         url = link['href']
        #         print(url)

    # content-app > div > div > section > section > div.sc-1sdj1hu-0.ePucrc > div > div:nth-child(1)
    # content-app > div > div > section > section > div.sc-1sdj1hu-0.ePucrc > div > div:nth-child(2)

    # content-app > div > div > section > section > div.sc-1sdj1hu-0.dPPxkl > div > div:nth-child(1)

    # content-app > div > div > section > section > div.sc-1sdj1hu-0.fRXXBp > div > div:nth-child(1)

    # // *[ @ id = "content-app"] / div / div / section / section / div[10]
    # // *[ @ id = "content-app"] / div / div / section / section / div[13]
    def test_product(self):
        self.sleep(3)

        label_produk = self.find_element("#content-app > div > div > section > section > div:nth-child(9) > div")
        print('label_produk: ', label_produk.text)
        cek_produk = self.assert_exact_text("Produk (Gratis Ongkir + Kupon Diskon + Cashback)", "#content-app > div > div > section > section > div:nth-child(9) > div")
        if cek_produk == True:
            child_produk = self.find_elements('// *[ @ id = "content-app"] / div / div / section / section / div[10]')

            for index, child_element in enumerate(child_produk):
                selector = child_element.get_attribute("outerHTML")
                soup = BeautifulSoup(selector, 'html.parser')
                links = soup.find_all('a', href=True)

                print('soup: ', soup)

                # for index, link in enumerate(links):
                if links:
                    link = links[0]
                    url = self.base_url + link['href']
                    teks = link.text

                    print('teks: ', teks)

                    self.driver.get(url)

                    self.wait_for_element_visible("#content-app > div > section > section.sc-16gfu33-3.jInVLK > div.sc-1crxk01-0.hImGyb > h1")
                    self.sleep(2)
                    self.scroll_to_bottom()
                    self.click("#content-app > div > section > div > button")

                    modal_tambah_keranjang = self.assert_exact_text("Tambah ke Keranjang", "#sheet-content > div > div.sc-EHOje.ffWHbE > div > div.sc-1crxk01-0.hImGyb > div.sc-1crxk01-0.imebcy > span")

                    if modal_tambah_keranjang == True:
                        self.click("#add-cart-button")

                        self.sleep(1)

                        test = self.wait_for_element_visible("span > span.sc-w647qe-0.WGnpq")
                        print('test: ', test.text)
                        notif_sukses_tambah_keranjang = self.assert_exact_text("Barang telah ditambahkan ke keranjang belanja", "span > span.sc-w647qe-0.WGnpq")
                        # self.wait_for_text("Barang telah ditambahkan ke keranjang belanja")
                        # notif_sukses_tambah_keranjang = self.find_text("Barang telah ditambahkan ke keranjang belanja","span > span.sc-w647qe-0.WGnpq")


                        print('notif: ', notif_sukses_tambah_keranjang)

                    # price_element = soup.find('')
                    # stock_info_start = teks.find("Stok tersedia")
                    # if stock_info_start != -1:
                    #     stock_info = teks[stock_info_start:]
                    #     print('url: ', self.base_url + url)
                    #     print('teks: ', stock_info)


    def test_product_voucher_pemasangan(self):
        self.sleep(3)

        label_produk = self.find_element("#content-app > div > div > section > section > div:nth-child(12) > div")
        print('label_produk: ', label_produk.text)
        cek_produk = self.assert_exact_text("Voucher Pemasangan + Cashback + Garansi (Aki) Shop & Drive", "#content-app > div > div > section > section > div:nth-child(12) > div")
        if cek_produk == True:
            child_produk = self.find_elements('//*[@id="content-app"]/div/div/section/section/div[13]/div')

            for index, child_element in enumerate(child_produk):
                selector = child_element.get_attribute("outerHTML")
                soup = BeautifulSoup(selector, 'html.parser')
                links = soup.find_all('a', href=True)

                print('soup: ', soup)

                # for index, link in enumerate(links):
                if links:
                    link = links[0]
                    url = self.base_url + link['href']
                    teks = link.text

                    print('teks: ', teks)

                    self.driver.get(url)

                    self.wait_for_element_visible("#content-app > div > section > section.sc-16gfu33-3.jInVLK > div.sc-1crxk01-0.hImGyb > h1")
                    self.sleep(2)
                    self.scroll_to_bottom()

                    current_url = self.get_current_url()

                    # button tambah keranjang
                    self.click("#content-app > div > section > div > button")

                    modal_pilih_lokasi = self.assert_exact_text("Pilih Lokasi", "body > div.ReactModalPortal > div > div > div > div.sc-1crxk01-0.ffGzzY > div > span.sc-w647qe-0.jAAZra")

                    if modal_pilih_lokasi == True:
                        self.click("body > div.ReactModalPortal > div > div > div > div.sc-1crxk01-0.cuXgWs > button.sc-1nihjkh-2.VYvtK.sc-hi7nq2-0.sc-hi7nq2-2.bnSWDy")
                        self.sleep(1)

                        page_pilihlokasi = self.wait_for_element_visible("#content-app > div.sc-15itbtn-11.dGAzqa > div.sc-1crxk01-0.dTRqRo > span.sc-w647qe-0.hgIfrm")
                        print('page_pilihlokasi: ', page_pilihlokasi)

                        page_pilihlokasi2 = self.assert_exact_text("Pilih Lokasi", "#content-app > div.sc-15itbtn-11.dGAzqa > div.sc-1crxk01-0.dTRqRo > span.sc-w647qe-0.hgIfrm")
                        print('page_pilihlokasi2: ', page_pilihlokasi2)

                        if page_pilihlokasi2 == True:
                            self.click('#content-app > div.sc-1crxk01-0.TStUl.sc-1p37un2-5.drQvKV > div.sc-1crxk01-0.engndw > button')

                            self.sleep(1)
                            notif_sukses_pilihlokasi = self.wait_for_element_visible("#portal > div > span")
                            print('notif_sukses_pilihlokasi: ', notif_sukses_pilihlokasi.text)
                            print('current_url: ', current_url)

                            self.open(current_url)

                            self.sleep(2)

                            # button tambah keranjang
                            self.click("#content-app > div > section > div > button")
                            modal_tambah_keranjang = self.assert_exact_text("Tambah ke Keranjang","#sheet-content > div > div.sc-EHOje.ffWHbE > div > div.sc-1crxk01-0.hImGyb > div.sc-1crxk01-0.imebcy > span")

                            if modal_tambah_keranjang == True:
                                self.sleep(3)

                            # test = self.wait_for_element_visible("span > span.sc-w647qe-0.WGnpq")
                            # print('test: ', test.text)
                            # notif_sukses_tambah_keranjang = self.assert_exact_text("Barang telah ditambahkan ke keranjang belanja", "span > span.sc-w647qe-0.WGnpq")
                            #
                            # print('notif: ', notif_sukses_tambah_keranjang)

                    # price_element = soup.find('')
                    # stock_info_start = teks.find("Stok tersedia")
                    # if stock_info_start != -1:
                    #     stock_info = teks[stock_info_start:]
                    #     print('url: ', self.base_url + url)
                    #     print('teks: ', stock_info)