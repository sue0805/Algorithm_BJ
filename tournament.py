n, player1, player2 = map(int, input().split())
player1, player2 = min(player1, player2), max(player1, player2)

rounds = 1
meet = False
while n > 1:
    if player2 - player1 == 1 and player1 % 2 == 1:
        meet = True
        break

    player1 = player1 // 2 if player1 % 2 == 0 else player1 // 2 + 1
    player2 = player2 // 2 if player2 % 2 == 0 else player2 // 2 + 1

    n = n // 2 if n % 2 == 0 else n // 2 + 1
    rounds += 1

print(rounds if meet else -1)