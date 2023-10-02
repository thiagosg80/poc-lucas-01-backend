def test_analise_general(client):
    url = ('/analises?faturamento-periodo=68574.83&valor-salarios=0&valor-pro-labore=3906&valor-medio-credito-icms=0'
           '&valor-medio-credito-pis=0&valor-medio-credito-cofins=0&lucro-apurado=49240.38&cnaes=10.91-1-01,'
           '10.91-1-02,47.29-6-99,56.20-1-04&periodo-inicio=01/01/2023&periodo-fim=31/03/2023')

    response = client.get(url)
    json = response.json
    input_analise = json['input']

    assert json['lucroPresumido']['presuncaoIRPJ']['aliquota'] == 0.08
    assert input_analise['quantidadeMeses'] == 3
    assert input_analise['rbt12'] == 274299.32
