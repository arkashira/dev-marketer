import re
import datetime
from dev_marketer import launch_product


def test_launch_structure():
    result = launch_product("My Awesome Product")
    # Top‑level keys
    expected_keys = {
        "product_name",
        "landing_page_url",
        "landing_page_copy",
        "email_list_id",
        "welcome_email",
        "scheduled_posts",
    }
    assert set(result.keys()) == expected_keys
    assert result["product_name"] == "My Awesome Product"


def test_landing_page_url():
    result = launch_product("Cool App")
    url = result["landing_page_url"]
    # Expected pattern: https://<slug>.dev-marketer.axentx.com
    pattern = r"^https://cool-app\.dev-marketer\.axentx\.com$"
    assert re.match(pattern, url)


def test_email_list_id_format():
    result = launch_product("Test Product")
    list_id = result["email_list_id"]
    assert re.fullmatch(r"list_\d{1,5}", list_id)


def test_welcome_email_contains_product_name():
    name = "SuperTool"
    result = launch_product(name)
    email = result["welcome_email"]
    assert name in email
    assert email.startswith("Subject: Welcome to")


def test_scheduled_posts():
    name = "Demo"
    result = launch_product(name)
    posts = result["scheduled_posts"]
    assert len(posts) == 7

    today = datetime.date.today()
    for i, post in enumerate(posts):
        # Platform alternates
        expected_platform = "Twitter" if i % 2 == 0 else "LinkedIn"
        assert post["platform"] == expected_platform

        # Content includes product name and landing page URL
        assert name in post["content"]
        assert result["landing_page_url"] in post["content"]

        # Date is tomorrow + i days
        expected_date = today + datetime.timedelta(days=i + 1)
        assert post["scheduled_date"] == expected_date.isoformat()
