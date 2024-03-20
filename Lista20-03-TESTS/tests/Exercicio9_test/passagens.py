class SistemaReservas:
    def __init__(self):
        self.voos_disponiveis = {}
        self.reservas = {}

    def adicionar_voo(self, numero_voo, lugares_disponiveis):
        self.voos_disponiveis[numero_voo] = lugares_disponiveis

    def realizar_reserva(self, numero_voo, numero_assentos):
        if numero_voo in self.voos_disponiveis:
            if self.voos_disponiveis[numero_voo] >= numero_assentos:
                if numero_voo not in self.reservas:
                    self.reservas[numero_voo] = 0
                self.reservas[numero_voo] += numero_assentos
                self.voos_disponiveis[numero_voo] -= numero_assentos
                return True
        return False

    def visualizar_reservas(self, numero_voo):
        return self.reservas.get(numero_voo, 0)

    def cancelar_reserva(self, numero_voo, numero_assentos):
        if numero_voo in self.reservas:
            if numero_assentos <= self.reservas[numero_voo]:
                self.reservas[numero_voo] -= numero_assentos
                self.voos_disponiveis[numero_voo] += numero_assentos
                return True
        return False