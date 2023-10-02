from pathlib import Path

resources = Path(__file__).parent / 'resources'


def perform_upload(client, url, file_name):
    file_bytes = (resources / file_name).open('rb')

    request_body = {
        'file': file_bytes
    }

    response = client.post(url, data=request_body)

    return response.json
