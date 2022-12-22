import socket
import sys
import time
import threading
import queue

from collections import Counter
from urllib.request import urlopen
from bs4 import BeautifulSoup
import json

BUFFSIZE = 1024

def url_handler(url, k):
    html = urlopen(url ).read()
    soup = BeautifulSoup(html, features="html.parser")
    for script in soup(["script", "style"]):
        script.extract()
    text = soup.get_text()
    lines = (line.strip() for line in text.splitlines())
    chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
    text = '\n'.join(chunk for chunk in chunks if chunk)

    text_set = text.split()
    counter = Counter(text_set)
    most_occur = dict(counter.most_common(k))
    return json.dumps(most_occur)


class Server:
    def __init__(self, worker_num=10, top_k=5, handler_func=url_handler, handler_print=print):
        self.serve_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM, proto=0)
        self.serve_socket.bind(('', 15000))
        self.serve_socket.listen()
        self.top_k = top_k
        self.url_queue = queue.Queue()
        self.worker_num = worker_num
        self.url_handled = 0
        self.handler_func = handler_func
        self.handler_print = handler_print
        self.lock = threading.Lock()

    def run_server(self):
        threads = [threading.Thread(target=self.handle_request, args=[i], daemon=True)
                   for i in range(self.worker_num)]
        for thread in threads:
            thread.start()

        while True:
            client_sock, addr = self.serve_socket.accept()
            if not client_sock:
                self.url_queue.put(('end', None))
                break
            data = client_sock.recv(BUFFSIZE)
            if not data:
                self.url_queue.put(('end', None))
                break
            self.url_queue.put((data.decode(), client_sock))

        for thread in threads:
            thread.join()

    def handle_request(self, thread_id):
        while True:
            data, client_sock = self.url_queue.get()
            if data == 'end':
                self.url_queue.put(('end', None))
                break
            try:
                data_handled = self.handler_func(data, self.top_k)
                client_sock.sendall(bytes(data_handled, encoding='utf-8'))
                self.handler_print(f'handled {self.url_handled} urls last by {thread_id}')
                client_sock.close()
                self.lock.acquire()
                self.url_handled += 1
                self.lock.release()
            except Exception as e:
                print(f'url {data} t_id{thread_id} error occured: {e}')
                continue


if __name__ == '__main__':
    server = Server(worker_num=int(sys.argv[1]), top_k=int(sys.argv[2]))
    t1 = time.time()
    server.run_server()
    print(f'Time passed for {sys.argv[1]} workers: {time.time() - t1}')