# Jumping on the Clouds

There is a new mobile game that starts with consecutively numbered clouds. Some of the clouds are thunderheads and others are cumulus. The player can jump on any cumulus cloud having a number that is equal to the number of the current cloud plus **_1_** or **_2_**. The player must avoid the thunderheads. Determine the minimum number of jumps it will take to jump from the starting postion to the last cloud. It is always possible to win the game.

For each game, you will get an array of clouds numbered **_0_** if they are safe or **_1_** if they must be avoided.

## Example:
c = [0,1,0,0,0,1,0]

Index the array from **_0...6_**. The number on each cloud is its index in the list so the player must avoid the clouds at indices **_1_** and **_5_**. They could follow these two paths: **_0 -> 2 -> 4 -> 6_** or **_0 -> 2 -> 3 -> 4 -> 6_**. The first path takes **_3_** jumps while the second takes **_4_**. Return **_3_**.

## Function Description:

Complete the jumpingOnClouds function in the editor below.

jumpingOnClouds has the following parameter(s):

* int c[n]: an array of binary integers
## Returns:

* int: the minimum number of jumps required
## Input Format:

The first line contains an integer **_n_**, the total number of clouds. The second line contains **_n_** space-separated binary integers describing clouds **_c[i]_** where **_0 <= i < n_**.

## Constraints:
* 2 <= n <= 100
* c[i] belongs {0,1}
* c[0] = c[n-1] = 0
## Output Format:

Print the minimum number of jumps needed to win the game.

## Sample Input 0:

7\
0 0 1 0 0 1 0
## Sample Output 0:

4
## Explanation 0:
The player must avoid **_c[2]_** and **_c[5]_**. The game can be won with a minimum of **_4_** jumps:

![alt text](https://s3.amazonaws.com/hr-challenge-images/20832/1461134731-c258160d15-jump2.png "4 jumps")

## Sample Input 1:

6\
0 0 0 0 1 0
## Sample Output 1:

3
## Explanation 1:
The only thundercloud to avoid is **_c[4]_**. The game can be won in **_3_** jumps:

![alt text](https://s3.amazonaws.com/hr-challenge-images/20832/1461136358-764298d363-jump5.png "3 jumps")
