class Solution:
    def defangIPaddr(self, address: str) -> str:
    	# Split the string by '.' into a list. Join it in a string with separator: '[.]'
        return '[.]'.join(address.split('.'))