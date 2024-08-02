# specification_doc_sample
プレーンテキストによるドキュメント作成テンプレートサンプルお試し用

## sphinx ドキュメント作成方法

1.以下コマンドを実行

```
sphinx-quickstart <ディレクトリ名>
```

1. markdownでも記述できるようにconf.pyのextensionに以下を入れる

```
extensions = ['myst_parser']
```

