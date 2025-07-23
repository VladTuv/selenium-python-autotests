import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from faker import Faker
from pages.home_page import HomePage
from pages.signup_login_page import SignupLoginPage
from pages.account_info_page import AccountInfoPage
from pages.account_created_page import AccountCreatedPage

def test_user_registration():
    fake = Faker()
    driver = None
    try:
        service = ChromeService(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service)
        driver.maximize_window()
        user_data = {
            'name': fake.name(),
            'email': fake.email(),
            'password': fake.password(length=12),
            'dob_day': str(fake.random_int(min=1, max=28)),
            'dob_month': str(fake.random_int(min=1, max=12)),
            'dob_year': str(fake.random_int(min=1980, max=2005)),
            'first_name': fake.first_name(),
            'last_name': fake.last_name(),
            'company': fake.company(),
            'address1': fake.street_address(),
            'address2': fake.secondary_address(),
            'country': 'United States', 
            'state': fake.state(),
            'city': fake.city(),
            'zipcode': fake.zipcode(),
            'mobile_number': fake.phone_number()
        }
        home_page = HomePage(driver)
        signup_login_page = SignupLoginPage(driver)
        account_info_page = AccountInfoPage(driver)
        account_created_page = AccountCreatedPage(driver)
        home_page.open()
        home_page.go_to_login_page()
        signup_login_page.signup_new_user(user_data['name'], user_data['email'])
        account_info_page.fill_account_information(user_data)
        success_message = account_created_page.get_success_message_text()
        assert success_message == 'ACCOUNT CREATED!', \
            f"Ожидалось сообщение 'ACCOUNT CREATED!', но получено '{success_message}'"
        account_created_page.click_continue()   
    finally:
        if driver:
            driver.quit()
