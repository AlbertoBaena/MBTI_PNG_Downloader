# How to use?
You just have download it and run it on the folder in which you may download the PNGs.
# How does it work?
If you read the code, you'll come across this matrix in which I gave a coordinate to each letter of the MBTI types:
|   | 0 | 1 | 2 | 3 |
| :------------: | :------------: | :------------: | :------------: | :------------: |
| 0 | E | N | F | J |
| 1 | I | S | T | P |

Getting the vertical coordinates of each type, I got this binary code:
| **E/I** | **N/S** | **F/T** | **J/P** | **MBTI Type**  |
| :------------: | :------------: | :------------: | :------------: | :------------: |
| 0 | 0 | 0 | 0 | ENFJ  |
| 1 | 0 | 0 | 1 | INFJ  |
| 0 | 1 | 0 | 0 | ESFJ  |
| 1 | 1 | 0 | 1 | ISFJ  |
| 0 | 0 | 1 | 0 | ENTJ  |
| 1 | 0 | 1 | 1 | INTJ  |
| 0 | 1 | 1 | 0 | ESTJ  |
| 1 | 1 | 1 | 1 | ISTJ  |
| 0 | 0 | 0 | 0 | ENFP  |
| 1 | 0 | 0 | 1 | INFP  |
| 0 | 1 | 0 | 0 | ESFP  |
| 1 | 1 | 0 | 1 | ISFP  |
| 0 | 0 | 1 | 0 | ENTP  |
| 1 | 0 | 1 | 1 | INTP  |
| 0 | 1 | 1 | 0 | ESTP  |
| 1 | 1 | 1 | 1 | ISTP  |

In each column, 0 means the first letter and 1 the second one.

## Iterations
The code will iterate 16 times, one for each MBTI type.
Inside each iteration there will be another 4 iterations, one for each letter.
To get each type, I used the binary numbers associated in order to get the coordinates on the matrix.

## Getting the PNGs
If you go to https://www.16personalities.com/images/types/[type].png, you'll get a PNG of that type.
Thus, I just get the letters and put them in the URL.
