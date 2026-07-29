# 配置文件解析器

import os
from src.utils.logger import task_logger

def parse_daily_config():
    """解析每日任务配置文件"""
    config_dir = "configs/daily"
    configs = []
    
    if not os.path.exists(config_dir):
        task_logger.warning(f"配置目录不存在：{config_dir}")
        return configs
    
    for filename in os.listdir(config_dir):
        if filename.endswith('.txt'):
            filepath = os.path.join(config_dir, filename)
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read().strip()
                if content:
                    config = parse_config_line(content)
                    if config:
                        configs.append(config)
    
    return configs

def parse_config_line(line):
    """解析单行配置：账号 - 体力副本 - 梦魇 - 截图编号"""
    parts = line.split('-')
    if len(parts) < 2:
        return None
    
    account = parts[0].strip()
    dungeons = parts[1].strip().split('|') if len(parts) > 1 else []
    nightmares = parts[2].strip().split('|') if len(parts) > 2 else []
    screenshot_id = parts[3].strip() if len(parts) > 3 else None
    
    return {
        'account': account,
        'dungeons': dungeons,
        'nightmares': nightmares,
        'screenshot_id': screenshot_id
    }
