# specification_doc_sample
プレーンテキストによるドキュメント作成テンプレートサンプルお試し用

## sphinx ドキュメント作成方法

### インストールモジュール

```bash
pip install sphinx
pip install sphinx-rtd-theme
pip install sphinxcontrib-mermaid
```

### 作成手順

1.以下コマンドを実行

```bash
sphinx-quickstart <ディレクトリ名>
```

1. markdownでも記述できるようにconf.pyのextensionに以下を入れる

```python
extensions = ['myst_parser']
```

### sphinx autobuildコマンド

```bash
sphinx-autobuild source build --open-browser --port=8888
```
