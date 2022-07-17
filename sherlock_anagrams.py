def sherlockAndAnagrams(string):
    
    string_subset = {}
    
    n = len(string)
    
    for i in range(n):
        for j in range(i,n):
            cur = string[i:j +1]
            cur = ''.join(sorted(cur))
            string_subset[cur] = string_subset.get(cur, 0) + 1
    
    
    anagram_count =0
    for word in string_subset:
        
        v = string_subset[word]
        anagram_count += (v * (v-1))//2
    
    print(anagram_count)
    
    
    
sherlockAndAnagrams('abba')   
sherlockAndAnagrams('kkkk')   