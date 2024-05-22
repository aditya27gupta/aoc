from typing import List, Dict
import re


class Solve:
    def __init__(self):
        self.stats: Dict = {}
        self.max_points: int = 0

    def parse_stats(self, stats: List[str]) -> None:
        for stat in stats:
            matches = re.findall(r"\d+", stat)
            name: str = stat.split()[0]
            self.stats[name] = {
                "speed": int(matches[0]),
                "duration": int(matches[1]),
                "rest_time": int(matches[2]),
                "points": 0,
                "distance_covered": 0,
            }

    def is_resting(self, name: str, current_second: int) -> bool:
        rem = current_second % (
            self.stats[name]["duration"] + self.stats[name]["rest_time"]
        )
        if rem in range(1, self.stats[name]["duration"] + 1):
            return False
        else:
            return True

    def get_points(self, max_distance):
        for name in self.stats.keys():
            if self.stats[name]["distance_covered"] == max_distance:
                self.stats[name]["points"] += 1
                if self.max_points < self.stats[name]["points"]:
                    self.max_points = self.stats[name]["points"]

    def winner_after_duration(self, duration: int) -> int:
        max_distance = 0

        for i in range(1, duration + 1):
            for name in self.stats.keys():
                if self.is_resting(name, i):
                    continue
                else:
                    self.stats[name]["distance_covered"] += self.stats[name]["speed"]
                    if self.stats[name]["distance_covered"] > max_distance:
                        max_distance = self.stats[name]["distance_covered"]

            self.get_points(max_distance)

        return max_distance


def main() -> None:
    with open("./input.txt", mode="r") as file:
        stats: str = file.readlines()

    solver = Solve()
    solver.parse_stats(stats)
    result = solver.winner_after_duration(duration=2503)
    print(result)
    print(solver.max_points)


if __name__ == "__main__":
    main()
