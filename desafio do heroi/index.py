
# Definindo a variável do nome e XP do herói
nome_heroi = "junior"

xp_heroi = 7000  # Experiência do herói

# Estrutura de decisão para determinar o nível do herói
if xp_heroi < 1000:
    nivel = "Ferro"
elif 1001 <= xp_heroi <= 2000:
    nivel = "Bronze"
elif 2001 <= xp_heroi <= 5000:
    nivel = "Prata"
elif 5001 <= xp_heroi <= 7000:
    nivel = "Ouro"
elif 7001 <= xp_heroi <= 8000:
    nivel = "Platina"
elif 8001 <= xp_heroi <= 9000:
    nivel = "Ascendente"
elif 9001 <= xp_heroi <= 10000:
    nivel = "Imortal"
elif xp_heroi >= 10001:
    nivel = "Radiante"

# Exibindo a mensagem final
print(f"O Herói de nome {nome_heroi} está no nível de {nivel}")

