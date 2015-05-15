Metis NY Data Science Bootcamp
McNulty Project
========================================================
author: Marco Lunardi
date: 
transition: rotate

Project Bank: the Data
========================================================

Bank_Additional_Full (supervised):

20 Features, 41'188 samples

It's the most complete one out of the provided datasets, and includes also macroeconomic variables

It contains the outcomes from a phone calls campaign by a Portuguese Bank to sell a term deposit product


First step: much of Exploratory Analysis
========================================================
Even after a first exploratory look at the data it turns out that some of the dataset features have a very low variance, and little influence (if non-existent) on the desired outcome

For instance, suprisingly features like "having a loan", or "having a mortgage" have almost no influence on the customer choice to buy or not to buy the proposed term deposit

Then, some features pruning should be made.


Features Preprocessing
========================================================
incremental: true

- Pruning down to 10 features: generalization capabilities should improve a bit
- Personal features: Age, Job, Marital Status
- Macroeconomic features: Employment Rate variation, 3 months Interest Rate
- Campaign features: Number of Contacts through previous Campaign, Days passed from previous Contacts, Outcome from past Campaign, Contacts through current Campaign, Means of Contact
- Scaling all features to  0 - 1  interval: some binary, some continuous

The Model
=======================================================

I tried many training/testing sizes, and many classifiers: 

K-Neighbors, Logistic, Decision Tree, SVM, Random Forest, Gaussian NB

The outcomes are quite similar for all the classifiers, and not quite satisfying

Accuracy around 90%

ROC Area between  0.76 -> 0.78

Stratified Folding confirms the average ROC Area value

Please, tell my "Why?"
=======================================================

ROC values are worse for SVC and Decision Tree (around 0.63 for both)

So, there are samples that are pretty hard to be classified

I selected and analyzed the samples that coulnd't be correctly classified even by the model that turned out to be the best (Logistic Regression)

They show much different patterns from the other samples, then it's quite hard to classify them correclty by using the available features

Then, "What should we do?"
=======================================================

Using the available features, the predicting model based on 10 inputs and the Logistic Regression Classifier is not much bad

It can be used to better focusing the bank campaigns, and to raise the chances of increasing the number of sold products with respect to the money invested into the same campaigns

More features should be added to get better outcomes

Features focused on the actual known profile of the client (total wealth, products bought in the past, risk aversion profile) should tell us more about the customer capabilities to stand a temporary lock on a portion of her/his wealth, that usually is the main customer fear about a term deposit


Conclusions
=======================================================

And now, to summarize... a little (very little) taste of D3!

http://localhost:8000/index.html

