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

                for link in links:
                    url = link['href']
                    print('url: ', self.base_url + url)
                # Lakukan sesuatu dengan setiap child_element
                # print(f'Elemen ke-{index + 1}: {selector}')