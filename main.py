import numpy as np

if __name__ == "__main__":
    # 1D array
    # arr = np.array([1, 2, 3])

    # 2D array
    # arr2 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

    # 3D array
    # array = np.array(
    #     [
    #         [[1, 2, 3], [4, 5, 6], [7, 8, 9]],
    #         [[10, 11, 12], [13, 14, 15], [16, 17, 18]],
    #         [[19, 20, 21], [22, 23, 24], [25, 26, 27]],
    #     ]
    # )

    arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]])

    # print(arr[0:2, 0:2])
    # print(arr[0:2, 2:4])
    # print(arr[2:4, 0:2])
    # print(arr[2:4, 2:4])

    arrary = np.array([1, 2, 3])

    # Scaler arathmetic operations

    # print(arrary + 1)
    # print(arrary - 2)
    # print(arrary * 3)
    # print(arrary / 4)
    # print(arrary ** 5)

    # Vector maths func
    arrary = np.array([1.22, 2.02, 3.99])

    print(np.sqrt(arrary))
    print(np.round(arrary))  # can alse use floor and ceil
    print(np.pi)

    # ecercise

    radii = np.array([1, 2, 3])
    print(np.pi * radii**2)

    # comparison operations

    marks = np.array([55, 89, 76, 45, 91])
    print(marks < 60)
    marks[marks < 60] = 0
    print(marks)

    # broadcasting
    arr = np.array([1, 2, 3])
    arr2 = np.array([[1], [2], [3]])

    print(arr + arr2)
    print(arr * arr2)

    # Aggregate Functions
    arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

    # print(np.sum(arr))
    # print(np.mean(arr))
    # print(np.min(arr))
    # print(np.max(arr))
    # print(np.argmin(arr))
    # print(np.argmax(arr))

    print(np.sum(arr, axis=0))  # column-wise sum
    print(np.sum(arr, axis=1))  # row-wise sum
