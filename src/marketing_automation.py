import json
from dataclasses import dataclass
from datetime import datetime

@dataclass
class MarketingAutomation:
    email_limit: int = 5000
    emails_sent: int = 0
    limit_reached: bool = False

    def send_email(self):
        if self.limit_reached:
            print("Warning: Email limit reached.")
            return
        if self.emails_sent < self.email_limit:
            self.emails_sent += 1
            print(f"Email sent. Remaining limit: {self.email_limit - self.emails_sent}")
        else:
            self.limit_reached = True
            print("Warning: Email limit reached.")

    def display_limit_usage(self):
        print(f"Email limit usage: {self.emails_sent}/{self.email_limit}")

    def increase_limit(self, new_limit):
        self.email_limit = new_limit
        print(f"Email limit increased to {self.email_limit}")

    def save_state(self, filename):
        with open(filename, 'w') as f:
            json.dump({
                'email_limit': self.email_limit,
                'emails_sent': self.emails_sent,
                'limit_reached': self.limit_reached
            }, f)

    @classmethod
    def load_state(cls, filename):
        try:
            with open(filename, 'r') as f:
                state = json.load(f)
                return cls(
                    email_limit=state['email_limit'],
                    emails_sent=state['emails_sent'],
                    limit_reached=state['limit_reached']
                )
        except FileNotFoundError:
            return cls()
