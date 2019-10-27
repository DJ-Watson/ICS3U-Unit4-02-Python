#!/usr/bin/env python3

# Created by DJ Watson
# Created on October 2019
# this program loops a rational


def main():
    loopn = 0
    answer = 1

    # input
    intc = input("enter factorial: ")
    print("")

    # process and output
    try:
        numinput = int(intc)
        if numinput > 0:
            while loopn < numinput:
                loopn += 1
                answer *= loopn
            print(answer)
        else:
            print("invalid input")
    except ValueError:
        print("invalid input")


if __name__ == "__main__":
    main()
