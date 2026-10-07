class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        '''
        create a table to track groups
        key will be the sorted anagram and value will be its group's index in the output list
        create output list
        for str in strs:
            sorted = sort str
            if sorted not in table:
                output.append([str])
                table[sorted] = len(output) - 1
            else:
                output[table[sorted]].append(str)
        return output
        '''
        table = {}
        output = []
        for str in strs:
            sorted_str = "".join(sorted(str))
            if sorted_str in table:
                output[table[sorted_str]].append(str)
            else:
                output.append([str])
                table[sorted_str] = len(output) - 1

        return output