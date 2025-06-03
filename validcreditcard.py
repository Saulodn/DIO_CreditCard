import re

def identificar_bandeira(cartao: str) -> str:
    cartao = cartao.replace(' ', '').replace('-', '')  # Remove espaços e hífens

    bandeiras = {
        'Visa': r'^4\d{12}(\d{3})?(\d{3})?$',
        'Mastercard': r'^(5[1-5]\d{14}|2(2[2-9]\d{12}|[3-6]\d{13}|7([01]\d{12}|20\d{12})))$',
        'Elo': r'^(4011\d{12}|4312\d{12}|4389\d{12}|4514\d{12}|4576\d{12}|5041\d{12}|50(6[7-9]|[7-9]\d)\d{12}|6277\d{12}|636[23]\d{12}|650[4-5]\d{12}|6516\d{12}|6550\d{12})$',
        'Amex': r'^3[47]\d{13}$',
        'Hipercard': r'^(38\d{14}|60\d{14})$',
        'Diners Club': r'^(3(0[0-5]|[68])\d{11})$',
        'Discover': r'^(6011\d{12}|65\d{14}|64[4-9]\d{13}|622(12[6-9]|1[3-9]\d|[2-8]\d{2}|9[0-1]\d|92[0-5])\d{10})$'
    }

    for bandeira, padrao in bandeiras.items():
        if re.match(padrao, cartao):
            return bandeira

    return 'Bandeira desconhecida'

# Exemplos de uso
cartoes = [
    '4111 1111 1111 1111',  # Visa
    '5500 0000 0000 0004',  # Mastercard
    '5067 0000 0000 0000',  # Elo
    '3400 0000 0000 009',   # Amex
    '6011 0000 0000 0004',  # Discover
    '3000 0000 0000 04',    # Diners Club
    '6062 8288 8866 6688'   # Hipercard
]

for cartao in cartoes:
    print(f'Cartão: {cartao} -> Bandeira: {identificar_bandeira(cartao)}')
