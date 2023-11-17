from aluno import Aluno
from turma import Turma

alunos = []
alunos.append(Aluno('Joao', 'Pedro', 11))
alunos.append(Aluno('Maria', 'Silva', 7))
alunos.append(Aluno('Carlos', 'Santos', 8))
alunos.append(Aluno('Luisa', 'Fernandes', 9))
alunos.append(Aluno('Antonio', 'Oliveira', 6))

turmaObject = Turma()
turmaObject.cadastrarAlunos(alunos)

turmaObject.mostrarAlunos()
print('*' * 30)
print('Aluno com menor nota:', turmaObject.menorNota.mostrarAluno())
print('Aluno com maior nota:', turmaObject.maiorNota.mostrarAluno())
turmaObject.maiorNota.mostrarAluno()
