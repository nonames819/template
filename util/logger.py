import logging
import time
log_path = './Logs/'
rq = time.strftime('%Y%m%d%H%M', time.localtime(time.time()))

logger = logging.getLogger()
logger.setLevel(logging.INFO)  # Log等级总开关
if not logger.handlers:
    # 创建一个handler，用于写入日志文件
    logfile = log_path + rq + '.log'  # log日志的文件名称

    filehandler = logging.FileHandler(logfile, mode='w')
    filehandler.setLevel(logging.DEBUG)  # 输出到file的log等级的开关

    streamhandler = logging.StreamHandler()
    streamhandler.setLevel(logging.DEBUG)  # 输出到console的log等级的开关

    # 第三步，定义handler的输出格式
    formatter = logging.Formatter("%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s")
    filehandler.setFormatter(formatter)
    streamhandler.setFormatter(formatter)

    # 第四步，将logger添加到handler里面
    logger.addHandler(filehandler)
    logger.addHandler(streamhandler)

# logger.info("训练集大小：" + str(train_dataset.shape))
# logger.info('Epoch=%d  step=%d/%d  loss=%.5f' % (epoch, step, batch_cnt, loss))
# logger.info("保存模型文件：" + current_model_path)