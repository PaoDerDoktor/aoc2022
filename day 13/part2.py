from typing import Union
from copy import deepcopy

package = list[Union[int, "package"]]


def compare(left: package, right: package, verbose: bool=False) -> bool:
    queue:   list[int] = [0]
    if verbose: print('------ NEW COMPARISON ------')
    if verbose: print(f"{left=}, {right=}")
    
    left = deepcopy(left)
    right = deepcopy(right)
    while len(queue) != 0:
        if queue[-1] >= len(left[-1]) or queue[-1] >= len(right[-1]):
            if verbose: print(f"Lists `{left[-1]}` and `{right[-1]}` with index `{queue[-1]}` came to an endpoint")
            if len(left[-1]) < len(right[-1]):
                if verbose: print(f"\tIt was `{right[-1]}`'s. Pair is unordered.")
                return True
            elif len(left[-1]) > len(right[-1]):
                if verbose: print(f"\tIt was `{right[-1]}`'s. Pair is ordered.")
                return False
            else:
                if verbose: print(f"\tIt was both's. Continuing research by going up one list-level.")
                queue.pop()
                left.pop()
                right.pop()
        elif isinstance(left[-1][queue[-1]], int) and isinstance(right[-1][queue[-1]], int):
            if verbose: print(f"Comparing two integers of `{left[-1]}` and `{right[-1]}` at index `{queue[-1]}`.")
            if left[-1][queue[-1]] < right[-1][queue[-1]]:
                if verbose: print(f"\tLeft was inferior. Pair is ordered.")
                return True
            elif left[-1][queue[-1]] > right[-1][queue[-1]]:
                if verbose: print(f"\tRight was inferior. Pair is unordered.")
                return False
            else:
                if verbose: print(f"\tBoth were equal. Continuing research")
                queue[-1] += 1
        elif isinstance(left[-1][queue[-1]], list) and isinstance(right[-1][queue[-1]], list):
            if verbose: print(f"Hopping into sublists of `{left[-1]}` and `{right[-1]}` at index `{queue[-1]}`.")
            queue[-1] += 1
            queue.append(0)
            left.append(left[-1][queue[-2]-1])
            right.append(right[-1][queue[-2]-1])
            if verbose: print(f"New sublists are : `{left[-1]}` and `{right[-1]}`.")
        elif isinstance(left[-1][queue[-1]], list) and isinstance(right[-1][queue[-1]], int):
            if verbose: print(f"Left is a list (`{left[-1]}`) while right is an int (`{right[-1]}`). Converting right to a list")
            right[-1][queue[-1]] = [right[-1][queue[-1]]]
        elif isinstance(left[-1][queue[-1]], int) and isinstance(right[-1][queue[-1]], list):
            if verbose: print(f"Left is an int (`{left[-1]}`) while right is a list (`{right[-1]}`). Converting left to a list")
            left[-1][queue[-1]] = [left[-1][queue[-1]]]

def day13_part2_main(verbose: bool=False) -> int:
    with open("day 13/inputs.txt", 'r') as inFile:
        groups: list[tuple[package, package]] = [(eval(group.strip().split("\n")[0]), eval(group.strip().split("\n")[1])) for group in inFile.read().split("\n\n")]
        
        wholeMessage: list[package] = [[[2]], [[6]]]
        for group in groups:
            wholeMessage.append(group[0])
            wholeMessage.append(group[1])
            
        for i in range(len(wholeMessage)-1, 0, -1):
            for j in range(i):
                if compare([wholeMessage[j]], [wholeMessage[j+1]]):
                    wholeMessage[j], wholeMessage[j+1] = wholeMessage[j+1], wholeMessage[j]
            
        indices: list[int] = []
        
        wholeMessage = wholeMessage[::-1]
        
        for i in range(len(wholeMessage)):
            if wholeMessage[i] == [[2]] or wholeMessage[i] == [[6]]:
                indices.append(i+1)
                
        return indices[0]*indices[1]

if __name__ == "__main__":
    print(day13_part2_main())
