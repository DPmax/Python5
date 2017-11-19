# Python5

Laboratory Project 5
Confidence Intervals

1.	Effect of sample size on confidence intervals
Introduction: Measuring a statistic in a large population of size N = 1000000 with mean value of 75 and standard deviation with 7.50. Drawing a sample of size n from the population, produces a distribution for the sample mean (X bar) with:
 E[X bar] = mu_x_bar = mu      and E[(X bar – mu_x_bar)^2] = sigma_x_bar^2
Methodology: For case 1 with 95% confidence, using the values of mu +- 1.96 sigma/sqrt(n) as a function of n. For case 2 with 99% confidence, using the values of mu +- 2.58 sigma/sqrt(n) as a function of n. 

Result: For case 1 visually confirmed by looking at how many of sample means fall outside of the red curves with approx. of 5%. For case 2 visually confirmed by looking at how many of sample fall outside of the green curves with approx. of 1%.
 


2.	Using the sample mean to estimate the population mean

Introduction:  To simulate the sample mean to estimate the population mean, generate a barrel of a million ball bearings with weights normally distributed, with a mean with 75 and standard deviation with 7.50.
There will be 3 different experiment when n = 5, 40 ,120; using both normal distribution and the t-distribution to complete of the table and compare the success rate between both normal distribution and t-distribution. 
Methodology: Choose a random sample which is n bearings from 1000000 bearings created in the previous problem and calculate the sample mean and the sample standard deviation. 
 
Check if the confidence interval includes the actual mean 75 µ = of the population of 1,000,000 bearings. If it does, then considered a success.
Conclusion: For large sample n > 30 the t-distribution will be very close to normal, so the differences between t-distribution and normal distribution is minimal.
Result:	
Sample size(n)	95% Confidence
(Using Normal distribution)	99% Confidence
(Using Normal distribution)	95% Confidence
(Using Student’s t distribution)	99% Confidence
(Using Student’s t distribution)
5	88.25%	95.05%	95.05%	99.19%
40	94.64%	99.12%	95.12%	98.92%
120	95.00%	99.38%	95.17%	99.17%
