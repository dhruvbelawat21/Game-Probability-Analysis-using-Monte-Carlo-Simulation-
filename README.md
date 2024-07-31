
PART 4:

There is no optimal strategy. No strategy effects the chances of a team to win the competition.

Let 
𝐴
=
∑
𝑖
=
1
𝑚
𝑎
𝑖
A= 
i=1
∑
m
​
 a 
i
​
  and 
𝐵
=
∑
𝑖
=
1
𝑛
𝑏
𝑖
.
B= 
i=1
∑
n
​
 b 
i
​
 . Then the chances of a team to win are proportional to its total strength, i.e., for the first team, it is 
𝐴
𝐴
+
𝐵
;
A+B
A
​
 ; for the second, it is 
𝐵
𝐴
+
𝐵
.
A+B
B
​
 .

The proof is by induction on 
𝑛
+
𝑚
,
n+m, assuming both 
𝑛
n and 
𝑚
m are greater than zero.

The claim is certainly true for 
𝑚
=
𝑛
=
1.
m=n=1. Assume it is true for 
𝑚
+
𝑛
=
𝑁
,
m+n=N, and let now that one team still has 
𝑚
m members, the other membership of the other grew to 
𝑛
+
1.
n+1.

So now 
𝐴
=
∑
𝑖
=
1
𝑚
𝑎
𝑖
A= 
i=1
∑
m
​
 a 
i
​
  and 
𝐵
=
∑
𝑖
=
1
𝑛
+
1
𝑏
𝑖
.
B= 
i=1
∑
n+1
​
 b 
i
​
 .

For the first duel, the first team sends a gladiator of strength 
𝑎
,
a, the second a gladiator of strength 
𝑏
.
b. The first wins with the probability of 
𝑎
𝑎
+
𝑏
,
a+b
a
​
 , the second with the probability of 
𝑏
𝑎
+
𝑏
.
a+b
b
​
 .

Depending on who wins that duel, there will be two possible distributions of strength:

𝑎
a wins: 
{
𝑎
1
,
…
,
𝑎
+
𝑏
,
…
,
𝑎
𝑚
}
{a 
1
​
 ,…,a+b,…,a 
m
​
 } and 
{
𝑏
1
,
…
,
𝑏
‾
…
,
𝑏
𝑛
+
1
}
,
{b 
1
​
 ,…, 
b
 …,b 
n+1
​
 },

𝑏
b wins: 
{
𝑎
1
,
…
,
𝑎
‾
,
…
,
𝑎
𝑚
}
{a 
1
​
 ,…, 
a
 ,…,a 
m
​
 } and 
{
𝑏
1
,
…
,
𝑏
+
𝑎
…
,
𝑏
𝑛
+
1
}
,
{b 
1
​
 ,…,b+a…,b 
n+1
​
 },

where overline means the absence of the fighter.

According to the induction assumption, in the first case, the chances of the first team to win equal 
𝐴
+
𝑏
𝐴
+
𝐵
,
A+B
A+b
​
 , in the second case they are equal to 
𝐴
−
𝑎
𝐴
+
𝐵
,
A+B
A−a
​
 , making the overall probability to be

\begin{align} P_a &= \frac{a}{a+b} \cdot \frac{A+b}{A+B} + \frac{b}{a+b} \cdot \frac{A-a}{A+B}\ &= \frac{a(A+b) + b(A-a)}{(a+b)(A+B)}\ &= \frac{aA + ab + bA - ab}{(a+b)(A+B)}\ &= \frac{aA + bA}{(a+b)(A+B)}\ &= \frac{(a+b)A}{(a+b)(A+B)}\ &= \frac{A}{A+B} \end{align}

The code for part 4 is given below wherein we have selected any warrior at random for both the arrays.
