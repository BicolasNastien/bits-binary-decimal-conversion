def is_binary_number(num_str):
    """Check if a string represents a valid binary number"""
    # Remove dots and spaces
    clean_num = num_str.replace('.', '').replace(' ', '')
    # Check if all characters are 0 or 1
    return all(bit in '01' for bit in clean_num)

def binary_to_decimal(binary_str):
    """Convert a binary number to decimal"""
    if '.' in binary_str:
        # Number with fractional part
        integer_part, fractional_part = binary_str.split('.')
        
        # Integer part conversion
        integer_decimal = int(integer_part, 2)
        
        # Fractional part conversion
        fractional_decimal = 0
        for i, bit in enumerate(fractional_part):
            if bit == '1':
                fractional_decimal += 2 ** -(i + 1)
        
        return integer_decimal + fractional_decimal
    else:
        # Integer part
        return int(binary_str, 2)

def decimal_to_binary(decimal_num):
    """Convert a decimal number to binary"""
    fract = decimal_num - int(decimal_num)
    integer = int(decimal_num)
    
    # Integer part conversion
    integer_binary = bin(integer)[2:] if integer != 0 else "0"
    
    # Fractional part conversion
    strBin = ""
    while fract > 0:
        fract = fract * 2
        bit = int(fract)
        strBin += str(bit)
        fract = fract - bit
        # Limit precision to avoid infinite loops
        if len(strBin) >= 20:
            break
    
    if strBin:
        return f"{integer_binary}.{strBin}"
    else:
        return integer_binary

def main():
    print("=== Base 2 ↔ Base 10 Converter ===")
    print("1. Decimal → Binary")
    print("2. Binary → Decimal")
    print("3. Automatic detection")
    
    choice = input("Choose conversion mode (1/2/3) > ")
    
    num_input = input("Enter the number to convert > ")
    
    if choice == "1":
        # Convert Base 10 → Base 2
        try:
            decimal_num = float(num_input)
            result = decimal_to_binary(decimal_num)
            print(f"\n{decimal_num}₁₀ = {result}₂")
        except ValueError:
            print("Error: Please enter a valid decimal number.")
    
    elif choice == "2":
        # Convert Base 2 → Base 10
        if is_binary_number(num_input):
            result = binary_to_decimal(num_input)
            print(f"\n{num_input}₂ = {result}₁₀")
        else:
            print("Error: Please enter a valid binary number (contains only 0 and 1).")
    
    elif choice == "3":
        # Auto detection
        if is_binary_number(num_input):
            # It's a binary number, convert to decimal
            result = binary_to_decimal(num_input)
            print(f"\nDetected: Binary number")
            print(f"{num_input}₂ = {result}₁₀")
        else:
            # It's probably a decimal number, convert to binary
            try:
                decimal_num = float(num_input)
                result = decimal_to_binary(decimal_num)
                print(f"\nDetected: Decimal number")
                print(f"{decimal_num}₁₀ = {result}₂")
            except ValueError:
                print("Error: Invalid number format.")
    
    else:
        print("Error: Please choose 1, 2 or 3.")

if __name__ == "__main__":
    main()
