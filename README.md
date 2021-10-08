# To flip or not to flip? 

**Overview**

This project focuses on home sales in King County Washington. We looked at information from the King County Assessor Website that shows House Sales Data. This data contains the selling prices of 21,597 homes and 21 unique features for each of those homes.  

**Business and Data Understanding**

When considering whether to flip a home or not we'll consider how to choose a home, what features of a home you need to consider when purchasing and selling a home that you've flipped, and what actions to take to increase the profitability of a flipped home. 

**Explain your stakeholder audience here**

Our Stakeholders are individuals looking for a home to purchase to flip or individuals who own a home that they've flipped. This project looks at how to choose a home, what features to consider, and what action to take with the predictions of the final model. 

**Modeling**

We chose to analyze home prices using linear regression models. These models allow us to evaluate and interpret the importance of each feature. 

Initial Exploration: 

- Square footage of a home has the highest correlation to price. 
- Homes with basements sell at a higher price on average. 

Baseline Model: 

The baseline model has one feature fed into the model, the square footage of the home, being that it has the highest correlation to price in the given dataset. 

Feature Engineering: 

- Created a new column for age of a home when sold. We did this by subtracting the year the home was built by the year the home was sold. 
- Created a categorical column for home condition that assigns a number, 0, 1, 2, 3, 4, to the condition, Poor, Fair, Average, Good, Very Good
- Created a new column representing the ratio of the size of a home compared to the neighbors that compares the sqft_living column to the sqft_living15 column. 
- Created a column for homes that have or don't have basements. Assigned 0 to homes without basements and 1 to homes with basements. 

Final Model: 

Our final model includes our original baseline feature sqft_living, age of the home when sold, condition ranking of the home, ratio of the size of the home compared to the nearest 15 neighbors, and homes with and without basements. 

**Regression Results**

- Log transform 
- Coefficients 
- R2
- MSE
- RMSE

The final model resulted in price predictions that were off by $150,000 on average. When holding all other features constant, an increase of 100 square feet results in a 5% increase in sale price, having a basement results in 7% increase in sale price, and improving the condition of a home from poor to good results in a 7% increase in sale price. 

**Conclusion**

To conclude, the final model is wrong, but useful. The results from the model are encouraging for further work on improving this model. A flaw of the data is that it's encompassing all of King County Washington. The area of Washington covered in this data is large and has many different types of neighborhoods that have many different features that may affect home prices. A home in the city center of Seattle might have near identical features to a home in a suburb of Seattle, but has drastically different sale prices. This may present an error when predicting sale price. 

Future Work: 

- Whether average income of the residents in a neighborhood. 
- How school systems may affect price if they're blue ribbon schools or if they're poorly rated schools. 
- Whether the safety rating of a neighborhood affects sale price. 

**Repository Navigation**
├── README.md                    <- The top-level README for reviewers of this project. 
├── data                         <- Sourced externally and generated from code. 
├── notebooks                    <- Folder containing Jen and Andrew Jupyter Notebooks housing individual work for this project. 
├── .gitignore                   <- Third Jupyter notebook. Linear regression models, evaluations, results.
├── HouseSales.ipynb             <- Final Jupyter notebook for this project, containing a combined, final model of the information form both Jen and Andrew Jupyter notebooks. 
├── presentation.pdf             <- PDF of the presentation slides for this project. 
└── utils.py                     <- .py folder containing three functions for evaluating linear regression models in Jupyter Notebooks throughout this repository. 
                     
