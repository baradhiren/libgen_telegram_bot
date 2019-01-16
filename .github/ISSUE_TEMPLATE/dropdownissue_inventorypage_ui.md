---
name: BUG_UI_InventoryPage_Dropdown
about: Bug report for dropdown issue on Inventory page.
title: 'Dropdown on Inventory page not organizing products according to the selection.'
labels: 'defect'
assignees: ''

---

**Describe the bug**

Selecting an option from the dropdown menu on the Inventory page should trigger a refresh of Inventory page and should organize all products according to the selected option. Like selecting Price (High to Low) option should sort all the products on the inventory page in orderly fashion starting from the most expensive product to the cheapest one.

**To Reproduce**

Steps to reproduce the behavior:
1. Go to 'https://www.saucedemo.com'
2. Login using standard_user credentials.
3. Verify that products are sorted Alphabetically for default selection of *Name (A to Z)*.
4. Select an option from the dropdown and verify that all products are sorted according to that option.

**Expected behavior**

Selecting an option from dropdown menu should trigger a refresh on Inventory page and all products on Inventory page should get sorted according to the selected option.

**Screenshots**

If applicable, add screenshots to help explain your problem.

**Desktop (please complete the following information):**

 - OS: Windows 10
 - Browser: Chrome
 - Version: 71

**Additional context**

Investigating the issue a bit, It seems that there are no javascript calls made while selecting an option from the dropdown menu.
