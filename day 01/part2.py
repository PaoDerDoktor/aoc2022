def day1_part2_main() -> int:
    with open("day 01/inputs.txt", 'r') as inFile:
        calories: list[int] = [sum([int(cal) for cal in calories.split()]) for calories in inFile.read().split("\n\n")]
        
        calories = sorted(calories)
        
        return sum(calories[-3:])

if __name__ == "__main__":
    print(day1_part2_main())
