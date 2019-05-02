import multiprocessing
import baseproxy.proxy as bp
import gbucket

def producter():
    # 生产端:代理截获m3u8请求信息,并推入multiprocessing的queue中
    proxy_server = bp.AsyncMitmProxy(server_addr=('', 9898), https=True)
    # proxy_server.register(ProxyIntercept)
    proxy_server.serve_forever()

class ProxyIntercept(bp.ReqIntercept):
    # 实现请求拦截接口的代理类
    def deal_request(self, data):
        g_queue = gbucket.get_g_queue()
        print(data)
        g_queue.put(data)
        print(g_queue)


if __name__ == '__main__':
    gbucket.set_g_queue(multiprocessing.Queue())
    #TODO:use multiprocessing.Pool
    producter()
