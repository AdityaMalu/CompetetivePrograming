def main():
    num_tests = int(input().strip())
    for _ in range(num_tests):
        initial_value, target_value, multiplier = map(int, input().strip().split())
        decrement_step = 0
        operations = 0
        
        while target_value > initial_value:
            if target_value % multiplier == 0:
                if target_value // multiplier < initial_value:
                    decrement_step = target_value - initial_value
                    operations += decrement_step
                    break
                else:
                    target_value //= multiplier
                    operations += 1
            else:
                remainder_step = target_value % multiplier
                decrement_step = target_value - initial_value
                decrement_amount = min(remainder_step, decrement_step)
                target_value -= decrement_amount
                operations += decrement_amount
                
        print(operations)

if __name__ == "__main__":
    main()
