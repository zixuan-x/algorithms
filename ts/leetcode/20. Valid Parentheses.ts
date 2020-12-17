function isValid(s: string): boolean {
    const stack: string[] = [];
    const mapping: { [index: string]: string } = {
        '}': '{',
        ']': '[',
        ')': '(',
    };
    for (let i = 0; i < s.length; i++) {
        const c = s[i];
        if (mapping[c]) {
            // right parentheses
            if (stack && stack[stack.length - 1] === mapping[c]) {
                stack.pop();
            } else {
                return false;
            }
        } else {
            // left parentheses
            stack.push(c);
        }
    }
    return !stack.length;
}
