## Definir a classe Turma
class Turma():
    #Método Construtor da turma
    def __init__(self,num_alunos,periodo,turno,curso):
        self.num_alunos = num_alunos
        self.periodo = periodo
        self.turno = turno
        self.curso = curso
        self.aluno = [] #Lista que contém todos os objetos "Alunos" que serão instanciados
    #Método de Inserção dos alunos
    def inserir_aluno(self,nome,idade,sexo):
        aluno = Aluno(nome,idade,sexo,self.num_alunos,self.periodo,self.turno,self.curso)
        self.aluno.append(aluno)
        self.num_alunos = self.num_alunos + 1 #Contador de Alunos de fato registrados
    #Método que mostra toda a informação sobre a turma e sobre cada Aluno
    def mostrar_turma(self):
        print("\n")
        print("########## Dados da turma ##########")
        print("Quantidade de alunos {}\nPeriodo : {} /// Turno : {}\nCursando : {}".format(self.num_alunos,self.periodo,self.turno,self.curso))
        print("\n")
        print("########## Alunos Matriculados ##########")
        for aluno in self.aluno:
            print("Nome : {} \nIdade : {} /// Sexo {}".format(aluno.nome,aluno.idade,aluno.sexo))
#Defino a classe Aluno, que herda caracteristicas da sua classe pai(Super Classe) Turma           
class Aluno(Turma):
    def __init__(self,nome,idade,sexo, num_alunos, periodo, turno, curso):
        super().__init__(num_alunos, periodo, turno, curso)
        #Parametros que são somente da classe Aluno
        self.nome = nome
        self.idade = idade
        self.sexo = sexo
#Teste Direto
#turma = Turma(0,'7° Período ',"Vespertino","Engenharia da Computação")
#turma.inserir_aluno("Matheus Rodrigues",24,"Masculino")
#turma.inserir_aluno("Genivalda Fiorentina",19,"Feminino")
#turma.inserir_aluno("Piroscovaldo",26,"Masculino")
#turma.mostrar_turma()

#Teste de usabilidade
DECISAO = True
verificador = 0
while True:
    print("################# Bem Vindo a Univesidade Federal do Pará #################")
    state = int(input("O que deseja Fazer?\n Inserir Turma [1] Inserir Aluno [2] Mostrar Turma [3] Sair [4]"))
    if state == 1:
        if verificador == 0:
            turma = Turma(0,input("Periodo : "),input("Turno : "),input("Curso : "))
            verificador = verificador + 1
        else:
            print("   AVISO : Você já possui o cadastro de uma turma em andamento   ")
            continue
    elif state == 2:
        if verificador == 0:
            print(" AVISO : Você precisa cadastrar uma turma primeiro   ")
            turma = Turma(0,'7° Período ',"Vespertino","Engenharia da Computação")
        elif verificador == 1:
             turma.inserir_aluno(input("Nome : ").upper(),int(input("Idade : ")),input("Sexo : "))
    elif state == 3:
        turma.mostrar_turma()
    elif state == 4:
        print("Muito Obrigado!!!")
        break
    else:
        print("Comando Não Encontrado")
        continue