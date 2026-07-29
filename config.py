# OK-WW Enhanced Configuration
# 鸣潮自动化工具增强版配置

import os
from pathlib import Path

# ============== 基础配置 ==============

# 项目根目录
PROJECT_ROOT = Path(__file__).parent

# 截图目录
SCREENSHOT_DIR = PROJECT_ROOT / "screenshots"
SCREENSHOT_DIR.mkdir(exist_ok=True)

# 日志目录
LOG_DIR = PROJECT_ROOT / "logs"
LOG_DIR.mkdir(exist_ok=True)

# 配置目录
CONFIG_DIR = PROJECT_ROOT / "configs"
CONFIG_DIR.mkdir(exist_ok=True)

# 每日任务配置目录
DAILY_CONFIG_DIR = CONFIG_DIR / "daily"
DAILY_CONFIG_DIR.mkdir(exist_ok=True)

# 活动配置目录
EVENT_CONFIG_DIR = CONFIG_DIR / "event"
EVENT_CONFIG_DIR.mkdir(exist_ok=True)

# 战斗配置目录
COMBAT_CONFIG_DIR = PROJECT_ROOT / "combat_config"
COMBAT_CONFIG_DIR.mkdir(exist_ok=True)

# ============== 副本类型定义 ==============

DUNGEON_TYPES = {
    '世界 boss': {
        'stamina': 60,
        'description': '世界 BOSS，消耗 60 体力'
    },
    '周本': {
        'stamina': 60,
        'weekly_limit': 3,
        'description': '周常副本，消耗 60 体力，每周限 3 次'
    },
    '副本': {
        'stamina': 40,
        'double_reward': True,
        'description': '普通副本，消耗 40 体力，双倍奖励'
    },
    '声骸': {
        'stamina': 60,
        'double_reward': True,
        'description': '声骸副本，消耗 60 体力，双倍奖励'
    }
}

# ============== 任务注册 ==============

# 所有可用的任务列表
AVAILABLE_TASKS = [
    {
        'name': 'CustomDailyTask',
        'display_name': '多账号每日任务',
        'description': '支持多账号自动执行每日任务，每个账号可配置不同副本',
        'module': 'src.task.CustomDailyTask',
        'class': 'CustomDailyTask'
    },
    {
        'name': 'WeeklyParadiseTask',
        'display_name': '周常自动乐园',
        'description': '自动执行周常任务',
        'module': 'src.task.WeeklyParadiseTask',
        'class': 'WeeklyParadiseTask'
    },
    {
        'name': 'ActivityFramework',
        'display_name': '活动框架',
        'description': '支持限时活动和周期活动',
        'module': 'src.task.ActivityFramework',
        'class': 'ActivityFramework'
    },
    {
        'name': 'ScreenshotTask',
        'display_name': '截图保存',
        'description': '自动截图保存到本地文件夹',
        'module': 'src.task.ScreenshotTask',
        'class': 'ScreenshotTask'
    },
    {
        'name': 'CombatModeTask',
        'display_name': '纯战斗模式',
        'description': '检测怪物后自动战斗',
        'module': 'src.task.CombatModeTask',
        'class': 'CombatModeTask'
    },
    {
        'name': 'ConnectionModeTask',
        'display_name': '连接模式',
        'description': '连接已运行的游戏窗口执行任务',
        'module': 'src.task.ConnectionModeTask',
        'class': 'ConnectionModeTask'
    }
]

# ============== GUI Tab 注册 ==============

# 所有可用的 GUI Tab
AVAILABLE_TABS = [
    {
        'name': 'DailyTaskConfigTab',
        'display_name': '每日任务配置',
        'description': '配置多账号每日任务',
        'module': 'src.gui.DailyTaskConfigTab',
        'class': 'DailyTaskConfigTab'
    },
    {
        'name': 'ActivityManagerTab',
        'display_name': '活动管理',
        'description': '管理和执行活动',
        'module': 'src.gui.ActivityManagerTab',
        'class': 'ActivityManagerTab'
    }
]

# ============== 运行模式 ==============

RUN_MODES = {
    'full_auto': {
        'name': '全自动模式',
        'description': '自动登录、执行任务、截图保存'
    },
    'connection': {
        'name': '连接模式',
        'description': '连接已运行的游戏窗口'
    },
    'combat_only': {
        'name': '纯战斗模式',
        'description': '仅执行战斗'
    }
}

# ============== 定时任务配置 ==============

SCHEDULE_CONFIG = {
    'default_time': '04:00',  # 默认凌晨 4 点执行
    'timezone': 'Asia/Shanghai'
}

# ============== 异常处理配置 ==============

EXCEPTION_HANDLING = {
    'monthly_card': {
        'name': '月卡弹窗',
        'action': 'auto_close',
        'timeout': 10
    },
    'ue4_crash': {
        'name': 'UE4 崩溃',
        'action': 'restart_game',
        'retry_count': 3
    },
    'key_reset': {
        'name': '键位重置',
        'action': 'reconfigure',
        'backup_config': True
    }
}

# ============== NAS 同步配置（可选） ==============

NAS_SYNC_CONFIG = {
    'enabled': False,
    'server': '',
    'port': 22,
    'username': '',
    'password': '',
    'remote_path': '/path/to/screenshots'
}

# ============== 日志配置 ==============

LOG_CONFIG = {
    'level': 'INFO',
    'format': '%(asctime)s - %(levelname)s - %(message)s',
    'max_size': 10 * 1024 * 1024,  # 10MB
    'backup_count': 5
}
