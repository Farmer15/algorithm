/**
 * @param {number} n
 * @return {number}
 */
var fib = function(n) {
  const dp = [0, 1]

  function aaa(num) {
    if (dp[num] !== undefined) {
      return dp[num]
    }

    const result = aaa(num - 1) + aaa(num - 2);

    dp[num] = result
    return dp[num]
  }
  
  return aaa(n)
};