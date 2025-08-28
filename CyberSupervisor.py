import time
import psutil
import os
import config


def show_notification(title, text):
    os.system("""
              osascript -e 'display notification "{}" with title "{}"'
              """.format(text, title))


# 判断程序是否运行
def is_running(process_exe):
    for p in psutil.process_iter():
        try:
            if p.exe() == process_exe:
                return True
        except psutil.NoSuchProcess:
            pass
        except psutil.AccessDenied:
            pass
    return False


# 启动未运行的程序
def start_process(process_exe):
    if not is_running(process_exe):
        try:
            app_path = process_exe.split('.app/')[0] + ".app"
            os.system(f'open "{app_path}"')
            print(f"{process_exe} 启动成功")
            show_notification("程序启动", f"{process_exe}")
        except Exception as e:
            print(e)
            show_notification("程序启动失败", str(e))


def check_apps():
    """检查并启动所有配置的应用程序"""
    app_list = config.get_app_list()
    for check_app in app_list:
        start_process(check_app)


def main():
    """主程序入口"""
    print("赛博监工 已启动")
    show_notification("赛博监工", "程序已启动，将按照配置的时间间隔检查应用")
    
    # 获取配置的检查时间
    first_check_delay, check_interval = config.get_check_timings()
    
    # 首次检查前等待
    print(f"将在 {first_check_delay} 秒后进行首次检查")
    time.sleep(first_check_delay)
    
    while True:
        print("开始检查应用...")
        check_apps()
        print(f"检查完成，{check_interval} 秒后再次检查")
        time.sleep(check_interval)


if __name__ == "__main__":
    main()
