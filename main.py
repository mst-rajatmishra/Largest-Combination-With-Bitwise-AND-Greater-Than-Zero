class Solution:
    def largestCombination(self, candidates: List[int]) -> int:
        # We will track counts for each bit position (there are 24 bits in max candidates[i] <= 10^7)
        bit_count = [0] * 24  # bit_count[i] will hold how many numbers have the i-th bit set
        
        # For each number in the candidates, check which bits are set
        for num in candidates:
            for i in range(24):  # Iterate through all 24 possible bit positions (0 to 23)
                if num & (1 << i):  # If the i-th bit is set in num
                    bit_count[i] += 1
        
        # The largest combination size is the maximum value in bit_count
        return max(bit_count)
