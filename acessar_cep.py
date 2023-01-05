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