def main(len_marker):
    for n in range(3, len(data)):
        if len({*data[n - len_marker:n]}) == len_marker:
            print(n)
            break


if __name__ == "__main__":
    with open("6.txt") as f:
        data = f.readlines()[0]

    # data = "mjqjpqmgbljsphdztnvjfqwrcgsmlb\n"

    main(14)
