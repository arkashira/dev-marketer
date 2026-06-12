# REQUIREMENTS.md
## Introduction
The dev-marketer project aims to develop a simple marketing automation engine that allows users to set a monthly email limit and stops sending emails when the limit is reached. This document outlines the functional and non-functional requirements for the project.

## Functional Requirements
1. **FR-1**: The system shall allow users to create an instance of the `MarketingAutomation` class.
2. **FR-2**: The system shall provide a `send_email` method to send emails.
3. **FR-3**: The system shall provide a `display_limit_usage` method to display the current email limit usage.
4. **FR-4**: The system shall provide an `increase_limit` method to increase the email limit.
5. **FR-5**: The system shall stop sending emails when the monthly email limit is reached.
6. **FR-6**: The system shall reset the email limit usage at the start of each month.

## Non-Functional Requirements
1. **Performance**: The system shall be able to send emails at a rate of at least 10 emails per minute.
2. **Security**: The system shall ensure that user data is stored securely and in accordance with relevant data protection regulations.
3. **Reliability**: The system shall be designed to handle a minimum of 100 concurrent users without significant performance degradation.
4. **Usability**: The system shall provide a simple and intuitive API for users to interact with.

## Constraints
1. **C-1**: The system shall be developed using Python as the primary programming language.
2. **C-2**: The system shall use a relational database management system to store user data.
3. **C-3**: The system shall be designed to work with a monthly email limit, which shall be set by the user.

## Assumptions
1. **A-1**: Users shall have a valid email address and shall be authorized to send emails.
2. **A-2**: The system shall have access to a mail server to send emails.
3. **A-3**: The system shall be deployed on a cloud-based infrastructure to ensure scalability and reliability.

## Testing Requirements
1. **TR-1**: The system shall be tested using pytest to ensure that all functional requirements are met.
2. **TR-2**: The system shall be tested for performance, security, and reliability to ensure that it meets the non-functional requirements.
3. **TR-3**: The system shall be tested for usability to ensure that it provides a simple and intuitive API for users to interact with.
