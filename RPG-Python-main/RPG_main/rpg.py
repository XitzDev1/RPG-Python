import random
import time
import json
#import pyautogui

#pyautogui.click(x=951, y=583)

inventario = []

tree_mago = ['Aumento de mana', 'Chance crítico', 'Explosão de mana']
tree_guerreiro = ['Nível extra', 'Aumento de vida', 'Menor meta']
tree_conjurador = ['Conjurador mestre', 'Suporte felino', 'Chance esquiva']

itens_drop = [
    'Poção de crítico',
    'Poção de Vida',
    'Poção de Mana',
    'Chave Dungeon da Floresta',
    'Desert Dungeon Key',
    'Final Dungeon Key'
]


class Classe:
    def __init__(self, nome = '', mana_custo = 0, dano = 0, nivel_req=0, burn = False, stun = False, spawm = False, spawm_dmg = 0):
        self.nome = nome
        self.mana = mana_custo
        self.dano = dano
        self.nivel_req = nivel_req
        self.burn = burn
        self.stun = stun
        self.spawm = spawm
        self.spawm_dmg = spawm_dmg

    def tree(self):
        pass


class Mago(Classe):
    def tree(self):
        for i, trees in enumerate(tree_mago):
            print(f'[{i}] {trees}')
            time.sleep(0.3)

        escolha = int(input('Skill a desbloquear: '))

        if escolha < 0 or escolha >= len(tree_mago):
            print('\nSkill inválida!')
            return

        if player.skill_points >= 2 and escolha >= 0 and escolha < len(tree_mago):

            upgrade = tree_mago[escolha]

            if upgrade not in player.poder and upgrade not in player.skill:

                player.poder.append(upgrade)
                player.skill_points -= 2

                if upgrade == 'Aumento de mana':
                    player.mana_max += 25
                    player.mana += 25

                elif upgrade == 'Chance crítico':
                    player.critico_real -= 1

                elif upgrade == 'Explosão de mana':
                        player.skill.append(explosao_de_mana)
        else:
            print('\nVocê não tem pontos necessários!')

class Guerreiro(Classe):
    def tree(self):
        for i, trees in enumerate(tree_guerreiro):
            print(f'[{i}] {trees}')
            time.sleep(0.3)

        escolha = int(input('Skill a desbloquear: '))

        if escolha < 0 or escolha >= len(tree_guerreiro):
            print('\nSkill inválida!')
            return

        if player.skill_points >= 2 and escolha >= 0 and escolha < len(tree_guerreiro):

            upgrade = tree_guerreiro[escolha]

            if upgrade not in player.poder:

                player.poder.append(upgrade)
                player.skill_points -= 2
                if upgrade == 'Nível extra':
                    player.nivel += 1

                elif upgrade == 'Aumento de vida':
                    player.vida_max += 20
                    player.vida += 20

                elif upgrade == 'Menor meta':
                    player.meta = max(10, player.meta - 10)
            else:
                print('\nVocê já possui essa skill!')
        else:
            print('\nVocê não tem pontos suficientes!')

class Conjurador(Classe):

    def tree(self):
        for i, trees in enumerate(tree_conjurador):
            print(f'[{i}] {trees}')
            time.sleep(0.3)

        escolha = int(input('Skill a desbloquear: '))

        if escolha < 0 or escolha >= len(tree_conjurador):
            print('\nSkill inválida!')
            return

        if player.skill_points >= 2 and escolha >= 0 and escolha < len(tree_conjurador):

            upgrade = tree_conjurador[escolha]

            if upgrade not in player.poder and upgrade not in player.skill:

                player.poder.append(upgrade)
                player.skill_points -= 2

                if upgrade == 'Conjurador mestre':
                    player.mana += 30
                    player.mana_max += 30

                elif upgrade == 'Suporte felino':
                    player.skill.append(suporte_felino)

                elif upgrade == 'Chance esquiva':
                    player.esquiva = 9
            else:
                print('\nVocê já possui essa skill!')
        else:
            print('\nVocê não tem pontos suficientes!')

class Player:
    def __init__(
        self,
        vida,
        nivel,
        xp,
        meta,
        mana,
        classe,
        critico_real = 11,
        poder = None,
        esquiva = 11,
        skill=None,
        skill_points = 0,
        item='Mão',
        hk = False
    ):
        self.esquiva = esquiva
        self.hk = hk
        self.critico_real = critico_real
        self.classe = classe
        self.item = item

        self.vida = vida
        self.vida_max = vida

        self.mana = mana
        self.mana_max = mana

        self.nivel = nivel
        self.xp = xp
        self.meta = meta
        self.poder = poder if poder else []

        self.skill = skill if skill else []
        self.skill_points = skill_points

    def atualizar_skills(self):

        if self.classe == 'Mago':

            if self.nivel >= 1 and soco not in self.skill:
                self.skill.append(soco)

            if self.nivel >= 1 and sopro_magico not in self.skill:
                self.skill.append(sopro_magico)

            if self.nivel >= 5 and raio_magico not in self.skill:
                self.skill.append(raio_magico)

            if self.nivel >= 10 and grito_abismal not in self.skill:
                self.skill.append(grito_abismal)

            if self.nivel >= 15 and explosao_de_mana not in self.skill:
                self.skill.append(explosao_de_mana)

        elif self.classe == 'Guerreiro':

            if self.nivel >= 1 and espada_basica not in self.skill:
                self.skill.append(espada_basica)

            if self.nivel >= 5 and corte_brutal not in self.skill:
                self.skill.append(corte_brutal)

            if self.nivel >= 10 and furia_guerreira not in self.skill:
                self.skill.append(furia_guerreira)

            if self.nivel >= 15 and esmagamento not in self.skill:
                self.skill.append(esmagamento)

        elif self.classe == 'Conjurador':

            if self.nivel >= 1 and invasao_sinistra not in self.skill:
                self.skill.append(invasao_sinistra)

            if self.nivel >= 1 and suporte_felino not in self.skill:
                self.skill.append(suporte_felino)

            if self.nivel >= 10 and raio_mortal not in self.skill:
                self.skill.append(raio_mortal)

            if self.nivel >= 20 and criador_dos_ceus not in self.skill:
                self.skill.append(criador_dos_ceus)

    def player_status(self):

        while self.xp >= self.meta:

            self.nivel += 1
            self.xp -= self.meta
            self.meta *= 2

            self.vida_max += 50
            self.vida = self.vida_max

            self.mana_max += 25
            self.mana = self.mana_max

            self.atualizar_skills()

            time.sleep(0.5)

            self.skill_points += 1

            print('\n====================')
            print('LEVEL UP')
            print(f'Você agora é nível {self.nivel}')
            print(f'Você recebeu um ponde de skill!')
            print('====================\n')

    def mostrar_status(self):

        print('\n===== STATUS =====')
        print(f'Classe: {self.classe}')
        print(f'Vida: {self.vida}/{self.vida_max}')
        print(f'Mana: {self.mana}/{self.mana_max}')
        print(f'Nível: {self.nivel}')
        print(f'XP: {self.xp}/{self.meta}')
        print(f'Item equipado: {self.item}')
        print('==================\n')

arvore = None

class Npc:
    def __init__(self, nome, vida, dano):
        self.nome = nome
        self.vida = vida
        self.dano = dano


lista_npcs = [
    Npc('Ogro', 80, 20),
    Npc('Piglin', 120, 35),
    Npc('Goblin', 160, 50)
]


soco = Mago('Soco', 0, 10, -1)
sopro_magico = Mago('Sopro Magico', 5, 12, 1, False, True)
raio_magico = Mago('Raio Mágico', 15, 20, 5)
grito_abismal = Mago('Grito Abismal', 30, 35, 10, False, True)
explosao_de_mana = Mago('Explosão de Mana', 50, 60, 15, True)

espada_basica = Guerreiro('Espada Básica', 0, 15, 1)
corte_brutal = Guerreiro('Corte Brutal', 10, 30, 5)
furia_guerreira = Guerreiro('Fúria Guerreira', 20, 45, 10, True)
esmagamento = Guerreiro('Esmagamento', 35, 70, 15, False, True)

invasao_sinistra = Conjurador('Invasão sinistra', 15, 30, 1, False, False, True, 5)
raio_mortal = Conjurador('Raio mortal', 20, 5, 10, False, True, False)
criador_dos_ceus = Conjurador('Criador dos céus', 50, 150, 20)
suporte_felino = Conjurador('Suporte felino', 10, 25, -1, False, True)


def salvar_jogo():

    save = {
        'skill_points': player.skill_points,
        'critico_real': player.critico_real,
        'classe': player.classe,
        'poder': player.poder,
        'vida': player.vida,
        'vida_max': player.vida_max,
        'mana': player.mana,
        'mana_max': player.mana_max,
        'nivel': player.nivel,
        'xp': player.xp,
        'meta': player.meta,
        'item': player.item,
        'esquiva': player.esquiva,
        'critico': player.critico,
        'inventario': inventario
    }

    with open('save.json', 'w') as arquivo:
        json.dump(save, arquivo, indent=4)


def carregar_jogo():

    global inventario
    global player

    quest = input('Você tem um save? (S/N): ').lower()

    if quest == 's':

        try:

            with open('save.json', 'r') as arquivo:
                save = json.load(arquivo)

            classe = save.get('classe', 'Guerreiro')

            if classe == 'Mago':
                player = Player(100, 1, 0, 300, 200, 'Mago')

            elif classe == 'Guerreiro':
                player = Player(125, 1, 0, 250, 100, 'Guerreiro')

            elif classe == 'Conjurador':
                player = Player(100, 1, 0, 300, 125, 'Conjurador')

            player.vida = save['vida']
            player.vida_max = save['vida_max']

            player.poder = save.get('poder', [])
            player.mana = save['mana']
            player.mana_max = save['mana_max']

            player.nivel = save['nivel']
            player.xp = save['xp']
            player.meta = save['meta']
            player.skill_points = save.get('skill_points', 0)
            player.critico_real = save['critico_real']

            player.critico = save.get('critico', 11)
            player.esquiva = save.get('esquiva', 11)
            player.item = save.get('item', 'Mão')

            inventario.clear()
            inventario.extend(save['inventario'])

            player.atualizar_skills()

            time.sleep(0.5)

            print('\nSave carregado com sucesso!')

        except FileNotFoundError:

            print('\nNenhum save encontrado!')
            time.sleep(0.5)
            print('Jogo iniciado do zero.')

            criar_novo_jogo()

    else:
        criar_novo_jogo()


def criar_novo_jogo():

    global player

    print('\nNovo jogo iniciado!')
    time.sleep(0.5)

    classe = input('Qual classe? [1] Guerreiro [2] Mago [3] Conjurador: ')

    if classe == '2':
        player = Player(100, 1, 0, 300, 200, 'Mago')
    elif classe == '1':
        player = Player(125, 1, 0, 250, 100, 'Guerreiro')
    elif classe == '3':
        player = Player(100, 1, 0, 300, 125, 'Conjurador')
    else:
        print('Opção inválida!')
        exit()

    player.atualizar_skills()


def adicionar_item():

    chance = random.randint(1, 10)

    if chance == 1:

        item = random.choice(itens_drop)

        inventario.append(item)

        time.sleep(0.5)

        print('\nItem encontrado:')
        print(item)


class Dungeon:
    def __init__(self, nome_dungeon, nome_boss, vida, dano):
        self.nome_dungeon = nome_dungeon
        self.nome_boss = nome_boss
        self.vida = vida
        self.dano = dano

    def raid(self):
        time.sleep(0.5)

        print(f'\nVocê entrou na {self.nome_dungeon}!')

        batalha = Batalha(self.nome_boss, self.vida, self.dano)
        batalha.batalha()

        if player.vida > 0:

            if self.nome_dungeon == 'Dungeon da Floresta':

                player.xp += 300

                inventario.append('Espada Ancestral')

                time.sleep(0.5)

                print('\nVocê recebeu: Espada Ancestral')

            elif self.nome_dungeon == 'Final Dungeon':

                player.xp += 600

                inventario.append('Cajado do Rei Mago')

                time.sleep(0.5)

                print('\nVocê recebeu: Cajado do Rei Mago')

            elif self.nome_dungeon == 'Dungeon do deserto':

                player.xp += 450

                inventario.append('Capacete de areia')

                time.sleep(0.5)

                print('\nVocê recebeu: Capacete de areia')


def usar_item():

    if len(inventario) == 0:
        time.sleep(0.5)

        print('\nInventário vazio!')
        return

    print('\n===== INVENTÁRIO =====')

    for i, item in enumerate(inventario):
        print(f'[{i}] {item}')
        time.sleep(0.3)

    escolha = input('\nEscolha o número do item: ')

    if not escolha.isdigit():
        time.sleep(0.5)

        print('\nEscolha inválida!')
        return

    escolha = int(escolha)

    if escolha < 0 or escolha >= len(inventario):
        time.sleep(0.5)

        print('\nItem inválido!')
        return

    item = inventario[escolha]

    if item == 'Poção de Vida':

        player.vida = min(player.vida + 50, player.vida_max)

        time.sleep(0.5)

        print('\nVocê recuperou vida!')

        inventario.pop(escolha)

    elif item == 'Poção de Mana':

        player.mana = min(player.mana + 40, player.mana_max)

        time.sleep(0.5)

        print('\nVocê recuperou mana!')

        inventario.pop(escolha)

    elif item == 'Poção de crítico':

        player.critico = 1

        time.sleep(0.5)

        print('\nSeu próximo ataque tem 50% de chance de ser crítico!')

        inventario.pop(escolha)

    elif item == 'Chave Dungeon da Floresta':

        inventario.pop(escolha)

        Dungeon(
            'Dungeon da Floresta',
            'Mago Ancestral',
            500,
            50
        ).raid()

    elif item == 'Final Dungeon Key':

        inventario.pop(escolha)

        Dungeon(
            'Final Dungeon',
            'Dragão Celestial',
            800,
            80
        ).raid()

    elif item == 'Desert Dungeon Key':

        Dungeon(
            'Dungeon do deserto',
            'Montro de areia',
            650,
            65
        ).raid()

    elif item == 'Espada Ancestral':

        if player.item != 'Mão':
            if player.item == 'Cajado do Rei Mago':
                player.mana_max -= 80

            elif player.item == 'Espada Ancestral':
                player.vida_max -= 30

            elif player.item == 'Capacete de areia':
                player.vida_max -= 30

            player.mana = player.mana_max
            inventario.append(player.item)

        player.item = 'Espada Ancestral'

        player.vida_max += 50
        player.vida = player.vida_max

        time.sleep(0.5)

        print('\nEspada Ancestral equipada!')

    elif item == 'Cajado do Rei Mago':

        if player.item != 'Mão':
            if player.item == 'Cajado do Rei Mago':
                player.mana_max -= 80

            elif player.item == 'Espada Ancestral':
                player.vida_max -= 50

            elif player.item == 'Capacete de areia':
                player.vida_max -= 30

            player.vida = player.vida_max
            inventario.append(player.item)

        player.item = 'Cajado do Rei Mago'

        player.mana_max += 80
        player.mana = player.mana_max
        time.sleep(0.5)

        print('\nCajado do Rei Mago equipado!')

    elif item == 'Capacete de areia':

        if player.item != 'Mão':
            if player.item == 'Cajado do Rei Mago':
                player.mana_max -= 80

            elif player.item == 'Espada Ancestral':
                player.vida_max -= 50

            elif player.item == 'Capacete de areia':
                player.vida_max -= 30

            player.vida = player.vida_max
            inventario.append(player.item)

        player.item = 'Capacete de areia'

        player.vida_max += 30
        player.vida = player.vida_max
        time.sleep(0.5)

        print('\nCapacete de areia equipado!')

    else:
        time.sleep(0.5)

        print('\nEsse item não pode ser usado agora!')


class Batalha:
    def __init__(self, nome, vida, dano):

        self.nome_npc = nome
        self.vida_npc = vida
        self.dano_npc = dano

    def batalha(self):

        print(f'\nUm {self.nome_npc} apareceu!')

        self.vida_npc += player.nivel * 20
        self.dano_npc += player.nivel * 5

        time.sleep(1)

        stun = False
        burn = False
        spawm = False
        spawm_dmg = 0

        while self.vida_npc > 0 and player.vida > 0:


            print('\n========== BATALHA ==========')
            print(f'{self.nome_npc}: {self.vida_npc} HP')
            print(f'Player: {player.vida} HP')
            print(f'Mana: {player.mana}')
            print('=============================')

            print('\nATAQUES:')

            time.sleep(0.5)

            for i, habilidade in enumerate(player.skill):
                print(
                    f'[{i}] {habilidade.nome} '
                    f'(Mana: {habilidade.mana})'
                )
                time.sleep(0.3)

            print('[9] Usar item')

            escolha = input('\nEscolha: ')

            if escolha.isdigit():

                escolha = int(escolha)

                if escolha >= 0 and escolha < len(player.skill):

                    if player.critico <= 0:
                        player.critico = 1

                    critico_dmg = 0
                    if random.randint(1, player.critico_real) == 1:
                        critico_dmg = 5 * player.nivel
                        player.critico = 11

                    habilidade = player.skill[escolha]

                    if player.mana < habilidade.mana:
                        time.sleep(0.5)

                        print('\nMana insuficiente!')
                        continue

                    dano = habilidade.dano + (player.nivel * 2) + critico_dmg + random.randint(-5, 10)

                    self.vida_npc -= dano

                    player.mana -= habilidade.mana

                    print(
                        f'\nVocê usou {habilidade.nome} '
                        f'e causou {dano} de dano!'
                    )
                    time.sleep(0.5)

                    if habilidade.stun:
                        stun = True

                    if habilidade.burn:
                        burn = True

                    if habilidade.spawm:
                        spawm = True
                        spawm_dmg = habilidade.spawm_dmg

                    if player.hk:
                        self.vida_npc = 0

                elif escolha == 9:

                    usar_item()
                    continue

                else:

                    print('\nOpção inválida!')
                    continue

            else:

                print('\nOpção inválida!')
                continue

            time.sleep(1)

            if self.vida_npc <= 0:
                time.sleep(0.5)

                print(f'\nVocê derrotou o {self.nome_npc}!')

                xp_ganho = random.randint(80, 150)

                player.xp += xp_ganho
                time.sleep(0.5)

                print(f'Você ganhou {xp_ganho} XP!')

                adicionar_item()

                player.player_status()

                salvar_jogo()

                time.sleep(0.5)

                print('\nO jogo foi salvo automaticamente!')

                player.mana = min(
                    player.mana + 30,
                    player.mana_max
                )

                player.vida = player.vida_max

                break

            #Ataque NPC

            if stun:
                print('O oponente está congelado!')
                chance = random.randint(1,5)
                if chance == 5:
                    stun = True
                else:
                    stun = False

            else:

                ataque_npc = random.randint(1, 2)

                if ataque_npc >= 2:
                    esquiva = random.randint(1, player.esquiva)

                    dano_real = random.randint(
                        max(1, self.dano_npc - 5),
                        self.dano_npc + 10
                    )

                    if esquiva == 1:
                        dano_real = 0

                    player.vida -= dano_real

                    if dano_real > 0:
                        time.sleep(0.5)
                        print(f'\nO {self.nome_npc} atacou!')
                        print(f'Você perdeu {dano_real} de vida!')
                    else:
                        time.sleep(0.5)
                        print('\nVocê esquivou!')

                    if burn:
                        print('O NPC está pegando fogo!')
                        burn_dano = 3 * player.nivel
                        self.vida_npc -= burn_dano
                        time.sleep(0.5)
                        print(f'Você deu {burn_dano}!')
                        chance = random.randint(1, 3)
                        if chance == 1:
                            print('\nO fogo apagou!')
                            burn = False

                    if spawm:
                        print('\nSua invocação causou dano!')
                        dano_spawm = spawm_dmg * player.nivel
                        self.vida_npc -= dano_spawm
                        time.sleep(0.5)
                        print(f'O NPC perdeu {dano_spawm} de vida!')
                        if random.randint(1, 3) == 2:
                            print('Sua invocação desapareceu!')
                            spawm = False

                else:

                    time.sleep(0.5)

                    print(f'\nO {self.nome_npc} errou o ataque!')

                time.sleep(1)

        if player.vida <= 0:

            time.sleep(0.5)

            print('\nGAME OVER')

            time.sleep(0.5)

            if player.nivel > 1:

                player.nivel -= 1

                print(
                    '\nVocê pode reencarnar, '
                    'mas perdeu um nível...'
                )

            else:

                print(
                    'Deus teve piedade da sua alma, '
                    'mais sorte dessa vez...'
                )

            player.vida = player.vida_max
            player.mana = player.mana_max

            salvar_jogo()


def main():

    carregar_jogo()

    global arvore

    if player.classe == 'Mago':
        arvore = Mago()

    elif player.classe == 'Guerreiro':
        arvore = Guerreiro()

    elif player.classe == 'Conjurador':
        arvore = Conjurador()

    while True:

        time.sleep(0.5)

        print('\n===== MENU =====')
        print('[1] Status')
        print('[2] Procurar batalha')
        print('[3] Inventário')
        print('[4] Usar Item')
        print('[5] Skill tree')
        print('[6] Sair (Salvar)')

        opcao = input('\nEscolha: ')

        if opcao == '1':

            player.mostrar_status()

        elif opcao == '2':

            npc = random.choice(lista_npcs)

            Batalha(
                npc.nome,
                npc.vida,
                npc.dano
            ).batalha()

        elif opcao == '3':

            print('\n===== INVENTÁRIO =====')

            if len(inventario) == 0:

                print('Inventário vazio')

            else:

                for item in inventario:
                    print(item)

        elif opcao == '4':

            usar_item()

        elif opcao == '6':

            salvar_jogo()

            print('\nSaindo...')

            break

        elif opcao == '5':

            arvore.tree()

        elif opcao == '/cheats':
            quest = input('Cheat: ')
            if quest == 'Skill_points':
                num = int(input('Skill points a adicionar: '))
                player.skill_points = num

            elif quest == 'BROKEN_FULL':
                player.mana = 999
                player.vida = 999
                player.esquiva = 1
                player.critico = 1
                player.nivel = 999
                player.hk = True
                player.atualizar_skills()
                player.player_status()
                inventario.append('Final Dungeon Key')
                inventario.append('Chave Dungeon da Floresta')
                inventario.append('Desert Dungeon Key')

            elif quest == 'HALF_BROKEN':
                player.mana = 999
                player.vida = 999
                player.esquiva = 1
                player.critico = 1
                player.nivel = 999
                player.atualizar_skills()
                player.player_status()
                inventario.append('Final Dungeon Key')
                inventario.append('Chave Dungeon da Floresta')
                inventario.append('Desert Dungeon Key')

            else:
                print('\nCheat inexistente!')

        else:

            print('\nOpção inválida!')


main()