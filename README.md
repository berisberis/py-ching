# Py-Ching

## Random i-ching trigram generator that iterates and graphs results

---
# Run with Docker

```
docker run -p 80:80 quay.io/berisberis/py-ching 
```
go to http://localhost/web/4096/1

or to http://localhost/api/4096/1 for an api version.

# Develop
``` 
$ git clone https://github.com/berisberis/py-ching
$ cd py-ching
```
## Create a virtual env and activate it:
```
$ python3 -m venv venv
$ . venv/bin/activate
```
## Run
```
$ export FLASK_APP=iching
$ export FLASK_ENV=development
$ flask run
```
Open http://127.0.0.1:5000 in a browser.

Make a [Chart](http://127.0.0.1:5000/web/4096/1) and refresh

Or make a get request to the [Api](http://127.0.0.1:5000/api/4096/4)

# About the I-ching
The I Ching is the oldest binary system developed by the chinese around 1000-750BC.
> the I Ching is an influential text read throughout the world, providing inspiration to the worlds of religion, psychoanalysis, literature, and art.
... The basic unit is the hexagram (卦 guà), a figure composed of six stacked horizontal lines (爻 yáo). Each line is either broken or unbroken. The received text of the Zhou yi contains all 64 possible hexagrams, along with the hexagram's name.
... In the canonical I Ching, the hexagrams are arranged in an order dubbed the King Wen sequence after King Wen of Zhou, who founded the Zhou dynasty and supposedly reformed the method of interpretation. The sequence generally pairs hexagrams with their upside-down equivalents, although in eight cases hexagrams are paired with their inversion.
... The contemporary scholar Shao Yong rearranged the hexagrams in a format that resembles modern binary numbers, although he did not intend his arrangement to be used mathematically. This arrangement, sometimes called the binary sequence, later inspired Leibnitz.
... The psychologist Carl Jung took interest in the possible universal nature of the imagery of the I Ching, discussing his theories of archetypes and synchronicity.
[Wikipedia](https://en.wikipedia.org/wiki/I_Ching)

The following image represents the Fu Xi Sequence which is exactly the order of the binary counting system we used today in computers.
The colors on the first column and row represent each of the 8 possible trigrams in the 3-bit color palette, and combined make every of the 64 possibilities of the 6-bit RGB color palette. 

![6-bit RGB hexagrams](https://fractaluniverse.files.wordpress.com/2019/03/screen-shot-2019-03-14-at-2.59.21-pm.png)

If you map every trigram in a cube you get the same arrangement used in bit error correction called [Hamming Space](https://en.wikipedia.org/wiki/Hamming_space).
Following the same rules you can map every color palette in use by computers. 

The following images represent the 3-bit RGB and 6-bit [RGB palettes](https://en.wikipedia.org/wiki/List_of_color_palettes) arranged in 3 dimensions.

![3bit color pallete cube](https://fractaluniverse.files.wordpress.com/2019/03/3-bit_rgb_cube.gif)
![6bit color pallete cube](https://fractaluniverse.files.wordpress.com/2019/03/6-bit_rgb_cube.gif)

The I-Ching also presents a binary fractal pattern that increases one dimension in each iteration.

![Iching fractal pattern](https://fractaluniverse.files.wordpress.com/2019/02/cache_897298771.png)

Gottfried Leibniz was inspired by the I Ching when he refined the binary numbering system in his 1703 Article called "Explanation of Binary Arithmetic". [Wikipedia on Leibniz and the I Ching](https://en.wikipedia.org/wiki/Binary_number#Leibniz_and_the_I_Ching)

![Binary counter](https://fractaluniverse.files.wordpress.com/2019/05/binary_counter.gif)

# About Randomness
> Several computational methods for pseudo-random number generation exist. All fall short of the goal of true randomness, although they may meet, with varying success, some of the statistical tests for randomness intended to measure how unpredictable their results are (that is, to what degree their patterns are discernible). This generally makes them unusable for applications such as cryptography. However, carefully designed cryptographically secure pseudo-random number generators (CSPRNG) also exist, with special features specifically designed for use in cryptography.

> There are two principal methods used to generate random numbers. The first method measures some physical phenomenon that is expected to be random and then compensates for possible biases in the measurement process. Example sources include measuring atmospheric noise, thermal noise, and other external electromagnetic and quantum phenomena. For example, cosmic background radiation or radioactive decay as measured over short timescales represent sources of natural entropy.

>The second method uses computational algorithms that can produce long sequences of apparently random results, which are in fact completely determined by a shorter initial value, known as a seed value or key. As a result, the entire seemingly random sequence can be reproduced if the seed value is known. This type of random number generator is often called a pseudorandom number generator. This type of generator typically does not rely on sources of naturally occurring entropy, though it may be periodically seeded by natural sources.

> Some systems take a hybrid approach, providing randomness harvested from natural sources when available, and falling back to periodically re-seeded software-based cryptographically secure pseudorandom number generators (CSPRNGs). The fallback occurs when the desired read rate of randomness exceeds the ability of the natural harvesting approach to keep up with the demand. This approach avoids the rate-limited blocking behavior of random number generators based on slower and purely environmental methods.
[Wikipedia](https://en.wikipedia.org/wiki/Random_number_generation)

Even the (cryptographically secure) Yarrow algorithm used today in iOS and MacOS (as /dev/random) alludes its name to the use of the yarrow plant in the random process of I Ching divination (although coins are used too).
>The Yarrow algorithm is a family of cryptographic pseudorandom number generators (PRNG). The name Yarrow alludes to the use of the yarrow plant in the random generating process of I Ching divination. Since the Xia dynasty (c. 2070 to c. 1600 BCE), Chinese have used yarrow stalks for divination. Fortunetellers divide a set of 50 yarrow stalks into piles and use modulo arithmetic recursively to generate two bits of random information that have a non-uniform distribution.
[Wikipedia](https://en.wikipedia.org/wiki/Yarrow_algorithm)

# Synchronicity and quantum mechanics

Derived from psychologist Carl Jung's study of the I Ching he developed a concept called synchronicity that holds:
> Meaningful connections in the world manifest through coincidence with no apparent causal link. What he referred to as “acausal connecting principle”. Proposing it as a functional explanation for how the I-Ching worked, although he was never clear about how synchronicity worked.
> Jung influenced one philosophical interpretation (not the science) of quantum physics with the concept of synchronicity regarding some events as non-causal. That idea influenced the physicist Wolfgang Pauli (with whom, via a letter correspondence, he developed the notion of unus mundus in connection with the notion of non-locality AKA entanglement) and some other physicists.
[Wikipedia](https://en.wikipedia.org/wiki/Carl_Jung#Interpretation_of_quantum_mechanics)

> According to a certain view, synchronicity serves as a way of making sense of or describing some aspects of quantum mechanics. It argues that quantum experiments demonstrate that, at least in the microworld of subatomic particles, there is an instantaneous connection between particles no matter how far away they are from one another. Known as quantum non-locality or entanglement, the proponents of this view argue that this points to a unified field that precedes physical reality. As with archetypal reasoning, the proponents argue that two events can correspond to each other (e.g. particle with particle, or person with person) in a meaningful way.
[Wikipedia](https://en.wikipedia.org/wiki/Synchronicity#Quantum_Physics)


## This is a work in progress

![Quantum I Ching](https://fractaluniverse.files.wordpress.com/2019/03/imagen-1481.jpg)