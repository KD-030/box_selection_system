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

## Deploy a free demo on Render

The repository includes a [`render.yaml`](render.yaml) Blueprint for a free Render web service and PostgreSQL database.

1. Push this repository to GitHub.
2. Sign in to [Render](https://dashboard.render.com/), open [Blueprints](https://dashboard.render.com/blueprints), and choose **New Blueprint Instance**.
3. Connect `KD-030/box_selection_system` and apply the Blueprint. Render will create the web service and database, generate a `SECRET_KEY`, and deploy the app.
4. Open the service's `onrender.com` URL after the deploy succeeds. Sample catalogue data is added only when the product or box catalogue is empty; existing records are preserved on later deploys.
5. To create an admin account, open the web service's Shell in Render and run `python manage.py createsuperuser`.

This is a free demo configuration, not a production setup: Render free web services can spin down when idle, and Render's free PostgreSQL databases expire 30 days after creation. After expiration, the database is inaccessible unless upgraded; Render deletes it after the 14-day grace period. Do not store important or irreplaceable data there. See [Render's free-instance limitations](https://render.com/docs/free) and [Django deployment guide](https://render.com/docs/deploy-django).

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
- [TEST_CASES.md](TEST_CASES.md)
- [TEST_OUTPUT.md](TEST_OUTPUT.md)

## Assignment materials to complete
- `CHAT_TRANSCRIPT.md` is an AI-assisted reconstruction, not a verbatim export of the conversation.
- Write your own reflection on what you learned; it is not generated or included here.

## Repository link
https://github.com/KD-030/box_selection_system
