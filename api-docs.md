## Notely - REST API Documentation

This document provides an overview of the Notely REST API, which allows you to create, manage, and organize notes.

### Authentication

The Notely API uses JSON Web Tokens (JWT) for authentication. You will need to obtain a token before you can perform any operations. To obtain a token, send a POST request to `/api/auth/login` with your username and password.

**Example:**

```bash
POST /api/auth/login HTTP/1.1
Content-Type: application/json

{
  "username": "alivaliyev",
  "password": "1234"
}
```

**Response:**

```json
{
  "token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6ImpvaG5kb2UiLCJleHAiOjE2NzM2MzA3MTd9.z9g1-507hZ4w6g448tO752v07d8q288yE4c31098"
}
```

Store the returned token in a secure location and include it in the `Authorization` header of all subsequent requests.

**Example:**

```bash
GET /api/notes HTTP/1.1
Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6ImpvaG5kb2UiLCJleHAiOjE2NzM2MzA3MTd9.z9g1-507hZ4w6g448tO752v07d8q288yE4c31098
```

### Endpoints

Here is a summary of some of the available API endpoints:

| Endpoint             | HTTP Method | Description                                                 |
|--------------------|--------------|---------------------------------------------------------------|
| /api/notes        | GET          | Retrieves a list of all notes for the authenticated user.     |
| /api/notes/{id}   | GET          | Retrieves a specific note by its ID.                        |
| /api/notes        | POST         | Creates a new note.                                        |
| /api/notes/{id}   | PUT          | Updates an existing note.                                   |
| /api/notes/{id}   | DELETE       | Deletes a note by its ID.                                     |
| /api/categories   | GET          | Retrieves a list of all categories.                          |
| /api/categories   | POST         | Creates a new category.                                    |
| /api/categories/{id}   | PUT          | Updates an existing category.                              |
| /api/categories/{id}   | DELETE       | Deletes a category by its ID.                               |

## /api/notes GET

This API endpoint retrieves a list of all notes for the currently authenticated user.

### Request

**HTTP method:** GET

**URL:** `/api/notes`

**Headers:**

* **Authorization:** Bearer `<JWT token>` (required)

**Parameters:**

* **page (optional):** The page number of the results to be returned. Defaults to 1.
* **limit (optional):** The number of results per page. Defaults to 10.
* **category_id (optional):** Filter notes by a specific category ID.
* **completed (optional):** Filter notes by completion status (True for completed, False for incomplete).

### Response

The response will be a JSON object with the following structure:

```json
{
  "count": 10, // Total number of notes
  "next": null, // URL for next page (if available)
  "previous": null, // URL for previous page (if available)
  "results": [
    {
      "id": 1,
      "title": "My first note",
      "content": "This is the content of my first note.",
      "category_id": 1,
      "completed": false,
      "created_at": "2023-12-12T20:39:00Z",
      "updated_at": "2023-12-12T20:39:00Z"
    },
    // ... other notes
  ]
}
```

* `count`: The total number of notes for the authenticated user.
* `next`: The URL for the next page of results (if available). This will be null if there are no more pages.
* `previous`: The URL for the previous page of results (if available). This will be null if there is no previous page.
* `results`: A list of note objects. Each object will contain the following information:
    * `id`: The unique identifier of the note.
    * `title`: The title of the note.
    * `content`: The content of the note.
    * `category_id`: The ID of the category the note belongs to (if any).
    * `completed`: A boolean flag indicating whether the note is completed or not.
    * `created_at`: The date and time the note was created.
    * `updated_at`: The date and time the note was last updated.

This response indicates that the user has 10 notes in total. The returned page contains the first 10 notes. There are no more pages of results available. Each note object contains information about the note's title, content, category, completion status, and creation/update timestamps.

## /api/notes/{id} GET

This API endpoint retrieves a specific note by its unique ID.

### Request

**HTTP method:** GET

**URL:** `/api/notes/{id}`

**Headers:**

* **Authorization:** Bearer `<JWT token>` (required)

**Path Parameters:**

* `{id}`: The unique identifier of the note.

### Response

The response will be a JSON object containing the following information about the requested note:

```json
{
  "id": 1,
  "title": "My first note",
  "content": "This is the content of my first note.",
  "category_id": 1,
  "completed": false,
  "created_at": "2023-12-12T20:39:00Z",
  "updated_at": "2023-12-12T20:39:00Z"
}
```

* `id`: The unique identifier of the note.
* `title`: The title of the note.
* `content`: The content of the note.
* `category_id`: The ID of the category the note belongs to (if any).
* `completed`: A boolean flag indicating whether the note is completed or not.
* `created_at`: The date and time the note was created.
* `updated_at`: The date and time the note was last updated.

### Error Codes

* **404 Not Found:** If the specified note ID does not exist.
* **401 Unauthorized:** If the request is unauthorized (missing or invalid JWT token).

### Example

**Request:**

```bash
GET /api/notes/1 HTTP/1.1
Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6ImpvaG5kb2UiLCJleHAiOjE2NzM2MzA3MTd9.z9g1-507hZ4w6g448tO752v07d8q288yE4c31098
```

**Response:**

```json
{
  "id": 1,
  "title": "My first note",
  "content": "This is the content of my first note.",
  "category_id": 1,
  "completed": false,
  "created_at": "2023-12-12T20:39:00Z",
  "updated_at": "2023-12-12T20:39:00Z"
}
```

## /api/notes POST

This API endpoint creates a new note for the authenticated user.

### Request

**HTTP method:** POST

**URL:** `/api/notes`

**Headers:**

* **Authorization:** Bearer `<JWT token>` (required)
* **Content-Type:** application/json (required)

**Body:**

The request body should be a JSON object with the following properties:

```json
{
  "title": "string", // required
  "content": "string", // optional
  "category_id": integer, // optional
}
```

* `title`: The title of the new note (required).
* `content`: The content of the new note (optional).
* `category_id`: The ID of the category the note belongs to (optional).

**Example Request:**

```bash
POST /api/notes HTTP/1.1
Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6ImpvaG5kb2UiLCJleHAiOjE2NzM2MzA3MTd9.z9g1-507hZ4w6g448tO752v07d8q288yE4c31098
Content-Type: application/json

{
  "title": "Buy groceries",
  "content": "- Milk\n- Bread\n- Eggs",
  "category_id": 2
}
```

### Response

The response will be a JSON object containing information about the newly created note:

```json
{
  "id": 1,
  "title": "Buy groceries",
  "content": "- Milk\n- Bread\n- Eggs",
  "category_id": 2,
  "completed": false,
  "created_at": "2023-12-12T20:40:00Z",
  "updated_at": "2023-12-12T20:40:00Z"
}
```

* `id`: The unique identifier of the newly created note.
* `title`: The title of the note.
* `content`: The content of the note.
* `category_id`: The ID of the category the note belongs to (if any).
* `completed`: A boolean flag indicating whether the note is completed or not.
* `created_at`: The date and time the note was created.
* `updated_at`: The date and time the note was last updated.

### Error Codes

* **400 Bad Request:** If the request body is invalid or missing required fields.
* **401 Unauthorized:** If the request is unauthorized (missing or invalid JWT token).

## /api/notes/{id} PUT

This API endpoint updates an existing note for the authenticated user.

**Request**

**HTTP method:** PUT

**URL:** `/api/notes/{id}`

**Headers:**

* **Authorization:** Bearer `<JWT token>` (required)
* **Content-Type:** application/json (required)

**Path Parameters:**

* `{id}`: The unique identifier of the note to be updated.

**Body:**

The request body should be a JSON object containing the properties you want to update. You can provide any of the following properties:

* `title`: string (optional)
* `content`: string (optional)
* `category_id`: integer (optional)
* `completed`: boolean (optional)

**Example Request:**

```bash
PUT /api/notes/1 HTTP/1.1
Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6ImpvaG5kb2UiLCJleHAiOjE2NzM2MzA3MTd9.z9g1-507hZ4w6g448tO752v07d8q288yE4c31098
Content-Type: application/json

{
  "title": "Updated note title",
  "completed": true
}
```

**Note:** You only need to provide the properties you want to update. If a property is not included in the request body, it will not be updated.

### Response

The response will be a JSON object containing information about the updated note:

```json
{
  "id": 1,
  "title": "Updated note title",
  "content": "- Milk\n- Bread\n- Eggs",
  "category_id": 2,
  "completed": true,
  "created_at": "2023-12-12T20:40:00Z",
  "updated_at": "2023-12-12T21:00:00Z"
}
```

* `id`: The unique identifier of the updated note.
* `title`: The updated title of the note.
* `content`: The content of the note (unchanged if not provided).
* `category_id`: The ID of the category the note belongs to (unchanged if not provided).
* `completed`: The updated completion status of the note.
* `created_at`: The date and time the note was created.
* `updated_at`: The updated date and time the note was last updated.

### Error Codes

* **400 Bad Request:** If the request body is invalid or missing required fields.
* **401 Unauthorized:** If the request is unauthorized (missing or invalid JWT token).
* **404 Not Found:** If the specified note ID does not exist.

## /api/notes/{id} DELETE

This API endpoint deletes a specific note by its unique ID.

**Request**

**HTTP method:** DELETE

**URL:** `/api/notes/{id}`

**Headers:**

* **Authorization:** Bearer `<JWT token>` (required)

**Path Parameters:**

* `{id}`: The unique identifier of the note to be deleted.

**Response:**

The response will be an empty body with status code 204 No Content.

**Example:**

```bash
DELETE /api/notes/1 HTTP/1.1
Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6ImpvaG5kb2UiLCJleHAiOjE2NzM2MzA3MTd9.z9g1-507hZ4w6g448tO752v07d8q288yE4c31098
```

**Response:**

```bash
HTTP/1.1 204 No Content
```

**Error Codes:**

* **404 Not Found:** If the specified note ID does not exist.
* **401 Unauthorized:** If the request is unauthorized (missing or invalid JWT token).

**Note:** Once a note is deleted, it cannot be recovered. Use this endpoint with caution.

## /api/notes/{id}/complete PUT

This API endpoint allows you to update the completion status of a specific note.

### Request

**HTTP method:** PUT

**URL:** `/api/notes/{id}/complete`

**Headers:**

- **Authorization:** Bearer `<JWT token>` (required)
- **Content-Type:** application/json (required)

**Path Parameters:**

- `{id}`: The unique identifier of the note to be updated.

**Body:**

The request body should be a JSON object containing the property you want to update:

```json
{
  "completed": true // required
}
```

- `completed`: A boolean indicating whether the note is completed or not (required).

**Example Request:**

```bash
PUT /api/notes/1/complete HTTP/1.1
Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6ImpvaG5kb2UiLCJleHAiOjE2NzM2MzA3MTd9.z9g1-507hZ4w6g448tO752v07d8q288yE4c31098
Content-Type: application/json

{
  "completed": true
}
```

### Response

The response will be a JSON object containing information about the updated note:

```json
{
  "id": 1,
  "title": "Updated note title",
  "content": "- Milk\n- Bread\n- Eggs",
  "category_id": 2,
  "completed": true,
  "created_at": "2023-12-12T20:40:00Z",
  "updated_at": "2023-12-12T21:15:00Z"
}
```

- `id`: The unique identifier of the updated note.
- `title`: The updated title of the note.
- `content`: The content of the note (unchanged if not provided).
- `category_id`: The ID of the category the note belongs to (unchanged if not provided).
- `completed`: The updated completion status of the note.
- `created_at`: The date and time the note was created.
- `updated_at`: The updated date and time the note was last updated.

### Error Codes

- **400 Bad Request:** If the request body is invalid or missing required fields.
- **401 Unauthorized:** If the request is unauthorized (missing or invalid JWT token).
- **404 Not Found:** If the specified note ID does not exist.

**Note:** You only need to provide the `completed` property in the request body. If the property is not included, the note's completion status will not be updated.

## /api/categories GET

This API endpoint retrieves a list of all categories available in the system.

**Request**

**HTTP method:** GET

**URL:** `/api/categories`

**Headers:**

* **Authorization:** Bearer `<JWT token>` (required)

**Parameters:**

* None

**Response**

The response will be a JSON object containing an array of category objects. Each object will contain the following information:

```json
[
  {
    "id": 1,
    "name": "Personal",
    "created_at": "2023-12-12T20:00:00Z",
    "updated_at": "2023-12-12T20:00:00Z"
  },
  {
    "id": 2,
    "name": "Work",
    "created_at": "2023-12-12T20:01:00Z",
    "updated_at": "2023-12-12T20:01:00Z"
  },
  // ... more categories
]
```

* `id`: The unique identifier of the category.
* `name`: The name of the category.
* `created_at`: The date and time the category was created.
* `updated_at`: The date and time the category was last updated.

**Example**

**Request:**

```bash
GET /api/categories HTTP/1.1
Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6ImpvaG5kb2UiLCJleHAiOjE2NzM2MzA3MTd9.z9g1-507hZ4w6g448tO752v07d8q288yE4c31098
```

**Response:**

```json
[
  {
    "id": 1,
    "name": "Personal",
    "created_at": "2023-12-12T20:00:00Z",
    "updated_at": "2023-12-12T20:00:00Z"
  },
  {
    "id": 2,
    "name": "Work",
    "created_at": "2023-12-12T20:01:00Z",
    "updated_at": "2023-12-12T20:01:00Z"
  },
  // ... more categories
]
```

## /api/categories POST

This API endpoint creates a new category.

**Request:**

**HTTP method:** POST

**URL:** `/api/categories`

**Headers:**

* **Authorization:** Bearer `<JWT token>` (required)
* **Content-Type:** application/json (required)

**Body:**

The request body should be a JSON object with the following property:

```json
{
  "name": "string" // required
}
```

* `name`: The name of the new category (required).

**Example Request:**

```bash
POST /api/categories HTTP/1.1
Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6ImpvaG5kb2UiLCJleHAiOjE2NzM2MzA3MTd9.z9g1-507hZ4w6g448tO752v07d8q288yE4c31098
Content-Type: application/json

{
  "name": "Shopping"
}
```

**Response:**

The response will be a JSON object containing information about the newly created category:

```json
{
  "id": 1,
  "name": "Shopping",
  "created_at": "2023-12-12T21:05:00Z",
  "updated_at": "2023-12-12T21:05:00Z"
}
```

* `id`: The unique identifier of the newly created category.
* `name`: The name of the category.
* `created_at`: The date and time the category was created.
* `updated_at`: The date and time the category was last updated.

**Error Codes:**

* **400 Bad Request:** If the request body is invalid or missing required fields.
* **401 Unauthorized:** If the request is unauthorized (missing or invalid JWT token).

## /api/categories/{id} PUT

This API endpoint updates an existing category.

**Request:**

**HTTP method:** PUT

**URL:** `/api/categories/{id}`

**Headers:**

* **Authorization:** Bearer `<JWT token>` (required)
* **Content-Type:** application/json (required)

**Path Parameters:**

* `{id}`: The unique identifier of the category to be updated.

**Body:**

The request body should be a JSON object containing the property you want to update:

```json
{
  "name": "string" // required
}
```

* `name`: The updated name of the category (required).

**Example Request:**

```bash
PUT /api/categories/1 HTTP/1.1
Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6ImpvaG5kb2UiLCJleHAiOjE2NzM2MzA3MTd9.z9g1-507hZ4w6g448tO752v07d8q288yE4c31098
Content-Type: application/json

{
  "name": "Groceries"
}
```

**Response:**

The response will be a JSON object containing information about the updated category:

```json
{
  "id": 1,
  "name": "Groceries",
  "created_at": "2023-12-12T21:05:00Z",
  "updated_at": "2023-12-12T21:10:00Z"
}
```

* `id`: The unique identifier of the updated category.
* `name`: The updated name of the category.
* `created_at`: The date and time the category was created.
* `updated_at`: The updated date and time the category was last updated.

**Error Codes:**

* **400 Bad Request:** If the request body is invalid or missing required fields.
* **401 Unauthorized:** If the request is unauthorized (missing or invalid JWT token).
* **404 Not Found:** If the specified category ID does not exist.

## /api/categories/{id} DELETE

This API endpoint deletes a category by its unique ID.

**Request:**

**HTTP method:** DELETE

**URL:** `/api/categories/{id}`

**Headers:**

* **Authorization:** Bearer `<JWT token>` (required)

**Path Parameters:**

* `{id}`: The unique identifier of the category to be deleted.

**Response:**

The response will be an empty body with status code 204 No Content.

**Example:**

```bash
DELETE /api/categories/1 HTTP/1.1
Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6ImpvaG5kb2UiLCJleHAiOjE2NzM2MzA3MTd9.z9g1-507hZ4w6g448tO752v07d8q288yE4c31098
```

**Response:**

```bash
HTTP/1.1 204 No Content
```

**Error Codes:**

* **404 Not Found:** If the specified category ID does not exist.
* **401 Unauthorized:** If the request is unauthorized (missing or invalid JWT token).

**Note:** Deleting a category will also delete all notes associated with that category. Use this endpoint with caution.
