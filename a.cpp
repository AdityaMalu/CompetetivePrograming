class Solution
{
public:
    char nextGreatestLetter(vector<char> &letters, char target)
    {
        int l = 0, h = letters.size();
        while (h >= l)
        {
            int mid = (l + h) / 2;

            if (nums[mid] == target)
            {
                break;
            }

            if (nums[mid] > target)
            {
                h = mid - 1;
            }
            else
            {
                l = mid + 1;
            }
        }
        return nums[mid + 1];
    }
};