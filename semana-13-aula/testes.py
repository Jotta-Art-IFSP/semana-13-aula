import unittest
from aluno import Aluno
from turma import Turma

class TurmaTest(unittest.TestCase):

    def setUp(self):
        print('Teste', self._testMethodName, 'sendo executado...')
        self.alunos = []
        self.alunos.append(Aluno('Joao', 'Pedro', 11))
        self.alunos.append(Aluno('Maria', 'Silva', 7))
        self.alunos.append(Aluno('Carlos', 'Santos', 8))
        self.alunos.append(Aluno('Luisa', 'Fernandes', 9))
        self.alunos.append(Aluno('Antonio', 'Oliveira', 6))
        self.turmaObject = Turma()
        self.turmaObject.cadastrarAlunos(self.alunos)

    def tearDown(self):
        print('Teste', self._testMethodName, 'finalizado.')

    def testMaior(self):
        self.assertEqual(9, self.turmaObject.maiorNota.nota, 'Erro ao encontrar maior nota')

    def testMenor(self):
        self.assertEqual(6, self.turmaObject.menorNota.nota, 'Erro ao encontrar menor nota')

    def testIntervalo(self):
        self.assertTrue((self.turmaObject.menorNota.nota > 0 and self.turmaObject.maiorNota.nota <= 10),
                        'Erro ao verificar intervalo')


if __name__ == "__main__":
    unittest.main()
