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
    

    def __str__(self):
        return self.format_cep()



object_cep = BuscarEndereco('62540970')

print(object_cep)