def calculate_mean(numbers):
    return sum(numbers) / len(numbers)

def calculate_median(numbers):
    numbers.sort()
    n = len(numbers)
    mid = n // 2
    if n % 2 == 0:
        return (numbers[mid - 1] + numbers[mid]) / 2
    else:
        return numbers[mid]

def calculate_mode(numbers):
    frequency = {}
    for number in numbers:
        frequency[number] = frequency.get(number, 0) + 1
    max_freq = max(frequency.values())
    modes = [num for num, freq in frequency.items() if freq == max_freq]
    return modes if len(modes) > 1 else modes[0]

def calculate_std_dev(numbers, mean):
    variance = sum((x - mean) ** 2 for x in numbers) / len(numbers)
    return variance ** 0.5

def statistics_calculator():
    print("Statistics Calculator")
    numbers = []
   
    while True:
        print("Enter a number, or type 'end' to end sequence")
        user_input = input(">> ")
        if user_input.lower() in ('end', 'e', 'done', 'exit'):
            break
        try:
            number = float(user_input)
            numbers.append(number)
        except ValueError:
            print("Please enter a valid number.")
   
    if len(numbers) == 0:
        print("No numbers entered.")
        return
   
    mean = calculate_mean(numbers)
    median = calculate_median(numbers)
    mode = calculate_mode(numbers)
    std_dev = calculate_std_dev(numbers, mean)
   
    print("\nResults:\n")

    print(f"Mean:                {mean}")
    print(f"Median:              {median}")
    print(f"Mode:                {mode}")
    print(f"Standard Deviation:  {std_dev}")

statistics_calculator()