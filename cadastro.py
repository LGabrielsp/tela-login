from PySimpleGUI import PySimpleGUI as sg

# Layout
sg.theme('DarkBlue12')
layout = [
	[sg.Text('Usuário'), sg.Input(key='usuario', size=(20,1))],
	[sg.Text('Senha  '), sg.Input(key='senha', password_char='*', size=(20,1))],
	[sg.Checkbox('Salvar o login?')],
	[sg.Button('Entrar')]
]

# Janela
Janela = sg.Window('Tela de Login', layout)

# Ler os eventos
while True:
	eventos, valores = Janela.read()
	if eventos == sg.WINDOW_CLOSED:
		break
	if eventos == 'Entrar':
		if valores['usuario'] == 'Poppy' and valores['senha'] == '123456':
			print('Bem-vindo')