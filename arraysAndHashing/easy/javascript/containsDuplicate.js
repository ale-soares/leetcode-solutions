/**
 * Hash Set
 * Time O(N) | Space O(N)
 * https://leetcode.com/problems/contains-duplicate/
 * @param {number[]} nums
 * @return {boolean}
 */

var containsDuplicate = (nums) => {
  const numsSet = new Set(nums);
  const isEqual = numsSet.size === nums.length;

  return !isEqual;
};
