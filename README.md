# Multi-Armed-Bandit-Problem

WHAT IS MULTI ARMED BANDIT PROBLEM ? 
The Multi Armed Bandit problem is a classic problem that gives us the practical explanation of the exploration-exploitation dilemma. We are given a row of slot machines with N arms (bandits) with each arm having a probability of winning. On pulling an arm from any machine, we are rewarded +1 for success, or 0 for failure. Our objective is to pull the arms in such a sequence so that we maximise our chances of winning in order to get the maximum reward till the end of the game. 
The concept originates from imagining a gambler at a casino standing in front of a row of slot machines, who has to decide whether to continue with the current machine or try a different machine, which machines to play, how many times to play each machine and in which order to play them. The objective of the gambler is to maximise the total rewards earned through a sequence of lever pulls.

The most difficult decision for the gambler is whether to keep playing on a machine that has the highest expected payoff i.e Exploitation or try playing on different machines to get knowledge about the winning or losing chances on them. 

In the problem, each machine provides a reward from a probability distribution specific to that machine.

EXPLORATION VS EXPLOITATION
The exploration-exploitation dilemma exists in our day to day life. Exploration here means to explore an unfamiliar area of which you have little or no knowledge whereas exploitation means exploring a familiar area of which you already have knowledge and are well acquainted.
Say, there is a cafe right outside your house on the other side of the road. You go there everyday to have lunch and breakfast. Since you go there everyday, you are well acquainted with the menu, the price, time taken to make the order, etc. This is exploitation. But if you keep going to the same cafe again and again you will miss the chances of discovering a better cafe with more options to dine. Going to a new cafe will be exploration. Also, if you try new cafes everytime, you might end up with getting food you don’t find tasty. Similarly, new sales companies find the most liked products by the customers and make a replica of the existing product under their name and sell at cheap prices in order to attract the customers.

Imagine a situation in which you have complete information about a recently opened cafe. You already have the menu containing the prices, the distance of the cafe from the house and the customer reviews of various dishes. You already have enough information to decide whether to go the new cafe or not. You already have every piece of information about the cafe existing right outside your house. The dilemma comes from the incomplete information. We need to have the complete information in order to make the best decisions with risks under control. With exploitation, we use the best option we know.       
With exploration, we select an unknown option with the help of the collected data. No pain, no gain. In order to make the best long term policy, we have to make many short term sacrifices. For example- one exploration trial could be a failure but it warns us to not take or say avoid that option in the future.




PROBABILITY DISTRIBUTION 
Basic Terminologies :
Probability : It is a measure quantifying the likelihood that an event will occur. Probability quantifies as a number between 0 and 1, where generally 0 indicates impossibility and 1 indicates certainty. The higher the probability of an event, the more likely it is that the event will occur. 
Statistics : It is a branch of mathematics working with data collection, organisation, analysis, interpretation and presentation. IN order to apply statistics to a scientific, industrial, or any social problem, it is conventional to begin with a statistical population or a model to be studied. Population can be a diverse group of people, such as ‘people living in the country of India’.
Probability Theory : It is the branch of mathematics concerned with probability. 
 Mean : In mathematics and statistics, the arithmetic mean or simply the mean or average when the context is clear, is the sum of a collection of numbers divided by the count of numbers in the collection. The collection is often a set of results of an experiment or an observational study, or frequently a set of results from a survey.
Standard Deviation : It's a measure that is used to quantify the amount of variation or dispersion of a set of data values.
Variance : In probability theory and statistics, variance is the expectation of the squared deviation of a random variable from its mean. Informally, it measures how far a set of (random) numbers are spread out from their average value.

In probability theory and statistics, a Probability distribution is a mathematical function that provides the probabilities of occurrence of different possible outcomes in an experiment. For instance, the random variable X is used to denote the outcome of a coin toss (‘the experiment’) then the probability distribution of X would take the value 0.5 for X= heads, and 0.5 for X=tails [1]. 
Probability distributions are generally divided into two classes. A discrete probability distribution can be described by a discrete list of the probabilities of the outcomes, known as a probability mass function. On the other hand, a continuous probability distribution is where the set of possible outcomes can take on values in a continuous range, such as the weather on a given day, is described by probability density functions (with the probability of any individual outcome actually being 0). The normal distribution is a commonly used continuous probability distribution. 

GAUSSIAN DISTRIBUTION 
Normal distribution, also known as the Gaussian distribution, is a probability distribution that is symmetric about the mean, showing that data near the mean are more frequent in occurrence than data far from the mean [2]. Graphically, normal distribution will appear as a bell curve.
                                          
We plotted Gaussian distribution by writing a code for it in Python using Spyder software in the Anaconda IDE.
ALGORITHM :
Import Numpy and Matplot libraries in Spyder
Generate N random numbers
Create Mean and Sigma by using the mean and sigma functions respectively
Define Gaussian function as :
def gauss(d, mean, sigma):
    			pi=np.pi
    			normd=2.*sigma*sigma
    			cons=1./np.sqrt(normd*pi)
    			func=cons*np.exp(-((d-mean)**2)/normd)
5) Plot the histogram of the Distribution by using the histogram function. 

OUTPUT :

With mean = 2.00097
And Variance = 0.501068

BETA DISTRIBUTION :
In probability theory and statistics, the beta distribution is a family of continuous probability distributions defined on the interval [0, 1] parametrized by two positive shape parameters, denoted by α and β, that appear as exponents of the random variable and control the shape of the distribution [3].
The probability density function (pdf) of the beta distribution, for 0 ≤ x ≤ 1, and shape parameters α, β > 0, is a power function of the variable x and its reflection (1 − x) as :
   
The beta function, β , is a normalization constant to ensure that the total probability is 1.

We plotted Beta distribution by writing a code for it in Python by importing Numpy, Scipy and Matplot libraries in Spyder software on Anaconda IDE.
ALGORITHM :
Import the Numpy, Matplot and Scipy libraries.
Generate N random numbers and set the value of α and β
Create mean and variance by using the mean and variance functions respectively
Define Beta function as :
def betadis(x, a, b):
    			From scipy.special import beta
    				numfx=x**(a-1)*(1-x)**(b-1)
    				denfx=beta(a,b)
    				return numfx/denfx
    				mean=beta(a/a+b)
    				var=beta(a*b)/(a+b)**2*(a+b+1)
    				return mean,var
5) Set eps = 0.0000001 
6) Set the sequence of evenly spaced numbers by using the linspace function
7) Call the Beta function
8) Plot the histogram of the distribution using the histogram function
Output :

For α = 1
And β = 1
For the above plotted graph : 
MEAN
VARIANCE
0.5013
0.0837

BANDIT SOLUTIONS :
On the basis of the way we do exploration, there are different ways to solve the multi bandit problem.
No exploration at all
In this approach, we don’t try to explore any new options for the problem. We keep on exploiting the current available known option only. Example : Greedy Algorithm
Random Exploration 
In this approach, we explore all the possible options available in order to learn in order to get the complete knowledge about the whole scenario.
Example : Epsilon Algorithm
Exploration with preference to uncertainty
In this approach, we have some partial knowledge about the options available and decision is made on the basis of that knowledge. Future decisions are made on the basis of the past results.
	Example : Thompson Sampling

POSSIBLE SOLUTIONS FOR MULTI ARMED BANDIT PROBLEM :
Random Sampling
Random sampling is a way of selecting a sample of observations from a population in order to make conclusions (on the basis of evidence and reasoning) about the population. For example, exit polls from voters that aim to predict the likely results of an election.
The key aspect of random sampling lays in its name. The selection of observations must occur in a 'random' way, meaning that they do not differ in any manner from the observations which have not been sampled. Normally, it is assumed that statistical tests contain data that has been obtained through random sampling.
It is a sampling technique in which each sample has an equal probability of being chosen. A sample chosen randomly should not be biased towards the population.
ALGORITHM : 
Generate N random numbers
From the generated random numbers, the user selects any number randomly or say plays the game once. The user is unaware of results of the played games in the past.
f the user wins, he continues to play on that machine whereas if he loses, he again selects a machine randomly from the left over bandits.
This loop goes on as long as the player plays the game.
We wrote a python code for it in Spyder in the Anaconda IDE and checked it for two different samples of size 10000 each.

OUTPUT (For Sample 1) :
Total reward : 1050

OUTPUT (For Sample 2):  
Total Reward : 1073

Thompson Sampling
Thompson sampling is an algorithm for decision problems where actions are taken sequentially in a manner that must balance between exploiting what is known to maximize current performance and accumulate new information that may improve future performance. The algorithm addresses a broad range of problems in a computationally efficient manner and is therefore enjoying wide use [4].
The basic idea of Thompson sampling is that in every round, we take our existing knowledge of the machines about the unknown parameters, and we sample the parameters from this distribution. This sampled parameter yields a set of expected rewards for every machine, and now we bet on the one with the highest expected return, under that sampled parameter.
Thompson Sampling is a method for making decisions in the exploration-exploitation dilemma. It basically involves choosing the action that maximizes the expected reward with respect to a randomly selected arm.
ALGORITHM :
Generate N random numbers
Here, every machine has some probability (values of alpha and beta). These probabilities are drawn from beta distribution which is the key to Thompson Sampling.
Now we will calculate the of win for each machine like :
   prob=np.random.beta(arm_win[k]+1,arm_luz[k]+1,1)
    4) The probabilities are then drawn from the beta distribution. The    machine having the highest probability is picked and it’s arm is pulled.
   5) If the user wins, then arm_win counter is incremented and if the user loses, then arm_lose counter is incremented.
  6) This process if repeated until the stopping criterion is met.
We used the concept of Random Sampling to solve the multi armed bandit problem. We wrote a python code for it in Spyder in the Anaconda IDE and checked it for two different samples of size 10000 each.

Output for Sample 1:
Total Reward : 1861
Output for Sample 2 :
Total Reward : 2733

For getting a distribution of the various rewards obtained, we run the code a thousand times, i.e. a for loop upto 1000.
OUTPUT (For Sample 1) :      

                                          Total Reward : 1944
OUTPUT (For Sample 2) :

Total Reward : 2672

Epsilon(ε) Greedy Algorithm
The ε-greedy algorithm takes the most greedy path of the time, but does random exploration occasionally. The action value is estimated according to the past experience by averaging the rewards associated with the target action that we have observed so far. It is a very simple algorithm and is used mostly in Machine Learning.
This Algorithm works by going to and fro between exploration with probability = 𝜖 and exploitation with probability 1 - 𝜖.  Suppose you are standing in front of k = 4 slot machines. Each machine pays out according to a different probability distribution, and these distributions are unknown to you. And suppose you can play a total of 100 times.
You have two goals. The first goal is to experiment in order to determine which machine pays out the best. The second, related, goal is to get as much money as possible. The terms “explore” and “exploit” are used to indicate that you have to use some coins to explore to find the best machine, and you can experiment as much on the best machine to exploit your knowledge. Epsilon-greedy is almost too simple. As you play the machines, you keep track of the average payout of each machine. Then, you select the machine with the highest current payout with probability = (1 – epsilon)  where epsilon is a small value like 0.10. And you select machines that don’t have the highest current payout with probability = epsilon.
ALGORITHM :
In this algorithm, we basically have two goals. Firstly, we have to determine experimentally which machine gives the highest reward. Secondly, earn as much money as possible.
The user plays the game and then selects the machine giving the highest payout with probability = (1 – epsilon) and the machines which don’t have the highest payout with probability = epsilon.
We used the concept of Epsilon Greedy to solve the multi armed bandit problem. We wrote a python code for it in Spyder in the Anaconda IDE and checked it for two different samples of size 10000 each.

OUTPUT (For Sample 1) :
Total Reward : 1244
OUTPUT (For Sample 2) :
Total Reward : 1407

COMPARISON BETWEEN THESE THREE ALGORITHMS :
A Case Study
All the three algorithms can be used to solve the multi armed bandit problem. Epsilon Greedy, as the name says is the greediest of all the algorithms. In this algorithm, the value of epsilon, i.e, is selected by the user before the experiment starts. The algorithm is so greedy that in spite of not having sufficient knowledge about the available options, it tends to choose the one having the most profit. On the other hand, Thompson Sampling is a combination of both exploration and exploitation. With practice, we can optimise our decisions eventually whereas Random Sampling does no exploration at all. It selects any bandit randomly and sticks to the arm having the highest payout or say having the highest reward. 
If we increase the size of the sample, Thompson Sampling will show the most accuracy as it follows the concept of best of both worlds, i.e, it exploits and explores both at the same time.
