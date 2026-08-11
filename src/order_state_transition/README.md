# Order State Transition

## テーマ

注文の状態によって実行できる操作や次に遷移できる状態が異なる処理を、Stateパターンに基づいて表現します。

注文にはDraft、Paid、Shipped、Cancelledといった状態があります。Draftでは支払いまたはキャンセルができますが、Paidでは発送のみが可能です。ShippedやCancelledの注文はそれ以上状態を変更できません。

このような状態ごとの条件分岐をOrderやUsecaseに集めず、それぞれのStateクラスに閉じ込めます。利用側は現在の状態や遷移条件を意識せず、Orderに対して共通の操作を実行できる構造を目指します。

## 目的

- 状態によって変化する振る舞いをStateクラスに分離する
- OrderやUsecaseに状態判定の条件分岐が増えることを防ぐ
- 許可された状態遷移と不正な状態遷移を明確にする
- Orderを具体的なStateクラスから分離する
- 新しい状態や遷移を追加するときの変更範囲を限定する

## 処理の流れ

```text
操作の入力
  ↓
Usecase
  ↓
Orderに対してpay、ship、cancelのいずれかを実行
  ↓
現在のOrderStateに処理を委譲
  ↓
遷移可能かを判定
  ↓
次のOrderStateへ遷移
```

Orderは現在のOrderStateを保持し、状態に関係する処理を共通のOrderState Portへ委譲します。各具象Stateは、自分の状態で許可されている操作と遷移先を決定します。そのため、Usecaseは状態ごとの実装差分を意識せず、Orderに対して同じ操作を実行できます。

想定する基本的な状態遷移は次のとおりです。

```text
Draft ── pay ──→ Paid ── ship ──→ Shipped
  │
  └── cancel ──→ Cancelled
```
