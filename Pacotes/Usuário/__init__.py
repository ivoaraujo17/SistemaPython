
class usuarios():
    def __init__(self):
        self.usuarioadmin = 'admin'
        self.senhaadmin = 12345
        self.listusuario = ['ivo', 'igo', 'ruan']
        self.listsenhas = [12345, 678910, 246810 ]

    def usuario(self):
        while True:
            try:#tenta receber o usuário e transformar a senha em inteiro
                self.usuario = input('\nDigite seu usuário-> ')
                self.senha = int(input('\nDigite sua senha-> '))
            
            except:
                #So dara erro se a senha digitada conter letras e caracteres especiais
                print('\nDigite uma senha apenas com números!')
            
            else:#Se não de erro no input, verifica se o usuario e senha
                #Verifica se o usuario é o administrador
                if self.usuario == self.usuarioadmin:
                    #Se for o ADM, Verifica a senha do ADM
                    if self.senha == self.senhaadmin:
                        #Se a senha está correta, boas vindas!
                        print('\nBem Vindo Administrador')
                        break
                    else:
                        #Caso não, informa que a senha está errada, e retorna o loop
                        print('\nCaro usuário administrador, sua senha está incorreta!')
                        continue

                #Verifica se o usuário está cadastrado na lista de usuários
                if self.usuario in self.listusuario:
                    #Se cadastrado, obtem o indice da lista de usuarios para verificar a senha
                    id = self.listusuario.index(self.usuario)
                    if self.senha == self.listsenhas[id]:
                        #Se a senha está correta, Boas vindas!
                        print(f'\nBem Vindo, {self.usuario}')
                        break
                    else:
                        #Caso não, informa o usuario e retorna o loop
                        print(f'\nCaro Sr(a) {self.usuario}, sua senha está incorreta! Tente novamente!')
                        continue
                #Se o usuário não tiver cadastrado, informa e retorna o loop
                print('\nUsuario não cadastrado, solicite o cadastro ao administrador do sistema!')
                continue
            