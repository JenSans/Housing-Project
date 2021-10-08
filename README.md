# To flip or not to flip? 

**Overview**

This project focuses on home sales in King County Washington. We looked at information from the King County Assessor Website that shows House Sales Data. This data contains the selling prices of 21,597 homes and 21 unique features for each of those homes.  

**Business and Data Understanding**

When considering whether to flip a home or not we'll consider how to choose a home, what features of a home to consider when purchasing and selling a home that's been flipped, and what actions to take to increase the profitability of a flipped home. 

**Stakeholder Audience**

Our Stakeholders are individuals looking for a home to purchase to flip or individuals who own a home they'd like to flip. This project looks at how to choose a home, what features to consider, and what action to take with the predictions of the final model. 

**Modeling**

We chose to analyze home prices using linear regression models. These models allow us to evaluate and interpret the importance of each feature. 

Initial Exploration: 

- Square footage of a home has the highest correlation to price. 
- Homes with basements sell at a higher price on average. 
- Square footage of homes is heavily right skewed showing most homes under 4,000 square feet, so we exclude homes above this amount of square footage. We transform our price column using a natural logaritm to create a more normally distributed target. 

Baseline Model: 

The baseline model has one feature fed into the model, the square footage of the home, being that it has the highest correlation to price in the given dataset. 

Feature Engineering: 

- Created a new column for age of a home when sold. We did this by subtracting the year the home was built by the year the home was sold. 
- Created a categorical column for home condition that assigns a number, 0, 1, 2, 3, 4, to the condition, Poor, Fair, Average, Good, Very Good, respectively. 
- Created a new column representing the ratio of the size of a home compared to the neighbors that compares the sqft_living column to the sqft_living15 column. 
- Created a column for homes that have or don't have basements. Assigned 0 to homes without basements and 1 to homes with basements. 

Final Model: 

Our final model includes our original baseline feature, square footage of the home, age of the home when it sold, condition ranking of the home, ratio of the size of the home compared to the nearest 15 neighbors, and homes with and without basements. 

**Regression Results**

Training Metrics: 
- R2: 0.463
- MAE: $138,864.70
- RMSE: $199,044.46

Testing Metrics: 
- R2: 0.450
- MAE: $138,978.64
- RMSE: $197,395.59

Coefficients (MinMax Scaled): 

- sqft_living:           1.886725
- ratio_sqft_living:     0.683970
- home_age_when_sold:    0.344939
- condition_rank:        0.089316
- has_basement:          0.076994

All P-Values came out to 0 in the final model, telling us that association between price and the chosen features (sqft_living, ratio_sqft_living, home_age_when_sold, condition_rank, has_basement) is statistically significant.


According to our model, holding all other features constant, an additional 12x12 ft room (average size of an addition to a home) results in a 7.77% increase in the price.

A one unit increase in ratio_sqft_living means going from 0.5 to 1.5 for example, or half the size of your neighbors to 1.5 times the size of your neighbors. According to our model, this change results in a 31.43% decrease in price, holding all other features constant. So, homes appear to be priced higher when they are smaller rather than larger than their neighbors, all else equal.

Having a basement vs not having one results in an 8% increase in sale price.

A one unit change in condition_rank means going up one level from one rating to the next (e.g. poor to fair, or average to good). A limitation of our model is the assumption that these intervals are equivalent when they may not be. According to our model, jumping up one rating results in a 2.26% increase in price, holding other features constant.

The final model resulted in price predictions that were off by $139,000 on average. When holding all other features constant, an increase of 100 square feet results in a 5% increase in sale price, having a basement results in an 8% increase in sale price, and improving the condition of a home from poor to good results in a 7% increase in sale price. 

Recommendations: 

- Compare the cost of a 100 sqft addition to a home to a 5% increase in home price to see if this is profitable for the flip. 
- When comparing similar homes and their potential for flipping, if one has a basement and the other does not, consider purchasing and flipping the home that has the basement. 
- Consider purchasing a home in poor condition and upgrading its condition to good. 

**Conclusion**

The final model is wrong, but useful. The results from the model are encouraging for further work on improving this model. A flaw of the data is that it's encompassing all of King County Washington. The area of Washington covered in this data is large and has many different types of neighborhoods that have many different features that may affect home prices. A home in the city center of Seattle might have near identical features to a home in a suburb of Seattle, but has drastically different sale prices. This may present an issue when predicting sale price. 

Future Work: 

- Research how average income of the residents in a neighborhood affects price.  
- How school systems may affect price if they're blue ribbon schools or if they're poorly rated schools. 
- Whether the safety rating of a neighborhood affects sale price. 

**Presentation Link:** 

[Presentation Link](https://github.com/JenSans/Housing-Project/blob/main/presentation.pdf)

**Repository Navigation**

```
├── README.md                    <- The top-level README for reviewers of this project. 
├── data                         <- Sourced externally and generated from code. 
├── notebooks                    <- Folder containing Jen and Andrew Jupyter Notebooks housing individual work for this project. 
├── .gitignore                   <- Plain text file where each line contains a pattern for files/directories to ignore.
├── HouseSales.ipynb             <- Final Jupyter notebook for this project, containing a combined, final model of the information form both Jen and Andrew Jupyter notebooks. 
├── presentation.pdf             <- PDF of the presentation slides for this project. 
└── utils.py                     <- .py folder containing three functions for evaluating linear regression models in Jupyter Notebooks throughout this repository. 
```
