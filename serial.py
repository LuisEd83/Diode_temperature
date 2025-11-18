"""
Módulo: main

Esse código será resposnsável por conectar a interface, o arduino e a plotagem de gráfico.

Objetivo:
- Criar código capaz de gerar um gráfico a partir dos dados fornecidos pelo usuário e a partir
do dado lido pelo arduino;
- A partir do código, calcular a temperatura em que o diodo se encontra (a partir da sua tensão
medida pelo arduino).

Com o código feito, será possível mostrar um termômetro digital.
"""

import serial
import time
import matplotlib.pyplot as plt

from interface import extração

#Conectando ao Arduino
arduino = serial.Serial('COM4', 9600)
time.sleep(2)

#Extraindo dados da interface
T1, Temp1, T2, Temp2, ok = extração()

if not ok:
    print("Erro: interface não retornou valores válidos.")
    exit()

#Reta: temperatura em função da tensão
m = (Temp2 - Temp1) / (T2 - T1)
b = Temp1 - m * T1

print(f"Equação: Temp = {m:.4f} * V + {b:.4f}")

#Criando janela gráfica
plt.ion()
fig = plt.figure(figsize=(10, 5))

ax_graph = fig.add_subplot(1, 2, 1)
ax_text = fig.add_subplot(1, 2, 2)
ax_text.axis("off")

#Reta de 0 a 5 V (faixa da conversão do Arduino)
xs = [0, 5]
ys = [m * x + b for x in xs]

ax_graph.plot(xs, ys, label="Reta Tensão x Temperatura")

#Ponto móvel
ponto, = ax_graph.plot([], [], 'ro', markersize=10)

ax_graph.set_xlim(0, 5)
ax_graph.set_ylim(min(ys) - 10, max(ys) + 10)
ax_graph.legend()
ax_graph.grid(True)

texto_temp = ax_text.text(
    0.1, 0.5,
    "Temperatura atual:\n-- °C",
    fontsize=16,
    va="center"
)

#Loop principal
while True:
    try:
        leitura = int(arduino.readline().decode().strip())
        tensao = leitura * (5.0 / 1023.0)

        temperatura = m * tensao + b

        #Atualiza ponto no gráfico
        ponto.set_xdata([tensao])
        ponto.set_ydata([temperatura])

        #Atualiza texto
        texto_temp.set_text(
            f"Temperatura atual:\n{temperatura:.2f} °C"
        )

        plt.pause(0.001)

    except Exception as e:
        print("Erro:", e)
        continue