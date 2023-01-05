import requests


class BuscarEndereco():
    def __init__(self, cep):
        cep = str(cep)
        if self.validar_cep(cep):
            self.cep = cep
        else:
            raise ValueError('CEP invalido!!')
    
    def validar_cep(self, cep):
        if len(cep) == 8:
            return True
        else:
            return False
    
    def format_cep(self):
        return f'{self.cep[:5]}-{self.cep[5:]}'

    def acesso_via_cep(self):
        url = f'http://viacep.com.br/ws/{self.cep}/json/'
        r = requests.get(url)
        dados = r.json()
        return (
             dados['bairro'],
             dados['localidade'],
             dados['uf'],
             dados['logradouro'],
        )

    def __str__(self):
        return self.format_cep()



object_cep = BuscarEndereco('62540970')
bairro, localidade, uf, logradouro = object_cep.acesso_via_cep()
print(f'{bairro}, {localidade}-{uf}, {logradouro}')