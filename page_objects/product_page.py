from seleniumbase import BaseCase

class ProductPage(BaseCase):
    btn_addtocart = "#add-cart-button"
    btn_modal_addtocart = "#content-app > div > section > div > button"
    notif_success_addtocart = "Barang telah ditambahkan ke keranjang belanja"
    notif_elem_succ_addtocart = "span > span.sc-w647qe-0.WGnpq"
    check_elem_book_time = "#sheet-content > div > div.sc-EHOje.ffWHbE > div > div.sc-1crxk01-0.hImGyb > div.sc-1crxk01-0.gDKkkC > label > div > div > div"
    notif_elem_succ_getlocation = "#portal > div > span"

    base_url = "https://astraotoshop.com"

    def open_page(self):
        self.open("https://astraotoshop.com")