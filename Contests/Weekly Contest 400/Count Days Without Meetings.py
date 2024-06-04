# Problem 3196: Count Days Without Meetings

"""
You are given a positive integer days representing the total number of days an employee is available for work (starting from day 1). You are also given a 2D array meetings of size n where, meetings[i] = [start_i, end_i] represents the starting and ending days of meeting i (inclusive).

Return the count of days when the employee is available for work but no meetings are scheduled.

Note: The meetings may overlap.

 

Example 1:

Input: days = 10, meetings = [[5,7],[1,3],[9,10]]

Output: 2

Explanation:

There is no meeting scheduled on the 4th and 8th days.

Example 2:

Input: days = 5, meetings = [[2,4],[1,3]]

Output: 1

Explanation:

There is no meeting scheduled on the 5th day.

Example 3:

Input: days = 6, meetings = [[1,6]]

Output: 0

Explanation:

Meetings are scheduled for all working days.

 

Constraints:

1 <= days <= 109
1 <= meetings.length <= 105
meetings[i].length == 2
1 <= meetings[i][0] <= meetings[i][1] <= days
"""

## Approach:
"""First i used straight simple approach ki apan 1-n tak ka boolean array bnaye aur jo jo range aa rha unko True set krte jaaye
and end me jo array Flase hai unka count return maar de
But this approach gave me TLE.

So my second approach was to merge intervals:
step 1: Sort the Meeting Intervals:
    Sort the given meeting intervals based on their start times. This makes it easier to merge overlapping intervals.
    Merge Overlapping Intervals:

step2: Initialize an empty list to store merged intervals.
    Use a variable to keep track of the current interval's start and end.
    Iterate through the sorted meeting intervals. For each interval, check if it overlaps with the current interval. If it does, extend the current interval to include it. If it doesn't, add the current interval to the merged list and start a new interval.
    Calculate the Number of Free Days:

step 3: Initialize a counter with the total number of days.
    Subtract the number of days occupied by each merged interval from the counter.
    Return the Result:

The result is the number of days left in the counter, representing the days when no meetings are scheduled.
"""