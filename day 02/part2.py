WIN_LOSS_SCORE: dict[str, dict[str, int]] = {
    "A": {
        "A": 3,
        "B": 6,
        "C": 0
    },
    "B": {
        "A": 0,
        "B": 3,
        "C": 6,
    },
    "C": {
        "A": 6,
        "B": 0,
        "C": 3
    }
}

CHOICE_SCORE: dict[str, int] = {
    "A": 1,
    "B": 2,
    "C": 3
}

CHOICE: dict[str, dict[str, str]] = {
    "A": {
        "X": "C",
        "Y": "A",
        "Z": "B"
    },
    "B" : {
        "X": "A",
        "Y": "B",
        "Z": "C"
    },
    "C": {
        "X": "B",
        "Y": "C",
        "Z": "A"
    }
}

def day2_part2_main(verbose: bool=True) -> int:
    with open("day 02/inputs.txt", 'r') as inFile:
        rounds: list[tuple[str, str]] = [(roundLine[0], roundLine[2]) for roundLine in inFile.readlines()]

        score: int = 0
        for round in rounds:
            playedShape: str = CHOICE[round[0]][round[1]]
            
            score += CHOICE_SCORE[playedShape]
            score += WIN_LOSS_SCORE[round[0]][playedShape]
            
            if verbose:
                print(f"{round[1]} : {round[0]} VS {playedShape}({CHOICE_SCORE[playedShape]}) -> {WIN_LOSS_SCORE[round[0]][playedShape]}")
            
        return score
        
        
if __name__ == "__main__":
    print(day2_part2_main(False))
