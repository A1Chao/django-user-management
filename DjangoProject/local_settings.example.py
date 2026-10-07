"""本地私有配置示例。

使用方法：
    1) 复制本文件为同目录下的 local_settings.py：
           cp DjangoProject/local_settings.example.py DjangoProject/local_settings.py
    2) 把下面的占位值换成你自己的值。

说明：
    - settings.py 末尾会执行 `from .local_settings import *`，用这里的值覆盖
      SECRET_KEY 和 DATABASES；文件不存在时项目仍能启动，但连不上 MySQL。
    - local_settings.py 已被 .gitignore 忽略，不会提交到仓库。
"""

# 生成一个随机密钥：
#   python -c "from django.core.management.utils import get_random_secret_key as g; print(g())"
SECRET_KEY = '请替换成你自己的随机密钥'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'mysite2',
        'USER': 'root',
        'PASSWORD': '请替换成你的MySQL密码',
        'HOST': '127.0.0.1',
        'PORT': 3306,
    }
}