
saldo=1000

class Cuenta:

    def deposito(self, saldo):
        d=saldo-500
        if saldo == 1000:
            return d

    def retiro(self,saldo):
        r=saldo-500

        if saldo == 1000:
            return r

Cuenta().deposito(saldo)
Cuenta().retiro(saldo)

