from pathlib import Path

resources = Path(__file__).parent / 'resources'


def test_upload_cnpj(client):
    json = __perform_upload_cnpj(client)

    assert json['identificacao']['nome_fantasia'] == 'SIMPLE PRODUTOS ARTESANAIS'


def test_upload_cnpj_atividade_principal(client):
    json = __perform_upload_cnpj(client)
    atividade_principal = json['identificacao']['atividade_principal']

    assert atividade_principal['cnae'] == '10.91-1-01'
    assert atividade_principal['descricao'] == 'Fabricação de produtos de panificação industrial'


def test_upload_cnpj_atividades_secundarias(client):
    json = __perform_upload_cnpj(client)
    atividades_secundarias = json['identificacao']['atividades_secundarias']

    assert len(atividades_secundarias) == 3
    assert atividades_secundarias[0]['cnae'] == '10.91-1-02'

    assert atividades_secundarias[0]['descricao'] == ('Fabricação de produtos de padaria e confeitaria com '
                                                      'predominância de produção própria')

    assert atividades_secundarias[1]['cnae'] == '47.29-6-99'

    assert atividades_secundarias[1]['descricao'] == ('Comércio varejista de produtos alimentícios em geral ou '
                                                      'especializado em produtos alimentícios nãoespecificados '
                                                      'anteriormente')

    assert atividades_secundarias[2]['cnae'] == '56.20-1-04'

    assert atividades_secundarias[2]['descricao'] == ('Fornecimento de alimentos preparados preponderantemente para '
                                                      'consumo domiciliar')


def __perform_upload_cnpj(client):
    url = '/arquivos/upload'
    file_bytes = (resources / 'CNPJSimple.pdf').open('rb')

    request_body = {
        'file': file_bytes
    }

    response = client.post(url, data=request_body)

    return response.json
