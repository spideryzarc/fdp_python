import csv
import random

def gerar_dados_ficticios(nome_arquivo, num_alunos=50):
    # Listas de primeiros e segundos nomes separados por gênero
    primeiros_nomes_femininos = [
        "Ana", "Daniela", "Fernanda", "Helena", "Isabela", "Joana",
        "Karla", "Mariana", "Olivia", "Renata", "Sofia", "Yasmin", 
        "Zuleide", "Vitória", "Wanessa", "Ximena", "Ursula", "Tatiana"
    ]
    primeiros_nomes_masculinos = [
        "Bruno", "Carlos", "Eduardo", "Gabriel", "João", "Leonardo",
        "Miguel", "Nicolas", "Pedro", "Rafael", "Tiago", "Vinícius",
        "Wagner", "Xavier", "Yuri", "Zélio", "Ubirajara", "Thiago"
    ]
    segundos_nomes_femininos = [
        "Beatriz", "Cristina", "Elisa", "Giovana", "Ingrid", "Lara",
        "Natália", "Paula", "Silvana", "Tatiana", "Valéria", "Zélia",
        "Wanda", "Xuxa", "Yara", "Ursula", "Viviane", "Talita", "Raquel"
    ]
    segundos_nomes_masculinos = [
        "Alex", "Diego", "Felipe", "Henrique", "Júlio", "Lucas",
        "Marcelo", "Otávio", "Ricardo", "Samuel", "Wesley", "Zeca",
        "Yago", "Xande", "Vitor", "Ubirajara", "Tadeu", "Raul", "Pedro"
    ]
    sobrenomes = [
        "Silva", "Santos", "Oliveira", "Souza", "Lima", "Ferreira",
        "Pereira", "Almeida", "Costa", "Gomes", "Martins", "Ribeiro",
        "Barbosa", "Rocha", "Carvalho", "Teixeira", "Mendes", "Nunes",
        "Machado", "Araújo", "Monteiro"
    ]

    # Disciplinas possíveis
    disciplinas = ["Cálculo I", "Cálculo II", "Álgebra Linear", "Física I", "Física II", "Química Geral", "Química Orgânica", "Programação I", "Programação II", "Estrutura de Dados", "Banco de Dados", "Redes de Computadores", "Sistemas Operacionais", "Engenharia de Software", "Inteligência Artificial", "Computação Gráfica", "Segurança da Informação", "Matemática Discreta", "Probabilidade e Estatística", "Lógica para Computação"]

    # Lista para armazenar as linhas antes de embaralhar
    dados = []

    # Gera os dados fictícios para cada aluno
    for i in range(1, num_alunos + 1):
        # Gerar matrícula única (ex: MAT001, MAT002, ...)
        mat = f"MAT{i:03d}"
        
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
        # remover espaços duplos
        nome = " ".join(nome.split())
        
        # Cada aluno aparecerá em 2 ou 3 disciplinas (se disponível)
        num_disciplinas = random.randint(2, 3)
        disciplinas_escolhidas = random.sample(disciplinas, num_disciplinas)
        
        for disciplina in disciplinas_escolhidas:
            # Gerar dados fictícios para a disciplina
            nota1 = round(random.uniform(0, 10), 1)
            nota2 = round(random.uniform(0, 10), 1)
            frequencia = random.randint(50, 100)
            
            # Armazena a linha na lista de dados
            dados.append([mat, nome, disciplina, nota1, nota2, frequencia])
    
    # Embaralha a ordem das linhas
    random.shuffle(dados)

    # Abrir arquivo CSV para escrita
    with open(nome_arquivo, mode="w", newline="", encoding="utf-8") as arquivo:
        escritor = csv.writer(arquivo)
        
        # Escrever o cabeçalho com identificador MAT
        escritor.writerow(["MAT", "Nome", "Disciplina", "Nota1", "Nota2", "Frequência (%)"])
        # Escrever as linhas embaralhadas
        # for linha in dados:
        #     escritor.writerow(linha)
        escritor.writerows(dados)

    print(f"Massa de dados fictícia gerada com sucesso no arquivo '{nome_arquivo}'!")

# Gerar o arquivo com os dados fictícios
gerar_dados_ficticios("dados.csv", num_alunos=500)
