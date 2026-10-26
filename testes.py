import unittest;
import aluno as a;
import turma as t;

class turmaTest(unittest.TestCase):

  def setUp(self):
    print('Teste', self._testMethodName, 'sendo executado...');
    self.alunos = [];
    
    self.alunos.append(a.Aluno('Fabio', 'Teixeira', 10));
    self.alunos.append(a.Aluno('Fabiano', 'Teixeira', 8));
    self.alunos.append(a.Aluno('Melissa', 'Teixeira', -1));    
    self.alunos.append(a.Aluno('Angela', 'Teixeira', 7));       
    
    self.turmaObject = t.Turma();
    self.turmaObject.cadastrarAlunos(self.alunos);
  
  def tearDown(self):
    print('Teste', self._testMethodName, 'finalizado.'); 
  
  def testMaior(self):      
    self.assertEqual(10, self.turmaObject.maiorNota.nota, 'Erro ao encontrar maior nota');

  def testMenor(self):    
    self.assertEqual(7, self.turmaObject.menorNota.nota, 'Erro ao encontrar menor nota');

  def testIntervalo(self):
    self.assertEqual(3, len(self.turmaObject.turma));
    for aluno in self.turmaObject.turma:
      with self.subTest(aluno=aluno.nome, nota=aluno.nota):
        self.assertGreaterEqual(aluno.nota, 0);
        self.assertLessEqual(aluno.nota, 10);

  def testLimitesDoIntervalo(self):
    turma = t.Turma();
    turma.cadastrarAlunos([
      a.Aluno('Negativa', 'Teste', -1),
      a.Aluno('Zero', 'Teste', 0),
      a.Aluno('Dez', 'Teste', 10),
      a.Aluno('Acima', 'Teste', 11),
    ]);
    self.assertEqual([0, 10], [aluno.nota for aluno in turma.turma]);
    self.assertEqual(0, turma.menorNota.nota);
    self.assertEqual(10, turma.maiorNota.nota);

  def testMaiorEMenorIndependemDaOrdem(self):
    for notas in ([10], [10, 8, 7], [7, 8, 10], [8, 10, 7]):
      with self.subTest(notas=notas):
        turma = t.Turma();
        turma.cadastrarAlunos([a.Aluno('Aluno', 'Teste', nota) for nota in notas]);
        self.assertEqual(min(notas), turma.menorNota.nota);
        self.assertEqual(max(notas), turma.maiorNota.nota);


if __name__ == "__main__":
  unittest.main()
