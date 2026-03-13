int tribonacci(int n) {
    int i;
    int next;
    int a, b, c;

    a = 0;
    b = 1;
    c = 1;

    if (n == 0) return a;
    if (n <= 2) return 1;

    for (i = 3; i <= n; i++)
    {
        next = a + b + c;
        a = b;
        b = c;
        c = next;
    }

    return c;
}