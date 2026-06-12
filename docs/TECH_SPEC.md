# Technical Specification
## Overview
The dev-marketer project is a marketing automation engine designed to manage and limit the number of emails sent to users. The engine provides a simple and efficient way to automate email marketing campaigns while preventing excessive emailing.

## Architecture Overview
The dev-marketer engine consists of the following components:

* **MarketingAutomation Class**: This is the core component of the engine, responsible for managing email limits and sending emails.
* **Email Service**: This component handles the actual sending of emails.
* **Limit Tracker**: This component keeps track of the current email limit usage.

## Components
### MarketingAutomation Class
This class provides the following methods:

* **`__init__`**: Initializes the marketing automation engine with a monthly email limit.
* **`send_email`**: Sends an email to a user if the email limit has not been reached.
* **`display_limit_usage`**: Displays the current email limit usage.
* **`increase_limit`**: Increases the email limit.

### Email Service
This component is responsible for sending emails. It can be implemented using a variety of email services such as SMTP or email APIs.

### Limit Tracker
This component keeps track of the current email limit usage. It can be implemented using a database or a simple counter.

## Data Model
The dev-marketer engine uses the following data model:

* **Email**: Represents an email sent to a user.
	+ **id**: Unique identifier for the email.
	+ **user_id**: Identifier for the user who received the email.
	+ **sent_at**: Timestamp when the email was sent.
* **Limit**: Represents the email limit for a user.
	+ **id**: Unique identifier for the limit.
	+ **user_id**: Identifier for the user who owns the limit.
	+ **monthly_limit**: The monthly email limit for the user.
	+ **current_usage**: The current email limit usage for the user.

## Key APIs/Interfaces
The dev-marketer engine provides the following APIs:

* **`send_email`**: Sends an email to a user if the email limit has not been reached.
	+ **Parameters**: `user_id`, `email_content`
	+ **Returns**: `True` if the email was sent successfully, `False` otherwise.
* **`display_limit_usage`**: Displays the current email limit usage for a user.
	+ **Parameters**: `user_id`
	+ **Returns**: The current email limit usage for the user.
* **`increase_limit`**: Increases the email limit for a user.
	+ **Parameters**: `user_id`, `new_limit`
	+ **Returns**: `True` if the limit was increased successfully, `False` otherwise.

## Tech Stack
The dev-marketer engine is built using the following technologies:

* **Python**: The programming language used to implement the engine.
* **Pytest**: The testing framework used to test the engine.

## Dependencies
The dev-marketer engine depends on the following libraries:

* **`pytest`**: The testing framework used to test the engine.

## Deployment
The dev-marketer engine can be deployed as a standalone application or as a service within a larger application. The engine can be deployed on a variety of platforms, including cloud platforms such as AWS or Google Cloud.

## Testing
The dev-marketer engine is tested using Pytest. The tests cover the following scenarios:

* **Test sending an email**: Tests that an email can be sent successfully when the email limit has not been reached.
* **Test displaying limit usage**: Tests that the current email limit usage can be displayed correctly.
* **Test increasing the limit**: Tests that the email limit can be increased successfully.

To run the tests, use the following command:
```bash
pytest
```
