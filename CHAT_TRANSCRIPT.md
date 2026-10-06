# Box Selection System — Conversation Recap

## 1. Project setup

User: “I need to build a Django-based system that recommends the best shipping box for an order. Each product has dimensions and weight, and each box has internal dimensions, maximum weight capacity, and cost. I want to keep the design clean and scalable. Where should I begin?”

Assistant: Given the attached Django hiring assignment, I have created a Django project with a shipping application. The app contains models of products, boxes, orders, and order items; implements a webpage for creating the order; recommends a box for shipping; prepares test data, runs automated tests, and provides setup instructions.



Implementation details:
I have added models, form validation, the order page, admin interface, a sample-data command, and some tests. For this development stage, I have used SQLite as the default database.

## 2.Models and relationships

User: That makes sense. What should the main models look like?

Implementation details : I’d recommend four core models:

Product
Box
Order
OrderItem
The idea is:

Product stores a product’s dimensions and weight
Box stores a box’s internal dimensions, max weight, and cost
Order represents a customer order
OrderItem links an order to one or more products with a quantity
This is clean and normalized, which is what we want for a small but robust Django app.

## 3. Fixing duplicate items



User: After submitting the form, I received an error
```python
UNIQUE constraint failed: shipping_orderitem.order_id, shipping_orderitem.product_id

```
Assistant: This error occurs because the database does not allow multiple entries of the same product in one order, but the form allows choosing the same product in different slots. I have fixed this issue by adjusting the form and made a test for this scenario.


Implementation details:
The order form now combines selections of the same product, and the test verifies that the submission of multiple identical items is handled correctly. This test, along with others, passed, and the page began to return HTTP 200.


## 4 Logic

User: That’s good. Should I keep the logic in the same app or split it further?

Implementation details: For a small project, one shipping app is enough. You do not need to over-engineer it. Keep it simple and explicit. The shipping app contains the following files:

models.py
serializers.py
views.py
services.py
tests.py
urls.py
This is a standard Django structure and keeps the code easy to follow.


## 4. Enhancing the design and selection rules



User: “- improve the design/UI,
-or-
add more advanced box-selection rules.”



Assistant: I have enhanced the UI and improved the recommendation rules. Specifically,



Implementation details:
I have implemented the warehouse packing interface where the user can choose products and boxes and see the results of fitting. The design is now suitable for a real application with product and box catalogues and separate sections for success and no-fit cases. The recommendation algorithm fits items with a 3D packing heuristic: it tries to rotate the boxes to fit their items along each axis, check boundaries, item intersections, and weight limits. The boxes are ranked by cost and, in case of a tie, by volume. I have added rotation tests, a test for impossible packing, a test for weight limits, and a test for recommendation costs. All shipping app tests passed.



The README file now describes the project, and the packing algorithm is heuristic, so it may fail some test cases.



## 5. Resolving the Laptop duplication



User: “laptop is there twice fix it”

Assistant: I have inspected the local catalogue and resolved the duplication by deleting the extra Laptop, Coffee Maker, boxes, and a test order. Other orders are intact, and the page is reloaded.



## 6. Deployment



User: I’ve finished building the Django app for the shipping box recommendation system. I need to deploy it for production. What is the best way to prepare the project for deployment?

Implementation details: The best production setup for a Django app usually includes:

A production-grade web server such as Gunicorn
A reverse proxy like Nginx
A PostgreSQL database
Environment variables for secrets and configuration
Static file handling with WhiteNoise or a dedicated CDN
A secure DEBUG = False setting
Proper ALLOWED_HOSTS and CSRF configuration
A process manager such as systemd or Docker
For a small production deployment, the simplest strong setup is:

Gunicorn + Nginx + PostgreSQL + environment variables
Optional: Docker for easier deployment and consistency
Optional: GitHub Actions for CI/CD




```url



https://github.com/KD-030/box_selection_system



```



Assistant: Having noted your request, I have initialized the git repository in the project directory instead of the parent one. I have kept the remote repo’s initial README commit and pushed the project files to the main branch.




## 6. Test description



User: Provide test cases in markdown, output screenshots, and improve the test output description.



Assistant: I have described the automated test cases in markdown and added three screenshots to the docs/screenshots directory. I have improved the test_output.md description, updated the README, and explained the results and the test command.



Verification results:



```python



python manage.py test shipping --verbosity 2



```



The test suite has 7 tests, and all of them have passed. Furthermore, Django’s system check did not report any issues.




## Project files



- Project repository: [box_selection_system repo](https://github.com/KD-030/box_selection_system)



- README: [README.md](README.md)



- Test cases with screenshots: [TEST_CASES.md](TEST_CASES.md)



- Automated test results: [TEST_OUTPUT.md](TEST_OUTPUT.md)

Want a second opinion?