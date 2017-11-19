# -*- coding: utf-8 -*-
"""

@author: LONGCHENG
381-LAB5
Confidence Intervals
"""

import numpy as np
import matplotlib.pyplot as plt

def EffectOfSampleSize(N):
# initialization
    mu = 75
    sigma = 7.5
    SampleSize = 200
    z_95 = 1.96
    z_99 = 2.58
    result = []
# random numbers
    bearings = np.random.normal(mu, sigma, N)    
    for i in range(SampleSize):
        sample = np.random.choice(bearings, (i+1))
        result.append(np.mean(sample))

    x = np.linspace(1, SampleSize)
# Plot for 95% confidence interval
    plt.figure(1)
    plt.title("Sample Means and 95% confidence intervals")
    plt.xlabel("Sample Size")
    plt.ylabel("x_ bar")
    plt.barh(mu, SampleSize, height=0.2, color='black')
    plt.plot(x, mu + z_95 * sigma / (np.sqrt(x)), color='r', linestyle='--')
    plt.plot(x, mu - z_95 * sigma / (np.sqrt(x)), color='r', linestyle='--')
    plt.scatter(range(SampleSize), result, marker='x')
    plt.show()
# Plot for 99% confidence interval
    plt.figure(2)
    plt.title("Sample Means and 99% confidence intervals")
    plt.xlabel("Sample Size")
    plt.ylabel("x_ bar")
    plt.barh(mu, SampleSize, height=0.2, color='black')
    plt.plot(x, mu + z_99 * sigma / (np.sqrt(x)), color='g', linestyle='--')
    plt.plot(x, mu - z_99 * sigma / (np.sqrt(x)), color='g', linestyle='--')
    plt.scatter(range(SampleSize), result, marker='x')
    plt.show()

    return result

def EstimatePopulationMean(N,M):
# initialization
    z_95 = 1.96
    z_99 = 2.78
    mu = 75
    sigma = 7.5
    successes_n95 = 0
    successes_t95 = 0
    successes_n99 = 0
    successes_t99 = 0
# random numbers
    bearings = np.random.normal(mu, sigma, 1000000)
    # M times of experiment
    for j in range(M):
        sample = np.random.choice(bearings, N)
        mu_s = np.mean(sample)
        sigma_s = 0
        # Sample Variance
        for i in range(len(sample)):
            sigma_s = sigma_s + ((sample[i]-mu_s)**2)
        sigma_s = np.sqrt((sigma_s/(N-1)))
        
        # For Normal Tables with 95% confidence
        lowerLimit_n95 = mu_s-z_95*sigma_s/(np.sqrt(N))
        upperLimit_n95 = mu_s+z_95*sigma_s/(np.sqrt(N))
        # For Normal Tables with 99% confidence
        lowerLimit_n99 = mu_s-z_99*sigma_s/(np.sqrt(N))
        upperLimit_n99 = mu_s+z_99*sigma_s/(np.sqrt(N))
        
        
        # Check the sample size of N For T-table
        if N == 5 :
            t_95 = 2.78
            t_99 = 4.60

        if N == 40:
            t_95 = 2.02
            t_99 = 2.70

        if N == 120:
            t_95 = 1.98
            t_99 = 2.62
        # For T-tables with 95% confidence
        lowerLimit_t95 = mu_s-(t_95*sigma_s/(np.sqrt(N)))
        upperLimit_t95 = mu_s+(t_95*sigma_s/(np.sqrt(N)))
        # For T-tables with 99% confidence
        lowerLimit_t99 = mu_s-(t_99*sigma_s/(np.sqrt(N)))
        upperLimit_t99 = mu_s+(t_99*sigma_s/(np.sqrt(N)))
        
        # Check mean if stays between lower limit and upper limit
        if mu >= lowerLimit_n95 and mu <= upperLimit_n95:
            successes_n95 = successes_n95 + 1
        if mu >= lowerLimit_n99 and mu <= upperLimit_n99:
            successes_n99 = successes_n99 + 1
        if mu >= lowerLimit_t95 and mu <= upperLimit_t95:
            successes_t95 = successes_t95 + 1
        if mu >= lowerLimit_t99 and mu <= upperLimit_t99:
            successes_t99 = successes_t99 + 1

    print("Normal table with 95% confidence n =",N,":",successes_n95 / M * 100,"%")
    print("Normal table with 99% confidence n =", N, ":", successes_n99 / M * 100,"%")
    print("T-table with 95% confidence n =",N,":",successes_t95 / M * 100,"%")
    print("T-table with 99% confidence n =", N, ":", successes_t99 / M * 100,"%")



EffectOfSampleSize(1000000)
EstimatePopulationMean(5,10000)
EstimatePopulationMean(40,10000)
EstimatePopulationMean(120,10000)
