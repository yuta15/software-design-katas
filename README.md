# Pattern Matrix

## このリポジトリについて

アーキテクチャやデザインパターンを、実際にコードを書きながら学ぶための練習用リポジトリです。

小さなテーマごとに実装し、クラスの責務、依存関係、レイヤーの境界、パターンの組み合わせ方について理解を深めることを目的としています。機能としての完成度を追求するのではなく、テーマの理解に必要な要素に焦点を当てています。

## リポジトリの見方

練習コードは、`src`ディレクトリ配下にテーマごとのディレクトリを分けて配置しています。

```text
src/
└── <theme>/
    ├── README.md
    ├── class.png
    └── ...
```

各テーマのディレクトリには、次の内容が含まれます。

- `README.md`: テーマの目的や、扱っているアーキテクチャ・デザインパターンの説明
- `class.png`: 実装を構成するクラスと、その関係を表したクラス図
- その他のファイル: テーマに沿った実装コード

各テーマの詳細については、それぞれのディレクトリ配下にある`README.md`を確認してください。クラス図で全体の構造と依存関係を把握してからコードを読むと、実装の意図を追いやすくなります。

## 学習テーマ

| 項番 | 名称 | テーマ |
| ---: | --- | --- |
| 1 | [Multi-format Output](./src/multi_format_output/README.md) | 複数形式へのデータ出力とClean Architecture |
| 2 | [Order State Transition](./src/order_state_transition/README.md) | 注文の状態遷移とStateパターン |
| 3 | [HTTP Client Decorator](./src/http_client_decorator/README.md) | HTTPクライアントへの機能追加とDecoratorパターン |
| 4 | [Invoice Batch Observer](./src/batch_progress_observer/README.md) | 請求書一括発行とObserverパターン |
