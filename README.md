# Exec unix command Python

Pythonでunixコマンドを実行する。

## 実行

``` sh
docker-compose build
docker-compose up
```

### 備考

- 例として```npm search aws-sdk --json=true```からdescriptionを取得しているが、Dockerコンテナにnpmをインストールするのが面倒らしく、Pythonコンテナではなく、NodeコンテナにPythonをインストールしている。

## 参考

- [Pythonでコマンドを実行する方法を現役エンジニアが解説【初心者向け】:TechAcademy](https://techacademy.jp/magazine/22133)
- [python3のbytes型とstr型の比較と変換方法:Python Snippets](https://python.civic-apps.com/python3-bytes-str-convert/)
- [python3 文字列を辞書に変換:Qiita](https://qiita.com/lamplus/items/b5d8872c76757b2c0dd9)