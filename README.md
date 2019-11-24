# varify
Our idea tries to improve purely text-based personality tests by adding other communication cues being assessed with our AI.
---

This repo contains the code for several neural network trying to predict the outcome of a personality test based on different iput data.

## data.py
Containes the training data the we created to be able to teach our algotrithms the personality of a canditate.

## nn.py
Simple neural network looking at the most important the we as software develpoes have to make: choosing our favourite editor ot the right programming language for the  job etc.

#### nn_test.py
Small application to test the output of nn.py with customazible inputs.

## nn_img
This neural network is trying to find the personality traints of a person based on their image itself. Using the nn_img_test.py script it is possible to run the trained algotimhn on an own image.

## nn_human
This network is filled with data that is collected from humans like the openess of a person to williing  a short interview.

|network| loss | accuracy |
|---|---|---|
| nn.py | 0.0345 | 0.7857 |
| nn_img | 0.1383 | 0.4118 |
| nn_human | 0.1273 | 0.4643 |

