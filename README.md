# 2024-Spring-HW2

Please complete the report problem below:

## Problem 1
Provide your profitable path, the amountIn, amountOut value for each swap, and your final reward (your tokenB balance).

> Solution
<img width="549" alt="截圖 2024-04-12 下午11 04 30" src="https://github.com/b12901183/Homework-2/assets/161189253/65973684-4444-40f7-9332-ad5ae4e5af90">
<img width="297" alt="截圖 2024-04-12 下午11 03 48" src="https://github.com/b12901183/Homework-2/assets/161189253/1496ae75-84e5-4052-aea4-179b25321b5a">

## Problem 2
What is slippage in AMM, and how does Uniswap V2 address this issue? Please illustrate with a function as an example.

> 
slippage is price change before swaping,we uniswap can set a minimum amount out
<img width="797" alt="截圖 2024-04-12 下午5 27 17" src="https://github.com/b12901183/Homework-2/assets/161189253/0c44320a-f339-4863-a807-72f8b32684d7">

## Problem 3
Please examine the mint function in the UniswapV2Pair contract. Upon initial liquidity minting, a minimum liquidity is subtracted. What is the rationale behind this design?


> This ensures the total supply is always greater than zero, preventing division by zero errors.

## Problem 4
Investigate the minting function in the UniswapV2Pair contract. When depositing tokens (not for the first time), liquidity can only be obtained using a specific formula. What is the intention behind this?
<img width="766" alt="截圖 2024-04-12 下午5 43 31" src="https://github.com/b12901183/Homework-2/assets/161189253/68f28179-a5f6-486c-a5c4-a3c280c0b19a">
maintain the pool 50/50

> Solution

## Problem 5
What is a sandwich attack, and how might it impact you when initiating a swap?


> A bigger order placed before my smaller order, then moved the price against me, ending up receiving fewer tokens

