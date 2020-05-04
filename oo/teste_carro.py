from unittest import TestCase
from oo.carro import Motor


class CarroTestCase(TestCase):
    
    def teste_velocidade_inicial(self):
        motor = Motor()
        self.assertEquals(0, motor.velocidade)

    def test_acelerar(self):
        motor = Motor()
        motor.acelerar()
        self.assertEquals(1, motor.velocidade)
    
    def test_frear(self):
        motor = Motor()
        motor.frear()
        self.assertEquals(0, motor.velocidade)