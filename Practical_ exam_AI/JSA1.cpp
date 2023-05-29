#include <bits/stdc++.h>
using namespace std;

//structure for holding values
typedef struct Job
{
    int jobNum;
    int deadline;
    int profit;
}Job;

bool compare(Job a, Job b)
{
    return (a.profit > b.profit);
}

void jobSequencing(Job input[], int num)
{
    sort(input, input + num, compare);

    int result[num];
    
    bool slot[num];
    // setting all values in slot as false
    memset(slot, 0, sizeof(slot));

    for (int i = 0; i < num; i++)
    {
        for (int j = min(num, input[i].deadline)-1; j >= 0; j--)
        {
            if(slot[j] == false)
            {
                result[j] = i;
                slot[j] = true;
                break;
            }
        }
    }

    cout << "Job sequenced in order: ";
    for (int i=0; i<num; i++)
    {
       if (slot[i] == true)
        cout << input[result[i]].jobNum << " ";
    }
}

int main()
{
    int num;
    cout<<"enter the no of jobs " ;
    cin >> num;
    Job input[num];
    // inputing the values
    for (int i = 0; i < num; i++)
    {	cout<<"enter the job number ";
        cin >> input[i].jobNum;
        cout<<"enter the deadline or time ";
        cin >> input[i].deadline;
        cout<<"enter the profit ";
        cin >> input[i].profit;
    }

    jobSequencing(input, num);
}

