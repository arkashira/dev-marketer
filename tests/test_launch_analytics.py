import pytest
from launch_analytics import LaunchAnalytics, LaunchData

def test_launch_data():
    data = LaunchData(10, 5, 2, 1, 'ads')
    assert data.clicks == 10
    assert data.email_opens == 5
    assert data.sign_ups == 2
    assert data.paid_conversions == 1
    assert data.source == 'ads'

def test_launch_analytics_update_data():
    analytics = LaunchAnalytics()
    analytics.update_data('ads', 10, 5, 2, 1)
    assert analytics.get_data()['ads'].clicks == 10
    assert analytics.get_data()['ads'].email_opens == 5
    assert analytics.get_data()['ads'].sign_ups == 2
    assert analytics.get_data()['ads'].paid_conversions == 1

def test_launch_analytics_get_data():
    analytics = LaunchAnalytics()
    analytics.update_data('ads', 10, 5, 2, 1)
    analytics.update_data('social', 20, 10, 5, 2)
    assert len(analytics.get_data()) == 2

def test_launch_analytics_get_total_clicks():
    analytics = LaunchAnalytics()
    analytics.update_data('ads', 10, 5, 2, 1)
    analytics.update_data('social', 20, 10, 5, 2)
    assert analytics.get_total_clicks() == 30

def test_launch_analytics_get_total_email_opens():
    analytics = LaunchAnalytics()
    analytics.update_data('ads', 10, 5, 2, 1)
    analytics.update_data('social', 20, 10, 5, 2)
    assert analytics.get_total_email_opens() == 15

def test_launch_analytics_get_total_sign_ups():
    analytics = LaunchAnalytics()
    analytics.update_data('ads', 10, 5, 2, 1)
    analytics.update_data('social', 20, 10, 5, 2)
    assert analytics.get_total_sign_ups() == 7

def test_launch_analytics_get_total_paid_conversions():
    analytics = LaunchAnalytics()
    analytics.update_data('ads', 10, 5, 2, 1)
    analytics.update_data('social', 20, 10, 5, 2)
    assert analytics.get_total_paid_conversions() == 3

def test_launch_analytics_get_data_by_source():
    analytics = LaunchAnalytics()
    analytics.update_data('ads', 10, 5, 2, 1)
    assert analytics.get_data_by_source('ads').clicks == 10
