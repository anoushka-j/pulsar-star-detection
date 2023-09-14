# pulsar-star-detection
predicting pulsar stars with machine learning

## Gathering Domain Knowledge

**Introduction**

The subject of this dataset are pulsar stars. In order to understand the features of the dataset, it is helpful to have some domain knowledge of the topic. 

Pulsars, short for “pulsating radio stars” are well described by their given name. Pulsars are a type of highly magnetized, rapidly rotating neutron star, which is a very dense type of star formed when an extremely large star undergoes a supernova explosion at the end of its life. *This supernova explosion is due to the star collapsing under the weight of its own gravity.* 

The rapidly rotating nature of pulsars provide an explanation as to why they are so named: as they rotate, sometimes completing a full rotation in a matter of milliseconds to seconds, they appear to pulse periodically as they appear in our line of sight here on Earth. 

The highly magnetized nature of pulsars (which can have magnetic fields up to trillions of times stronger than that of our own Earth’s) is caused due to their rapid rotation. Firstly, the types of massive stars that tend to become pulsars in the first place usually have significant magnetic fields to begin with. Following the core collapse of the star (having exhausted its nuclear fuel) under its own gravitational pull, the **conservation of angular momentum** is a concept that can be seen. As the star collapses, its radius (and other measurements) shrink rapidly, causing the remnants of the star to rotate faster. The core contracts as it spins faster, the progenitor star’s magnetic field becomes more concentrated and intense, in a process called **magnetic flux conservation.** 

As the remnants form the neutron star, the intensified magnetic field interacts with the charged particles around it (from the star’s collapse), causing them to emit beams of radiation along the star’s magnetic poles. These beams are what form the pulses of pulsars, and are what give them this name. 

### **Integrated Profile**

An integrated profile is the time averaged (average intensity of the observed signal). In the context of pulsar observations, the integrated profile provides a clearer and more representative view of the pulsar's emission behaviour over its rotational period by time-averaging the data collected during multiple rotations. Comparing the integrated profile of the classified non-pulsars and pulsars could provide insight into which types of signal intensity generates each and if there is a pattern. 

### DN-SNR Curve

A DN-SNR curve, often referred to as a "Digital Number-Signal-to-Noise Ratio" curve, is a graphical representation used in the context of image processing and remote sensing to assess the quality of digital images or data acquired from sensors. It plots the Signal-to-Noise Ratio (SNR) against the Digital Number (DN) values for pixels in an image.

Here's what the components of a DN-SNR curve represent:

Digital Number (DN): In remote sensing or digital imaging, the DN represents the numerical value assigned to each pixel in the image. It typically corresponds to the pixel's brightness or intensity level. DNs can range from 0 (e.g., representing complete darkness) to a maximum value (e.g., representing full brightness or saturation).

Signal-to-Noise Ratio (SNR): SNR is a measure of the quality of the signal (useful information) in an image compared to the noise (unwanted interference or random variations). In the context of remote sensing or imaging, SNR quantifies how distinguishable the useful information (e.g., features on the ground) is from random variations or noise in the image. SNR is usually expressed in decibels (dB) and is calculated as:

SNR (dB) = 10 * log10(Signal Power / Noise Power)
Signal Power represents the power of the signal (useful information).
Noise Power represents the power of the noise.
The DN-SNR curve shows how the SNR varies across different DN values in an image. Typically, you'll find that the SNR is higher for brighter or more intense pixels and lower for darker pixels. The curve can help analysts and researchers understand the image quality, identify the dynamic range of the sensor, and assess the trade-offs between capturing dim details and avoiding saturation (i.e., pixels with the maximum DN value).
Features:

1. Mean of the integrated profile.
2. Standard deviation of the integrated profile.
3. Excess kurtosis of the integrated profile.
4. Skewness of the integrated profile.
5. Mean of the DM-SNR curve.
6. Standard deviation of the DM-SNR curve.
7. Excess kurtosis of the DM-SNR curve.
8. Skewness of the DM-SNR curve.
9. Class (Target Variable)
