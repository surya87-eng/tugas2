# Fungsi untuk menggabungkan dua sub-array yang sudah terurut
def merge(left, right):
    sorted_list = []
    i = j = 0

    # Bandingkan elemen dari kedua sub-array dan gabungkan ke dalam sorted_list
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            sorted_list.append(left[i])
            i += 1
        else:
            sorted_list.append(right[j])
            j += 1

    # Tambahkan elemen yang tersisa di left atau right
    sorted_list.extend(left[i:])
    sorted_list.extend(right[j:])
    return sorted_list

# Fungsi utama merge_sort
def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    # Bagi array menjadi dua bagian
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    # Gabungkan kedua bagian menggunakan fungsi merge
    return merge(left, right)

# Data awal
data = [34, 7, 23, 32, 5, 62]

# Pemanggilan fungsi merge_sort
sorted_data = merge_sort(data)
print("Data awal:", data)
print("Data setelah diurutkan:", sorted_data)
