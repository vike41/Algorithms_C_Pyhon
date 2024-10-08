#include <iostream>
#include <vector>
#include <cassert>
#include <algorithm>

class TwoWaymerger 
{
	public:
		// Merges two sorted vectors into one sorted vector
		std::vector<int> merge_two_lists(const std::vector<int>& list1, const std::vector<int>& list2) {
		{
			std::vector<int> merged_list;
			int i = 0, j = 0;

			// Merge untile one list is exhausted
			while (i < list1.size() && j < list2.size()){
				if (list1[i] < list2[j]) {
					merged_list.push_back(list1[i++]);
				}
				else{
					merged_list.push_back(list2[j++]);
				}
			}
			// add remaining elements from list
			while (i < list1.size()) {
				merged_list.push_back(list1[i++]);
			}	

			while (i < list2.size()) {
				merged_list.push_back(list2[j++]);
			}
			
			return merged_list;

		}

};