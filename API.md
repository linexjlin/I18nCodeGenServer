# Project API Documentation

This documentation outlines the API endpoints provided for interacting with a project's translation data.

## Endpoints

### Get Project Data (Export)

`GET /{id}`

Fetches the export of a project's data.

#### Parameters

- `id` (path variable) - Unique identifier for the project.
- `file` (query) - The name of the export file, including its extension to determine the file type.
- `notes` (query, optional) - Translation notes to include.
- `languages` (query, optional) - Comma-separated list of languages to export.
- `template` (query, optional) - The coding lanuages template to be used for the export.

#### Response

- `FileResponse` - The exported file content for the project.

### Update Project Data

`POST /{id}`

Updates the project's data with the provided information.

#### Parameters

- `id` (path variable) - Unique identifier for the project.
- `update_data` (body) - Data containing the updates to apply to the project.

#### Response

- `message` - Confirmation message indicating the successful data update.

### Delete Project Key

`DELETE /{id}/key`

Deletes a specific key from the project's data.

#### Parameters

- `id` (path variable) - Unique identifier for the project.
- `k` (query) - The key that needs to be deleted.

#### Response

- `message` - Confirmation message indicating the key has been deleted.

### Add Project Key

`PUT /{id}/key`

Adds a new key to the project's data.

#### Parameters

- `id` (path variable) - Unique identifier for the project.
- `k` (query) - The new key to add.

#### Response

- `message` - Confirmation message indicating the key has been added.

### Add Project Translation

`PUT /{id}/translate`

Adds a translation to a specific key in the project's data.

#### Parameters

- `id` (path variable) - Unique identifier for the project.
- `k` (query) - The key to which the translation should be added.
- `l` (query) - The language code for the translation.
- `v` (query) - The translation value.

#### Response

- `message` - Confirmation message showing the translation key, language, value, and return status.

#### Example

```python
import requests

def test():
    url = "https://i18n.linkown.com/{id}/translate"
    id = "ce435723-a840-468d-a57f-0bb95cbfbcfb"
    k = "APP"
    l = "en"
    v = f"""
v
"""

    response = requests.put(url.format(id=id), params={"k": k, "l": l, "v": v})

    assert response.status_code == 200
    print("Test passed!",response.json())

test()
```

### Get Project Translation

`GET /{id}/key`

Retrieves the translation value for a specific key in a given language.

#### Parameters

- `id` (path variable) - Unique identifier for the project.
- `k` (query) - The key for which the translation is being requested.
- `l` (query) - The language code for the requested translation.

#### Response

- `result` - The translation value for the specified key and language.
```