# Test Run Output

**Result: PASS — 8 tests passed, 0 failures.**

- **Date:** 6 October 2026
- **Command:** `python manage.py test shipping --verbosity 2`
- **Environment:** Django 4.2.30, Python 3.9.6
- **Duration:** 0.036 seconds

The Django test runner creates and destroys an isolated test database for this run; it does not use the local development database.

## Terminal output

```text
Creating test database for alias 'default' ('file:memorydb_default?mode=memory&cache=shared')...
Found 8 test(s).
Operations to perform:
  Synchronize unmigrated apps: messages, staticfiles
  Apply all migrations: admin, auth, contenttypes, sessions, shipping
Synchronizing apps without migrations:
  Creating tables...
    Running deferred SQL...
Running migrations:
  Applying contenttypes.0001_initial... OK
  Applying auth.0001_initial... OK
  Applying admin.0001_initial... OK
  Applying admin.0002_logentry_remove_auto_add... OK
  Applying admin.0003_logentry_add_action_flag_choices... OK
  Applying contenttypes.0002_remove_content_type_name... OK
  Applying auth.0002_alter_permission_name_max_length... OK
  Applying auth.0003_alter_user_email_max_length... OK
  Applying auth.0004_alter_user_username_opts... OK
  Applying auth.0005_alter_user_last_login_null... OK
  Applying auth.0006_require_contenttypes_0002... OK
  Applying auth.0007_alter_validators_add_error_messages... OK
  Applying auth.0008_alter_user_username_max_length... OK
  Applying auth.0009_alter_user_last_name_max_length... OK
  Applying auth.0010_alter_group_name_max_length... OK
  Applying auth.0011_update_proxy_permissions... OK
  Applying auth.0012_alter_user_first_name_max_length... OK
  Applying sessions.0001_initial... OK
  Applying shipping.0001_initial... OK
System check identified no issues (0 silenced).
test_product_can_be_rotated_to_fit (shipping.tests.BoxRecommendationTests) ... ok
test_recommends_cheapest_box_that_can_physically_pack_order (shipping.tests.BoxRecommendationTests) ... ok
test_rejects_order_over_box_weight_limit (shipping.tests.BoxRecommendationTests) ... ok
test_rejects_order_that_fails_three_dimensional_packing (shipping.tests.BoxRecommendationTests) ... ok
test_repeated_product_selections_are_combined (shipping.tests.BoxRecommendationTests) ... ok
test_returns_none_when_no_box_can_fit (shipping.tests.BoxRecommendationTests) ... ok
test_seed_command_preserves_existing_catalogue_records (shipping.tests.BoxRecommendationTests) ... ok
test_total_weight_and_volume_are_calculated (shipping.tests.BoxRecommendationTests) ... ok

----------------------------------------------------------------------
Ran 8 tests in 0.036s

OK
Destroying test database for alias 'default' ('file:memorydb_default?mode=memory&cache=shared')...
```

For the scenario descriptions and application screenshots, see [TEST_CASES.md](TEST_CASES.md).
