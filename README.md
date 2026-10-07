# Django 用户管理系统

一个 Django 练手项目，实现了用户管理模块（列表 / 添加 / 删除），界面用 Bootstrap 3.4.1。

## 技术栈

| 项目 | 版本 |
| --- | --- |
| Python | 3.12 |
| Django | 5.2 |
| 数据库 | MySQL 8.0 |
| 前端 | Bootstrap 3.4.1 + jQuery 3.6.0（已内置在 `app01/static/`，无需联网） |

> Django 5.2 要求 Python **3.10 或更高**版本。

## 功能

| 功能 | 地址 | 说明 |
| --- | --- | --- |
| 用户列表 | `/info/list/` | 表格展示全部用户（序号 / id / 姓名 / 密码 / 年龄） |
| 添加用户 | `/info/add/` | 表单提交，带前端校验（必填、长度、年龄范围） |
| 删除用户 | `/info/delete/` | POST + CSRF + 删除前二次确认 |

删除同时兼容 `?nid=<id>` 的 GET 写法。

项目里还保留了教程练习用的其他路由：`/index/`、`/user/list/`、`/user/add/`、`/tpl/`、`/login/`、`/weather/`、`/orm/`、`/admin/`。

## 快速开始

### 1. 安装依赖

```bash
pip install django mysqlclient
```

`mysqlclient` 是 MySQL 驱动。Windows 上如果编译失败，也可以改用 `pymysql`（需在 `DjangoProject/__init__.py` 里加 `pymysql.install_as_MySQLdb()`）。

### 2. 创建数据库

```sql
CREATE DATABASE mysite2 DEFAULT CHARACTER SET utf8mb4;
```

数据库名要和 `local_settings.py` 里的 `NAME` 一致。

### 3. 配置私有设置（必做）

密钥和数据库密码**不会**提交到仓库，需要你自己创建一个本地文件：

```bash
cp DjangoProject/local_settings.example.py DjangoProject/local_settings.py
```

然后编辑 `DjangoProject/local_settings.py`，填上你自己的 `SECRET_KEY` 和 MySQL 账号密码。

生成一个随机 `SECRET_KEY`：

```bash
python -c "from django.core.management.utils import get_random_secret_key as g; print(g())"
```

> `local_settings.py` 已在 `.gitignore` 中，不会被提交。别人克隆本项目后也必须自己创建它，否则 MySQL 密码为空、连不上数据库。

### 4. 建表并启动

```bash
python manage.py migrate
python manage.py runserver
```

浏览器打开 <http://127.0.0.1:8000/info/list/>

## 目录结构

```
DjangoProject/
├── manage.py
├── .gitignore
├── DjangoProject/                  # 项目配置
│   ├── settings.py                 # 公共配置（不含任何密钥）
│   ├── local_settings.example.py   # 私有配置模板
│   ├── local_settings.py           # 私有配置（需自行创建，已被忽略）
│   ├── urls.py                     # 路由
│   └── wsgi.py / asgi.py
└── app01/                          # 业务应用
    ├── models.py                   # UserInfo / Department
    ├── views.py                    # 视图，含 info_list / info_add / info_delete
    ├── templates/
    │   ├── layout.html             # 公共布局（导航栏 + 资源引入）
    │   ├── info_list.html          # 用户列表
    │   └── info_add.html           # 添加用户
    ├── static/                     # Bootstrap 3.4.1 / jQuery / 图片
    └── migrations/
```

## 数据模型

`app01/models.py`：

- `UserInfo` —— `name`(max 32) / `password`(max 64) / `age`(默认 999)
- `Department` —— `title`(max 32)

## 两个小说明

1. **列表页的「序号」和「id」不是一回事。** 删除记录后自增 `id` 会出现空洞，这是 MySQL 的设计行为（自增 id 只保证**唯一**和**递增**，不保证**连续**；MySQL 8.0 起计数器持久化，空洞不会被回收）。列表页的「序号」列用的是模板的 `forloop.counter`，所以始终是连续的 1、2、3…；而 `id` 作为主键用来定位记录，不做重排。
2. `db.sqlite3` 是早期遗留的 0 字节空文件，项目实际使用 MySQL，已加入 `.gitignore`。