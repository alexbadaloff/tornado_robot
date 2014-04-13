# encoding: utf8
import tornado.httpserver
import tornado.ioloop
import tornado.web
import tornado.websocket
import tornado.gen
from tornado.options import define, options
import time
import multiprocessing
import lego_main


define("port", default=80, help="run on the given port", type=int)
l = ''
k = 0
timer = time.time()

clients = []

class IndexHandler(tornado.web.RequestHandler):
    def get(self):
        self.render('test.html')

class WebSocketHandler(tornado.websocket.WebSocketHandler):
    waiters = set()
    cache = []
    cache_size = 200
    timer = time.time()

    def open(self):
        global l,k
        print ('new connection ')
        # print(dir(WebSocketHandler.waiters))
        WebSocketHandler.waiters.add(self)
        self.write_message(l)

    def on_message(self, message):
        global l,k,timer

        # print dir(self)
        # print self.waiters
        print ('tornado received from client: %s' % message)
        # l = l + int(message)
        if k==9:
            k=0; l = '';
        else:
            k = k + 1

        # print(k)
        # if time.time() - timer < float(2):
        #     l = l + '%s - <font color="orange">Занято</font><br>'%k
        #     WebSocketHandler.send_updates(l)
        #     return
        # else:
        #     timer = time.time()

        if message == '1':
            l = l +  '%s - <font color="green">Влево</font><br>'%k
            lego_main.action('a')
        elif message == '2':
            l = l + '%s - <font color="green">Вправо</font><br>'%k
            lego_main.action('d')
        elif message == '3':
            l = l + '%s - <font color="green">Вперёд</font><br>'%k
            lego_main.action('w')
        elif message == '4':
            l = l + '%s - <font color="green">Назад</font><br>'%k
            lego_main.action('s')
        if message == '5':
            l = l + '%s - <font color="orange">Стоп</font><br>'%k
            lego_main.action('q')

        # l = l + message.encode('utf8')
        WebSocketHandler.send_updates(l)

    @classmethod
    def send_updates(cls, message):
        for waiter in cls.waiters:
            waiter.write_message(message)

    def on_close(self):
        print ('connection closed')
        WebSocketHandler.waiters.remove(self)
 
################################ MAIN ################################


# def get_ip_address(ifname):
#     # example get_ip_address('wlan0')
#     import socket
#     import fcntl
#     import struct
#     s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
#     return socket.inet_ntoa(fcntl.ioctl(
#         s.fileno(),
#         0x8915,  # SIOCGIFADDR
#         struct.pack('256s', ifname[:15])
#     )[20:24])

def main():
 
    taskQ = multiprocessing.Queue()
    tornado.options.parse_command_line()
    app = tornado.web.Application(
        handlers=[
            (r"/", IndexHandler),
            (r"/ws", WebSocketHandler)
        ], queue=taskQ
    )
    httpServer = tornado.httpserver.HTTPServer(app)
    httpServer.listen(options.port)
    print ("Listening on port:", options.port)
 
    mainLoop = tornado.ioloop.IOLoop.instance()
    mainLoop.start()
 
if __name__ == "__main__":
    main()
