import L4_Exercicio06 as ex6

# Programa principal
if __name__ == '__main__':
    # lista para dados de N alunos
    lista_alunos = []
    # definição do valor de N
    N = int(input('Número de alunos? '))
    # laço de repetição para entrada de dados de N alunos
    for i in range(N):
        # Cria dicionário de dados de aluno
        aluno = ex6.cria_dicio_aluno(f'Aluno {i+1}')
    # Exibe dados dos aluno
    print('Alunos')
    for i in range(N):
        ex6.exibe_dicio_aluno(aluno, f'Aluno {i+1} ')
