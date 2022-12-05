def pad(s: str, length: int) -> str:
    while len(s) < length:
        s += ' '
    return s

def day5_part1_main() -> str:
    with open("day 05/inputs.txt", 'r') as inFile:
        inLines: list[str] = [line for line in inFile.readlines()]
        
        stacksLines: list[str] = []
        
        lineBuffer: str = inLines[0][:-1]
        lineNumber: int = 1
        while lineBuffer != "":
            stacksLines.append(lineBuffer)
            lineBuffer = inLines[lineNumber][:-1]
            lineNumber += 1
            
        stacks: dict[int, list[str]] = {} # 0 is bottom, len(stacks)[-1] is top
        for i in stacksLines[-1].split():
            stacks[int(i)] = []
        
        for stacksLine in stacksLines[:-1][::-1]:
            for stack, crate in enumerate(pad(stacksLine, len(stacks)*4)[1::4]):
                if crate != ' ':
                    stacks[stack+1].append(crate)
        
        instructions: list[tuple[int, int, int]] = [
            (int(line.split()[1]), int(line.split()[3]), int(line.split()[5])) for line in inLines[lineNumber:]
        ] # 0: amount, 1 : origin, 2: destination
        
        # Parsing is done
        
        for instruction in instructions:
            for _ in range(instruction[0]):
                stacks[instruction[2]].append(stacks[instruction[1]].pop())
        
        # Moving is done
        
        result: str = ""
        for stack in stacks:
            result += stacks[stack][-1]
        
        return result

if __name__ == "__main__":
    print(day5_part1_main())
