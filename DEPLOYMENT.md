# SpecAgent AI 网站部署指南

本文档提供了在生产环境（如 Linux 服务器）上部署 SpecAgent AI 网站的详细步骤。

## 1. 环境要求

*   **操作系统**: Linux (Ubuntu 22.04 LTS / CentOS 7+ 等)
*   **Python**: Python 3.10+
*   **数据库**: SQLite (默认) 或 PostgreSQL
*   **Web 服务器**: Nginx (推荐)
*   **进程管理器**: Gunicorn + Systemd (或 Supervisor)

## 2. 代码获取与依赖安装

1.  **克隆代码库**
    ```bash
    git clone https://github.com/liushuono1/Specient-web.git
    cd Specient-web
    ```

2.  **创建虚拟环境**
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```

3.  **安装依赖**
    ```bash
    pip install -r requirements.txt
    pip install gunicorn  # 生产环境需要安装 Gunicorn
    ```

## 3. 环境变量配置

在项目根目录下创建一个 `.env` 文件，用于存放敏感配置。

```bash
touch .env
```

`.env` 文件内容示例：

```ini
# Generate a secure key: python -c 'from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())'
SECRET_KEY=your-secure-generated-secret-key-here

# 生产环境必须设置为 False
DEBUG=False

# 允许访问的域名，用逗号分隔
ALLOWED_HOSTS=example.com,www.example.com,127.0.0.1
```

## 4. 静态文件与数据库

1.  **收集静态文件**
    将所有静态资源（CSS, JS, 图片）收集到 `STATIC_ROOT` 目录，以便 Nginx 提供服务。
    ```bash
    python manage.py collectstatic
    ```

2.  **数据库迁移**
    ```bash
    python manage.py migrate
    ```

## 5. 使用 Gunicorn 运行

测试 Gunicorn 是否能正常启动应用：

```bash
gunicorn hello_world.wsgi:application --bind 0.0.0.0:8000
```
*如果看到启动成功的日志，按 `Ctrl+C` 停止。*

## 6. 配置 Systemd 服务 (推荐)

创建一个 systemd 服务文件来管理 Gunicorn 进程，确保开机自启和奔溃重启。

文件路径: `/etc/systemd/system/specagent.service`

```ini
[Unit]
Description=gunicorn daemon for SpecAgent AI
After=network.target

[Service]
User=root
Group=www-data
WorkingDirectory=/path/to/Specient-web
ExecStart=/path/to/Specient-web/venv/bin/gunicorn \
          --access-logfile - \
          --workers 3 \
          --bind unix:/path/to/Specient-web/specagent.sock \
          hello_world.wsgi:application

[Install]
WantedBy=multi-user.target
```
*注意：请将 `/path/to/Specient-web` 用于实际的项目路径，建议使用非 root 用户运行。*

启动服务：
```bash
sudo systemctl start specagent
sudo systemctl enable specagent
```

## 7. 配置 Nginx 反向代理

安装 Nginx：
```bash
sudo apt update
sudo apt install nginx
```

创建 Nginx 配置文件 `/etc/nginx/sites-available/specagent`：

```nginx
server {
    listen 80;
    server_name example.com www.example.com;

    location = /favicon.ico { access_log off; log_not_found off; }
    
    # 静态文件服务
    location /static/ {
        root /path/to/Specient-web/hello_world/staticfiles; # 注意这里是 STATIC_ROOT 的路径
    }

    # 媒体文件服务 (如果有)
    location /media/ {
        root /path/to/Specient-web/hello_world/media;
    }

    location / {
        include proxy_params;
        proxy_pass http://unix:/path/to/Specient-web/specagent.sock;
    }
}
```

启用配置并重启 Nginx：
```bash
sudo ln -s /etc/nginx/sites-available/specagent /etc/nginx/sites-enabled
sudo nginx -t
sudo systemctl restart nginx
```

## 8. 维护与更新

当有代码更新时：

1.  拉取最新代码：`git pull`
2.  更新依赖（如果有）：`pip install -r requirements.txt`
3.  应用迁移（如果有）：`python manage.py migrate`
4.  收集静态文件：`python manage.py collectstatic`
5.  重启应用服务：`sudo systemctl restart specagent`

---
**提示**: 对于 Tailwind CSS，由于本项目使用 CDN，无需构建步骤。如果后续改为本地构建，需要增加 npm build 步骤。
