# Future Tide

## Inspiration
Every year the sea level rises slightly due to the effects of global warming. In order to promote the deceleration of climate change, we created this project to visualize how the ocean will reclaim YOUR house in the future.

## What it does
This bot allows the user to input any address in the world and it will calculate the number of years it would take for that location to be totally submerged in water at the current pace of sea-level rise. It will also output the same metric but if the temperature is 3°C lower each year so that the user can compare the effects that even a small decrease in temperature will have.

## How we built it
The backend of the program is built on a python framework which uses the positionstack and openelevation APIs to convert a human-readable address into coordinates, and another API to find the distance to the nearest coastline from there. This data is fed into a machine-learning model that was trained on data from Brest(France) and Durbin(South Africa) to determine the coefficients and biases of a polynomial regression estimate. With this generalization of the past data, we can predict the year in which the land will go underwater at the current rate.

## Challenges we ran into
A big challenge was adapting our code to the newly-updated discord api. Moreover, another challenge was obtaining the desired metrics for our machine learning model that are from the same location and measured at similar intervals. Additionally, we had issues with the logistical implementation of our machine learning model and how we would obtain one equation from two separate datasets. A major limitation was time as we wanted to create a more sophisticated web application with more complex and accurate algorithms.

## Accomplishments that we're proud of
We were able to accomplish the monumental task of building a discord bot from scratch powered by a regression/machine learning program in 9 short hours. The discord bot will hopefully serve to ensure the future of humanity and continue our species on the upward track of evolution without losing a major portion of our land. Moreover, we were able to learn a lot of new things and most importantly, have fun.

## What we learned
We learned that discord bots can be an appropriate and compelling medium for a front-end, and that machine learning and AI can help with anything, even if it is not actively a part of the backend. We hope to utilize these findings in future projects. 

## What's next for Future Tide
The machine learning model and python backend can be adapted to connect to a web applet to embed in other websites, a mobile app, a tool to estimate future real estate value, or as a research tool for scientists to analyze and improve the algorithm for more accurate predictions. The first improvement will be finding more similar datasets across the world to reduce the possible bias of the current sample and training the model for longer on more powerful hardware to make it closer emulate the data. The next step for our program is to link to Google Maps and display live visualizations of where the coast could be in many years, and connect people with activist groups to reduce climate change.