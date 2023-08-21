from kivy.app import App
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.config import Config

Config.set('graphics', 'height', 600)
Config.set('graphics', 'width', 450)
def somatorio(num):
    soma = 0
    for i in range(1, num+1):
        soma+=i
    return soma

def wesley_safadao(dia, mes, ano):
    if (dia > 31) or (dia < 0) or (mes > 12) or (mes < 0) or (ano > 99) or (ano < 0):
        return 'Data inválida'
    safadeza = somatorio(mes)+(ano/100)*(50-dia)
    anjo = 100 - safadeza
    return f'Você é {anjo}% anjo , e {safadeza}% safado.'

class Manager(ScreenManager):
    def __init__(self, **kwargs):
        super(Manager, self).__init__(**kwargs)
        self.current = 'mainscreen'
    pass


class MainScreen(Screen):
    def __init__(self, **kwargs):
        super(MainScreen, self).__init__(**kwargs)
        pass
    
    dia = mes = ano = 0
    def calcular(self):
        try:
            self.dia = int(self.ids.inputdia.text)
            self.mes = int(self.ids.inputmes.text)
            self.ano = int(self.ids.inputano.text)
            resultado = wesley_safadao(self.dia, self.mes, self.ano)
            self.ids.resultado.text = resultado
        except:
            self.ids.resultado.text = 'Data inválida'
        pass

    pass


class Safadometro(App):
    def build(self):
        return Manager()
    pass


Safadometro().run()