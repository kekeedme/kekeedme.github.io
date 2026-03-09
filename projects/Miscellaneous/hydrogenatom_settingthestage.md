# Hydrogen Atom

## Introduction
Quantum mechanics is undoubtedly one of the most succesfull theories to date. In addition to being the basis for understanding the structure, composition and interaction of matter, its applications are at the root of all the technological developments of this century and the last.  
There are a lot of examples in the history of science that demonstrated the need to develop a quantum theory. Indeed, some of the examples often cited were the need to understand: i) blackbody radiation, the fact that objects heated to certain temperatures only emitted discrete frequencies (colors) of light; ii) the photoelectric effect, the observation that electrons could be emitted ("kicked off") from the surface of metals when the surface was illuminated with light, but only when the frequency (energy) of the incoming light beam was equal to or greater than a certain treshold energy, characteristic of the metal; or iii) the stability and the discrete light absorption and emission spectrum of matter. All of these observations went against what was understood at the time. The body of physics knowledge of the time, that included Newtonian mechanics, thermodynamics, electricity and magnetism and certain elements of optics, is typically referred to as classical mechanics. In classical mechanics, there were no explanations as to why matter exchanged energy with its surroundings in discrete chunks (quanta). In addition, from what was understood about electricity and magnetism, and the knowledge that atoms constituted of a central positively charged nucleus, and negatively charged electrons moving "around" this nucleus, it was unclear how atoms could be stable.  

In this series of posts, we will discuss the aformentioned third point by specifically focusing on the hydrogen atom. The hydrogen atom is indeed the simplest atom in that it only consists of one positively charged proton, which makes up its nucleus, and one negatively charged electron that occupies space outside that proton. The hydrogen atom is also the simplest quantum mechanical atom to study. It is indeed one of the only quantum systems which can be solved mathematically by hand (i.e. without the use of computers). However, this is not to say that describing this system mathematically is trivial, only that it can be done.  

Our approach will be to first explore how the physicists Niels Bohr developped a hypothesis to explain: i) why the hydrogen atom was stable, and ii) how, from this hypothesis, he could calculate the allowed energies that the atom could absorb and emit when it interacted with specific frequencies of light. We will see how his model was successful in reproducing the experimental absorption/emission spectrum of the hydrogen atom.  
We will then focus on developping the more accepted solution for the hydrogen atom, which comes from solving the Schrodinger equation for the system. We will see that the energy solutions from the Schrodinger equation are equivalent to Bohr's, and we will discuss how the Schrodinger equation is able to go further than the limits of the Bohr model for atoms and molecules.

## Electric fields from charged particles
From our understanding of electricity and magnetism, we know that a charged particle generates an electric field $\vec{E}$ that permeates space around it. The field is a dynamical variable, in that it has a value at different points in space and in time. It could influence (i.e. attract or repel depending on the charge of the source particle) any other charged particle that were to pass in the region surrounding the source particle. The field is a vector quantity, hence it has a magnitude, which is strongest closer to the source and falls as the inverse of the square of the distance from the source. It also has an orientation in space. Conventionally, the electric field lines for negatively charged particles are drawned pointing towards the source, and away from the source in the case of positively charged particles (Figure 1).  

<figure>
    <img src="charged-paricles.png" alt="figure">
    <figcaption>Figure 1. Charged particles generating electric field lines. (Left) negatively-charged particle generating electric field lines that point towards the particle. (Right) positively charged particle generating electric field lines that point away from the particle.  
</figcaption>
</figure>  

###
If we were to bring two, equal in magnitude, but oppositely charged particle, next to one another, the electric field lines emanating out of the positive charge would bend towards the negatively charged particle, in such a way that the field lineswould merge and converge towards the negative charge particle (Figure 2). Although it is not drawn on figure 2, we should also imagnine the field lines at the "back" of the positively charged particles to extend far out of the page and to wrap around and converge towards the negative charge, making even bigger semicircular circle then the ones pictured. These two equal but opposite charges form a dipole, in which, the charges cancel, and what remains is a neutral composite particle.  


<figure>
    <img src="dipole.png" alt="figure">
    <figcaption>Figure 2. Two equal but oppositely charged particles form a neutral dipole.  
</figcaption>
</figure>  

## Atoms should not be stable
A hydrogen atom is built from one proton, which is positively charged, and an electron, which is negatively charged. We know that the proton and electron form a bound state, which is evidenced by the very existence of the hydrogen atom (not a free electron here, and a free proton there). The two particles have charges equal in magnitude but opposite in charge. Hence, from what we have discussed, they form a neutral dipole. These charges should not be seen as stationary, in fact they both are moving around a common center of mass. 
