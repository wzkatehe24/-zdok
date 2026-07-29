# 日志系统

import logging
import os
from datetime import datetime

class TaskLogger:
    def __init__(self):
        self.logger = logging.getLogger('task_logger')
        self.logger.setLevel(logging.INFO)
        
        # 创建日志目录
        log_dir = "logs"
        os.makedirs(log_dir, exist_ok=True)
        
        # 按日期创建日志文件
        log_file = os.path.join(log_dir, f"task_{datetime.now().strftime('%Y%m%d')}.log")
        
        handler = logging.FileHandler(log_file, encoding='utf-8')
        handler.setLevel(logging.INFO)
        
        formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
        handler.setFormatter(formatter)
        
        self.logger.addHandler(handler)
    
    def info(self, msg):
        self.logger.info(msg)
        print(f"[INFO] {msg}")
    
    def warning(self, msg):
        self.logger.warning(msg)
        print(f"[WARNING] {msg}")
    
    def error(self, msg):
        self.logger.error(msg)
        print(f"[ERROR] {msg}")

task_logger = TaskLogger()
