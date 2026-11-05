from datetime import date as Date

EXERCISES = [
    "レッグプレス", "ショルダープレス", "チェストプレス", "ラットプルダウン", "懸垂",
    "ペックフライ", "ケーブルプルオーバー",
]


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

class WorkoutLog:
    def __init__(self):
        self.workouts = []   # Workout を入れるリスト

    def add(self, workout):
        if not isinstance(workout, Workout):
            raise TypeError(f"Workoutを追加してください（受け取った型：{type(workout).__name__}）")
        self.workouts.append(workout)

    def all(self):
        return list(self.workouts)

    def filter_by_exercise(self, name):
        return [w for w in self.workouts if w.exercise == name]

    def __len__(self):
        return len(self.workouts)


if __name__ == "__main__":
    log = WorkoutLog()
    log.add(Workout("2026-11-05", "レッグプレス", 135, 10, 3))
    log.add(Workout("2026-11-05", "ショルダープレス", 32, 9, 3))
    log.add(Workout("2026-11-07", "レッグプレス", 135, 10, 3))

    print(len(log))
    print(len(log.filter_by_exercise("レッグプレス")))
    print(log.filter_by_exercise("懸垂"))

    copied = log.all()
    copied.clear()
    print(len(log))

    try:
        log.add({"exercise": "レッグプレス"})
    except TypeError as e:
        print("OK:", e)