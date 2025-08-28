import os
import json

# 使用用户主目录下的配置文件
HOME_DIR = os.path.expanduser("~")
CONFIG_DIR = os.path.join(HOME_DIR, ".cybersupervisor")
CONFIG_FILE = os.path.join(CONFIG_DIR, "config.json")

# 默认配置
DEFAULT_CONFIG = {
    'app_list': [
        "/Applications/Bob.app/Contents/MacOS/Bob",
        "/Applications/PasteNow.app/Contents/MacOS/PasteNow",
        "/Applications/Shottr.app/Contents/MacOS/Shottr",
        "/Applications/Clash Verge.app/Contents/MacOS/clash-verge",
        "/Applications/MonitorControl.app/Contents/MacOS/MonitorControl",
        "/Applications/Calendr.app/Contents/MacOS/Calendr", 
        "/Applications/RunCat.app/Contents/MacOS/RunCat",
        "/Applications/Ice.app/Contents/MacOS/Ice",
        "/Applications/LuLu.app/Contents/MacOS/LuLu"
    ],
    'first_check_delay': 60,  # 防止开机后软件先于其他软件启动，设置启动后多少秒进行第一次检查（秒）
    'check_interval': 600     # 之后的检查间隔（秒）
}


def load_config():
    """加载配置文件，如果不存在则创建默认配置"""
    # 确保配置目录存在
    if not os.path.exists(CONFIG_DIR):
        try:
            os.makedirs(CONFIG_DIR)
        except Exception as e:
            print(f"创建配置目录失败: {e}")
            return DEFAULT_CONFIG
    
    if not os.path.exists(CONFIG_FILE):
        save_config(DEFAULT_CONFIG)
        return DEFAULT_CONFIG
    
    try:
        with open(CONFIG_FILE, 'r', encoding='utf-8') as f:
            config = json.load(f)
        return config
    except Exception as e:
        print(f"加载配置文件失败: {e}")
        return DEFAULT_CONFIG


def save_config(config):
    """保存配置到文件"""
    # 确保配置目录存在
    if not os.path.exists(CONFIG_DIR):
        try:
            os.makedirs(CONFIG_DIR)
        except Exception as e:
            print(f"创建配置目录失败: {e}")
            return False
    
    try:
        with open(CONFIG_FILE, 'w', encoding='utf-8') as f:
            json.dump(config, f, ensure_ascii=False, indent=4)
        return True
    except Exception as e:
        print(f"保存配置文件失败: {e}")
        return False


def get_app_list():
    """获取需要检查的应用列表"""
    config = load_config()
    return config.get('app_list', DEFAULT_CONFIG['app_list'])


def get_check_timings():
    """获取检查时间设置"""
    config = load_config()
    first_check = config.get('first_check_delay', DEFAULT_CONFIG['first_check_delay'])
    interval = config.get('check_interval', DEFAULT_CONFIG['check_interval'])
    return first_check, interval


def update_app_list(app_list):
    """更新应用列表"""
    config = load_config()
    config['app_list'] = app_list
    return save_config(config)


def update_check_timings(first_check_delay, check_interval):
    """更新检查时间设置"""
    config = load_config()
    config['first_check_delay'] = first_check_delay
    config['check_interval'] = check_interval
    return save_config(config)