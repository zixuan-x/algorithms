function reverse(x: number): number {
    if (x < 0) return -reverse(-x);
    let result = 0;
    while (x > 0) {
        const digit = x % 10;
        x = Math.floor(x / 10);

        if (result >= 214748365) return 0;

        result = result * 10 + digit;
    }
    return result;
}
