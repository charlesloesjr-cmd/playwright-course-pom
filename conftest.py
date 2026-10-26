import pytest
from pages.login_page import LoginPage

@pytest.fixture
def page(page):
    page.set_viewport_size({"width": 1920, "height": 1080})
    page.goto("https://leogcarvalho.github.io/simulabank/login.html")
    return page
    
@pytest.fixture
def login_page(page):
    return LoginPage(page)


# import pytest
# from pages.login_page import LoginPage

# @pytest.fixture(scope="session")
# def browser_context_args(browser_context_args):
#     return {
#         **browser_context_args,
#         "viewport": {"width": 1920, "height": 1080}
#     }

# @pytest.fixture
# def login_page(page):
#     return LoginPage(page)