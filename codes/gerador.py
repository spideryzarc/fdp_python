import csv
import random

def gerar_dados_ficticios(nome_arquivo, num_alunos=50):
    # Listas de primeiros e segundos nomes separados por gênero
    primeiros_nomes_femininos = [
        "Ana", "Daniela", "Fernanda", "Helena", "Isabela", "Joana",
        "Karla", "Mariana", "Olivia", "Renata", "Sofia", "Yasmin"
    ]
    primeiros_nomes_masculinos = [
        "Bruno", "Carlos", "Eduardo", "Gabriel", "João", "Leonardo",
        "Miguel", "Nicolas", "Pedro", "Rafael", "Tiago", "Vinícius"
    ]
    segundos_nomes_femininos = [
        "Beatriz", "Cristina", "Elisa", "Giovana", "Ingrid", "Lara",
        "Natália", "Paula", "Silvana", "Tatiana", "Valéria", "Zélia"
    ]
    segundos_nomes_masculinos = [
        "Alex", "Diego", "Felipe", "Henrique", "Júlio", "Lucas",
        "Marcelo", "Otávio", "Ricardo", "Samuel", "Wesley", "Zeca"
    ]
    sobrenomes = [
        "Silva", "Santos", "Oliveira", "Souza", "Lima", "Ferreira",
        "Pereira", "Almeida", "Costa", "Gomes", "Martins", "Ribeiro",
        "Barbosa", "Rocha", "Carvalho", "Teixeira", "Mendes", "Nunes",
        "Machado", "Araújo", "Monteiro"
    ]

    # Disciplinas possíveis
    disciplinas = ["Estatística", "Matemática", "Programação"]

    # Abrir arquivo CSV para escrita
    with open(nome_arquivo, mode="w", newline="", encoding="utf-8") as arquivo:
        escritor = csv.writer(arquivo)
        
        # Escrever o cabeçalho
        escritor.writerow(["ID", "Nome", "Disciplina", "Nota1", "Nota2", "Frequência (%)"])
        
        for i in range(1, num_alunos + 1):
            # Escolher gênero aleatoriamente
            genero = random.choice(["feminino", "masculino"])
            
            # Escolher nomes com base no gênero
            if genero == "feminino":
                primeiro_nome = random.choice(primeiros_nomes_femininos)
                segundo_nome = random.choice(segundos_nomes_femininos) if random.random() < 0.5 else ""
            else:
                primeiro_nome = random.choice(primeiros_nomes_masculinos)
                segundo_nome = random.choice(segundos_nomes_masculinos) if random.random() < 0.5 else ""
            
            # Montar o nome completo
            nome = f"{primeiro_nome} {segundo_nome} {random.choice(sobrenomes)}".strip()
            
            # Gerar dados fictícios
            disciplina = random.choice(disciplinas)
            nota1 = round(random.uniform(0, 10), 1)
            nota2 = round(random.uniform(0, 10), 1)
            frequencia = random.randint(50, 100)
            
            # Escrever a linha no arquivo
            escritor.writerow([i, nome, disciplina, nota1, nota2, frequencia])

    print(f"Massa de dados fictícia gerada com sucesso no arquivo '{nome_arquivo}'!")

# Gerar o arquivo com os dados fictícios
gerar_dados_ficticios("dados_ficticios.csv", num_alunos=50)
