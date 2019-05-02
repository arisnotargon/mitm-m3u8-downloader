#存放全局变量
global g_queue

def set_g_queue(v):
    global  g_queue
    g_queue = v

def get_g_queue():
    global g_queue
    return g_queue