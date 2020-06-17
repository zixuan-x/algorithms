class Knapsack {

    /**
     * 1. Recursion - O(2 ^ n) time, O(n) stack space
     */
    public int solveKnapsack(int[] profits, int[] weights, int capacity) {
      return this.knapsackRecursive(profits, weights, capacity, 0);
    }
  
    private int knapsackRecursive(int[] profits, int[] weights, int capacity, int currentIndex) {
      // base checks
      if (capacity <= 0 || currentIndex >= profits.length)
        return 0;
  
      // recursive call after choosing the element at the currentIndex
      // if the weight of the element at currentIndex exceeds the capacity, we shouldn't process this
      int profit1 = 0;
      if( weights[currentIndex] <= capacity )
          profit1 = profits[currentIndex] + knapsackRecursive(profits, weights,
                  capacity - weights[currentIndex], currentIndex + 1);
  
      // recursive call after excluding the element at the currentIndex
      int profit2 = knapsackRecursive(profits, weights, capacity, currentIndex + 1);
  
      return Math.max(profit1, profit2);
    }

    /**
     * 2. Recursion with Memoization - O(n * c) time, O(n * c + n) = O(n * c) space
     */
    public int solveKnapsackWithMemo(int[] profits, int[] weights, int capacity) {
        Integer[][] dp = new Integer[profits.length][capacity + 1];
        return this.knapsackRecursive(dp, profits, weights, capacity, 0);
      }
    
      private int knapsackRecursive(Integer[][] dp, int[] profits, int[] weights, int capacity,
          int currentIndex) {
    
        // base checks
        if (capacity <= 0 || currentIndex >= profits.length)
          return 0;
    
        // if we have already solved a similar problem, return the result from memory
        if(dp[currentIndex][capacity] != null)
          return dp[currentIndex][capacity];
    
        // recursive call after choosing the element at the currentIndex
        // if the weight of the element at currentIndex exceeds the capacity, we shouldn't process this
        int profit1 = 0;
        if( weights[currentIndex] <= capacity )
            profit1 = profits[currentIndex] + knapsackRecursive(dp, profits, weights,
                    capacity - weights[currentIndex], currentIndex + 1);
    
        // recursive call after excluding the element at the currentIndex
        int profit2 = knapsackRecursive(dp, profits, weights, capacity, currentIndex + 1);
    
        dp[currentIndex][capacity] = Math.max(profit1, profit2);
        return dp[currentIndex][capacity];
      }
    

    /**
     * 3. Bottom-up Dynamic Programming - O(n * c) time, O(n * c) space
     */
    



    
}
  