# Text Search API

This project is a Django REST API that allows users to store paragraphs of text and perform searches based on words within those paragraphs. It utilizes Django Rest Framework for API endpoints and PostgreSQL for data storage.

## Tech Stack

- Django
- Django Rest Framework
- PostgreSQL

## Setup Instructions

### Prerequisites

- Python 3.x installed
- PostgreSQL installed and running locally

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/4d4r5h/text-search-api.git
   cd text-search-api
   ```

2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Set up PostgreSQL database:

   - Create a database named `text_search_db` (or any preferred name).
   - Update database settings in `text_search_project/settings.py`:

     ```python
     DATABASES = {
         'default': {
             'ENGINE': 'django.db.backends.postgresql',
             'NAME': 'text_search_db',
             'USER': 'your_db_user',
             'PASSWORD': 'your_db_password',
             'HOST': 'localhost',
             'PORT': '5432',
         }
     }
     ```

4. Apply migrations:

   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

5. Create a superuser for accessing Django admin:

   ```bash
   python manage.py createsuperuser
   ```

6. Run the development server:

   ```bash
   python manage.py runserver
   ```

7. The API will be accessible at `http://127.0.0.1:8000/`.

## API Endpoints and Usage

### 1. User Registration

**Endpoint:** `/api/users/`  
**Method:** `POST`  
**Description:** Register a new user.

**Request:**

```json
{
  "email": "john@example.com",
  "name": "John Doe",
  "dob": "1990-01-01",
  "password": "password123"
}
```

**Response:**

```json
{
  "id": 1,
  "email": "john@example.com",
  "name": "John Doe",
  "dob": "1990-01-01",
  "created_at": "2023-06-16T12:34:56.789Z",
  "modified_at": "2023-06-16T12:34:56.789Z"
}
```

### 2. User Login

**Endpoint:** `/api/token/`  
**Method:** `POST`  
**Description:** Obtain JWT token for authentication.

**Request:**

```json
{
  "email": "john@example.com",
  "password": "password123"
}
```

**Response:**

```json
{
  "refresh": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9...",
  "access": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9..."
}
```

### 3. Create Paragraphs

**Endpoint:** `/api/paragraphs/`  
**Method:** `POST`  
**Description:** Create new paragraphs. The text input should be separated by two newline characters (`\n\n`).

**Request:**

```text
Authorization: Bearer <access_token>
```

```json
{
  "text": "Lorem ipsum dolor sit amet.\n\nConsectetur adipiscing elit."
}
```

**Response:**

```json
{
  "paragraph_ids": [1, 2]
}
```

### 4. Search for Paragraphs

**Endpoint:** `/api/search/<word>/`  
**Method:** `GET`  
**Description:** Search for paragraphs containing the specified word.

**Request:**

```txt
Authorization: Bearer <access_token>
```

**Response:**

```json
[
  {
    "id": 1,
    "text": "Lorem ipsum dolor sit amet."
  }
]
```

### Here’s a step-by-step example of how to use the endpoints:

### Step 1: Register a User

```bash
curl -X POST http://127.0.0.1:8000/api/users/ -H "Content-Type: application/json" -d '{
  "email": "john@example.com",
  "name": "John Doe",
  "dob": "1990-01-01",
  "password": "password123"
}'
```

### Step 2: Obtain JWT Token

```bash
curl -X POST http://127.0.0.1:8000/api/token/ -H "Content-Type: application/json" -d '{
  "email": "john@example.com",
  "password": "password123"
}'
```

Copy the `access` token from the response.

### Step 3: Create Paragraphs

```bash
curl -X POST http://127.0.0.1:8000/api/paragraphs/ -H "Authorization: Bearer <access_token>" -H "Content-Type: application/json" -d '{
  "text": "Lorem ipsum dolor sit amet.\n\nConsectetur adipiscing elit."
}'
```

### Step 4: Search for Paragraphs

```bash
curl -X GET http://127.0.0.1:8000/api/search/lorem/ -H "Authorization: Bearer <access_token>"
```

This setup will allow you to register a user, log in to obtain a JWT token, create paragraphs, and search for paragraphs containing a specific word. Make sure to replace `<access_token>` with the actual JWT token obtained during the login step.

## Models

### `CustomUser`

- **Fields:**
  - `id`: Primary key
  - `email`: Email address (unique)
  - `name`: User's name
  - `dob`: Date of birth
  - `created_at`: Date when user was created
  - `modified_at`: Date when user was last modified

### `Paragraph`

- **Fields:**
  - `id`: Primary key
  - `text`: Text content of the paragraph

### `Word`

- **Fields:**
  - `id`: Primary key
  - `word`: Individual word from paragraphs (indexed)
  - `paragraph`: Foreign key to `Paragraph`, indicating which paragraph the word belongs to

## Authentication

- JWT (JSON Web Token) authentication is implemented using `djangorestframework-simplejwt`.
- Upon successful authentication (via `POST /api/token/`), the API issues an access token (`access`) and a refresh token (`refresh`).
- Access tokens are used to authenticate subsequent API requests by including them in the `Authorization` header (`Bearer <access_token>`).
- Refresh tokens are used to obtain new access tokens without requiring users to re-enter their credentials.

This setup ensures secure and efficient user authentication and API access control within the Django application.
