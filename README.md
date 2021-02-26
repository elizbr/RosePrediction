# RosePrediction
smarter than your producer team 

Using NLP to predict Bachelor season winners based on dialogue, in episode installments.


Many questionable and unethical prediction models for bachelor season winners have appeared online over 
the past few years. Ranging from fitting mod- els based on occupation, age, and other factors to the sh
eer perceived beauty score of women’s faces. Inspired by more recent ’reality’ shows such as Netflix’s 
Love is Blind, I am setting out to test if we can accurately predict a contestant’s final stand- ing bas
ed on her words. If yes, then how many episodes of dialogue are required to predict the right winner? Ke
eping in mind that this is a highly edited and produced show, we will see, when ap- plying the mentality 
the famous phrase ”Love is blind,” from the Merchant of Venice, how accurate can our prediction for love
be?

Evaluation Plan

In terms of evaluating the performance, I think it will be important to compare the model’s selected win
ner after introducing a new episode’s worth of content. This way we will be able to see how many episode
s need to take place before the model can accurately predict the winner of the season. As a baseline, it 
could be interesting to introduce a base model that fits only on the metadata available from Kaggle, but 
this doesn’t seem that interesting to me. Alternatively, I could require the model to rank all of the con
testants from winner to loser for each episode and rate the model’s accuracy based on how the contestants
did actually finish in the season. Let me know if this is more interesting than the first approach I menti
oned above. Overall, I think we can agree that accuracy is most important?
