int tribonacci(int n) {
    int i;
    int next;
    int* memo = malloc(sizeof(int) * 3);

    memo[0] = 0;
    memo[1] = 1;
    memo[2] = 1;

    if (n <= 2) return memo[n];

    for (i = 3; i <= n; i++)
    {
        next = memo[0] + memo[1] + memo[2];
        memo[0] = memo[1];
        memo[1] = memo[2];
        memo[2] = next;
    }

    return memo[2];
}