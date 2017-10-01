from search_engine import SearchEngine


def start():
    searchEngine = SearchEngine("data/")

    print("For finish write 'exit'")
    request = input("User: ")
    while (request != "exit"):
        answer = searchEngine.search(request)
        print_result(answer)
        request = input("User: ")


def print_result(result):
    if len(result) > 0:
        print("Found:" + str(len(result)))
        for ind, r in enumerate(result):
            print(str(ind) + ". " + r[0] + " (" + str(r[1]) + ")")
            for pos_info in r[2]:
                print("   Position of '" + pos_info[0] + "': " + str(pos_info[1]))
    else:
        print("Search didn't give result")


if __name__ == "__main__":
    start()
