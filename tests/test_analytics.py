import time
import pytest
from analytics import AnalyticsEngine, needs_update, ALLOWED_EVENT_TYPES


def test_needs_update_true():
    last = time.time() - 31  # 31 seconds ago
    assert needs_update(last) is True


def test_needs_update_false():
    last = time.time() - 10  # 10 seconds ago
    assert needs_update(last) is False


def test_record_event_happy_path():
    eng = AnalyticsEngine()
    eng.record_event("ads", "click", 5)
    eng.record_event("social", "signup", 2)
    snap = eng.snapshot()
    assert snap["total"]["click"] == 5
    assert snap["total"]["signup"] == 2
    assert snap["by_source"]["ads"]["click"] == 5
    assert snap["by_source"]["social"]["signup"] == 2


def test_record_event_invalid_type():
    eng = AnalyticsEngine()
    with pytest.raises(ValueError) as exc:
        eng.record_event("ads", "invalid_event")
    assert "Unsupported event type" in str(exc.value)


def test_record_event_negative_count():
    eng = AnalyticsEngine()
    with pytest.raises(ValueError) as exc:
        eng.record_event("ads", "click", -1)
    assert "count must be non‑negative" in str(exc.value)


def test_snapshot_aggregates_multiple_sources():
    eng = AnalyticsEngine()
    # source A
    eng.record_event("ads", "click", 10)
    eng.record_event("ads", "email_open", 4)
    # source B
    eng.record_event("social", "click", 3)
    eng.record_event("social", "paid_conversion", 1)

    snap = eng.snapshot()
    # totals
    assert snap["total"]["click"] == 13
    assert snap["total"]["email_open"] == 4
    assert snap["total"]["paid_conversion"] == 1
    # per source
    assert snap["by_source"]["ads"]["click"] == 10
    assert snap["by_source"]["ads"]["email_open"] == 4
    assert snap["by_source"]["social"]["click"] == 3
    assert snap["by_source"]["social"]["paid_conversion"] == 1


def test_compare_with_api_within_tolerance():
    eng = AnalyticsEngine()
    eng.record_event("ads", "click", 100)
    eng.record_event("ads", "signup", 20)

    api_data = {
        "total": {"click": 102, "signup": 19, "email_open": 0, "paid_conversion": 0},
        "by_source": {
            "ads": {"click": 101, "signup": 21, "email_open": 0, "paid_conversion": 0}
        },
    }

    # Differences are <=2% -> within default 5%
    assert eng.compare_with_api(api_data) is True


def test_compare_with_api_outside_tolerance():
    eng = AnalyticsEngine()
    eng.record_event("ads", "click", 100)

    api_data = {
        "total": {"click": 80, "email_open": 0, "signup": 0, "paid_conversion": 0},
        "by_source": {"ads": {"click": 80, "email_open": 0, "signup": 0, "paid_conversion": 0}},
    }

    # 20% diff exceeds 5% tolerance
    assert eng.compare_with_api(api_data) is False


def test_compare_with_api_missing_source_treated_as_zero():
    eng = AnalyticsEngine()
    # No internal data for "landing"
    api_data = {
        "total": {"click": 0, "email_open": 0, "signup": 0, "paid_conversion": 0},
        "by_source": {"landing": {"click": 5, "email_open": 0, "signup": 0, "paid_conversion": 0}},
    }
    # Since internal is zero and external is non‑zero, diff = 1 > tolerance
    assert eng.compare_with_api(api_data) is False
