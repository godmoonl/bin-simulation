import matplotlib.pyplot as plt

prev_cnt = 5380
cnt = 5380

st = ed = d = 0

garbage = 2910000
total_salay = 2548100000
personal_cost = 2548100000
recycling_profit = 1844 * 29100

ittering = 0.01
collection_rate = 0
recycling_rate = 40
clean_rate = 1

gradient = (875 / 2120) * 0.0001

costs = [250000, 700000, 2400000]

tcs = [[0 for j in range(2120)] for i in range(3)]
rps = [[0 for j in range(2120)] for i in range(3)]


def graph():
    x_values = list(range(st, ed + 1, d))
    y_values = [[tcs[j][i - st] for i in x_values] for j in range(0, 3)]

    for i in range(0, 3):
        plt.plot(
            x_values, y_values[i], marker="o", label=f"{costs[i] // 10000} (10K ₩)"
        )

    plt.title("Total Cost on Number of Bins")
    plt.xlabel("Number of Bins")
    plt.ylabel("Total Cost")
    plt.grid(True)
    plt.legend()
    plt.show()


def update():

    global littering, personal_cost, collection_rate

    collection_rate = (1 / 2120) * 0.01 * (cnt - prev_cnt)
    littering = 0.01 - collection_rate
    personal_cost = total_salay * (1 / 2120) * (cnt - prev_cnt)


def p(is_clean):

    if littering == 0.01:
        return 0

    if is_clean:
        return 0.01 - littering
    else:
        return 0.8 * (0.01 - littering)


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

    pleasent_rate = list(map(p, [True, False]))

    recycling_rates = []

    for i, c in enumerate(costs):
        total_cost = t(c)

        tcs[i][cnt - st] = total_cost

        recycling_rates = [20, 40] if clean_rate == 1 else [20, 40, 60, 80]

        for rr in recycling_rates:
            res = r(total_cost, rr)

            rps[i][cnt - st] = recycling_profit

            print(
                f"쓰레기통 개수: {cnt} / 쓰레기통 비용: {c} / 청결도: {clean_rate}",
                end=" ",
            )
            print(f"/ 재활용율: {rr}")

            print(f"-> 청결시 거리 쾌적도: {pleasent_rate[0]}입니다.")
            print(f"-> 불결시 거리 쾌적도: {pleasent_rate[1]}입니다.")

            print(f"-> 연간 추가 쓰레기통 총 비용: {total_cost}입니다.")
            print(f"-> 연간 재활용 이익: {recycling_profit}입니다.")
            print("-> 연간 재활용 이익은 연간 쓰레기 비용보다", end=" ")

            if res == 1:
                print("크거나 같습니다")
            else:
                print("작습니다")

            print("\n")

        print("\n")


def f():
    update()
    run()


st, ed, d, clean_rate = map(int, input().split())

for cnt in range(st, ed + 1, d):
    f()

graph()
