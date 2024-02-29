familia = {
    "Julianne": {"idade": 18, "cor_olhos": "castanho"},
    "José Carlos": {"idade": 49, "cor_olhos": "verde"},
    "Manoela": {"idade": 10, "cor_olhos": "castanho"},
    "Claudia": {"idade": 40, "cor_olhos": "castanho"},
    "Theodoro": {"idade": 6, "cor_olhos": "preto"}
}
for nome, info in familia.items():
    print(f"Nome: {nome}, Idade: {info['idade']} anos, Cor dos olhos: {info['cor_olhos']}")
