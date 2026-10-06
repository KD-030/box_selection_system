# AI Usage

## Tool used
- GitHub Copilot SDK in VS Code.

## Prompts and requests
The user asked for the assignment project to be built, shared an `IntegrityError` from duplicate order items, requested a UI redesign and more advanced box-selection rules, and reported that Laptop appeared twice in the catalogue.

## AI output used
- Django project and shipping-app scaffolding.
- Product, box, order, and order-item models, plus the order form and page.
- A recommendation heuristic that checks rotation, weight, and non-overlapping 3D placements.
- Regression tests and the responsive interface.

## Output changed or rejected
- Repeated selections of one product are combined before saving to avoid violating the order-item uniqueness constraint.
- The initial recommendation approach was replaced with a three-dimensional placement heuristic and tested against rotation, weight, and impossible-packing cases.
- Temporary duplicate catalogue rows were removed from the local database.
- An AI-generated summary was initially saved as `CHAT_TRANSCRIPT.md`. It is not a genuine exported transcript and must not be submitted as one; it is excluded from the GitHub commit.

## Verification
- Ran `python manage.py migrate`.
- Ran `python manage.py test shipping --verbosity 2`; all 7 tests passed.
- Opened the running local app and confirmed the homepage loads.
- Reloaded the catalogue after cleanup and confirmed Laptop appears once.

## Author review
AI-assisted code should be reviewed and understood by the author before submission. The algorithm is heuristic and may fail to find some valid 3D packing layouts.
