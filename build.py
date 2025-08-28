import os
import subprocess

# 使用当前项目路径
current_dir = os.path.dirname(os.path.abspath(__file__))
os.chdir(current_dir)

# 检查 CyberSupervisor.py 是否存在
if os.path.exists('CyberSupervisor.py'):
    # 使用 --name 参数指定输出的应用名称为"赛博监工"
    subprocess.run(['.venv/bin/pyinstaller', 'CyberSupervisor.py', '-F', '-i', 'icon.icns', '-y', '-w', '--name', '赛博监工'])
else:
    print("错误: 找不到 CyberSupervisor.py 文件")
