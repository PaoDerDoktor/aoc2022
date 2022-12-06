def day6_part2_main() -> int:
    with open("day 06/inputs.txt", 'r') as inFile:
        data: str = inFile.read().strip()
        
        for i in range(13, len(data)-1):
            elementsSet: set[str] = {l for l in data[i-13:i+1]}
            if len(elementsSet) == 14:
                return i+1
        
        return -1
    
if __name__ == "__main__":
    print(day6_part2_main())
