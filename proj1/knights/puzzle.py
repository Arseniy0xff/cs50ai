from logic import *

AKnight = Symbol("A is a Knight")
AKnave = Symbol("A is a Knave")

BKnight = Symbol("B is a Knight")
BKnave = Symbol("B is a Knave")

CKnight = Symbol("C is a Knight")
CKnave = Symbol("C is a Knave")


base_rules = And(
    Or(AKnight, AKnave), Not(And(AKnight, AKnave)),
    Or(BKnight, BKnave), Not(And(BKnight, BKnave)),
    Or(CKnight, CKnave), Not(And(CKnight, CKnave))
)

# Puzzle 0
# A says "I am both a knight and a knave."
knowledge0 = And(
    base_rules,
    Biconditional(Biconditional(AKnight, Not(AKnave)), And(AKnight, AKnave))
)

# Puzzle 1
# A says "We are both knaves."
# B says nothing.
knowledge1 = And(
    knowledge0,
    Biconditional(Biconditional(AKnight, Not(AKnave)), And(AKnave, BKnave))
)

# Puzzle 2
# A says "We are the same kind."
# B says "We are of different kinds."
knowledge2 = And(
    knowledge1,
    Biconditional(Biconditional(AKnight, Not(AKnave)), Or(Biconditional(AKnight, BKnight), Biconditional(AKnave, BKnave))),
    Biconditional(Biconditional(BKnight, Not(BKnave)), Or(Not(Biconditional(AKnight, BKnight)), Not(Biconditional(AKnave, BKnave)))),

)

# Puzzle 3
# A says either "I am a knight." or "I am a knave.", but you don't know which.
# B says "A said 'I am a knave'."
# B says "C is a knave."
# C says "A is a knight."
knowledge3 = And(
    knowledge2,
    Biconditional(Biconditional(AKnight, Not(AKnave)), Or(AKnight, AKnave)),
    Biconditional(Biconditional(BKnight, Not(BKnave)), And(
        Biconditional(Biconditional(AKnight, Not(AKnave)),
                      AKnave),
        CKnave)),

    Biconditional(Biconditional(CKnight, Not(CKnave)), AKnight)
)


def main():
    symbols = [AKnight, AKnave, BKnight, BKnave, CKnight, CKnave]
    puzzles = [
        ("Puzzle 0", knowledge0),
        ("Puzzle 1", knowledge1),
        ("Puzzle 2", knowledge2),
        ("Puzzle 3", knowledge3)
    ]
    for puzzle, knowledge in puzzles:
        print(puzzle)
        if len(knowledge.conjuncts) == 0:
            print("    Not yet implemented.")
        else:
            for symbol in symbols:
                if model_check(knowledge, symbol):
                    print(f"    {symbol}")


if __name__ == "__main__":
    main()
