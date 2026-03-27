class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        
        s = s.replace("-", "").upper()
        
        result = []
        count = 0
        
        # Traverse from end
        for ch in reversed(s):
            if count == k:
                result.append('-')
                count = 0
            
            result.append(ch)
            count += 1
        
        # Reverse final result
        return ''.join(reversed(result))
        