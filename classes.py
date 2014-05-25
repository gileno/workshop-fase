

class Say(object):

    def say(self, texto):
        print(texto)

class Conta(object):

    saldo = 9000
    numero = 111

    def debito(self, valor):
        self.saldo = self.saldo - valor

    def tipo(self):
        return 'Conta Simples'

class ContaCorrente(Conta, Say):

    def tipo(self):
        tipo_base = super(ContaCorrente, self).tipo()
        return tipo_base + ' Modificada'
