# gunicorn_conf.py
import multiprocessing

# # 绑定地址和端口
# bind = "0.0.0.0:5000"
# # 工作进程数
# workers = 4
# # 指定 worker 类为 gevent
# # worker_class = "gevent"
# # 每个 worker 的最大客户端连接数
# worker_connections = 1200
# # 预加载应用，可以减少 worker 启动的开销并节省内存
# preload_app = True
# # 等待队列的最大连接数，超过将拒绝新连接
# backlog = 2048
# # 超时时间（秒）
# timeout = 90

import multiprocessing
import logging
import sys

bind = "0.0.0.0:5001"
#workers = multiprocessing.cpu_count() * 2 + 1
workers = 4
accesslog = "/data/dify_feihu/pyserver/api/access.log"
errorlog = "/data/dify_feihu/pyserver/api/error.log"
loglevel = "debug"
capture_output = True
timeout = 300

# Optional: Customize the log format
access_log_format = '%(h)s %(l)s %(u)s %(t)s "%(r)s" %(s)s %(b)s "%(f)s" "%(a)s"'

# Ensure that logging configuration captures application logs
logging.basicConfig(
    level=logging.INFO,  # This should match the gunicorn loglevel
    format='%(asctime)s %(levelname)s %(message)s',
    handlers=[
        logging.StreamHandler(sys.stdout),
        #logging.StreamHandler(sys.stderr)
    ]
)
