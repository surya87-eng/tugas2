# Fungsi untuk Counting Sort
def counting_sort(arr):
    # Temukan nilai maksimum dan minimum dalam array
    max_val = max(arr)
    min_val = min(arr)
    range_of_elements = max_val - min_val + 1

    # Inisialisasi count array
    count = [0] * range_of_elements

    # Hitung frekuensi setiap elemen
    for num in arr:
        count[num - min_val] += 1

    # Bangun array hasil dari count array
    sorted_arr = []
    for i, freq in enumerate(count):
        sorted_arr.extend([i + min_val] * freq)

    return sorted_arr

# Data awal
data = [34, 7, 23, 32, 5, 62]

# Pemanggilan fungsi counting_sort
sorted_data = counting_sort(data)
print("Data awal:", data)
print("Data setelah diurutkan:", sorted_data)
