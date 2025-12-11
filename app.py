import logging
import time
from uuid import uuid4

from flask import Flask

app = Flask(__name__)

logger = logging.Logger(__name__)
@app.route('/')
def hello_world():
    uuid = str(uuid4())
    logger.info(f"uuid:{uuid}请求开始")
    time.sleep(0.1)  # 由于打了猴子补丁，此时 sleep 也是非阻塞的    # put application's code here
    logger.info(f"uuid:{uuid}请求结束")
    return 'Hello World!'


if __name__ == '__main__':
    app.run()
