# Particle-Simualtor

A small and simple non-optmized particle simulator, built-in with *two particles* types. Using *Euler's method* as gravity system.

>Particles Types

- **Fluid** → Can move sideways and downwards.
- **Solid (Moveable)** → Can move downwards, but not sideways directly as fluids, but, moving *diagonally down*.
- **Solid (Frozen)** → Cannot move at all, *not applied by gravity*.

‎ 

> Particles Names

- **Water** → A *fluid type* particle, light blue-ish colored, *keybind = 1.*
- **Sand** → A *moveable solid type* particle, yellow-ish colored, *keybind = 2.*
- **Grass** → A *frozen solid type* particle, green-ish colored, *keybind = 3.*

‎ 

> How it works

It stores *particles information* into a *python list*, with the values:
**(x,y, c)**
- **x** → X axis cordinates of the particle
- **y** → Y axis cordinates of the partcile
- **c** → Color/Type of the particle, based on color values.

‎ 

> Creating new particles**

- Get mouse cordinates
- Checks into *particles list* if there's a particle in that cordinates
- Append cordinates and desired type to the list *(if there is no particle in that location)*

‎ 

> Deleting particles**

- Get mouse cordinates
- Checks into *particles list* if there's a particle in that cordinates
- Delete particle from *particle list*

**Be happy :)**
