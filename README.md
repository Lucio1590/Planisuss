<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html lang="en" xmlns="http://www.w3.org/1999/xhtml">

<head>
    <title></title>
</head>

<body>
    <p><br></p>
    <h2>Universit&agrave; degli Studi di Pavia</h2>
    <h3>Bachelor degree in Artificial Intelligence</h3>
    <p><br></p>
    <p>Planisuss &mdash; ***** exam project &mdash; A.Y. 2022/23</p>
    <p>Stefano Ferrari</p>
    <p><br></p>
    <h3>Computer programming, ********** and Data str., Mod. 1</h3>
    <p>Computer programming, Algorithms and Data str., Mod. 1</p>
    <p>Stefano Ferrari</p>
    <p><br></p>
    <p>Planisuss &mdash; Final exam project &mdash; A.Y.</p>
    <p><br></p>
    <h1>Contents</h1>
    <ol>
        <li>
            <p>The Planisuss world</p>
        </li>
        <li>
            <p>The ecosystem<span>&nbsp;</span>5</p>
            <ol id="l2">
                <li>
                    <p>Vegetob<span>&nbsp;</span>5</p>
                </li>
                <li>
                    <p>Erbast<span>&nbsp;</span>6</p>
                </li>
                <li>
                    <p>Carviz<span>&nbsp;</span>6</p>
                </li>
                <li>
                    <p>Ecosystem limits<span>&nbsp;</span>6</p>
                </li>
            </ol>
        </li>
        <li>
            <p>A day on Planisuss<span>&nbsp;</span>7</p>
            <ol id="l3">
                <li>
                    <p>Growing<span>&nbsp;</span>7</p>
                </li>
                <li>
                    <p>Movement<span>&nbsp;</span>7</p>
                </li>
                <li>
                    <p>Grazing<span>&nbsp;</span>8</p>
                </li>
                <li>
                    <p>Struggle<span>&nbsp;</span>8</p>
                    <p>Fight<span>&nbsp;</span>8</p>
                    <p>Hunt<span>&nbsp;</span>8</p>
                </li>
                <li>
                    <p>Spawning<span>&nbsp;</span>9</p>
                </li>
            </ol>
        </li>
        <li>
            <p>Data visualization<span>&nbsp;</span>9</p>
            <ol id="l4">
                <li>
                    <p>Maps<span>&nbsp;</span>10</p>
                </li>
                <li>
                    <p>Plots<span>&nbsp;</span>11</p>
                </li>
                <li>
                    <p>Trajectories<span>&nbsp;</span>11</p>
                </li>
                <li>
                    <p>Cells details<span>&nbsp;</span>11</p>
                    <p>3</p>
                </li>
                <li>
                    <p>Logs and replay<span>&nbsp;</span>11</p>
                </li>
                <li>
                    <p>Simulation controls<span>&nbsp;</span>12</p>
                </li>
            </ol>
        </li>
        <li>
            <p>Notes<span>&nbsp;</span>12</p>
            <ol id="l5">
                <li>
                    <p>Differences with Game of Life and Wa-Tor<span>&nbsp;</span>12</p>
                </li>
                <li>
                    <p>Computational complexity<span>&nbsp;</span>13</p>
                </li>
                <li>
                    <p>Social groups<span>&nbsp;</span>14</p>
                </li>
                <li>
                    <p>Variants<span>&nbsp;</span>14</p>
                </li>
                <li>
                    <p>Development suggestions<span>&nbsp;</span>14</p>
                </li>
            </ol>
        </li>
        <li>
            <p>Constants<span>&nbsp;</span>14</p>
        </li>
        <li>
            <p>Resources<span>&nbsp;</span>15</p>
            <ol id="l6">
                <li>
                    <p>The <span>matplotlib&nbsp;</span>library<span>&nbsp;</span>15</p>
                </li>
                <li>
                    <p>*** <span>numpy&nbsp;</span>library<span>&nbsp;</span>15</p>
                </li>
                <li>
                    <p>Constants<span>&nbsp;</span>15</p>
                </li>
            </ol>
        </li>
    </ol>
    <p>References<span>&nbsp;</span>16</p>
    <p><br></p>
    <p>date: February 7, 2023</p>
    <p>version: 0.95</p>
    <p><br></p>
    <p>The final exam project consists ** the design and implementation of a simulation ** a ********** world ****** &ldquo;Planisuss&rdquo;, freely inspired ** Wa-*** [1][2] and Conway&rsquo;s Game of Life [3][4]. The simulation ** intended to provide data to be ************* visualized using the library matplotlib [5] (*** Sect. 7.2). In ***** to ***** some flexibility in the design, the specifications below described **** refer to the simulation parameters through suitable constants, summarized in Sect. 6. The constants are represented using in uppercase ********** font (e.g., CONST).</p>
    <p>*** Planisuss world is constituted of a single continent which is populated by three species: Vegetob, Erbast, and Carviz. In *** simulation, several individuals of the species interact evolving their ********** under the rules explained in the next sections.</p>
    <p><br></p>
    <ol id="l7">
        <li>
            <h4>The Planisuss world</h4>
            <p>Planisuss is ********* structured in geographical units ****** <em>cells</em>. Cells are organized in a ******* grid structure and ***** position *** be identified by a bidimensional coordinate.</p>
            <p>The size of Planisuss is NUMCELLS <span>&times;&nbsp;</span>NUMCELLS cells.</p>
            <p>The cells can be occupied by water or ground. Cells on the boundary of the grid are ****** occupied by water. All *** other cells are suitably assigned either to water or ground at the ********* of the simulation.</p>
            <p>Each ****** cell can host individuals of the three species, ***** water cells are uninhabitable. A suitable procedure initializes the ******* of the cells at *** beginning ** the simulation.</p>
            <p>All the Erbast in a cell constitute a herd. Similarly, all *** Carviz in a cell constitute a pride.</p>
            <p>The basic events on *************** in discrete time units ****** <em>days</em>. For practical purposes, the simulation can be terminated after a predefined number ** days, NUMDAYS.</p>
            <p><br></p>
        </li>
        <li>
            <h4>*** ecosystem</h4>
            <p>Three species populates Planisuss:</p>
            <p><strong>Vegetob&nbsp;</strong>(<em>pl.&nbsp;</em>Vegetob) is a vegetable species. Spontaneously ***** on the ground **** a ******* cycle. Vegetob is the nutrient of Erbast.</p>
            <p><strong>Erbast&nbsp;</strong>(<em>pl.&nbsp;</em>Erbast) is a herbivore species. Erbast eat Vegetob. They can move on the continent to find better living conditions. Individuals can group together, forming a <em>herd</em>.</p>
            <p><strong>Carviz&nbsp;</strong>(<em>pl.&nbsp;</em>Carviz) is a carnivore species. Carviz predate Erbast. **** can move on the continent to find better living conditions. Individuals can group together, ******* a <em>pride</em>.</p>
            <p>Erbast and ****** are animal species.</p>
            <p><br></p>
            <ol id="l8">
                <li>
                    <p>Vegetob</p>
                    <p>Vegetob are ************* by their ******* ** a cell. *** density can have a value between 0 and 100.</p>
                    <p><br></p>
                </li>
                <li>
                    <p>Erbast</p>
                    <p>Erbast *** characterized by the following properties:</p>
                    <ul id="l9">
                        <li>
                            <p>Energy<span>: represents the strength of the individual. It is consumed for the activities (movement and fight) and *** ** increased by grazing. When *** energy value ******* 0, the Erbast dies.</span></p>
                        </li>
                        <li>
                            <p>Lifetime<span>: duration ** the life of the Erbast expressed in days. Its ***** is *** at *** ***** *** does not change.</span></p>
                        </li>
                        <li>
                            <p>Age<span>: number ** days from birth. When the *** reaches the lifetime values, the individual terminates its existence.</span></p>
                        </li>
                        <li>
                            <p>Social attitude<span>: ******** the likelihood of an individual to join ** a herd. It is *********** by a value in [0, 1].</span></p>
                            <p>****** **** knowledge about the ****** of the cells around their position up to a distance of</p>
                            <p>NEIGHBORHOOD cells. Erbast ** *** same cell form a herd.</p>
                            <p><br></p>
                        </li>
                    </ul>
                </li>
                <li>
                    <p>Carviz</p>
                    <p>****** are ************* by the following properties:</p>
                    <ul id="l10">
                        <li>
                            <p>Energy<span>: represents the strength ** the individual. It is consumed for the activities (movement and fight) and can be increased by hunting. When the ****** value reaches 0, the Carviz dies.</span></p>
                        </li>
                        <li>
                            <p>Lifetime<span>: duration of the life ** the Carviz expressed in days. *** value is set at the birth and does not change.</span></p>
                        </li>
                        <li>
                            <p>Age<span>: number of days from birth. When the age reaches the lifetime values, *** ********** terminates its existence.</span></p>
                        </li>
                        <li>
                            <p>****** attitude<span>: measures the likelihood of an ********** to join to a pride. It is represented by a value in [0, 1].</span></p>
                            <p>Carviz **** knowledge about the ****** of *** cells around ***** position up to a distance of</p>
                            <p>NEIGHBORHOOD cells. Carviz in the **** cell form a pride.</p>
                            <p><br></p>
                        </li>
                    </ul>
                </li>
                <li>
                    <p>Ecosystem limits</p>
                    <p>Some design choices must ** made to proper ************ the simulation:</p>
                    <p><strong>Cell capacity&nbsp;</strong>While the Vegetob density is specified as ****** ** <span>[</span>0, 100<span>]</span>, its ****** as integer or real number can be questioned. *** simplest choice would be using an integer to represent the density, but this limits the minimum change in this property to be equal to 1.</p>
                    <p>Another ******** ********** is *** number of *********** constituting a **** or a pride. This has the ********* ********** in limiting *** computational complexity and the ********* motivation **** only a ******* number of individuals can crowd a ******* area. However, if not set, other factors related to the dynamics of the ****** can indirectly limit the population numerosity. In the following, these limits will be ******** as MAX_**** and</p>
                    <p><br></p>
                    <p>MAX_PRIDE *** the herd and pride, respectively. In case these constants are not used or defined, they can ** interpreted as an indefinitely large value. In Python, *** maximum number of elements of a <strong>list&nbsp;</strong>******* on the architecture of the used platform, but they are really quite large for the ******** of this project (in the order of 10<span>9&nbsp;</span>for 32-bit and 10<span>18&nbsp;</span>for 64-bit systems).</p>
                    <p>Energy limit <span>A ********** of the ****** is not explicitly needed (and integer can be proper), but can be **** to avoid a divergent trajectory of the species, which *** involve *** extinction of one ** the two animal species. It will be referred ** MAX_ENERGY.</span></p>
                    <p>Lifetime limit <span>Similarly to the Energy, the lack of limitation of the Lifespan value can involve a ***** with a strange dynamics. It will be ******** ** MAX_LIFE.</span></p>
                    <p><br></p>
                </li>
            </ol>
        </li>
        <li>
            <h4>A *** on Planisuss</h4>
            <p>The time on Planisussis structured in units ****** <em>day</em>. A *** is articulated in the following phases:</p>
            <p>******* <span>******* grow everywhere ** a ***** ******** (GROWING).</span></p>
            <p>Movement <span>The individuals of animal species (Erbast and Carviz) ****** if move in another area. ******** is articulated ** individual and ****** ***** (herd ** pride) movement.</span></p>
            <p>Grazing <span>Erbast which did not move, can graze the Vegetob in the area.</span></p>
            <p>Struggle <span>Carviz insisting on the same area can fight or hunt.</span></p>
            <p>Spawning <span>*********** of animal species can generate ***** offspring.</span></p>
            <p>Conventionally, long ******* of time on Planisuss are measured in months, years, decades and centuries, where a month is 10 days long, a year is ** months long, a decade is 10 years long, and a century is ** decades long.</p>
            <p><br></p>
            <ol id="l11">
                <li>
                    <p>Growing</p>
                    <p>The Vegetob density is increased by GROWING. If a cell is completely surrounded by cells having the maximum Vegetob density, *** animals present in the cell are overwhelmed by the Vegetob and terminated.</p>
                    <p><br></p>
                </li>
                <li>
                    <p>Movement</p>
                    <p>** the Movement phase, *********** and ****** groups evaluate *** possibility to move in another cell. Based on suitable rules, *** **** appealing cell in the neighborhood ** identified. The evaluation is carried on first by ****** group basis (herd and pride).</p>
                    <p>All the Erbast in a cell at the ********* of the day form a herd. Similarly, *** the ****** ** a cell constitute a pride. ****** groups can have memories and strategies: ****** values can be stored and used in the evaluation and planning. For instance, they can be provided with *** ********** of the last **** visited to avoid to move back, or the density ** nutrients of cells visible ** previous days.</p>
                    <p>Once *** herd and the pride of *** cell made a decision (stay or move), the individuals can choose if they will follow the social group or made a ********* decision, ********* ** the social group.</p>
                    <p><br></p>
                    <p>Splitting decision can be formed considering *** properties ** the individual (e.g., the herd will move, while the individual having a low value of energy may stay; or, on the contrary, the herd will stay, but strong Erbast may want ** move, due to the lack of Vegetob in the cell) *** is weighted with the social attitude of the individual.</p>
                    <p>Movements take place *** all the cells at the same time and are instantaneous. The movement costs ** each individual one point of Energy.</p>
                    <p><br></p>
                </li>
                <li>
                    <p>Grazing</p>
                    <p>The Erbast that did *** move, can graze ** increment their Energy. The grazing decreases the ******* ******* of the cell. Every Erbast can have 1 point of ****** *** 1 ***** of ******* density. If the Vegetob density ** ***** than the number of Erbast, 1 point is assigned ** those Erbast having the lowest value of Energy, up to ********** of the Vegetob of the cell.</p>
                    <p>Optionally, the Social attitude of those individuals **** did not eat (due to lack of Vegetob) can be decreased.</p>
                    <p><br></p>
                </li>
                <li>
                    <p>Struggle</p>
                    <p>After the movements, the social groups in the cells may need ** be reorganized. In fact, different social groups of the same species can reach the same cell.</p>
                    <p>Erbast in the **** joint to the same herd. If two or more herds moves in the same cell, the herds are fused (and their memories *** be joined).</p>
                    <p>If more than one Carviz ***** reach the cell, they evaluate the ******* ** a single pride. The ********** is made on pride-basis, using the social ******** of ***** members. If *** of the ****** decide not to join, a fight takes place. In case of more than *** prides reaching the same cell, *** above ********* is applied iteratively to ***** of prides (i.e., starting from those with less individuals). The prides that decided to join can form the single pride before starting the fight.</p>
                    <p><br></p>
                    <p>Fight</p>
                    <p>The fight between *** prides is a last-blood match. ** *** simplest form, a random number is drawn and **** pride has a winning probability proportional ** the sum of the Energy on its components.</p>
                    <p>A more complex scheme may consider one-to-one matches between the champions of the pride (those having the higher Energy), until one of *** prides has no more components.</p>
                    <p>Optionally, the Social attitude of *** winning pride components can be increased.</p>
                    <p><br></p>
                    <p>Hunt</p>
                    <p>When only one pride is present in *** cell, a hunt takes place. The pride identifies *** stronger Erbast in the cell and combat with him. Similarly to the fight, several scheme can be adopted:</p>
                    <ul id="l12">
                        <li>
                            <p>No combat: The prey is always took down. No Energy *********** for the pride.</p>
                        </li>
                        <li>
                            <p>Single assault: The pride has only one opportunity to take down the prey. A random ****** is ***** and the probability of success depends on *** relative value of *** cumulative Energy of the ***** and the ****** of the prey.</p>
                            <p><br></p>
                        </li>
                        <li>
                            <p>Last blood: The single assault ****** is repeated, but every fruitless assault costs **** ****** to the pride (e.g., one ****** from a random individual).</p>
                        </li>
                        <li>In case ** success, the Energy ** the prey is shared by the pride individuals, increasing their energy value (spare energy points are ******** to the Carviz with *** lowest Energy).</li>
                    </ul>
                    <p><br></p>
                    <p>Optionally, *** events can change the Social ******** of the individuals. For instance, the Social attitude of the winning pride ********** and the surviving **** components can be increased. Alternatively, if no prey is hunt (due to absence of preys or to failure of *** hunt) the Social attitude of *** pride *********** can decrease.</p>
                    <p><br></p>
                </li>
                <li>
                    <p>Spawning</p>
                    <p>The Spawning is the last phase of the day. The Age value of the animals are increased by one day.</p>
                    <p>Those **** reach an age multiple of 10 (one month) have their Energy decreased by AGING.</p>
                    <p>Those that reach their Lifetime are terminated by spawning two offsprings. The offsping properties are set with the following rules:</p>
                    <ul id="l13">
                        <li>
                            <p>Age: set to 0.</p>
                        </li>
                        <li>
                            <p>Energy: *** sum of the ****** of the offsprings is equal to the ****** of the parent.</p>
                        </li>
                        <li>
                            <p>Other properties: the average of the properties of the offsprings are ***** ** the corresponding properties of the parent.</p>
                            <p>&ndash; <span>Hence, the sum of *** property values of the offsprings ** the ****** ** the corresponding ******** of the parent.</span></p>
                            <p>In case MAX_HERD and MAX_PRIDE are defined, the spawning is allowed only if the social group can be enlarged to ******* the offsprings. Any rule can be **** to decide which *********** can spawn.</p>
                            <p><br></p>
                        </li>
                    </ul>
                </li>
            </ol>
        </li>
        <li>
            <h4>Data visualization</h4>
            <p>*** status and the dynamics ** Planisuss can be ******** represented in the user ********* of the simulation program. While global ********** (such as, for instance, the population of a species) can be represented as a single ****** (at a given time or on the average), **** elaborated visual *************** should be used to display trends *** local properties ** larger scale. For instance, the population vs. time can ** represented as a time plot graph, while a pseudocolors map can ** used ** provide an overall representation ** the instantaneous population of Planisuss.</p>
            <p>*** visualization may be interactive, allowing *** user ** operate on *** simulation speed (basically it could be the ability to reset/pause/restart the simulation), to change *** displayed properties, ** ****** the parameters ** the elements in the simulation, and to limit the visualization to a ***** portion of the graph (e.g., zooming on a map or a plot).</p>
            <p>The matplotlib ******* provides the functionalities to display data and to build ** interactive interface [5][6].</p>
            <p>Among others the following ************* graphs *** be implemented:</p>
            <ul id="l14">
                <li>
                    <p>Overall map: it allows to represent graphically the current ****** of the simulated world by mapping the parameters of interest. Optionally, zooming on an area can be also provided.</p>
                    <p><br></p>
                </li>
                <li>
                    <p>Population plots: ********** of the inhabitants (e.g., average or cumulative Energy) can be plotted versus the simulation time to show trends. Also, the plots may show *** relationship ** a pair ** properties (e.g., *** numerosity of Erbast wrt. Carviz).</p>
                </li>
                <li>
                    <p>Trajectories: shows *** position of the populations on the map *** wrt. time.</p>
                </li>
                <li>
                    <p>Cell inspection: the properties of the inhabitants ** a given cell can be represented in detail. Optionally the events occurring in the different phases of the day may be depicted.</p>
                </li>
                <li>Besides realtime visualization, replay of ** already runned simulation can be provided. **** would require the ******* of the populations properties of interest, such as ********** or ******* Energy.</li>
            </ul>
            <p><br></p>
            <p><br></p>
            <ol id="l15">
                <li>
                    <p>Maps</p>
                    <p>The most suitable ************** of the global ****** of Planisuss is probably by means of a map. ***** Planisuss has a planar topology and its ******* is structured as a regular square grid, the *** can be realized ** a ******* image, where each ***** corresponds to a cell of the world grid.</p>
                    <p>The *** of values **** a ****** property of a cell can assume can then be mapped on a color *** to be visualized: the ******** ** **** cell is codified as a color and this color is assigned to the corresponding pixel of the *** image. For instance, the ******* of *** Vegetob *** range between 0 and 100. Hence, a suitable function to map an integer number in <span>[</span>0, 100<span>]&nbsp;</span>to a color can be used to represent the Vegetob density as a NUMCELLS <span>&times;&nbsp;</span>NUMCELLS image.</p>
                    <p>In color images, the color of a pixel can be described using the *********** of the three primary ****** (red, green, and blue). The shades of the primary colors are usually represented ** values in <span>[</span>0, 1<span>]&nbsp;</span>(being 0 the ******* of the color and 1 its maximum intensity), ** as ******** in <span>{</span>0, <span>. . .&nbsp;</span>, 255<span>}&nbsp;</span>(being 0 *** ******* of the color and 255 its maximum intensity). The matrix containing the all *** coefficients of a given primary color is called a channel. Hence, a color image can be represented by three matrices that are the red (R), green (G), and blue (B) channels.</p>
                    <p>For instance, the mapping *** representing the Vegetob density is then a function <span>[</span>0, 100<span>]&nbsp;</span><span>&rarr;</span></p>
                    <p>[<span>0, 1</span>]<span>3</span><span>.</span></p>
                    <p>A useful map can show the numerosity of the population using one channel for each species. For example:</p>
                    <ul id="l16">
                        <li>
                            <p>R: Carviz</p>
                        </li>
                        <li>
                            <p>G: Erbast</p>
                        </li>
                        <li>
                            <p>B: water/Vegetob density</p>
                        </li>
                        <li>Two ******** need to ** addressed: *** mapping of the population of ****** *** ****** in <span>[</span>0, 1<span>]&nbsp;</span>*** the mapping of two features (**** ** the cell as water or ground, *** the Vegetob density).</li>
                    </ul>
                    <p><br></p>
                    <p>For the first mapping, if MAX_**** and MAX_PRIDE have been defined, *** function can simply map 0 in 0 and MAX_**** (** MAX_PRIDE) to 1 (hence a normalization **** respect to the maximum value). If the constants are set to a **** high value, the mapping can be non-linear (e.g., logarithmic). Otherwise, ** MAX_HERD and MAX_PRIDE have not been ******* (** ** its value is very high with respect to the current situation), the scaling can be done with respect to the ******* ****** ** elements ** the corresponding ****** group at the given time.</p>
                    <p>The mapping ** mix two features (that are mutually exclusive) can be done using *** first half of the ******* spectrum for *** water and the second *** the Vegetob density. Since the population</p>
                    <p><br></p>
                    <p>in water cells are always zero, this mapping will ****** zero to all the channels of ***** cells, representing them ** black pixels. A ground cell ****** zero individuals of any species would be represented as a mid-blue pixel.</p>
                    <p>An alternative visualization *** consist in several single-feature maps.</p>
                    <p>Also, if the grid size is small with respect to the resolution of the screen (or the ******* ** the ****** ********* to the map), *** cell can be represented as a group ** pixels, ***** each element of the group represents a single feature.</p>
                    <p>Details on how a map can ** realized and visualized using matplotlib can be found ** [6].</p>
                    <p><br></p>
                </li>
                <li>
                    <p>Plots</p>
                    <p>While a map can represent a geographical distribution of the properties of the cells (******** value vs. *** cell position), a plot can represent the relationship between two entities. The simplest plot family ********** a property value vs. the time. For instance, the overall numerosity of a species wrt the simulation **** (e.g., measured in simulated days). Different graphical elements (like the color, the thickness, or the style of a line) can be used to distinguish different properties on the same plot.</p>
                    <p>Another way to compare and relate two properties is plotting one vs. *** other. For instance, the numerosity of two species can be ******* ** a ********* axis, where *** values of these properties at the **** simulation **** are the *********** of the points on the graph. The line joining the ****** ** the time order provides a ************** of the trajectory of the simulation in the domain of the properties.</p>
                    <p>Three-dimensional plots *** also be considered.</p>
                    <p><br></p>
                </li>
                <li>
                    <p>Trajectories</p>
                    <p>The movements ** some social ****** or individual of interests *** ** tracked and shown on the map. In this case, the information does not consist in the content of the cells, but in time and ******** of the element of interest. Hence, the color of the cells of the map can just reflect ** the cell is water or ground. Instead, additional information (e.g., the numerosity of a herd) *** be added using the line appearance (e.g., color or thickness).</p>
                    <p><br></p>
                </li>
                <li>
                    <p>Cells details</p>
                    <p>*** events happening in a single **** can be represented in several forms. ******* the content of a cell at a single instant, other information could be of interest. For instance, the average population of the species or the relative frequency with which *** cell remains unpopulated. ***** ********** can be represented as **** plots.</p>
                    <p>Optionally, the description can have a finer resolution, by ********* the *** phase events.</p>
                    <p><br></p>
                </li>
                <li>
                    <p>Logs *** replay</p>
                    <p>Some information generated during *** simulation *** be ***** to be re-********* later. The usage of the ****** values may be of different nature.</p>
                    <p>The first ** simply the replay of the evolution of the simulated word. Different level of detail can be considered for this goal. *** instance, at the least level ** detail, the ******* ********** can</p>
                    <p><br></p>
                    <p>** considered. This information can be represented as time ***** or property vs. property plots, as described in Section 4.2.</p>
                    <p>Higher level of detail logging can consider grid-level information, ******* also the ************ positions *** the content of each cell.</p>
                    <p>The full logging of the properties of the simulated world allows a full replay of the simulation as well as the evaluation of alternative evolutions. ******* possible usage of *** logged data may be reconstruct the life of ********** of interest (e.g., the strongest Carviz, ** the the one generating the largest family tree).</p>
                    <p>The logging for archival and replay purposes can ** different than the ******* for in-simulation inspection or visualization. The ****** *** be obtained from the latter by discarding some information.</p>
                    <p><br></p>
                </li>
                <li>
                    <p>Simulation controls</p>
                    <p>The ********* of the simulation may ** realized allowing the **** a ******* interaction.</p>
                    <p>Basically, *** user can start, pause, and terminate a simulation. Other ****** interactions *** be slowing down or speeding up the simulation.</p>
                    <p>Also, in case the simulation are tuned to run for a long time, a <em>Save</em>/<em>Load&nbsp;</em>functionality should be provided. In this case, all the *********** characterizing the ****** of the simulation must be stored and a ********* ** recall them and assign the proper value to the program ********* has to be devised. ** particular format is required in this specification, and any library (such as pickle) can be **** for this purpose.</p>
                    <p>Additionally, the user may ** allowed ** change some simulation parameters, from a global parameter to the content of a single cell.</p>
                    <p><br></p>
                </li>
            </ol>
        </li>
        <li>
            <h4>Notes</h4>
            <ol id="l17">
                <li>
                    <p>Differences with Game of Life and Wa-Tor</p>
                    <p>This ******* consists in the design *** implementation of a simulation freely inspired by Wa-Tor [1][2] and Conway&rsquo;s Game of Life [3][4]. A short comparison with these two simulated world *** help. ** both of them, the world is represented ** a square grid and in each cell **** one individual (if any) may exist.</p>
                    <p><br></p>
                    <p>**** of Life <span>**** cell can be populated or unpopulated. At any time step, a cell is evaluated and, based on its ****** and its neighbors status, the status (populated/unpopulated) can change.</span></p>
                    <p><br></p>
                    <p>Wa-Tor <span>The world has the topology of a torus and two species: shark and fish. ** each time step, an individual can randomly move in a *********** cell, provided that it is unpopulated. A shark can also **** in a cell populated by a fish: in this case, *** **** is removed from the simulation and *** shark gains a certain quantity of energy. This property control the shark population: each time step, the ****** is decreased and a shark dies when its energy reaches zero. After a given number ** time steps, *** individuals *** reproduce. It happens by generating a new ********** in an empty neighboring cell, resetting *** ******* for the reproduction.</span></p>
                    <p><br></p>
                    <p>The Planisuss&rsquo;s rules *** hence an extension of the Wa-Tor&rsquo;s rules. Planisuss differs from Wa-Tor by *** complexity ** the rules (in Wa-Tor **** are either deterministic or based on randomness, while Planisuss allows the use of some goodness function), the structure of the ecosystem, and the condivision ** *** grid elements. In fact, *** main ********** is **** ** Planisuss a single cell *** host more than one individual, also ** different species. Also, in ********* three species are present, although *** (Vegetob) *** the role of nutrient for the prey species (Erbast) and its dynamic ** very simple (like the cells in Game of Life).</p>
                    <p>Another difference is the presence of social groups that ***** to simplify some of the operations by deciding some collective behavior for a large ****** of individuals instead of computing *** (complex) decision procedure for each of them.</p>
                    <p>Also, predators (Carviz) *** clash for the dominance of the same territory.</p>
                    <p><br></p>
                </li>
                <li>
                    <p>Computational complexity</p>
                    <p>*** present specification allows great *********** in the definition of the procedures driving the evolution ** the simulated ecosystem. This choice ** motivated ** the *********** to have *********** variegated spectrum of ******** and to ***** anyone to set the more ****** level of detail ** the simulation.</p>
                    <p>Several factors influence the computational **** required ** the simulation:</p>
                    <p><br></p>
                    <p>Time span <span>The duration of the simulation can be ******** by the number of simulated days it lasts. The computational complexity ** the simulation is directly proportional to the number of simulated days, NUMDAYS.</span></p>
                    <p><strong>Grid size&nbsp;</strong>Each time unit, several ********** have to be evaluated for each **** cell. Hence *** computational time is directly proportional to the grid size, NUMCELLS<span>2</span>.</p>
                    <p><strong>Decision policy&nbsp;</strong>In every cell, at most one herd *** one ***** are present. Every social ***** must take **** decision ****** the day. The first one ** the movement. After that, each ********** has to decide whether follow the social group or operate a different decision. The complexity of the decision policy *** the social group can be relatively high, but it has a mild impact on the ***** complexity (it ****** only for NUMCELLS<span>2&nbsp;</span>times). The complexity of *** ********** decision, ******* *** have a higher impact: it should not be made as exceedingly high.</p>
                    <p>******** <span>The struggle phase *** have some impact in the complexity of the single cell, but ******** it represents a relatively rare event. Hence, its impact on the total computational cost should ** mild.</span></p>
                    <p><br></p>
                    <p>The computational cost of the simulation is then proportional to NUMDAYS<span>&times;</span>NUMCELLS<span>2</span>. For a 1 000 <span>&times;&nbsp;</span>1 *** grid and *** 100 years (i.e., 10<span>4&nbsp;</span>days) simulation, the computational cost is ***** 10<span>10&nbsp;</span>times the cost of the decision policy. Considering that the current *** has a clock speed in the ***** of 10<span>9&nbsp;</span>operation per second, each operation in *** decision policy may add tenth of ******* in the physical duration of the simulation.</p>
                    <p>Hence, simulations on larger ***** or for a larger number ** years may require a substantial ****** of machine time.</p>
                    <p>A compromise between the size of the grid, the duration ** the simulation, and the complexity of the daily procedure (i.e., the smartness of *** species) may be necessary.</p>
                    <p><br></p>
                </li>
                <li>
                    <p>Social groups</p>
                    <p>The collective behavior is a factor that allowed the surviving and the evolution of species (and also ** Planisuss can help weak individuals), but it is a feature that allows to run a simulation with a large number of individuals.</p>
                    <p>**** effect is **** evident if the Social attitude ******** is large. In this case, once of the ****** ***** decision ***** the movement has been made, if most ** *** individuals will follow the group, the computational cost for the ********** decision is negligible.</p>
                    <p>In order to keep low *** ************* cost of the simulation, *** individual decision procedures should be kept as simple ** possible. On the ***** hand, the social group decisions may use more computational resources ** **** the group decision smarter. A simple technique can be storing the ********** of the last visited cells, in order to avoid to move back in a territory that could have been already exploited. The stored cells may cover regions that do not belong ** the explorable ************ of NEIGHBORHOOD radius.</p>
                    <p><br></p>
                </li>
                <li>
                    <p>Variants</p>
                    <p>The ************* of the dynamics of Planisuss are intentionally flexible to allow ****** to ********** the preferred characterization and degree of complexity.</p>
                    <p>More complex scenarios may include geological or climatic phenomena. For instance, a tidal cycle *** be devised, which periodically allows ******* cells ** become water, and viceversa.</p>
                    <p>******* option, to allow a gaming user interaction, is to provide *** user ** &ldquo;God-mode&rdquo; interaction tools, which strongly change the evolution of *** populations. For instance, a period of drought can stop the growing of Erbast (in given regions or globally), meteors can destroy the life in a region, or on the contrary, in a region a given species can have some advantage (e.g., ******** Lifetime).</p>
                    <p><br></p>
                </li>
                <li>
                    <p>Development suggestions</p>
                    <p>The simulation of Planisuss has the purpose of providing data ** *** interactive data visualization, using the library matplotlib [5] (see Sect. 7.2).</p>
                    <p>A complex set of rules for the evolution of the ecosystem may provide a rich and interesting scenario for the visualization, but its development should not shade *** focus, **** is the **** visualization that make observable what is going on the ********* world.</p>
                    <p>In order ** get familiar with matplotlib (and the problem of simulation), Game of **** *** Wa-Tor can ** used in *** first development rounds. Once the visualization tools have been tuned, the complexity of ********* can ** implemented.</p>
                    <p>Similarly, the simplest options described in the ******* document can be considered (e.g., randomness instead of smartness), but *********** the classes with attributes and methods needed for more complex functionalities.</p>
                    <p><br></p>
                </li>
            </ol>
        </li>
        <li>
            <h4>Constants</h4>
            <p>** this section, some parameters that characterize the simulation are reported as constants. Their values should be chosen ** customize the dynamics of the designed simulation. Referring ** them ** the **** allows to modify easily the overall dynamics of the simulation. A proposal for an implementation ** these parameters is ******* described in Sect. 7.3.</p>
            <p><br></p>
            <p>NUMCELLS: **** of matrix representing the Planisuss map. It is *** number of ******** in each row and each column. A possible variant may consider a *********** map, *********** as a NUMCELLS_R <span>&times;&nbsp;</span>NUMCELLS_C matrix.</p>
            <p>NEIGHBORHOOD: The radius of the region that a social group can evaluate ** decide *** movement. Its value could be ********* for Erbast and Carviz (NEIGHBORHOOD_E *** NEIGHBORHOOD_C, respectively). *** value may impact the **** of the movement decision.</p>
            <p>MAX_**** and MAX_PRIDE: *** maximum numerosity of the social groups. These values can be undefined and not used in the program. If used, they ****** be interpreted as a soft-max value. For instance, if the ***** move ** the same cell, they ***** together, and their number *** exceeds MAX_HERD. This should be allowed, and the **** splitting can be ****** in the next day.</p>
            <p>NUMDAYS: ****** ** the simulation. Although this value is not required (the termination could be ******** controlled by the user), it can ** set in order to easy *** simulation management and the plotting.</p>
            <p>MAX_****** and MAX_LIFE: Respectively the maximum value of Energy and Lifetime. They are not required, *** a proper value can avoid simulation divergency. In fact, a large value ** Lifetime allows an individual ** collect high value of Energy and ****** the generation of stronger and more long-lived one of its offspring, ********** this property in the next generations. *** two ****** may have different value for these constants (MAX_ENERGY_E *** MAX_LIFE_E for Erbast, and (MAX_ENERGY_C and MAX_LIFE_C for Carviz).</p>
            <p>AGING: The quantity of energy lost each month. It is not required (it can be zero) and can be different for *** *** species (AGING_E and AGING_C for Erbast and Carviz, respectively).</p>
            <p>GROWING: The ******** of Vegetob ******* **** grows in every cell at the beginning of the day.</p>
            <p><br></p>
        </li>
        <li>
            <h4>Resources</h4>
            <ol id="l18">
                <li>
                    <p>*** <span>matplotlib&nbsp;</span>library</p>
                    <p>matplotlib is a free and open-****** cross-******** library for interactive data visualization using Python [5].</p>
                    <p>A short tutorial on its use (with code examples) can be ***** in [6].</p>
                    <p><br></p>
                </li>
                <li>
                    <p>*** <span>numpy&nbsp;</span>library</p>
                    <p>***** is a library for scientific ********* in Python [7]. It ******** *** data structures for the data visualization in matplotlib.</p>
                    <p>A ***** tutorial on its use (**** code examples) can be found in [6].</p>
                    <p><br></p>
                </li>
                <li>
                    <p>Constants</p>
                </li>
            </ol>
        </li>
    </ol>
    <p>The value of the constants described in Sect. 6 ****** be chosen *********** to several factors. A possible implementation is proposed ** [8].</p>
    <p><br></p>
    <p><br></p>
    <p>Every ******* in Planisuss, a Erbast wakes up. ** ***** it must outrun the fastest Carviz or it **** ** killed.</p>
    <p>Every morning in Planisuss, a Carviz wakes up. It knows it must run faster than the slowest Erbast, or ** will starve.</p>
    <p>It doesn&rsquo;t matter whether you&rsquo;re the ****** or a Erbast&mdash;when the sun comes up, you&rsquo;d ****** be running.</p>
    <p>Unless you are a Vegetob.</p>
    <p><br></p>
    <p><br></p>
    <p>Planisuss proverb</p>
    <p><br></p>
    <h1>References</h1>
    <p><br></p>
    <ol id="l19">
        <li>
            <p>A. K. Dewdney, &ldquo;Computer recreations: Sharks and fish wage an ecological war on the toroidal planet wa-tor,&rdquo; <em>Scientific American</em>, vol. 251, pp. 14&ndash;22, December 1984.</p>
        </li>
        <li>
            <p>&ldquo;Wa-tor.&rdquo; https://en.wikipedia.org/wiki/Wa-Tor.</p>
        </li>
        <li>
            <p>M. Gardner, &ldquo;The fantastic ************ of John Conway&rsquo;s *** solitaire game &rdquo;life&rdquo;,&rdquo; <em>Scientific American</em>, vol. 223, pp. 120&ndash;123, October 1970.</p>
        </li>
        <li>
            <p>&ldquo;Conway&rsquo;s game of life.&rdquo; https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life.</p>
        </li>
        <li>
            <p>&ldquo;Matplotlib website.&rdquo; https://matplotlib.org/.</p>
        </li>
        <li>
            <p>S. Ferrari, &ldquo;Numpy and matplotlib minimal tutorial.&rdquo; https://elearning.unipv.it/mod/ folder/view.php?id=67083, 2023.</p>
        </li>
        <li>
            <p>&ldquo;NumPy website.&rdquo; https://numpy.org/.</p>
        </li>
        <li>
            <p>&ldquo;********* for planisuss.&rdquo; https://elearning.unipv.it/pluginfile.php/269900/mod_ folder/content/0/planisuss_constants.py, 2023.</p>
        </li>
    </ol>
    <p><br></p>
    <p>17</p>
</body>

</html>