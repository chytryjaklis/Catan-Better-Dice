The goal of this project was simple — to enhance the board game Catan by replacing traditional dice, which can be very random, with virtual dice that allow for more accurate tracking of results and provide greater control over the gameplay. In the traditional Catan board game, the dice rolls are fully random, and each roll can lead to large fluctuations in the results, which affects the pace of the game and the players' emotions. This project aimed to create an alternative solution that not only replaces the traditional way of rolling dice but also introduces a more thoughtful method of generating results based on weighted probabilities of the possible numbers.

By reducing randomness, this version of the game makes the gameplay more predictable, allowing players to better plan their actions and make strategic decisions. With weights assigned to the dice results, players can adjust their strategies to more stable and logical distributions of outcomes, reducing the frustration associated with unfavorable random results. As a result, the game gains depth, offering players more opportunities to showcase their skills and make more complex decisions. This increases the satisfaction of the game, as the outcome becomes more dependent on strategy, rather than just chance.

Weight Distribution and Probabilities
The weights assigned to each number in this project were determined based on the probability of obtaining certain results when rolling two standard six-sided dice, as well as the actual distribution of results in the Catan game. Below is the table that shows the probability distribution for the weighted dice rolls:

Result	Weight (%)	Probability	Notes
2     	2.78%        	1/36	    One possible outcome (1+1)
3      	5.56%        	2/36	    Two possible outcomes (1+2, 2+1)
4      	8.33%        	3/36	    Three possible outcomes (1+3, 2+2, 3+1)
5      	11.11%      	4/36	    Four possible outcomes (1+4, 2+3, 3+2, 4+1)
6      	13.89%      	5/36	    Five possible outcomes (1+5, 2+4, 3+3, 4+2, 5+1)
7      	16.67%      	6/36	    Six possible outcomes (1+6, 2+5, 3+4, 4+3, 5+2, 6+1)
8      	13.89%      	5/36	    Five possible outcomes (2+6, 3+5, 4+4, 5+3, 6+2)
9      	11.11%      	4/36    	Four possible outcomes (3+6, 4+5, 5+4, 6+3)
10    	8.33%        	3/36	    Three possible outcomes (4+6, 5+5, 6+4)
11    	5.56%        	2/36	    Two possible outcomes (5+6, 6+5)
12    	2.78%        	1/36    	One possible outcome (6+6)

Project Versions:

Catan_Better_Dice_simple.py (CLI) – The simplest version, allowing for dice rolls, with game statistics displayed at the end.

Catan_Better_Dice.py (CLI) – A more advanced version, allowing the user to choose the number of players and assign names to each player rolling the dice. It has a more user-friendly interface.

Catan_Better_Dice_GUI.py – A GUI version of the game, featuring all the functions from previous projects.

Catan_Better_Dice.exe (CLI) – The project in an executable file based on the code from Catan_Better_Dice.py. This version does not require running from the terminal. (Recommended)

Catan_Better_Dice_GUI.exe – The project in an executable file based on the code from Catan_Better_Dice_GUI.py. This version does not require running from the terminal. (Recommended if you want to play in GUI)

Inspiration:
This project was inspired by the game on the website Colonist.io, specifically the concept of a balanced dice.
