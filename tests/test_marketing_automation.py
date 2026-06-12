from marketing_automation import MarketingAutomation

def test_send_email():
    ma = MarketingAutomation()
    ma.send_email()
    assert ma.emails_sent == 1

def test_send_email_limit_reached():
    ma = MarketingAutomation(email_limit=1, emails_sent=1)
    ma.send_email()
    assert ma.limit_reached

def test_display_limit_usage():
    ma = MarketingAutomation(email_limit=100, emails_sent=50)
    ma.display_limit_usage()

def test_increase_limit():
    ma = MarketingAutomation(email_limit=100)
    ma.increase_limit(200)
    assert ma.email_limit == 200

def test_save_and_load_state():
    ma = MarketingAutomation(email_limit=100, emails_sent=50)
    ma.save_state('state.json')
    loaded_ma = MarketingAutomation.load_state('state.json')
    assert loaded_ma.email_limit == 100
    assert loaded_ma.emails_sent == 50
