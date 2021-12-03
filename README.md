# README
- サンプルのブログアプリケーションです。
- 使用方法をご確認の上、コマンドを実行するとアプリケーションを動かすことができます。

## バージョン
- django 3.0.4
- Python 3.9.7
___

## 使用方法
1. まずアプリケーションを任意の場所にクローンし、ディレクトリを移動します。
```
$ git clone git@github.com:mo09e/dj_sample_pjt.git
$ cd dj_sample_pjt
```
2. PostgreSQLに接続し、下記のコマンドを実行してください。
```
$ psql postgres
postgres=# CREATE DATABASE test_project;
postgres=# CREATE USER django_user WITH PASSWORD 'password';
postgres=# \q
```
3. マイグレーションを実行してください。
```
$ python manage.py migrate
```
4. サーバーを立ち上げ、アプリケーションを起動してください。
```
$ python manage.py runserver
```
5. サーバーを起動させた状態で以下のURLをコピーし、アドレスバーに貼り付けてください。
```
http://localhost:8000/blog/post_list
```