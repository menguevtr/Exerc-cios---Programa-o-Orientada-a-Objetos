# 25/08/2026 - Lista de Exercícios POO - AULA 4 - Vitor Mengue Dorneles
# Exercício 1 - Criar duas classes, Aluno e Disciplina

# A palavra-chave class é usada para criar uma classe.
class Disciplina:
    # __init__ é o método especial chamado para criar o objeto.
    def __init__(self, nome):
        # self.nome cria um atributo chamado "nome" dentro do objeto disciplina.
        self.nome = nome


# Criando a classe Aluno.
class Aluno:
    # Método inicializador da classe Aluno.
    def __init__(self, nome):
        # self.nome guarda o nome do aluno.
        self.nome = nome

    # Definindo o método para inscrever o aluno em uma disciplina.
    # Ele recebe o parâmetro "disciplina", que é um objeto da classe Disciplina.
    def inscrever(self, disciplina):
        # print mostra uma mensagem na tela.
        # f"..." permite usar variáveis como self.nome e disciplina.nome no texto.
        print(f"{self.nome} se inscreveu na disciplina de {disciplina.nome}.")


# --- Executando o programa ---

# Criando um objeto da classe Disciplina.
disciplina1 = Disciplina("Programação Orientada a Objetos")

# Criando um objeto da classe Aluno.
aluno1 = Aluno("Maria")

# Chamando o método inscrever do objeto aluno1, passando a disciplina1 como argumento.
aluno1.inscrever(disciplina1)
