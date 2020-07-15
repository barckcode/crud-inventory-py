clients = 'Pablo,Ricardo,'

# Welcome Message
def _print_welcome():
	print('WELCOME TO PLATZI VENTAS')
	print('*' * 50)
	print('What would you like to do today?')
	print('[C]reate client')
	print('[R]ead clients list')
	print('[U]pdate client')
	print('[D]elete client')
	print('[S]earch client')


# Utils
def list_clients():
	global clients
	print(clients)


def _add_comma():
	global clients
	clients += ','


def _get_client_name():
	client_name = input('What is the client name? ')
	client_name = client_name.capitalize()
	return client_name


# Actions
def create_client(client_name):
	global clients

	if client_name not in clients:
		clients += client_name
		_add_comma()
	else:
		print('Client already is in the clients list')


def update_client(client_name):
	global clients

	if client_name in clients:
		update_client_name = input('What is the updated client name? ')
		clients = clients.replace(client_name, update_client_name)
	else:
		print(f'{client_name} is not in clients list')


def delete_client(client_name):
	global clients

	if client_name in clients:
		clients = clients.replace(client_name + ',', '')
	else:
		print(f'{client_name} is not in clients list')


def search_client(client_name):
	global clients

	clients_list = clients.split(',')

	for client in clients_list:
		if client != client_name:
			continue
		else:
			return True


# Entry Program
if __name__ == '__main__':
	_print_welcome()

	command = input('Select option: ')
	command = command.upper()

	if command == 'C':
		client_name = _get_client_name()
		create_client(client_name)
		list_clients()
	elif command == 'R':
		list_clients()
	elif command == 'U':
		client_name = _get_client_name()
		update_client(client_name)
		list_clients()
	elif command == 'D':
		client_name = _get_client_name()
		delete_client(client_name)
		list_clients()
	elif command == 'S':
		client_name = _get_client_name()
		found = search_client(client_name)

		if found:
			print(f'{client_name} is in the clients list')
		else:
			print(f'The client {client_name} is not in our clients list')
	else:
		print('Invalid option')