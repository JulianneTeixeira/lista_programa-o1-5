distancia = float(input("a digitar a distância de um objeto(m):"))
velocidade0 = float(input("a digitar a a velocidade inicial de um objeto(m/s^2)"))
#queda livre
#S= So + Vot + gt2/2=> So = 0 e g= 10

descobrir_tempo = (0 + velocidade0 - distancia)
#10*t/2 = 5t
t= descobrir_tempo / 5
t_quadrado= t**2

print("O tempo é de(s): ",t_quadrado)