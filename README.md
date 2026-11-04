# workout-log-cli
筋トレの記録を行うアプリ

## 要件
- 記録の追加：日付・種目・重量・回数・セット数
- 一覧表示
- 種目別の最大重量の表示
- JSONファイルへの保存・読み込み

## クラス設計
### Workout（1回分の記録）
- 属性：date, exercise, weight, reps, sets
- メソッド：to_dict(), from_dict()
- 拒否する値：存在しない日付、登録されていない種目、負の重量、1未満の回数・セット数

### WorkoutLog（記録の集まり）
- 属性：workouts
- メソッド：add(), all(), filter_by_exercise(), filter_by,date(), max_weight()

## ファイル構成
- `models.py`：Workout / WorkoutLog
- `storage.py`：JSON保存・読み込み
- `cli.py`：入力と表示
- `tests/`：pytestのテスト

## 11月のマイルストーン
- 第1週（11/2〜）：モデル＋テスト
- 第2週（11/9〜）：保存・CLI
- 第3週（11/16〜）：集計機能
- 第4週（11/23〜）：仕上げ・公開