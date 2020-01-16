class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:        
        # Account for empty list as input
        if len(strs) == 0:
            return ''
        # If strs has only one string the string is the output
        elif len(strs) == 1:
            return strs[0]
        else:
            # Select the shortest string in strs
            short_str = min(strs, key=len)
            # Counter for common prefix len
            len_prefix = 0
            # Loop through the shortest string and count len of common prefix
            for i in range(len(short_str)):            
                if len(set(word[i] for word in strs)) == 1:
                    len_prefix += 1
                else:
                    break
        # Return counted len of common prefix as string, if any
        if len_prefix == 0:
            return ''
        else:
            return short_str[:len_prefix]