学习笔记

进度越来越吃力了，难

记一个重点

动态规划的关键点：

1. 最优子结构 

   dp[n] = best_of(dp[n - 1], dp[n - 2],…)

2. 储存中间状态 dp[i]

3. 递推公式（状态转移方程或者dp方程）

   Fib：dp[i] = dp[i - 1] + dp[i - 2]
