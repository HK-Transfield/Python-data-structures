from IList import IList


def main():
    num_array = [1, 3, 5, 23, 5, 7, 2, 2, 23, 13, 25]
    num_list = IList()

    for num in num_array:
        if num_list.is_empty():
            print('!!EMPTY!!')

        if num_list.has_val(num):
            print('Found ', num)
            num_list.remove(num)

            if num_list.has_val(num):
                print('Oh dear, you did not remove ', num)
        else:
            print('Not found ', num)
            num_list.insert(num)

            if num_list.has_val(num) is False:
                print('Oh dear, you did not insert ', num)

    print('\n---VALUES IN LIST---')
    num_list.dump_vals()


if __name__ == "__main__":
    main()
