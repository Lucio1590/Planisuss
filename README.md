<div class="markdown prose w-full break-words dark:prose-invert light">
    <h1>Wa-Tor: Carviz, Vegetob, and Erbast Edition</h1>
    <p>This is a modified version of the Wa-Tor simulation for a bachelor project in Artificial Intelligence. The
        simulation focuses on the interaction between three entities: Carviz, Vegetob, and Erbast.</p>
    <h2>Table of Contents</h2>
    <ul>
        <li><a href="#introduction" target="_new">Introduction</a></li>
        <li><a href="#rules" target="_new">Rules</a>
            <ul>
                <li><a href="#carviz" target="_new">Carviz</a></li>
                <li><a href="#vegetob" target="_new">Vegetob</a></li>
                <li><a href="#erbast" target="_new">Erbast</a></li>
            </ul>
        </li>
        <li><a href="#simulation" target="_new">Simulation</a></li>
        <li><a href="#installation" target="_new">Installation</a></li>
        <li><a href="#running-the-simulation" target="_new">Running the Simulation</a></li>
        <li><a href="#customization" target="_new">Customization</a></li>
        <li><a href="#license" target="_new">License</a></li>
    </ul>
    <h2>Introduction</h2>
    <p>Wa-Tor is a cellular automaton and ecosystem simulation, originally created by Alexander Keewatin Dewdney. It
        simulates the interaction between fish and sharks in a toroidal (wrap-around) world. In this modified version,
        the fish and sharks are replaced by Carviz, Vegetob, and Erbast, with new rules and interactions to create a
        unique ecosystem.</p>
    <h2>Rules</h2>
    <h3>Carviz</h3>
    <p>Carviz are the primary consumers in this ecosystem. They feed on Vegetob to survive and reproduce. Carviz follow
        these rules:</p>
    <ol>
        <li>Each Carviz has an energy level, which increases when it feeds on Vegetob.</li>
        <li>Carviz lose energy each turn as they move or stay in place.</li>
        <li>If a Carviz's energy reaches zero, it dies.</li>
        <li>A Carviz can reproduce once its energy reaches a certain threshold. When reproducing, a new Carviz is
            created in a neighboring cell.</li>
    </ol>
    <h3>Vegetob</h3>
    <p>Vegetob are the producers in this ecosystem. They grow in the environment and serve as a food source for Carviz.
        Vegetob follow these rules:</p>
    <ol>
        <li>Vegetob have a growth rate, which determines how quickly they grow and spread to neighboring cells.</li>
        <li>Vegetob can be consumed by Carviz, which decreases their population in the cell.</li>
    </ol>
    <h3>Erbast</h3>
    <p>Erbast are the secondary consumers in this ecosystem. They feed on Carviz to survive and reproduce. Erbast follow
        these rules:</p>
    <ol>
        <li>Each Erbast has an energy level, which increases when it feeds on Carviz.</li>
        <li>Erbast lose energy each turn as they move or stay in place.</li>
        <li>If an Erbast's energy reaches zero, it dies.</li>
        <li>An Erbast can reproduce once its energy reaches a certain threshold. When reproducing, a new Erbast is
            created in a neighboring cell.</li>
    </ol>
    <h2>Simulation</h2>
    <p>This simulation uses a grid of cells, each representing a location in the world. Carviz, Vegetob, and Erbast can
        occupy these cells, and their interactions are determined by the rules outlined above. The simulation proceeds
        in discrete time steps or turns, during which each entity follows its rules.</p>
    <h2>Installation</h2>
    <p>To install the simulation, follow these steps:</p>
    <ol>
        <li>Clone the repository:
            <pre><div class="bg-black rounded-md mb-4"><div class="flex items-center relative text-gray-200 bg-gray-800 px-4 py-2 text-xs font-sans justify-between rounded-t-md"><span>bash</span><button class="flex ml-auto gap-2"><svg stroke="currentColor" fill="none" stroke-width="2" viewBox="0 0 24 24" stroke-linecap="round" stroke-linejoin="round" class="h-4 w-4" height="1em" width="1em" xmlns="http://www.w3.org/2000/svg"><path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2"></path><rect x="8" y="2" width="8" height="4" rx="1" ry="1"></rect></svg>Copy code</button></div><div class="p-4 overflow-y-auto"><code class="!whitespace-pre hljs language-bash">git <span class="hljs-built_in">clone</span> https://github.com/username/wa-tor-carviz-vegetob-erbast.git
</code></div></div></pre>
        </li>
        <li>Install the required dependencies:
            <pre><div class="bg-black rounded-md mb-4"><div class="flex items-center relative text-gray-200 bg-gray-800 px-4 py-2 text-xs font-sans justify-between rounded-t-md"><button class="flex ml-auto gap-2"><svg stroke="currentColor" fill="none" stroke-width="2" viewBox="0 0 24 24" stroke-linecap="round" stroke-linejoin="round" class="h-4 w-4" height="1em" width="1em" xmlns="http://www.w3.org/2000/svg"><path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2"></path><rect x="8" y="2" width="8" height="4" rx="1" ry="1"></rect></svg>Copy code</button></div><div class="p-4 overflow-y-auto"><code class="!whitespace-pre hljs">pip install -r requirements.txt
</code></div></div></pre>
        </li>
    </ol>
    <h2>Running the Simulation</h2>
    <p>To run the simulation, execute the following command in the terminal:</p>
    <pre><div class="bg-black rounded-md mb-4"><div class="flex items-center relative text-gray-200 bg-gray-800 px-4 py-2 text-xs font-sans justify-between rounded-t-md"><button class="flex ml-auto gap-2"><svg stroke="currentColor" fill="none" stroke-width="2" viewBox="0 0 24 24" stroke-linecap="round" stroke-linejoin="round" class="h-4 w-4" height="1em" width="1em" xmlns="http://www.w3.org/2000/svg"><path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2"></path><rect x="8" y="2" width="8" height="4" rx="1" ry="1"></rect></svg>Copy code</button></div><div class="p-4 overflow-y-auto"><code class="!whitespace-pre hljs">python wator.py
</code></div></div></pre>
    <p>This will start the simulation with the default settings. The simulation will run until you close the window or
        press <code>Ctrl+C</code> in the terminal.</p>
    <h2>Customization</h2>
    <p>You can customize various parameters of the simulation, such as the grid size, initial populations, and
        reproduction rates. Edit the <code>config.py</code> file to change these settings.</p>
    <h2>License</h2>
    <p>This project is released under the MIT License. See the <code>LICENSE</code> file for more information.</p>
</div>