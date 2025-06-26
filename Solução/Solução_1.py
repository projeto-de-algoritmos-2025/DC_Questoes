class Solution(object):
    def numberOfPermutations(self, n, requirements):
        """
        :type n: int
        :type requirements: List[List[int]]
        :rtype: int
        """
        MOD = 10**9 + 7

        # Convert requirements to a dictionary for easy lookup
        # {endi: cnti}
        req_map = {req[0]: req[1] for req in requirements}

        # The maximum possible number of inversions for n elements is n * (n - 1) / 2.
        # However, the maximum required cnti is 400. When we add element i,
        # it can add up to i new inversions. So, the maximum relevant inversion count
        # we might need to track is max(cnti) + (n-1) approximately.
        # Let's be safe and use 400 (max cnti) + n (max additional inversions)
        MAX_INVERSIONS_DP = 400 + n 
        
        # dp[j] will store the number of permutations of [0, ..., current_num - 1]
        # with exactly j inversions, satisfying all previous requirements.
        dp = [0] * (MAX_INVERSIONS_DP + 1)
        dp[0] = 1  # Base case: 0 elements ([]) has 0 inversions, 1 way.

        # Iterate current_num from 1 to n.
        # This represents building permutations of [0, ..., current_num - 1].
        for current_num_elements in range(1, n + 1):
            # new_dp for permutations of [0, ..., current_num_elements - 1]
            new_dp = [0] * (MAX_INVERSIONS_DP + 1)
            
            # Use prefix sums for optimization.
            # prefix_sum[j] = sum(dp[0]...dp[j])
            prefix_sum = [0] * (MAX_INVERSIONS_DP + 1)
            prefix_sum[0] = dp[0]
            for j in range(1, MAX_INVERSIONS_DP + 1):
                prefix_sum[j] = (prefix_sum[j-1] + dp[j]) % MOD

            # Iterate over possible new inversion counts
            # 'inv' represents the total inversions for current_num_elements elements.
            # 'k' is the number of new inversions added by placing current_num_elements - 1.
            # The current_num_elements - 1 can be placed in 'current_num_elements' positions,
            # generating 0, 1, ..., current_num_elements - 1 new inversions.
            for inv in range(MAX_INVERSIONS_DP + 1):
                # The minimum number of previous inversions needed is inv - (current_num_elements - 1)
                # The maximum number of previous inversions needed is inv - 0
                
                # So we need to sum dp[inv - k] for k from 0 to current_num_elements - 1
                # This sum is prefix_sum[inv] - prefix_sum[inv - current_num_elements - 1]
                
                # Lower bound for previous inversions (inv - k_max)
                lower_bound = max(0, inv - (current_num_elements - 1))
                
                # Upper bound for previous inversions (inv - k_min)
                upper_bound = inv

                if lower_bound > upper_bound:
                    continue # No valid prev_inv

                # Calculate sum using prefix sums
                count_from_prev_states = (prefix_sum[upper_bound] - (prefix_sum[lower_bound - 1] if lower_bound > 0 else 0) + MOD) % MOD
                new_dp[inv] = count_from_prev_states
            
            dp = new_dp

            # Apply requirement if it exists for the current prefix length
            if (current_num_elements - 1) in req_map:
                required_inversions = req_map[current_num_elements - 1]
                # If the required_inversions is out of our current DP range,
                # or if the count for required_inversions is 0,
                # then no valid permutations exist.
                if required_inversions > MAX_INVERSIONS_DP or dp[required_inversions] == 0:
                    return 0
                
                # All other inversion counts become 0, as only the required count is valid.
                temp_dp = [0] * (MAX_INVERSIONS_DP + 1)
                temp_dp[required_inversions] = dp[required_inversions]
                dp = temp_dp
                
        # The final answer is the number of permutations of [0, ..., n-1]
        # that satisfy all requirements, which is stored at dp[req_map[n-1]].
        # The problem statement guarantees that there is at least one i such that endi == n - 1.
        return dp[req_map[n-1]]