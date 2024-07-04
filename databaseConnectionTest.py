import psycopg2

try:
    # 数据库连接参数
    db_config = {
        'dbname': 'social-platform',
        'user': 'postgres',
        'password': '123456',
        'host': 'localhost',
        'port': '5432'
    }

    # 尝试连接数据库
    connection = psycopg2.connect(**db_config)
    print("数据库连接成功！")
    connection.close()
except psycopg2.Error as err:
    print(f"数据库连接失败：{err}")
except UnicodeDecodeError as ude:
    print(f"UnicodeDecodeError: {ude}")
except Exception as e:
    print(f"An unexpected error occurred: {e}")