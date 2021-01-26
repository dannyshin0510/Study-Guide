[![forthebadge made-with-python](http://ForTheBadge.com/images/badges/made-with-python.svg)](https://www.python.org/)

# Welcome to challengeMe! :white_check_mark:

Pen and paper is cool, but you just gotta code it! :desktop_computer:

## Featuring 	:pushpin:

* Diverse Data Structures and Algorithms
* Optimized algorithm progressions
* Friendly comments:
  * explanations
  * time / space complexity
  * expected outputs
  * topic headings
  
## Format :bookmark_tabs:

#### Banks :classical_building:: for refreshing skills!
Example:
```bash
#LISTS
# ***********************************************
# append() - Add an element to the end of the list
# extend() - Add all elements of a list to the another list
# insert() - Insert an item at the defined index
                       .
                       .
# ***********************************************

# Demonstrating insert() method
odd = [2, 7]
odd.insert(1,3)

print(odd)

odd[2:2] = [12, 13]

print(odd)

# Expect:
# [2, 3, 7]
# [2, 3, 12, 13, 7]
```

#### Problems :mag:: for reviewing solutions!
Example:
```bash
# Jack submits his soccer team with the following numbers = [2,3,6,7]
# The jersy numbers must sum up to target = 7
# Please note that Jack has purchased numerous copies of each jersey number

def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
    dp = [[] for _ in range(target + 1)]
    for c in candidates:  # O(N): for each candidate
        for i in range(c, target + 1):  # O(M): for each possible value <= target
            if i == c: dp[i].append([c])
            for comb in dp[i - c]: dp[i].append(comb + [c])  # O(M) worst: for each combination
    return dp[-1]

# Time Complexity: O(M*M*N), N = len(candidates), M = target
# Space Complexity: O(M*M)
```
## Great for 	:monocle_face:

* Learning Algorithms
* Refreshing skills
* Preparing for competition/interviews
* Sharing tactics!

## Upcoming / In-development :construction_worker:
* Linear Programming:
* Spanning Trees
* Making sorting algorithms easier to understand

## Contributing :bulb:
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

