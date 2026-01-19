import numpy as np

if __name__ == "__main__":
    # 1D array
    arr = np.array([1, 2, 3])

    # 2D array
    arr2 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

    # 3D array
    array = np.array(
        [
            [[1, 2, 3], [4, 5, 6], [7, 8, 9]],
            [[10, 11, 12], [13, 14, 15], [16, 17, 18]],
            [[19, 20, 21], [22, 23, 24], [25, 26, 27]],
        ]
    )

    print(array)
    print(array.ndim)
