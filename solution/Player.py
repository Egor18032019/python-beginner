from Variants import Variants


class Player:
    def __init__(self, *, variants: Variants, name: str) -> None:
        self.variants = variants
        self.name = name

    def whoWins(self, *, target: "Player"):
        if self.variants == Variants.SCISSORS and target.variants == Variants.ROCK:
            return target
        if self.variants == Variants.ROCK and target.variants == Variants.SCISSORS:
            return self

        if self.variants == Variants.PAPER and target.variants == Variants.SCISSORS:
            return target
        if self.variants == Variants.SCISSORS and target.variants == Variants.PAPER:
            return self

        if self.variants == Variants.PAPER and target.variants == Variants.ROCK:
            return target
        if self.variants == Variants.ROCK and target.variants == Variants.PAPER:
            return self

    def whoWinsDefault(self, foo, target) -> None:
        if foo.variants == Variants.SCISSORS and target.variants == Variants.ROCK:
            print(f"{target.name} wins! with {foo.name}")
        if foo.variants == Variants.ROCK and target.variants == Variants.SCISSORS:
            print(f"{foo.name} wins! with {target.name}")

        if foo.variants == Variants.PAPER and target.variants == Variants.SCISSORS:
            print(f"{target.name} wins! with {foo.name}")
        if foo.variants == Variants.SCISSORS and target.variants == Variants.PAPER:
            print(f"{foo.name} wins! with {target.name}")

        if foo.variants == Variants.PAPER and target.variants == Variants.ROCK:
            print(f"{target.name} wins! with {foo.name}")
        if foo.variants == Variants.ROCK and target.variants == Variants.PAPER:
            print(f"{foo.name} wins! with {target.name}")

    def __str__(self) -> str:
        return f"{self.name} with variants: {self.variants.value} "


