import json



lista_jogos = ['WITCHER 3', 'METAL GEAR SOLID V', 'RED DEAD REDEMPTION 2', 'SPIDER-MAN', 'SHADOW OF THE TOMB RAIDER'
               'GOD OF WAR', 'FORTNITE', 'GTA V', 'FIFA 19', 'HORIZON ZERO DAWN', "ASSASSIN'S CREED ODYSSEY", 'SOUL CALIBUR VI',
               'CALL OF DUTY: BLACK OPS 4', 'PES 2019', 'MADDEN NFL 19', 'DETROIT: BECOME HUMAN',
               'FALLOUT SHELTER', "ASSASSIN'S CREED BROTHERHOOD", 'THE ELDER SCROLLS ONLINE']
contador_mencoes_jogos = {}

with open('tweets.json', 'r') as f:
    for line in f:
        tweet = json.loads(line)
        if 'extended_tweet' in tweet:
            texto = tweet['extended_tweet']['full_text']
        else:
            texto = tweet['text']

        texto = texto.upper()

        jogos_lidos = []
        for jogo in lista_jogos:
            if (jogo in texto) and (jogo not in jogos_lidos):
                jogos_lidos.append(jogo)
                if jogo in contador_mencoes_jogos:
                    contador_mencoes_jogos[jogo] += 1
                else:
                    contador_mencoes_jogos[jogo] = 1


for key, value in contador_mencoes_jogos.items():
    print(key, ':', value)