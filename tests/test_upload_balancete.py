from tests.perform_upload import perform_upload


def test_upload_balancete_periodo(client):
    json = perform_upload(client, '/arquivos/upload', 'balancete01a03_2023.pdf')
    periodo = json['input_analise']['periodo']

    assert periodo['inicio'] == '01/01/2023'
    assert periodo['fim'] == '31/03/2023'

