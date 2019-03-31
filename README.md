# Detection of Degree of Parkinsonism via the Spiral Test
Parkinson's Disease (PD) is a neurodegenerative disease which affects, movement, posture and agility. It involves the gradual loss of dopamine producing neurons in the substantia nigra of the brain which severely affects, fine motor movement, posture, muscular dexterity and strength.
Long before Parkinson's is officially diagnosed, a myriad of symptoms start to appear. The earliest ones are trouble having control over fine motor movement like drawing figures and shapes. 
The "Spiral Test" is a scientifically designed diagnostic tool that helps the neurologist in assessing the degree of Parkinsonian symptoms exhibited by the test taker by evaluating the drawing pattern and using Artifical Intelligence to make a better estimate at determining the degree of Parkinsonian symptoms.
The test consists of **3 parts**:
 - [1] **The Static Spiral Test**:- It involves tracing an Archimidean Spiral on a piece of a paper or a digitised display that is receptive to touch via the finger or a stylus.
 - [2] **The Dynamic Spiral Test**:- It involves tracing the same spiral, but when it sporadically disappears and reappears. Tracing becomes tougher and requires fine motor dexterity and control.
 - [3] **Stability Test on a Certain Point**:- It often happens that patients with PD have a characteristic jerky movement of hands referred to as "pill rolling" tremors. This makes holding the hand steady at a fixed location tough and toilsome. This test, assesses the ability of the test giver to control his fingers/stylus on a dot for a specified period of time.
 
 The test data is collected in the form of lists annotated by the *X, Y, Time* coordinates of the touch points that are involved in the drawing of the spiral. This data is anaylsed using AI techniques to predict a probability of Parkinsonism symptoms which is then provided to the neurologist who can further infer and diagnose ahead and start early treatment.
 
The test also saves a lot of useful time and money that would be otherwise wasted at the neurologist's office, hence being economical and resourceful at the same time.

---
The repository consists of a standalone Android app and a Pygame based Application that provides an intuitive UI for the user to give the test.
The AI analysis is done on the basis of a mathematical test that calculates a score which provides the probability function of the Parkinsonism Symptom.
We have referred to the following paper for the calculation of the DAH Score.

[Link to the paper](https://www.researchgate.net/profile/Muhammed_Isenkul/publication/291814924_Improved_Spiral_Test_Using_Digitized_Graphics_Tablet_for_Monitoring_Parkinson's_Disease/links/56a6211408ae2c689d39d821/Improved-Spiral-Test-Using-Digitized-Graphics-Tablet-for-Monitoring-Parkinsons-Disease.pdf)

---

## How to use the Pygame App?
 - [1] Install pygame:
 ```python
 pip install pygame
 ```
 - [2] Browse to the directory "pygame-app"
 - [3] Run by typing:
 ```python
 python main.py
 ```
## How to use the Android App?
 - [1] Clone the repository
 - [2] Emulate/Run on your device using Android Studio.
 
---
Note that the app doesn't utilises any dataset/model as of now*

