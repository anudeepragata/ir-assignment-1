## R S Anudeep
## 19230

Q1  
$ \text{Total Time Required to Cover a Cell} =  \text{Total Time to Moving Forward} + \text{Total Time of Turning}$  
$\Rightarrow \frac {\text{Total Distace Travelled Forward}} {\text{Forward speed}} + (\text{Number of Turns} \times \text{Time Taken on each Turn})$  
$\Rightarrow \frac {\text{Total Distace Travelled Forward}} {\text{Forward speed}} + (\text{Number of Turns} \times \frac{\pi}{2 \times \text{Rotational Speed}})$  
$\text{Rotational Speed} = 4.856 rad/s$  
$\text{Forward Speed} = 0.128 m/s$  

$\text{Total Time Required to Cover a Cell} = \frac {\text{Total Distace Travelled Forward}} {\text{0.128}} + (\text{Number of Turns} \times \frac{\pi}{9.712})$
<br/>

1. Cell 0  
$\text{Total Time Required to Cover Cell} = \frac {49.92} {0.128} + (46 \times \frac{\pi}{9.712})$  
$= 389.25 \text{ sec}$
1. Cell 1  
$\text{Total Time Required to Cover Cell} = \frac {0.42} {0.128} + (0 \times \frac{\pi}{9.712})$  
$= 3.28\text{ sec}$
1. Cell 2  
$\text{Total Time Required to Cover Cell} = \frac {10.77} {0.128} + (12 \times \frac{\pi}{9.712})$  
$= 88.02\text{ sec}$
1. Cell 3  
$\text{Total Time Required to Cover Cell} = \frac {0.22} {0.128} + (0 \times \frac{\pi}{9.712})$  
$= 1.72\text{ sec}
1. Cell 4  
$\text{Total Time Required to Cover Cell} = \frac {6.32} {0.128} + (14 \times \frac{\pi}{9.712})$  
$= 53.90\text{ sec}$
1. Cell 5  
$\text{Total Time Required to Cover Cell} = \frac {7.07} {0.128} + (20 \times \frac{\pi}{9.712})$  
$= 61.70\text{ sec}$
1. Cell 6  
$\text{Total Time Required to Cover Cell} = \frac {9.92} {0.128} + (8 \times \frac{\pi}{9.712})$  
$= 80.09\text{ sec}$
1. Cell 7  
$\text{Total Time Required to Cover Cell} = \frac {6.57} {0.128} + (36 \times \frac{\pi}{9.712})$  
$= 62.97\text{ sec}$  
  
$\text{Total Time to cover all cells} =  740.96\text{ sec}$
</br>
</br>

Q2  We will construct a graph using the Reeb graph with vertices as the time taken to clean the cell from where the bot is leaving from. These times have been computed in question 2.  
After thus graph is constructed, we will find out the minimum spanning tree of the graph contructed. Afterthis graph is construced, we now have the order of the cells in which the bot has to clean each cell.  
In our case, the bot has to move from c4 to c3 to c2 to c1 to c0 to c7 to c6 to c5. The bot is now at the end and has cleaned all of the cells.  


Q5  
In the assignment question regarding pursuer evader, I could not implement the code completely but developed the idea for the implementation.  
I thought of using the Art-Galley theorem to decide which nodes that the pursuer should go through. If we place cameras at these nodes, then we can see the whole polygon. Analogous to this problem, we can move out pursuer/pursuers randomly from one node to another. Eventually one of the pursuer will capture the evader because the process is random and the evader cannot predict where the pursuers will go.  
Using two pursuers instead of one will ideally result in faster capturing of the evader as the pursuers will sweep more conatminated area.  
  

Q6  We can implement an obstacle avoidance on both the pursuers which will make sure that the pursuers dont collide even if they have intersecting paths.  