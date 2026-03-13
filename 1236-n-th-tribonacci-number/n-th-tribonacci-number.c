int tribonacci(int n) {
    int i;
    int* memo = malloc(sizeof(int) * 38);

    memo[0] = 0;
    memo[1] = 1;
    memo[2] = 1;

    for (i = 3; i <= n; i++)
    {
        memo[i] = memo[i - 3] + memo[i - 2] + memo[i - 1];
    }

    return memo[n];
}