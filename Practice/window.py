numbers = [1, 2, 3, 7, 9]
window_size = 3

i = 0
output = []

while i < len(numbers) - window_size + 1:
    this = numbers[i : i+window_size]
    avg = (sum(this)/float(window_size))
    output.append(avg)
    i += 1

print output