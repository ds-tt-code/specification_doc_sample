=============================
functional ロール一覧
=============================

.. list-table::
  :header-rows: 1

  * - ロール名
    - 親ロール
    - カスタムロール
    - 説明

  * - ACCOUNTADMIN	
    -	
    -	
    - Snowflakeアカウントの管理用ロール。

  * - SECURITYADMIN
    - ACCOUNTADMIN
    - 
    - 

  * - USERADMIN
    - SECURITYADMIN
    - 
    -	ユーザ作成などを担当する組み込みの管理用ロール。

  * - SYSADMIN
    - ACCOUNTADMIN	
    - 
    -	"データベースオブジェクトを管理する管理用ロール。DATABASE,WAREHOUSEの所有者権限を持つロール。"

  * - DB_ADMINISTRATOR
    - SYSADMIN
    - ◯
    - "開発管理者が使用するロール。SCHEMA以下のオブジェクト(テーブルなど)に対する所有者権限を有するロール。"

  * - ANALYST
    - SYSADMIN
    - ○
    - "分析者が使用するロール。本番環境で集計などを行う。"

  * - OPERATOR
    - SYSADMIN
    - ◯
    - "運用保守担当者が使用するロール。本番環境で調査・修正などを行う"

  * - BILLING_VIEWER
    - SYSADMIN
    - ◯
    - Snowflake請求画面の確認に使用するロール。

  * - QLIKSENSE_VIEWER
    - SYSADMIN
    - ◯
    - BIからのアクセスに使用するロール。

