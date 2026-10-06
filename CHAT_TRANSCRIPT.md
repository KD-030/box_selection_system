# Box Selection System — Conversation Record

> **Record type:** AI-assisted reconstruction, not a verbatim platform export. User requests below are quoted where available; assistant responses are summarized for readability. This document records the project work and should not be mistaken for a complete, exact transcript.

## 1. Building the project

**User:** “i want to make this project make it for me”

**Assistant (summary):** Reviewed the supplied Django hiring assignment and set up a Django project with a shipping app. The app models products, boxes, orders, and order items; provides a web form for creating an order; recommends a box; includes sample data, automated tests, and setup documentation.

**Implementation notes:**
- Installed Django 4.2.30 in a project-local Python 3.9.6 virtual environment.
- Added models, form validation, the order page, admin registration, a sample-data command, and an initial test suite.
- Chose SQLite for the local development database.

## 2. Fixing duplicate order items

**User:** Reported an `IntegrityError` on order submission:

```text
UNIQUE constraint failed: shipping_orderitem.order_id, shipping_orderitem.product_id
```

**Assistant (summary):** Traced the error to the order form allowing the same product in multiple slots while the database permits only one line per product per order. Updated the form to combine repeated selections and added a regression test.

**Outcome:** The duplicate-selection test passed, and the homepage returned HTTP 200.

## 3. Improving the UI and packing rules

**User:** “- improve the design/UI, - or add more advanced box-selection rules.”

**Assistant (summary):** Updated both the interface and recommendation logic:
- Redesigned the page as a responsive warehouse packing workspace with product and box catalogues and separate success and no-fit results.
- Added a deterministic 3D placement heuristic that checks axis-aligned rotations, box boundaries, item overlap, and maximum weight.
- Ranks feasible boxes by cost, preferring the smaller-volume box when prices tie.
- Added tests for rotation, an impossible packing arrangement, weight limits, and recommendation cost.

**Outcome:** All seven shipping app tests passed. The README documents that the packing algorithm is heuristic and may miss some valid arrangements.

## 4. Removing the duplicate Laptop listing

**User:** “laptop is there twice fix it”

**Assistant (summary):** Inspected the local catalogue and found additional records left by earlier testing. Removed the duplicate Laptop, duplicate Coffee Maker, and temporary box rows, along with a temporary test order. Preserved the other orders and reloaded the page to verify the catalogue.

## 5. Publishing the project

**User:** Asked to push the project to GitHub, then provided the repository URL:

```text
https://github.com/KD-030/box_selection_system
```

**Assistant (summary):** Initialized Git inside the project folder rather than using the unrelated parent repository. Preserved the remote repository's initial README commit, committed the project, and pushed it to `main`.

**Later update:** Added `TEST_CASES.md` with seven case descriptions and screenshots for the order form, successful recommendation, and no-fit outcome. Improved `TEST_OUTPUT.md`, integrated a newer remote commit without force-pushing, and pushed the documentation and screenshots.

## 6. Preparing test documentation

**User:** Asked for test cases in Markdown, output screenshots, and an improved test output report.

**Assistant (summary):** Documented the automated cases and added three screenshots under `docs/screenshots/`. Updated the README to link to the test-case document and clarified the test run's result and command.

**Verification recorded:** `python manage.py test shipping --verbosity 2` — 7 tests passed, 0 failures. Django's system check reported no issues.

## 7. Transcript request

**User:** Asked for a professional transcript and clarified that the project was for learning, not an assignment submission.

**Assistant (summary):** Replaced an earlier inaccurate draft with this transparent, concise reconstruction. It distinguishes quoted user requests from summarized assistant actions and does not claim to be a verbatim export.

## Project references

- [Project repository](https://github.com/KD-030/box_selection_system)
- [README](README.md)
- [Test cases and screenshots](TEST_CASES.md)
- [Test output](TEST_OUTPUT.md)
