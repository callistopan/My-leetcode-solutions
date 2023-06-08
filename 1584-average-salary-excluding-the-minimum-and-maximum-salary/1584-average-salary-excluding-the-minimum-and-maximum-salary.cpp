class Solution {
public:
    double average(vector<int>& salaries) {
        double sum = 0;
		double max = std::numeric_limits<double>::min();
		double min = std::numeric_limits<double>::max();
		for (int const salary : salaries)
		{
			sum += salary;
			if (salary > max)
			{
								max = salary;
			}
			if (salary < min)
			{
								min = salary;
			}
		}
		return (sum - max - min) / (salaries.size() - 2);
    }
};