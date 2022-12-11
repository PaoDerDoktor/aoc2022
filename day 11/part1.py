import math

def execute_operation(oldValue: int, tokens: list[str]) -> int:
    if tokens[1] == "*":
        return (int(tokens[0]) if tokens[0]!="old" else oldValue) * (int(tokens[2]) if tokens[2]!="old" else oldValue)
    elif tokens[1] == "+":
        return (int(tokens[0]) if tokens[0]!="old" else oldValue) + (int(tokens[2]) if tokens[2]!="old" else oldValue)
    else:
        raise NotImplementedError(f"Following string is not an implemented operator : `{tokens[1]}`.")

def day11_part1_main() -> int:
    with open("day 11/inputs.txt", 'r') as inFile:
        rawMonkeys: list[str] = [rawMonkey.strip() for rawMonkey in inFile.read().split("\n\n")]
        
        inspections: list[int]                  = [0 for _ in rawMonkeys]
        inventories: list[list[int]]            = []
        operations:  list[list[str]]            = []
        tests:       list[tuple[int, int, int]] = [] # (argument, destinationTrue, destinationFalse)
        
        for rawMonkey in rawMonkeys:
            splitMonkey: list[list[str]] = [line.strip().split() for line in rawMonkey.split('\n')]
            
            inventories.append([int(object) if object[-1] != ',' else int(object[:-1]) for object in splitMonkey[1][2:]][::-1])
            operations.append(splitMonkey[2][3:])
            tests.append((int(splitMonkey[3][-1]), int(splitMonkey[4][-1]), int(splitMonkey[5][-1])))
            
        for turn in range(20):
            for monkey in range(len(inventories)):
                objPointer: int = len(inventories[monkey])-1
                while objPointer != -1:
                    inspections[monkey] += 1
                    worryLevel: int =  math.floor(execute_operation(inventories[monkey].pop(), operations[monkey])/3)
                    if worryLevel % tests[monkey][0] == 0:
                        inventories[tests[monkey][1]].insert(0, worryLevel)
                    else:
                        inventories[tests[monkey][2]].insert(0, worryLevel)
                    objPointer -= 1
                
        
        return math.prod(sorted(inspections)[-2:])

if __name__ == "__main__":
    print(day11_part1_main())
