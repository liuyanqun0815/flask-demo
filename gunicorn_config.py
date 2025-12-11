# gunicorn_conf.py
import multiprocessing

# 绑定地址和端口
bind = "0.0.0.0:5000"
# 工作进程数
workers = 4
# 指定 worker 类为 gevent
# worker_class = "gevent"
# 每个 worker 的最大客户端连接数
worker_connections = 1200
# 预加载应用，可以减少 worker 启动的开销并节省内存
preload_app = True
# 等待队列的最大连接数，超过将拒绝新连接
backlog = 2048
# 超时时间（秒）
timeout = 90