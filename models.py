from datetime import date as Date

EXERCISES = ["レッグプレス", "ショルダープレス", "チェストプレス", "ラットプルダウン", "懸垂"]


class Workout:
    def __init__(self, date, exercise, weight, reps, sets):
        #   1. date が存在しない日付
        Date.fromisoformat(date)
        #   2. exercise が EXERCISES に含まれていない
        if exercise not in EXERCISES:
            raise ValueError(f"Invalid exercise: {exercise}")
        #   3. weight が負
        if weight < 0:
            raise ValueError(f"Invalid weight: {weight}")
        #   4. reps または sets が 1 未満
        if reps < 1 or sets < 1:
            raise ValueError(f"Invalid reps or sets: {reps}, {sets}")
        self.date = date
        self.exercise = exercise
        self.weight = weight
        self.reps = reps
        self.sets = sets

    def to_dict(self):
        return {
            "date": self.date,
            "exercise": self.exercise,
            "weight": self.weight,
            "reps": self.reps,
            "sets": self.sets
        }

    @classmethod
    def from_dict(cls, data):
        return cls(**data)


if __name__ == "__main__":
    w = Workout("2026-11-05", "レッグプレス", 125, 12, 3)
    d = w.to_dict()
    print(d)
    print(Workout.from_dict(d).to_dict() == d)

    bad_inputs = [
        ("2026-02-30", "レッグプレス", 125, 12, 3),
        ("2026-11-05", "スクワット", 60, 10, 3),
        ("2026-11-05", "レッグプレス", -5, 12, 3),
        ("2026-11-05", "レッグプレス", 125, 0, 3),
    ]
    for args in bad_inputs:
        try:
            Workout(*args)
            print("NG: エラーが出なかった", args)
        except ValueError as e:
            print("OK:", e)