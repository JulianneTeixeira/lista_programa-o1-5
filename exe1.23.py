distancia_percorrida = float(input("Digite a distância percorrida:"))
tempo_gasto = float(input("Digite o tempo gasto:"))
aceleracao = float(input("Digite a aceleração:"))
velocidade_inicial = 0
velocidade_final = velocidade_inicial + (aceleracao * tempo_gasto)
print(f"Velocidade inicial: {velocidade_inicial} m/s")
print(f"Velocidade final: {velocidade_final} m/s")
