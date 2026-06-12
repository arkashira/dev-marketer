import json
import time
from dataclasses import dataclass
from typing import Dict

@dataclass
class LaunchData:
    clicks: int
    email_opens: int
    sign_ups: int
    paid_conversions: int
    source: str

class LaunchAnalytics:
    def __init__(self):
        self.data = {}

    def update_data(self, source: str, clicks: int, email_opens: int, sign_ups: int, paid_conversions: int):
        if source not in self.data:
            self.data[source] = LaunchData(clicks, email_opens, sign_ups, paid_conversions, source)
        else:
            existing_data = self.data[source]
            self.data[source] = LaunchData(
                existing_data.clicks + clicks,
                existing_data.email_opens + email_opens,
                existing_data.sign_ups + sign_ups,
                existing_data.paid_conversions + paid_conversions,
                source
            )

    def get_data(self):
        return self.data

    def get_total_clicks(self):
        return sum(data.clicks for data in self.data.values())

    def get_total_email_opens(self):
        return sum(data.email_opens for data in self.data.values())

    def get_total_sign_ups(self):
        return sum(data.sign_ups for data in self.data.values())

    def get_total_paid_conversions(self):
        return sum(data.paid_conversions for data in self.data.values())

    def get_data_by_source(self, source: str):
        return self.data.get(source)

def main():
    analytics = LaunchAnalytics()
    while True:
        # Simulate updating data every 30 seconds
        analytics.update_data('ads', 10, 5, 2, 1)
        analytics.update_data('social', 20, 10, 5, 2)
        analytics.update_data('landing page', 30, 15, 10, 5)
        print(json.dumps({
            'total_clicks': analytics.get_total_clicks(),
            'total_email_opens': analytics.get_total_email_opens(),
            'total_sign_ups': analytics.get_total_sign_ups(),
            'total_paid_conversions': analytics.get_total_paid_conversions(),
            'data_by_source': {source: {
                'clicks': data.clicks,
                'email_opens': data.email_opens,
                'sign_ups': data.sign_ups,
                'paid_conversions': data.paid_conversions
            } for source, data in analytics.get_data().items()}
        }))
        time.sleep(30)

if __name__ == '__main__':
    main()
