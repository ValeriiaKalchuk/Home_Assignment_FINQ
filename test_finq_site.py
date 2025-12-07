import time

import pytest
from selenium import webdriver
from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


BASE_URL = "https://finqai.co.il"
TIMEOUT = 15


@pytest.fixture(scope="module")
def driver():
    # Driver to be used for tests execution
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    driver = webdriver.Chrome(options=options)
    driver.implicitly_wait(5)
    yield driver
    driver.quit()


def test_homepage_title_contains_finq(driver):
    """
    Test that assures correctness of homepage title
    """
    driver.get(BASE_URL)
    WebDriverWait(driver, TIMEOUT).until(lambda d: d.title != "")

    assert "FINQ" in driver.title, f"Expected 'FINQ' in title, got: {driver.title}"


def test_pensions_ranking_table_and_header_visible(driver):
    """
    Test that verifies visibility of pensions ranking table header
    """
    driver.get(f"{BASE_URL}/pensions-ranking")
    wait = WebDriverWait(driver, TIMEOUT)

    # Button to show rating table (label can differ)
    ranking_button = wait.until(
        EC.element_to_be_clickable(
            (By.XPATH, "//a[contains(normalize-space(),'לצפייה')]")
        )
    )
    ranking_button.click()

    # Waiting for column header 'דמי ניהול'
    column_header = wait.until(
        EC.visibility_of_element_located(
            (By.XPATH, "//*[contains(normalize-space(),'דמי ניהול')]")
        )
    )
    assert column_header.is_displayed(), "Expected 'דמי ניהול' column header to be visible"

    # Asserting that rows/list exist under table header — not empty UI
    rows = driver.find_elements(By.XPATH, "//table//tr | //div[contains(@class,'row')]")
    assert len(rows) > 1, "Expected data rows to appear under the table"

def test_ai_funds_faq_expand(driver):
    """
    Test that assures visibility of hidden text in the FAQ section after expand action
    """
    driver.get(f"{BASE_URL}/ai-funds")
    wait = WebDriverWait(driver, TIMEOUT)

    # Waiting here 5 seconds to let the browser load fully before scrolling to prevent elements from jumping
    time.sleep(5)

    # Scrolling to the FAQ title
    faq_anchor = wait.until(
        EC.visibility_of_element_located(
            (By.XPATH, "//*[contains(normalize-space(),'שאלות?')]")
        )
    )
    driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", faq_anchor)
    time.sleep(1)

    # Expanding the first FAQ question
    question = wait.until(
        EC.element_to_be_clickable(
            (By.XPATH, "//h4[contains(normalize-space(),'מה זה מודל FINQFIRST')]")
        )
    )
    question.click()
    # Waiting here for 2 seconds to let the element open
    time.sleep(2)

    # Verifying hidden answer being visible  now
    answer = wait.until(
        EC.visibility_of_element_located(
            (By.XPATH, "//h4[contains(normalize-space(),'מה זה מודל FINQFIRST')]/following-sibling::*[1]")
        )
    )
    assert answer.is_displayed(), "Expected FAQ answer to be visible after click"
    assert answer.text.strip() != "", "FAQ answer appears empty"
