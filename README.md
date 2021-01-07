[![forthebadge made-with-python](http://ForTheBadge.com/images/badges/made-with-python.svg)](https://www.python.org/)

# Welcome to challengeMe! :white_check_mark:

Pen and paper is cool, but you just gotta code it! :desktop_computer:

## Featuring 	:pushpin:

* Diverse Data Structures and Algorithms
* Friendly comments:
  * explanations
  * time / space complexity
  * expected outputs
  * topic headings
* Optimized algorithm progressions
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
# Combination Sum.
# Input: candidates = [2,3,6,7], target = 7
# Output: [[2,2,3],[7]]
# Explanation:
# 2 and 3 are candidates, and 2 + 2 + 3 = 7. Note that 2 can be used multiple times.
# 7 is a candidate, and 7 = 7.
# These are the only two combinations.

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

