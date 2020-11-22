pos = -1


def search(list1, n):
    lower = 0
    upper = len(list1) - 1
    if list1[0] == n:
        globals()["pos"] = 0
        return True
    else:
        while lower <= upper:
            mid = (lower + upper) // 2

            if list1[mid] == n:
                globals()["pos"] = mid
                return True
            else:
                if list1[mid] < n:
                    lower = mid + 1
                else:
                    upper = mid - 1

        return False


userList = [90, 12, 60, 123, 89, 2472, 231, 2231, 3455, 6768]
searchElement = int(input("Enter the number you want to search:"))

if search(userList, searchElement):
    print('Element found at position: ', pos + 1)
else:
    print("Element not found")
