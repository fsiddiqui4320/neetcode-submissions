class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # '''
        # create a table to track groups
        # key will be the sorted anagram and value will be its group's index in the output list
        # create output list
        # for str in strs:
        #     sorted = sort str
        #     if sorted not in table:
        #         output.append([str])
        #         table[sorted] = len(output) - 1
        #     else:
        #         output[table[sorted]].append(str)
        # return output

        # table to track groups
        # key is dict with key = anagram's chars and value = count of each char value is its group's index in the output list
        # create output list
        # for str in strs:
        #     count frequency of each char in string, store in temp dict
        #     if that dict in table, add to output list index associated with that dict
        #     if not in table then add and append str to output
        # return output

        # best solution:
        # table dict with key as frequency of chars tuple and value is index of anagram list in output
        # initialize output list

        # loop through strings:
        #     initilize temp list size 26 for tracking character frequency
        #     loop through chars in str:
        #         use temp to count frequency of chars in string
            
        #     convert temp to a tuple
        #     if tuple is already a key in table:
        #         append current string to the output list for that anagram group
        #     else:
        #         append current string to output
        #         add tuple as a key and make value anagram's index in output
        
        # return output

        # instead of separate output list and tracking output indices with dict, make dict values lists of string in each anagram group and then just return dict.values()
        # # '''
        result = defaultdict(list)
        for str in strs:
            temp = [0] * 26
            for char in str:
                int_char = ord(char) - 97
                temp[int_char] += 1
            result[tuple(temp)].append(str)

        return list(result.values())