result = []
used = [False] * len(strs)

for i in range(len(strs)):
    if used[i]:
        continue
            
        group = [strs[i]]
        used[i] = True
             
        for j in range(i + 1, len(strs)):
            if used[j]:
                 continue

            if len(strs[i]) == len(strs[j]):
                count_i = {}
                count_j = {}

                for char in strs[i]:
                    count_i[char] = count_i.get(char,0) + 1
                for char in strs[j]:
                    count_j[char] = count_j.get(char, 0) + 1

                if count_i == count_j:
                    group.append(strs[j])
                    used[j] = True

        
        result.append(group)

return result