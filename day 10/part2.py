def day10_part2_main() -> list[list[str]]:
    with open("day 10/inputs.txt", 'r') as inFile:
        instructions: list[list[str]] = [line.strip().split() for line in inFile.readlines()]
        
        pc:    int = 0 # Program counter
        x:     int = 1 # x register
        clock: int = 1 # Time measurement
        
        log:      list[int] = []    # Signal strength logging
        clocking: bool      = False # Wether or not current iteration should "skip a cycle"
        
        while pc != len(instructions):
            log.append(x)
            
            if clocking:
                x += int(instructions[pc][1])
                clock += 1
                pc += 1
                
                clocking = False
                
                continue
            
            if not clocking and instructions[pc][0] == "noop" :
                clock += 1
                pc += 1
            elif not clocking and instructions[pc][0] == "addx":
                clocking = True
                clock += 1
            elif instructions[pc][0] not in ["noop", "addx"]:
                raise NotImplementedError(f"Opcode `{instructions[pc][0]}` is not implemented")

        log.append(x)
        
        crt: list[list[str]] = [[' ' for i in range(40)] for j in range(6)]
        
        for cycle, xValue in enumerate(log[:241]):
            if xValue-1 <= int(cycle%40) <= xValue+1:
                crt[int(cycle/40)][int(cycle%40)] = '#'
        
        return crt

if __name__ == "__main__":
    screen: list[list[str]] = day10_part2_main()
    
    for scanLine in screen:
        print(''.join(scanLine))
