import pytest
from models import Workout

def test_正しい値で作成できる():
    w = Workout("2026-11-05", "レッグプレス", 125, 12, 3)
    assert w.exercise == "レッグプレス"
    assert w.weight == 125


def test_to_dictからfrom_dictで元に戻る():
    w = Workout("2026-11-05", "レッグプレス", 125, 12, 3)
    d = w.to_dict()
    w2 = Workout.from_dict(d)
    assert w2.to_dict() == d


def test_存在しない日付でエラー():
    with pytest.raises(ValueError):
        Workout("2026-02-30", "レッグプレス", 125, 12, 3)

def test_登録されていない種目でエラー():
    with pytest.raises(ValueError):
        Workout("2026-02-28", "ベンチプレス", 125, 12, 3)

def test_重量が負でエラー():
    with pytest.raises(ValueError):
        Workout("2026-02-28", "レッグプレス", -125, 12, 3)


def test_重量0なら作成できる():
    w = Workout("2026-02-28", "懸垂", 0, 6, 3)
    assert w.weight == 0
    

def test_回数またはセット数が1未満でエラー():
    with pytest.raises(ValueError):
        Workout("2026-02-28", "レッグプレス", 125, 0, 3)
    with pytest.raises(ValueError):
        Workout("2026-02-28", "レッグプレス", 125, 12, 0)
