littering = 0.01
is_clean = True
prev_cnt = 5380
cnt = 5380
garbage = 2910000
personal_cost = 2548100000
recycling_profit = 1844 * 29100
collection_rate = 0.99
recycling_rate = 40
clean_rate = 1
gradient = (875 / 2120) * 0.0001


def update():

    global littering, personal_cost

    if cnt != prev_cnt:
        littering += gradient * (cnt - prev_cnt)
        personal_cost *= (1 / 2120) * (cnt - prev_cnt)
        collection_rate = 1 - littering


def p():

    if littering == 1:
        return 0

    if is_clean:
        return 1 - littering
    else:
        return 0.8 * (1 - littering)


def t(c):
    return c * (cnt - prev_cnt) / 10 + personal_cost


def r(tc, rr):

    global recycling_profit
    recycling_profit = collection_rate * garbage * 1844 * (rr / 40)

    if recycling_profit < tc:
        return 0
    else:
        return 1


def run():

    pleasent_rate = p()

    costs = [250000, 700000, 2400000]
    recycling_rates = []

    for c in costs:
        total_cost = t(c)

        if clean_rate == 1:
            recycling_rates = [20, 40]
        else:
            recycling_rates = [20, 40, 60, 80]

        for rr in recycling_rates:
            print(f"쓰레기통 개수: {cnt}/ 쓰레기통 비용: {c} /", end=" ")
            print(f"청결도: {clean_rate} / 재활용율: {rr}")
            print(f"-> 거리 쾌적도: {pleasent_rate}입니다.")
            print(f"-> 연간 추가 쓰레기통 총 비용: {total_cost}입니다.")
            print(f"-> 연간 재활용 이익: {recycling_profit}입니다.")
            print("-> 연간 재활용 이익은 연간 쓰레기 비용보다", end=" ")

            res = r(total_cost, rr)

            if res == 1:
                print("크거나 같습니다")
            else:
                print("작습니다")


def f():
    update()
    run()


cnt, clean_rate = map(int, input().split())
f()
