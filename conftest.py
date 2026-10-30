from typing import Any

import pytest
from pages.common_page import CommonPage
from pages.login_page import LoginPage
from pages.home_page import HomePage
from pages.pix_page import PixPage
from pages.emprestimos_page import EmprestimosPage

@pytest.fixture
def common_page(page: Any):
    return CommonPage(page)

@pytest.fixture
def page(page: Any):
    page.set_viewport_size({"width": 1800, "height": 960})
    page.goto("https://leogcarvalho.github.io/simulabank/login.html")
    return page
    
@pytest.fixture
def login_page(page: Any):
    return LoginPage(page)

@pytest.fixture
def home_page(page: Any):
    return HomePage(page)

@pytest.fixture
def pix_page(page: Any):
    return PixPage(page)

@pytest.fixture
def emprestimos_page(page: Any):
    return EmprestimosPage(page)
