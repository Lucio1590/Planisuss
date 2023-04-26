  

Università degli Studi di Pavia
-------------------------------

### Bachelor degree in Artificial Intelligence

  

Planisuss —  exam project — A.Y. 2022/23

Stefano Ferrari

  

### Computer programming,  and Data str., Mod. 1

Computer programming, Algorithms and Data str., Mod. 1

Stefano Ferrari

  

Planisuss — Final exam project — A.Y.

  

Contents
========

1.  The Planisuss world
    
2.  The ecosystem 5
    
    1.  Vegetob 5
        
    2.  Erbast 6
        
    3.  Carviz 6
        
    4.  Ecosystem limits 6
        
3.  A day on Planisuss 7
    
    1.  Growing 7
        
    2.  Movement 7
        
    3.  Grazing 8
        
    4.  Struggle 8
        
        Fight 8
        
        Hunt 8
        
    5.  Spawning 9
        
4.  Data visualization 9
    
    1.  Maps 10
        
    2.  Plots 11
        
    3.  Trajectories 11
        
    4.  Cells details 11
        
        3
        
    5.  Logs and replay 11
        
    6.  Simulation controls 12
        
5.  Notes 12
    
    1.  Differences with Game of Life and Wa-Tor 12
        
    2.  Computational complexity 13
        
    3.  Social groups 14
        
    4.  Variants 14
        
    5.  Development suggestions 14
        
6.  Constants 14
    
7.  Resources 15
    
    1.  The matplotlib library 15
        
    2.   numpy library 15
        
    3.  Constants 15
        

References 16

  

date: February 7, 2023

version: 0.95

  

The final exam project consists  the design and implementation of a simulation  a  world  “Planisuss”, freely inspired  Wa- \[1\]\[2\] and Conway’s Game of Life \[3\]\[4\]. The simulation  intended to provide data to be  visualized using the library matplotlib \[5\] ( Sect. 7.2). In  to  some flexibility in the design, the specifications below described  refer to the simulation parameters through suitable constants, summarized in Sect. 6. The constants are represented using in uppercase  font (e.g., CONST).

 Planisuss world is constituted of a single continent which is populated by three species: Vegetob, Erbast, and Carviz. In  simulation, several individuals of the species interact evolving their  under the rules explained in the next sections.

  

1.  #### The Planisuss world
    
    Planisuss is  structured in geographical units  _cells_. Cells are organized in a  grid structure and  position  be identified by a bidimensional coordinate.
    
    The size of Planisuss is NUMCELLS × NUMCELLS cells.
    
    The cells can be occupied by water or ground. Cells on the boundary of the grid are  occupied by water. All  other cells are suitably assigned either to water or ground at the  of the simulation.
    
    Each  cell can host individuals of the three species,  water cells are uninhabitable. A suitable procedure initializes the  of the cells at  beginning  the simulation.
    
    All the Erbast in a cell constitute a herd. Similarly, all  Carviz in a cell constitute a pride.
    
    The basic events on  in discrete time units  _days_. For practical purposes, the simulation can be terminated after a predefined number  days, NUMDAYS.
    
      
    
2.  ####  ecosystem
    
    Three species populates Planisuss:
    
    **Vegetob** (_pl._ Vegetob) is a vegetable species. Spontaneously  on the ground  a  cycle. Vegetob is the nutrient of Erbast.
    
    **Erbast** (_pl._ Erbast) is a herbivore species. Erbast eat Vegetob. They can move on the continent to find better living conditions. Individuals can group together, forming a _herd_.
    
    **Carviz** (_pl._ Carviz) is a carnivore species. Carviz predate Erbast.  can move on the continent to find better living conditions. Individuals can group together,  a _pride_.
    
    Erbast and  are animal species.
    
      
    
    1.  Vegetob
        
        Vegetob are  by their   a cell.  density can have a value between 0 and 100.
        
          
        
    2.  Erbast
        
        Erbast  characterized by the following properties:
        
        *   Energy: represents the strength of the individual. It is consumed for the activities (movement and fight) and   increased by grazing. When  energy value  0, the Erbast dies.
            
        *   Lifetime: duration  the life of the Erbast expressed in days. Its  is  at    does not change.
            
        *   Age: number  days from birth. When the  reaches the lifetime values, the individual terminates its existence.
            
        *   Social attitude:  the likelihood of an individual to join  a herd. It is  by a value in \[0, 1\].
            
              knowledge about the  of the cells around their position up to a distance of
            
            NEIGHBORHOOD cells. Erbast   same cell form a herd.
            
              
            
    3.  Carviz
        
         are  by the following properties:
        
        *   Energy: represents the strength  the individual. It is consumed for the activities (movement and fight) and can be increased by hunting. When the  value reaches 0, the Carviz dies.
            
        *   Lifetime: duration of the life  the Carviz expressed in days.  value is set at the birth and does not change.
            
        *   Age: number of days from birth. When the age reaches the lifetime values,   terminates its existence.
            
        *    attitude: measures the likelihood of an  to join to a pride. It is represented by a value in \[0, 1\].
            
            Carviz  knowledge about the  of  cells around  position up to a distance of
            
            NEIGHBORHOOD cells. Carviz in the  cell form a pride.
            
              
            
    4.  Ecosystem limits
        
        Some design choices must  made to proper  the simulation:
        
        **Cell capacity** While the Vegetob density is specified as   \[0, 100\], its  as integer or real number can be questioned.  simplest choice would be using an integer to represent the density, but this limits the minimum change in this property to be equal to 1.
        
        Another   is  number of  constituting a  or a pride. This has the   in limiting  computational complexity and the  motivation  only a  number of individuals can crowd a  area. However, if not set, other factors related to the dynamics of the  can indirectly limit the population numerosity. In the following, these limits will be  as MAX\_ and
        
          
        
        MAX\_PRIDE  the herd and pride, respectively. In case these constants are not used or defined, they can  interpreted as an indefinitely large value. In Python,  maximum number of elements of a **list**  on the architecture of the used platform, but they are really quite large for the  of this project (in the order of 109 for 32-bit and 1018 for 64-bit systems).
        
        Energy limit A  of the  is not explicitly needed (and integer can be proper), but can be  to avoid a divergent trajectory of the species, which  involve  extinction of one  the two animal species. It will be referred  MAX\_ENERGY.
        
        Lifetime limit Similarly to the Energy, the lack of limitation of the Lifespan value can involve a  with a strange dynamics. It will be   MAX\_LIFE.
        
          
        
3.  #### A  on Planisuss
    
    The time on Planisussis structured in units  _day_. A  is articulated in the following phases:
    
      grow everywhere  a   (GROWING).
    
    Movement The individuals of animal species (Erbast and Carviz)  if move in another area.  is articulated  individual and   (herd  pride) movement.
    
    Grazing Erbast which did not move, can graze the Vegetob in the area.
    
    Struggle Carviz insisting on the same area can fight or hunt.
    
    Spawning  of animal species can generate  offspring.
    
    Conventionally, long  of time on Planisuss are measured in months, years, decades and centuries, where a month is 10 days long, a year is  months long, a decade is 10 years long, and a century is  decades long.
    
      
    
    1.  Growing
        
        The Vegetob density is increased by GROWING. If a cell is completely surrounded by cells having the maximum Vegetob density,  animals present in the cell are overwhelmed by the Vegetob and terminated.
        
          
        
    2.  Movement
        
         the Movement phase,  and  groups evaluate  possibility to move in another cell. Based on suitable rules,   appealing cell in the neighborhood  identified. The evaluation is carried on first by  group basis (herd and pride).
        
        All the Erbast in a cell at the  of the day form a herd. Similarly,  the   a cell constitute a pride.  groups can have memories and strategies:  values can be stored and used in the evaluation and planning. For instance, they can be provided with   of the last  visited to avoid to move back, or the density  nutrients of cells visible  previous days.
        
        Once  herd and the pride of  cell made a decision (stay or move), the individuals can choose if they will follow the social group or made a  decision,   the social group.
        
          
        
        Splitting decision can be formed considering  properties  the individual (e.g., the herd will move, while the individual having a low value of energy may stay; or, on the contrary, the herd will stay, but strong Erbast may want  move, due to the lack of Vegetob in the cell)  is weighted with the social attitude of the individual.
        
        Movements take place  all the cells at the same time and are instantaneous. The movement costs  each individual one point of Energy.
        
          
        
    3.  Grazing
        
        The Erbast that did  move, can graze  increment their Energy. The grazing decreases the   of the cell. Every Erbast can have 1 point of   1  of  density. If the Vegetob density   than the number of Erbast, 1 point is assigned  those Erbast having the lowest value of Energy, up to  of the Vegetob of the cell.
        
        Optionally, the Social attitude of those individuals  did not eat (due to lack of Vegetob) can be decreased.
        
          
        
    4.  Struggle
        
        After the movements, the social groups in the cells may need  be reorganized. In fact, different social groups of the same species can reach the same cell.
        
        Erbast in the  joint to the same herd. If two or more herds moves in the same cell, the herds are fused (and their memories  be joined).
        
        If more than one Carviz  reach the cell, they evaluate the   a single pride. The  is made on pride-basis, using the social  of  members. If  of the  decide not to join, a fight takes place. In case of more than  prides reaching the same cell,  above  is applied iteratively to  of prides (i.e., starting from those with less individuals). The prides that decided to join can form the single pride before starting the fight.
        
          
        
        Fight
        
        The fight between  prides is a last-blood match.   simplest form, a random number is drawn and  pride has a winning probability proportional  the sum of the Energy on its components.
        
        A more complex scheme may consider one-to-one matches between the champions of the pride (those having the higher Energy), until one of  prides has no more components.
        
        Optionally, the Social attitude of  winning pride components can be increased.
        
          
        
        Hunt
        
        When only one pride is present in  cell, a hunt takes place. The pride identifies  stronger Erbast in the cell and combat with him. Similarly to the fight, several scheme can be adopted:
        
        *   No combat: The prey is always took down. No Energy  for the pride.
            
        *   Single assault: The pride has only one opportunity to take down the prey. A random  is  and the probability of success depends on  relative value of  cumulative Energy of the  and the  of the prey.
            
              
            
        *   Last blood: The single assault  is repeated, but every fruitless assault costs   to the pride (e.g., one  from a random individual).
            
        *   In case  success, the Energy  the prey is shared by the pride individuals, increasing their energy value (spare energy points are  to the Carviz with  lowest Energy).
        
          
        
        Optionally,  events can change the Social  of the individuals. For instance, the Social attitude of the winning pride  and the surviving  components can be increased. Alternatively, if no prey is hunt (due to absence of preys or to failure of  hunt) the Social attitude of  pride  can decrease.
        
          
        
    5.  Spawning
        
        The Spawning is the last phase of the day. The Age value of the animals are increased by one day.
        
        Those  reach an age multiple of 10 (one month) have their Energy decreased by AGING.
        
        Those that reach their Lifetime are terminated by spawning two offsprings. The offsping properties are set with the following rules:
        
        *   Age: set to 0.
            
        *   Energy:  sum of the  of the offsprings is equal to the  of the parent.
            
        *   Other properties: the average of the properties of the offsprings are   the corresponding properties of the parent.
            
            – Hence, the sum of  property values of the offsprings  the   the corresponding  of the parent.
            
            In case MAX\_HERD and MAX\_PRIDE are defined, the spawning is allowed only if the social group can be enlarged to  the offsprings. Any rule can be  to decide which  can spawn.
            
              
            
4.  #### Data visualization
    
     status and the dynamics  Planisuss can be  represented in the user  of the simulation program. While global  (such as, for instance, the population of a species) can be represented as a single  (at a given time or on the average),  elaborated visual  should be used to display trends  local properties  larger scale. For instance, the population vs. time can  represented as a time plot graph, while a pseudocolors map can  used  provide an overall representation  the instantaneous population of Planisuss.
    
     visualization may be interactive, allowing  user  operate on  simulation speed (basically it could be the ability to reset/pause/restart the simulation), to change  displayed properties,   the parameters  the elements in the simulation, and to limit the visualization to a  portion of the graph (e.g., zooming on a map or a plot).
    
    The matplotlib  provides the functionalities to display data and to build  interactive interface \[5\]\[6\].
    
    Among others the following  graphs  be implemented:
    
    *   Overall map: it allows to represent graphically the current  of the simulated world by mapping the parameters of interest. Optionally, zooming on an area can be also provided.
        
          
        
    *   Population plots:  of the inhabitants (e.g., average or cumulative Energy) can be plotted versus the simulation time to show trends. Also, the plots may show  relationship  a pair  properties (e.g.,  numerosity of Erbast wrt. Carviz).
        
    *   Trajectories: shows  position of the populations on the map  wrt. time.
        
    *   Cell inspection: the properties of the inhabitants  a given cell can be represented in detail. Optionally the events occurring in the different phases of the day may be depicted.
        
    *   Besides realtime visualization, replay of  already runned simulation can be provided.  would require the  of the populations properties of interest, such as  or  Energy.
    
      
    
      
    
    1.  Maps
        
        The most suitable  of the global  of Planisuss is probably by means of a map.  Planisuss has a planar topology and its  is structured as a regular square grid, the  can be realized  a  image, where each  corresponds to a cell of the world grid.
        
        The  of values  a  property of a cell can assume can then be mapped on a color  to be visualized: the    cell is codified as a color and this color is assigned to the corresponding pixel of the  image. For instance, the  of  Vegetob  range between 0 and 100. Hence, a suitable function to map an integer number in \[0, 100\] to a color can be used to represent the Vegetob density as a NUMCELLS × NUMCELLS image.
        
        In color images, the color of a pixel can be described using the  of the three primary  (red, green, and blue). The shades of the primary colors are usually represented  values in \[0, 1\] (being 0 the  of the color and 1 its maximum intensity),  as  in {0, . . . , 255} (being 0   of the color and 255 its maximum intensity). The matrix containing the all  coefficients of a given primary color is called a channel. Hence, a color image can be represented by three matrices that are the red (R), green (G), and blue (B) channels.
        
        For instance, the mapping  representing the Vegetob density is then a function \[0, 100\] →
        
        \[0, 1\]3.
        
        A useful map can show the numerosity of the population using one channel for each species. For example:
        
        *   R: Carviz
            
        *   G: Erbast
            
        *   B: water/Vegetob density
            
        *   Two  need to  addressed:  mapping of the population of    in \[0, 1\]  the mapping of two features (  the cell as water or ground,  the Vegetob density).
        
          
        
        For the first mapping, if MAX\_ and MAX\_PRIDE have been defined,  function can simply map 0 in 0 and MAX\_ ( MAX\_PRIDE) to 1 (hence a normalization  respect to the maximum value). If the constants are set to a  high value, the mapping can be non-linear (e.g., logarithmic). Otherwise,  MAX\_HERD and MAX\_PRIDE have not been  (  its value is very high with respect to the current situation), the scaling can be done with respect to the    elements  the corresponding  group at the given time.
        
        The mapping  mix two features (that are mutually exclusive) can be done using  first half of the  spectrum for  water and the second  the Vegetob density. Since the population
        
          
        
        in water cells are always zero, this mapping will  zero to all the channels of  cells, representing them  black pixels. A ground cell  zero individuals of any species would be represented as a mid-blue pixel.
        
        An alternative visualization  consist in several single-feature maps.
        
        Also, if the grid size is small with respect to the resolution of the screen (or the   the   to the map),  cell can be represented as a group  pixels,  each element of the group represents a single feature.
        
        Details on how a map can  realized and visualized using matplotlib can be found  \[6\].
        
          
        
    2.  Plots
        
        While a map can represent a geographical distribution of the properties of the cells ( value vs.  cell position), a plot can represent the relationship between two entities. The simplest plot family  a property value vs. the time. For instance, the overall numerosity of a species wrt the simulation  (e.g., measured in simulated days). Different graphical elements (like the color, the thickness, or the style of a line) can be used to distinguish different properties on the same plot.
        
        Another way to compare and relate two properties is plotting one vs.  other. For instance, the numerosity of two species can be   a  axis, where  values of these properties at the  simulation  are the  of the points on the graph. The line joining the   the time order provides a  of the trajectory of the simulation in the domain of the properties.
        
        Three-dimensional plots  also be considered.
        
          
        
    3.  Trajectories
        
        The movements  some social  or individual of interests   tracked and shown on the map. In this case, the information does not consist in the content of the cells, but in time and  of the element of interest. Hence, the color of the cells of the map can just reflect  the cell is water or ground. Instead, additional information (e.g., the numerosity of a herd)  be added using the line appearance (e.g., color or thickness).
        
          
        
    4.  Cells details
        
         events happening in a single  can be represented in several forms.  the content of a cell at a single instant, other information could be of interest. For instance, the average population of the species or the relative frequency with which  cell remains unpopulated.   can be represented as  plots.
        
        Optionally, the description can have a finer resolution, by  the  phase events.
        
          
        
    5.  Logs  replay
        
        Some information generated during  simulation  be  to be re- later. The usage of the  values may be of different nature.
        
        The first  simply the replay of the evolution of the simulated word. Different level of detail can be considered for this goal.  instance, at the least level  detail, the   can
        
          
        
         considered. This information can be represented as time  or property vs. property plots, as described in Section 4.2.
        
        Higher level of detail logging can consider grid-level information,  also the  positions  the content of each cell.
        
        The full logging of the properties of the simulated world allows a full replay of the simulation as well as the evaluation of alternative evolutions.  possible usage of  logged data may be reconstruct the life of  of interest (e.g., the strongest Carviz,  the the one generating the largest family tree).
        
        The logging for archival and replay purposes can  different than the  for in-simulation inspection or visualization. The   be obtained from the latter by discarding some information.
        
          
        
    6.  Simulation controls
        
        The  of the simulation may  realized allowing the  a  interaction.
        
        Basically,  user can start, pause, and terminate a simulation. Other  interactions  be slowing down or speeding up the simulation.
        
        Also, in case the simulation are tuned to run for a long time, a _Save_/_Load_ functionality should be provided. In this case, all the  characterizing the  of the simulation must be stored and a   recall them and assign the proper value to the program  has to be devised.  particular format is required in this specification, and any library (such as pickle) can be  for this purpose.
        
        Additionally, the user may  allowed  change some simulation parameters, from a global parameter to the content of a single cell.
        
          
        
5.  #### Notes
    
    1.  Differences with Game of Life and Wa-Tor
        
        This  consists in the design  implementation of a simulation freely inspired by Wa-Tor \[1\]\[2\] and Conway’s Game of Life \[3\]\[4\]. A short comparison with these two simulated world  help.  both of them, the world is represented  a square grid and in each cell  one individual (if any) may exist.
        
          
        
         of Life  cell can be populated or unpopulated. At any time step, a cell is evaluated and, based on its  and its neighbors status, the status (populated/unpopulated) can change.
        
          
        
        Wa-Tor The world has the topology of a torus and two species: shark and fish.  each time step, an individual can randomly move in a  cell, provided that it is unpopulated. A shark can also  in a cell populated by a fish: in this case,   is removed from the simulation and  shark gains a certain quantity of energy. This property control the shark population: each time step, the  is decreased and a shark dies when its energy reaches zero. After a given number  time steps,  individuals  reproduce. It happens by generating a new  in an empty neighboring cell, resetting   for the reproduction.
        
          
        
        The Planisuss’s rules  hence an extension of the Wa-Tor’s rules. Planisuss differs from Wa-Tor by  complexity  the rules (in Wa-Tor  are either deterministic or based on randomness, while Planisuss allows the use of some goodness function), the structure of the ecosystem, and the condivision   grid elements. In fact,  main  is   Planisuss a single cell  host more than one individual, also  different species. Also, in  three species are present, although  (Vegetob)  the role of nutrient for the prey species (Erbast) and its dynamic  very simple (like the cells in Game of Life).
        
        Another difference is the presence of social groups that  to simplify some of the operations by deciding some collective behavior for a large  of individuals instead of computing  (complex) decision procedure for each of them.
        
        Also, predators (Carviz)  clash for the dominance of the same territory.
        
          
        
    2.  Computational complexity
        
         present specification allows great  in the definition of the procedures driving the evolution  the simulated ecosystem. This choice  motivated  the  to have  variegated spectrum of  and to  anyone to set the more  level of detail  the simulation.
        
        Several factors influence the computational  required  the simulation:
        
          
        
        Time span The duration of the simulation can be  by the number of simulated days it lasts. The computational complexity  the simulation is directly proportional to the number of simulated days, NUMDAYS.
        
        **Grid size** Each time unit, several  have to be evaluated for each  cell. Hence  computational time is directly proportional to the grid size, NUMCELLS2.
        
        **Decision policy** In every cell, at most one herd  one  are present. Every social  must take  decision  the day. The first one  the movement. After that, each  has to decide whether follow the social group or operate a different decision. The complexity of the decision policy  the social group can be relatively high, but it has a mild impact on the  complexity (it  only for NUMCELLS2 times). The complexity of   decision,   have a higher impact: it should not be made as exceedingly high.
        
         The struggle phase  have some impact in the complexity of the single cell, but  it represents a relatively rare event. Hence, its impact on the total computational cost should  mild.
        
          
        
        The computational cost of the simulation is then proportional to NUMDAYS×NUMCELLS2. For a 1 000 × 1  grid and  100 years (i.e., 104 days) simulation, the computational cost is  1010 times the cost of the decision policy. Considering that the current  has a clock speed in the  of 109 operation per second, each operation in  decision policy may add tenth of  in the physical duration of the simulation.
        
        Hence, simulations on larger  or for a larger number  years may require a substantial  of machine time.
        
        A compromise between the size of the grid, the duration  the simulation, and the complexity of the daily procedure (i.e., the smartness of  species) may be necessary.
        
          
        
    3.  Social groups
        
        The collective behavior is a factor that allowed the surviving and the evolution of species (and also  Planisuss can help weak individuals), but it is a feature that allows to run a simulation with a large number of individuals.
        
         effect is  evident if the Social attitude  is large. In this case, once of the   decision  the movement has been made, if most   individuals will follow the group, the computational cost for the  decision is negligible.
        
        In order to keep low   cost of the simulation,  individual decision procedures should be kept as simple  possible. On the  hand, the social group decisions may use more computational resources   the group decision smarter. A simple technique can be storing the  of the last visited cells, in order to avoid to move back in a territory that could have been already exploited. The stored cells may cover regions that do not belong  the explorable  of NEIGHBORHOOD radius.
        
          
        
    4.  Variants
        
        The  of the dynamics of Planisuss are intentionally flexible to allow  to  the preferred characterization and degree of complexity.
        
        More complex scenarios may include geological or climatic phenomena. For instance, a tidal cycle  be devised, which periodically allows  cells  become water, and viceversa.
        
         option, to allow a gaming user interaction, is to provide  user  “God-mode” interaction tools, which strongly change the evolution of  populations. For instance, a period of drought can stop the growing of Erbast (in given regions or globally), meteors can destroy the life in a region, or on the contrary, in a region a given species can have some advantage (e.g.,  Lifetime).
        
          
        
    5.  Development suggestions
        
        The simulation of Planisuss has the purpose of providing data   interactive data visualization, using the library matplotlib \[5\] (see Sect. 7.2).
        
        A complex set of rules for the evolution of the ecosystem may provide a rich and interesting scenario for the visualization, but its development should not shade  focus,  is the  visualization that make observable what is going on the  world.
        
        In order  get familiar with matplotlib (and the problem of simulation), Game of   Wa-Tor can  used in  first development rounds. Once the visualization tools have been tuned, the complexity of  can  implemented.
        
        Similarly, the simplest options described in the  document can be considered (e.g., randomness instead of smartness), but  the classes with attributes and methods needed for more complex functionalities.
        
          
        
6.  #### Constants
    
     this section, some parameters that characterize the simulation are reported as constants. Their values should be chosen  customize the dynamics of the designed simulation. Referring  them  the  allows to modify easily the overall dynamics of the simulation. A proposal for an implementation  these parameters is  described in Sect. 7.3.
    
      
    
    NUMCELLS:  of matrix representing the Planisuss map. It is  number of  in each row and each column. A possible variant may consider a  map,  as a NUMCELLS\_R × NUMCELLS\_C matrix.
    
    NEIGHBORHOOD: The radius of the region that a social group can evaluate  decide  movement. Its value could be  for Erbast and Carviz (NEIGHBORHOOD\_E  NEIGHBORHOOD\_C, respectively).  value may impact the  of the movement decision.
    
    MAX\_ and MAX\_PRIDE:  maximum numerosity of the social groups. These values can be undefined and not used in the program. If used, they  be interpreted as a soft-max value. For instance, if the  move  the same cell, they  together, and their number  exceeds MAX\_HERD. This should be allowed, and the  splitting can be  in the next day.
    
    NUMDAYS:   the simulation. Although this value is not required (the termination could be  controlled by the user), it can  set in order to easy  simulation management and the plotting.
    
    MAX\_ and MAX\_LIFE: Respectively the maximum value of Energy and Lifetime. They are not required,  a proper value can avoid simulation divergency. In fact, a large value  Lifetime allows an individual  collect high value of Energy and  the generation of stronger and more long-lived one of its offspring,  this property in the next generations.  two  may have different value for these constants (MAX\_ENERGY\_E  MAX\_LIFE\_E for Erbast, and (MAX\_ENERGY\_C and MAX\_LIFE\_C for Carviz).
    
    AGING: The quantity of energy lost each month. It is not required (it can be zero) and can be different for   species (AGING\_E and AGING\_C for Erbast and Carviz, respectively).
    
    GROWING: The  of Vegetob   grows in every cell at the beginning of the day.
    
      
    
7.  #### Resources
    
    1.   matplotlib library
        
        matplotlib is a free and open- cross- library for interactive data visualization using Python \[5\].
        
        A short tutorial on its use (with code examples) can be  in \[6\].
        
          
        
    2.   numpy library
        
         is a library for scientific  in Python \[7\]. It   data structures for the data visualization in matplotlib.
        
        A  tutorial on its use ( code examples) can be found in \[6\].
        
          
        
    3.  Constants
        

The value of the constants described in Sect. 6  be chosen  to several factors. A possible implementation is proposed  \[8\].

  

  

Every  in Planisuss, a Erbast wakes up.   it must outrun the fastest Carviz or it   killed.

Every morning in Planisuss, a Carviz wakes up. It knows it must run faster than the slowest Erbast, or  will starve.

It doesn’t matter whether you’re the  or a Erbast—when the sun comes up, you’d  be running.

Unless you are a Vegetob.

  

  

Planisuss proverb

  

References
==========

  

1.  A. K. Dewdney, “Computer recreations: Sharks and fish wage an ecological war on the toroidal planet wa-tor,” _Scientific American_, vol. 251, pp. 14–22, December 1984.
    
2.  “Wa-tor.” https://en.wikipedia.org/wiki/Wa-Tor.
    
3.  M. Gardner, “The fantastic  of John Conway’s  solitaire game ”life”,” _Scientific American_, vol. 223, pp. 120–123, October 1970.
    
4.  “Conway’s game of life.” https://en.wikipedia.org/wiki/Conway%27s\_Game\_of\_Life.
    
5.  “Matplotlib website.” https://matplotlib.org/.
    
6.  S. Ferrari, “Numpy and matplotlib minimal tutorial.” https://elearning.unipv.it/mod/ folder/view.php?id=67083, 2023.
    
7.  “NumPy website.” https://numpy.org/.
    
8.  “ for planisuss.” https://elearning.unipv.it/pluginfile.php/269900/mod\_ folder/content/0/planisuss\_constants.py, 2023.
    

  

17