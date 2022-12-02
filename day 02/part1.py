WIN_LOSS_SCORE: dict[str, dict[str, int]] = {
    "A": {
        "X": 3,
        "Y": 6,
        "Z": 0
    },
    "B": {
        "X": 0,
        "Y": 3,
        "Z": 6,
    },
    "C": {
        "X": 6,
        "Y": 0,
        "Z": 3
    }
}

CHOICE_SCORE: dict[str, int] = {
    "X": 1,
    "Y": 2,
    "Z": 3
}

def day2_part1_main(verbose: bool=True) -> int:
    with open("day 02/inputs.txt", 'r') as inFile:
        rounds: list[tuple[str, str]] = [(roundLine[0], roundLine[2]) for roundLine in inFile.readlines()]

        score: int = 0
        for round in rounds:
            score += WIN_LOSS_SCORE[round[0]][round[1]]
            score += CHOICE_SCORE[round[1]]
            
            if verbose:
                print(f"{round[0]} VS {round[1]}({CHOICE_SCORE[round[1]]}) -> {WIN_LOSS_SCORE[round[0]][round[1]]}")
        
        return score

if __name__ == "__main__":
    print(day2_part1_main(False))
