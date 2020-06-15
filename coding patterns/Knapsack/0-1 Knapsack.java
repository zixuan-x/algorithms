class Knapsack {

    // W 为背包总体积
    // N 为物品数量
    // weights 数组存储 N 个物品的重量
    // values 数组存储 N 个物品的价值
    public int knapsack(int W, int N, int[] weights, int[] values) {
        int[][] dp = new int[N + 1][W + 1];
        for (int i = 1; i <= N; i ++) {
            int w = weights[i - 1], v = values[i - 1];
            for (int j = 1; j < W; j++) {
                
            }
        }
        return dp[N][W];
    }

}