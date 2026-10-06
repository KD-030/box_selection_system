# AI-Assisted Box Selection System

This project is a small Django-based shipping recommendation system for ecommerce orders. It allows a warehouse team to enter products and quantities, then recommends the cheapest box that can safely contain the order while respecting the box dimensions and weight capacity.

## Features
- Product catalogue with dimensions and weight
- Box catalogue with internal dimensions, weight limit, and cost
- Order entry with up to three products
- Repeated selections of the same product are combined into one order line
- Automatic recommendation of the best-fitting box
- Validation for incompatible or oversized orders
- Test suite covering the core recommendation logic

## Project structure
- `shipping/models.py` – Product, Box, Order, and OrderItem models
- `shipping/views.py` – recommendation logic and page rendering
- `shipping/forms.py` – order form used to collect product choices
- `shipping/templates/shipping/index.html` – user interface
- `shipping/tests.py` – unit tests for box selection rules

## How to run locally
1. Open a terminal in the project root.
2. Activate the virtual environment:
   ```bash
   source .venv/bin/activate
   ```
3. Run migrations:
   ```bash
   python manage.py migrate
   ```
4. Seed sample data:
   ```bash
   python manage.py seed_data
   ```
5. Start the local server:
   ```bash
   python manage.py runserver
   ```
6. Visit `http://127.0.0.1:8000/` in the browser.

## Recommendation rules
The recommendation logic applies these checks:
- total product volume cannot exceed the internal box volume,
- order weight must be within the box maximum capacity,
- products may be rotated into any of their six axis-aligned orientations,
- a deterministic 3D corner-placement heuristic checks that items are in-bounds and do not overlap,
- among the boxes that pass, the system selects the lowest-cost box; ties prefer smaller volume.

The placement method is a practical heuristic, not an exhaustive solution to the 3D bin-packing problem. It will not recommend a box unless it finds a valid placement, but a valid arrangement might be missed for some complex orders.

## What I learned
- How to model product inventory and box constraints as Django models.
- How to create a recommendation algorithm that balances capacity, weight, and cost.
- How to build a simple and testable Django workflow using forms and templates.
- How to validate behavior through automated tests before considering the app complete.

## Related files
- [AI_USAGE.md](AI_USAGE.md)
- [TEST_OUTPUT.md](TEST_OUTPUT.md)

## Assignment materials to complete
- Export and include the genuine chat transcript yourself. `CHAT_TRANSCRIPT.md` is not included because it is only an AI-generated summary, not an exported transcript.
- Write your own reflection on what you learned; it is not generated or included here.

## Repository link
https://github.com/KD-030/box_selection_system
