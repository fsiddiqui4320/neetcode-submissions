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

        table to track groups
        key is dict with key = anagram's chars and value = count of each char value is its group's index in the output list
        create output list
        for str in strs:
            count frequency of each char in string, store in temp dict
            if that dict in table, add to output list index associated with that dict
            if not in table then add and append str to output
        return output
        # '''
        table = {}
        output = []
        for str in strs:
            temp = [0] * 26
            for char in str:
                int_char = ord(char) - 97
                temp[int_char] += 1
            
            temp = tuple(temp)
            if temp in table:
                output[table[temp]].append(str)
            else:
                output.append([str])
                table[temp] = len(output) - 1

        return output