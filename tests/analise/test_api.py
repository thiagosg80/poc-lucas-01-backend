def test_aliquota_lucro_presumido(client):
    url = ('/analises?faturamento-periodo=68574.83&valor-salarios=0&valor-pro-labore=3906&valor-medio-credito-icms=0'
           '&valor-medio-credito-pis=0&valor-medio-credito-cofins=0&lucro-apurado=49240.38')

    response = client.get(url)
    json = response.json

    assert json['lucroPresumido']['presuncaoIRPJ']['aliquota'] == 0.08
