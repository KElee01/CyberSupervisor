# 赛博监工 (CyberSupervisor)

赛博监工是一个 macOS 应用程序，用于自动监控和启动指定的应用程序。当监控的应用程序未运行时，赛博监工会自动将其启动，确保您的必要应用始终处于运行状态。

## 功能特点

- 自动监控指定的应用程序
- 当应用程序未运行时自动启动
- 可自定义监控的应用程序列表
- 可配置首次检查延迟和检查间隔
- 系统通知提醒应用程序启动状态
- 配置文件保存在用户主目录，便于管理

## 安装方法

### 下载预编译版本

1. 从 [Releases](https://github.com/yourusername/CyberSupervisor/releases) 页面下载最新版本的 `赛博监工.app`
2. 将应用拖到 Applications 文件夹
3. 首次运行时可能需要在系统偏好设置中允许运行
4. 如果需要开机自启的话，需要自行在“系统设置-通用-登录项与扩展-登录时打开”中添加“赛博监工.app”

### 从源码构建

1. 克隆仓库
   ```bash
   git clone https://github.com/KElee01/CyberSupervisor.git
   cd CyberSupervisor
   ```

2. 创建虚拟环境并安装依赖
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   pip install psutil pyinstaller
   ```

3. 构建应用
   ```bash
   python build.py
   ```

4. 构建完成后，可以在 `dist` 目录找到 `赛博监工.app`
5. 将应用拖到 Applications 文件夹
6. 首次运行时可能需要在系统偏好设置中允许运行
7. 如果需要开机自启的话，需要自行在“系统设置-通用-登录项与扩展-登录时打开”中添加“赛博监工.app”

## 配置说明

赛博监工使用 JSON 格式的配置文件，位于 `~/.cybersupervisor/config.json`。首次运行时会自动创建默认配置文件。

配置文件结构如下：

```json
{
    "app_list": [
        "/Applications/App1.app/Contents/MacOS/App1",
        "/Applications/App2.app/Contents/MacOS/App2"
    ],
    "first_check_delay": 60,
    "check_interval": 600
}
```

### 配置项说明

- `app_list`: 需要监控的应用程序列表，使用应用程序可执行文件的完整路径
- `first_check_delay`: 首次检查延迟时间（秒），防止开机后软件先于其他软件启动
- `check_interval`: 后续检查的时间间隔（秒）

### 如何找到应用程序的可执行文件路径

通常，macOS 应用程序的可执行文件路径格式为：
```
/Applications/应用名称.app/Contents/MacOS/可执行文件名
```

可执行文件名通常与应用名称相同，但有时会有所不同。

## 许可证

[MIT License](LICENSE)

## 贡献

欢迎提交 Issue 和 Pull Request！