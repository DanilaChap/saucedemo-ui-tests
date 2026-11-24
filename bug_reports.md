# Bug Reports — SauceDemo (`problem_user`)

This document contains 4 bug reports discovered during exploratory testing of the [SauceDemo](https://www.saucedemo.com) web application under the `problem_user` test account.

---

## BUG-001: [Checkout] Typing into the 'Last Name' field overwrites 'First Name' with a single character and blocks checkout

- **Environment / Build:** macOS, Chromium 130 / Chrome, SauceDemo Web (`https://www.saucedemo.com`)
- **Reproduction Rate:** 100% (5/5)
- **Severity:** Critical (Blocker)
- **Priority:** High
- **Preconditions:**
  1. User is logged in as `problem_user`.
  2. At least one product is added to the cart.
  3. User is on the `Checkout: Your Information` page (`/checkout-step-one.html`).

**Steps to Reproduce:**
1. Enter `"Danila"` into the `First Name` input field.
2. Enter `"Chapurka"` into the `Last Name` input field.
3. Enter `"51100"` into the `Zip/Postal Code` input field.
4. Click the `Continue` button.

**Actual Result:**
Typing into the `Last Name` field leaves `Last Name` empty and overwrites the `First Name` field with only the last typed character (`"a"`). Clicking `Continue` fails with the validation error: `Error: Last Name is required`. The user cannot complete the purchase.

**Expected Result:**
The `Last Name` field should accept and display `"Chapurka"`, `First Name` should retain `"Danila"`, and clicking `Continue` should navigate the user to `Checkout: Overview` (`/checkout-step-two.html`).

---

## BUG-002: [Inventory] Clicking 'Remove' on a product card does not remove the item from the cart

- **Environment / Build:** macOS, Chromium 130 / Chrome, SauceDemo Web (`https://www.saucedemo.com`)
- **Reproduction Rate:** 100% (5/5)
- **Severity:** Major
- **Priority:** High
- **Preconditions:**
  1. User is logged in as `problem_user` on the `Products` page (`/inventory.html`).
  2. The shopping cart is empty.

**Steps to Reproduce:**
1. Click `Add to cart` on the `Sauce Labs Backpack` product card (the button changes to `Remove` and the cart badge shows `1`).
2. Click the `Remove` button on the same `Sauce Labs Backpack` product card.

**Actual Result:**
Nothing happens when clicking `Remove`: the button stays in the `Remove` state, and the shopping cart badge still displays `1`. (Workaround: the item can only be removed from inside the `/cart.html` page).

**Expected Result:**
The item is removed from the cart, the cart badge disappears (or decrements by 1), and the button on the product card reverts to `Add to cart`.

---

## BUG-003: [Inventory] Product sorting dropdown does not change the order of products

- **Environment / Build:** macOS, Chromium 130 / Chrome, SauceDemo Web (`https://www.saucedemo.com`)
- **Reproduction Rate:** 100% (5/5)
- **Severity:** Major
- **Priority:** Medium
- **Preconditions:** User is logged in as `problem_user` on the `Products` page (`/inventory.html`).

**Steps to Reproduce:**
1. Click the sort dropdown in the top-right corner (default is `Name (A to Z)`).
2. Select `Name (Z to A)`, `Price (low to high)`, or `Price (high to low)`.

**Actual Result:**
The product list remains in the default `Name (A to Z)` order regardless of the selected sorting option.

**Expected Result:**
The product cards on the page should reorder dynamically according to the selected criterion (alphabetically descending or by price ascending/descending).

---

## BUG-004: [Inventory] All product cards display the same placeholder dog image instead of actual product photos

- **Environment / Build:** macOS, Chromium 130 / Chrome, SauceDemo Web (`https://www.saucedemo.com`)
- **Reproduction Rate:** 100% (5/5)
- **Severity:** Minor
- **Priority:** High
- **Preconditions:** User is logged in as `problem_user`.

**Steps to Reproduce:**
1. Navigate to the `Products` page (`/inventory.html`).
2. Inspect the product thumbnails across all 6 product cards.

**Actual Result:**
Every product card displays the exact same image of a pug/dog (`/static/media/sl-404.168b1cce.jpg`) instead of the corresponding product image.

**Expected Result:**
Each product card should display its own unique product photo matching the item title and description.
