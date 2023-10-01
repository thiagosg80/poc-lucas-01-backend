from pathlib import Path

resources = Path(__file__).parent / 'resources'


def test_upload_cnpj(client):
    url = '/arquivos/upload'
    file_bytes = (resources / 'CNPJSimple.pdf').open('rb')

    request_body = {
        'file': file_bytes
    }

    response = client.post(url, data=request_body)
    json = response.json

    assert json['identificacao']['nome_fantasia'] == 'SIMPLE PRODUTOS ARTESANAIS'
