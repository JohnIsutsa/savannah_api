# `Savannah API`

🚀 **Scalable Customer and Order Management System - Django Backend**

## Table of Contents

- [`Savannah API`](#savannah-api)
  - [Table of Contents](#table-of-contents)
  - [Introduction](#introduction)
  - [Features](#features)
  - [Technologies Used](#technologies-used)
  - [Setup and Installation](#setup-and-installation)
    - [Prerequisites](#prerequisites)
    - [Installation](#installation)
    - [Configuration](#configuration)
  - [Usage](#usage)
  - [API Endpoints](#api-endpoints)
  - [Authentication](#authentication)
  - [Testing](#testing)
  - [Continuous Integration and Continuous Deployment](#continuous-integration-and-continuous-deployment)
  - [Contributing](#contributing)
  - [License](#license)

## Introduction

**Savannah API** is a scalable backend application built using Django. It provides REST APIs for managing customers and orders, along with authentication and authorization using OpenID Connect. Additionally, it integrates with Twilio for sending SMS alerts to customers when orders are added.

## Features

- REST APIs for managing customers and orders
- Authentication and authorization via OpenID Connect
- Integration with Twilio for sending SMS alerts to customers
- Secure handling of sensitive data
- Unit tests with coverage checking
- Continuous Integration and Continuous Deployment (CI/CD) setup

## Technologies Used

- **Python Django:** Backend framework for building web applications
- **PostgreSQL:** Relational database for storing customer and order data
- **Twilio:** Communication API for sending SMS alerts
- **OpenID Connect:** Authentication and authorization protocol with Google

## Setup and Installation

### Prerequisites

Before you begin, ensure you have the following installed:

- Python (3.x)
- pip
- PostgreSQL or your preferred database

### Installation

1. Clone the repository:

   ```bash
   git clone <repository_url>
   cd savannah_api
   ```

2. Create and activate a virtual environment:

   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

### Configuration

1. Set up your database and configure the connection in `.env` file. Sample is provided below.

   ```plaintext
   SECRET_KEY=your_secret_key_here
   EMAIL_HOST_USER=development.nere@gmail.com
   EMAIL_HOST_PASSWORD=your_email_host_password_here
   GOOGLE_CLIENT_ID=your_google_client_id_here
   GOOGLE_CLIENT_SECRET=your_google_client_secret_here
   SOCIAL_SECRET=your_social_secret_here
   DATABASE_URL=your_database_url_here
   TWILIO_ACCOUNT_SID=your_twilio_account_sid_here
   TWILIO_AUTH_TOKEN=your_twilio_auth_token_here
   TWILIO_PHONE_NUMBER=your_twilio_phone_number_here
   ```

2. Configure any environment variables needed for your project.

## Usage

To use the Savannah API:

1. Ensure that the backend server is running by executing:

    ```bash
    python manage.py runserver
    ```

2. Access the API documentation by visiting `http://localhost:8000/docs` in your web browser. This documentation provides detailed information about all available endpoints and how to interact with them.

3. To authenticate using OpenID Connect, follow these steps to generate a token:
    - Navigate to the project directory and locate the `google.html` file.
    - Host the `google.html` file on a local server. You can use tools like Python's `http.server` module or any other web server of your choice.

      ```bash
      cd path/to/project
      python -m http.server 5500
      ```

    - Open a web browser and visit `http://localhost:5500/google.html`.
    - Follow the instructions on the page to sign in with your Google account and generate a token.
    - Copy the generated token and use it for authentication in the API requests.
    - Use the `POST api/social_auth/google` endpoint and pass the Google generated token to sign up/in and receive your access and refresh tokens.
  
4. When creaing an order an email is sent to the order recepient. The send message code block is currently commented out because the API has a cost associated to it but should work.

## API Endpoints

Explore the API endpoints and documentation by visiting `http://localhost:8000/docs` or `http://localhost:8000/redoc` after starting the backend server.

## Authentication

To authenticate using OpenID Connect, follow the steps mentioned in the [Usage](#usage) section to generate a token.

## Testing

Run unit tests:

```bash
coverage python manage.py test
```

## Continuous Integration and Continuous Deployment

This project is integrated with CircleCI for CI/CD. Upon pushing changes to the repository, CircleCI automatically triggers the build, runs tests, and deploys.

## Contributing

Contributions are welcome! Please feel free to submit a pull request or open an issue for any suggestions or improvements.

## License

This project is licensed under the [MIT License](LICENSE).
