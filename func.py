def func_and_args(func, *args):
    """Функция, которая печатает имя переданной ей функции и значения аргументов"""
    edit_func = func.__name__.title().replace('_', ' ')
    print(edit_func, *args)

def open_browser(browser_name):
    func_and_args(open_browser, browser_name)

def go_to_companyname_homepage(page_url):
    func_and_args(go_to_companyname_homepage,page_url)

def find_registration_button_on_login_page(page_url, button_text):
    func_and_args(find_registration_button_on_login_page, page_url, button_text)


open_browser('chrome')
go_to_companyname_homepage('https://www.gazprom.ru/')
find_registration_button_on_login_page('https://www.gazprom.ru/', 'О «Газпроме»')