liquidity = {
    ("tokenA", "tokenB"): (17, 10),
    ("tokenA", "tokenC"): (11, 7),
    ("tokenA", "tokenD"): (15, 9),
    ("tokenA", "tokenE"): (21, 5),
    ("tokenB", "tokenC"): (36, 4),
    ("tokenB", "tokenD"): (13, 6),
    ("tokenB", "tokenE"): (25, 3),
    ("tokenC", "tokenD"): (30, 12),
    ("tokenC", "tokenE"): (10, 8),
    ("tokenD", "tokenE"): (60, 25),
}

tokens = ["tokenA", "tokenB", "tokenC", "tokenD", "tokenE"]


def AmountsOut(liquidity, amountIn, path):
    if len(path) < 2:
        raise ValueError('Invalid path: Path should contain at least two tokens')

    amounts = [0] * len(path)
    amounts[0] = amountIn

    for i in range(len(path) - 1):
        reserveIn, reserveOut = GetReserves(liquidity, path[i], path[i + 1])
        amounts[i + 1] = GetAmountOut(amounts[i], reserveIn, reserveOut)

    return amounts


def GetReserves(liquidity, tokenIn, tokenOut):
    if (tokenIn, tokenOut) in liquidity:
        reserveIn, reserveOut = liquidity[(tokenIn, tokenOut)]
    else:
        reserveOut, reserveIn = liquidity[(tokenOut, tokenIn)]  # Swap reserves
    
    return reserveIn, reserveOut


def GetAmountOut(amountIn, reserveIn, reserveOut):
    # Example implementation, replace with actual logic to calculate output amount
    amount_in_with_fee = amountIn * 997  # Applying fee
    numerator = amount_in_with_fee * reserveOut
    denominator = reserveIn * 1000 + amount_in_with_fee  # Adding fee to reserveIn
    amountOut = numerator / denominator
    return amountOut


def find_cycles_with_token_B(liquidity, tokens):
    cycles = []
    for token in tokens:
        if token == "tokenB":
            path = ["tokenB"]
            find_cycles_recursive(liquidity, token, path, cycles)
    return cycles


def find_cycles_recursive(liquidity, current_token, path, cycles):
    if len(path) > 2:
        pathB = path + ["tokenB"]
        amountIn = 5
        amountsOut = AmountsOut(liquidity, amountIn, pathB)
        final_amount = amountsOut[-1]
        if final_amount > 20:
            cycles.append((pathB, final_amount))

    for token in tokens:
        if token not in path and ((current_token, token) in liquidity or (token, current_token) in liquidity):
            new_path = path + [token]
            find_cycles_recursive(liquidity, token, new_path, cycles)


cycles = find_cycles_with_token_B(liquidity, tokens)

max_amount = 0
max_Path = None
for cycle, final_amount in cycles:
    if final_amount > max_amount:
        max_amount = final_amount
        max_Path = cycle
max_Path_str = '->'.join(max_Path) 
print(f"path: {max_Path_str}, tokenB balance={max_amount:.10f}")
