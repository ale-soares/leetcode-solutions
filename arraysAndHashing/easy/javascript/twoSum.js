function twoSum(nums, target) {
  const numObject = {};

  for (let i = 0; i < nums.length; i++) {
    const num = nums[i];
    const complement = target - num;

    if (numObject.hasOwnProperty(complement)) {
      return [numObject[complement], i];
    }

    numObject[num] = i;
  }

  return [];
}
