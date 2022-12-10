def day10_part1_main() -> int:
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
        coefficients: list[int] = [i for i in range(20, len(log), 40)]
        
        timedAcc: list[int] = [i*log[i-1] for i in coefficients]
        
        return sum(timedAcc)

if __name__ == "__main__":
    print(day10_part1_main())
