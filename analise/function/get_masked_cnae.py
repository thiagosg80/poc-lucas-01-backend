def get_masked_cnae(cnae_input) -> str:
    return cnae_input[0:2] + '.' + cnae_input[2:4] + '-' + cnae_input[4] + '-' + cnae_input[5:7]
