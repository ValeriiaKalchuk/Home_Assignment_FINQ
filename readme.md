# FINQ – Light Automation Assignment

## Tools Used
- Python 3.14
- pytest (test runner)
- Selenium WebDriver (Chrome browser)

Selenium Manager (built into Selenium 4.6+) automatically finds chromedriver,
so no manual driver installation is needed.

## How to Install
Downalod the project, and run the following command in cmd in the project:
```bash
pip install selenium pytest
```

## Tests info
**test_homepage_title_contains_finq**  - Test that assures correctness of homepage title
- Opens https://finqai.co.il
- Asserts the page title contains “FINQ”

**test_pensions_ranking_table_and_header_visible** - Test that verifies visibility of pensions ranking table header
- Opens /pensions-ranking
- Clicks the rating button “לצפייה…”
- Verifies a ranking table/list appears
- Asserts the column header “דמי ניהול” is visible

**test_ai_funds_faq_expand** (bonus test) -  Test that assures visibility of hidden text in the FAQ section after expand action
- Opens /ai-funds
- Scrolls to FAQ section
- Expands “מה זה מודל FINQFIRST?”
- Verifies hidden answer becomes visible

## How to run tests
Run the following command in cmd in the project:
```bash
pytest -v test_finq_site.py
```



