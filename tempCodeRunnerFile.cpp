#include<iostream>
#include<vector>
#include<unordered_set>

int countConsistentString(const std::string& allowed, const std::vector<std::string> words){
    std::unordered_set<char> allowedSet(allowed.begin(), allowed.end());
    
    int count = 0;
    for (const std::string& word : words){
        bool isConsistent = true;
        for (char ch : word){
            if (allowedSet.find(ch) == allowedSet.end()){
                isConsistent = false;
                break;
            }
        }
        if (isConsistent){
            count++;
        }
    }
    return count;
}

int main(){
    std::string allowed = "abc";
    std::vector<std::string> words = {"a", "b", "c", "ab", "ac", "bc", "abc"};
    std::cout << countConsistentString(allowed, words);
    return 0;
}   