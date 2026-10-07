from django.apps import AppConfig


class App01Config(AppConfig):
    name = 'app01'
    # 显式声明主键类型，消除启动时的 models.W042 警告。
    # 用 AutoField（而不是 BigAutoField）是为了和现有表的 id int 类型保持一致，
    # 否则 makemigrations 会想生成一条改字段类型的迁移。
    default_auto_field = 'django.db.models.AutoField'
