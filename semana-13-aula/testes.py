import unittest
from aluno import Aluno
from turma import Turma

class TurmaTest(unittest.TestCase):

    def setUp(self):
        print('Teste', self._testMethodName, 'sendo executado...')
        self.alunos = []
        self.alunos.append(Aluno('Fabio', 'Teixeira', 11))
        self.alunos.append(Aluno('Fabiano', 'Teixeira', 7))
        self.alunos.append(Aluno('Melissa', 'Teixeira', 8))
        self.alunos.append(Aluno('Rafael', 'Teixeira', 9))
        self.alunos.append(Aluno('Angela', 'Teixeira', 6))
        self.alunos.append(Aluno('Angela', 'Teixeira', -1))
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
