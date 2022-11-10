def roman_convert(s):
    rom_value = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    result = 0
    for i in range(len(s)):
        if i > 0 and rom_value[s[i]] > rom_value[s[i-1]]:
            result += rom_value[s[i]] - 2 * rom_value[s[i - 1]]
        else:
            result += rom_value[s[i]]
    return result
