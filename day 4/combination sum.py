class Solution {

    public List<List<Integer>> combinationSum(int[] candidates, int target) {
        List<List<Integer>> ans = new ArrayList<>();
        backtrack(candidates, 0, target, 0, new ArrayList<>(), ans);
        return ans;
    }

    private void backtrack(
        int[] nums,
        int i,
        int target,
        int currSum,
        List<Integer> comb,
        List<List<Integer>> ans
    ) {
        if (currSum == target) {
            ans.add(new ArrayList<>(comb));
            return;
        }
        if (currSum > target || i == nums.length) {
            return;
        }

        // Include nums[i]
        comb.add(nums[i]);
        backtrack(nums, i, target, currSum + nums[i], comb, ans); // Do not move i forward since repetition is allowed
        comb.remove(comb.size() - 1); // Backtrack

        // Exclude nums[i] and move i forward
        backtrack(nums, i + 1, target, currSum, comb, ans);
    }
}
