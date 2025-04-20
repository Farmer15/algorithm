/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
var twoSum = function(nums, target) {
  const store = {

  };

  for (let i = 0; i < nums.length; i++) {
    const key = target - nums[i]
    console.log(store);
    if (store[key] !== undefined) {
      return [store[key], i];
    }

    store[nums[i]] = i;
  }
};