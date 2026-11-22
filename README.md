# SauceDemo UI Tests

Automated UI tests for the demo online store https://www.saucedemo.com,
written with Python, pytest and Playwright using the Page Object Model.

## What is covered
- Login: successful login and negative scenarios (locked out user, empty username,
  empty password, wrong password)
- Inventory: adding and removing products, cart badge counter
- Cart: product presence, items count, cart URL
- Checkout: end-to-end purchase (login, add to cart, checkout, order confirmation)
  and form validation (first name is required)

## Tech stack
- Python
- pytest
- Playwright (pytest-playwright, Chromium)
- ruff

## Project structure
- `pages/` - Page Objects (`LoginPage`, `InventoryPage`, `CartPage`, `CheckoutPage`)
- `conftest.py` - fixtures that create page objects
- `test_*.py` - test files (login, inventory, cart, checkout)
- `pytest.ini` - screenshot and trace settings

## How to run
1. Create and activate a virtual environment:

   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   ```
2. Install dependencies and the browser:

   ```bash
   pip install -r requirements.txt
   python -m playwright install chromium
   ```
3. Run the tests:

   ```bash
   python -m pytest -v
   ```

## Debugging failed tests
On failure, a screenshot and a Playwright trace are saved to `test-results/`.
Open a trace with:

```bash
python -m playwright show-trace test-results/<test-folder>/trace.zip
```
