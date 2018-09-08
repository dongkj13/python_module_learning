import logging

# myLogger = logging.getLogger()    # 等价于logging.root，在logging中已经定义好，采用的是basicConfig
myLogger = logging.getLogger("mylog")

# 设置最低严重级别，默认warning
myLogger.setLevel(logging.INFO)

# 创建一个handler，用于写入日志文件
fh = logging.FileHandler('test.log')

# 再创建一个handler，用于输出到控制台
ch = logging.StreamHandler()

formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
fh.setFormatter(formatter)
ch.setFormatter(formatter)
myLogger.addHandler(fh) #myLogger对象可以添加多个fh和ch对象
myLogger.addHandler(ch)

# myLogger
myLogger.debug('myLogger debug message')
myLogger.info('myLogger info message')
myLogger.warning('myLogger warning message')
myLogger.error('myLogger error message')
myLogger.critical('myLogger critical message')

# root
# logging.root.error("logging error message")
# 等价于
# logging.error("logging error message")