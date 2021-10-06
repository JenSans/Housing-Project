# imports
from sklearn.metrics import r2_score, mean_absolute_error, mean_squared_error
import matplotlib.pyplot as plt
import statsmodels.api as sm

# functions
def evaluate(trn_y, trn_preds, tst_y, tst_preds):
    """
    Calculate the coefficient of determination (R^2), MAE, and MSE.
    Plot the residuals vs predictions and a QQ plot.
    
    Inputs:
        trn_y: array-like
            The target observations for training set.
        trn_preds: array-like
            The target predictions for training set.
        tst_y: array-like
            The target observations for test set.
        tst_preds: array-like
            The target predictions for test set.
        
    Outputs:
        None    
    """
    
    # calculate residuals
    trn_residuals = trn_y - trn_preds
    tst_residuals = tst_y - tst_preds
    
    #display metrics
    print("Training Metrics:")
    # R2
    print(f"R2: {r2_score(trn_y, trn_preds):.3f}")
    # MAE
    print(f"Mean Absolute Error: ${mean_absolute_error(trn_y, trn_preds):,.3f}")
    # RMSE
    print(f"Root Mean Squared Error: ${mean_squared_error(trn_y, trn_preds, squared=False):,.3f}")
    
    print('----')
    
    print("Testing Metrics:")
    # R2
    print(f"R2: {r2_score(tst_y, tst_preds):.3f}")
    # MAE
    print(f"Mean Absolute Error: ${mean_absolute_error(tst_y, tst_preds):,.3f}")
    # RMSE
    print(f"Root Mean Squared Error: ${mean_squared_error(tst_y, tst_preds, squared=False):,.3f}")
    
    # create fig, axes
    fig1, (ax1, ax2, ax3) = plt.subplots(3, figsize=(8,16))
    
    # create residual plot
    ax1.scatter(trn_preds, trn_residuals, label='Train', alpha=0.5)
    ax1.scatter(tst_preds, tst_residuals, label='Test', alpha=0.5)
    ax1.axhline(y=0, color = 'red', label = '0')
    
    ax1.set_xlabel("Predictions ($ millions)")
    ax1.set_ylabel("Residuals ($ millions)")
    ax1.set_title("Residuals vs Predictions")
    ax1.legend()
    
    # create qq plots
    sm.qqplot(trn_residuals, line = 'r', ax=ax2)
    ax2.set_title('Training Residuals', y=1.0, pad=-14)
    
    sm.qqplot(tst_residuals, line = 'r', ax=ax3)
    ax3.set_title('Testing Residuals', y=1.0, pad=-14)

def model_predict(trn_data, features, target, tst_data):
    """
    Fit a linear regression model to the data given features and a target.
    
    Inputs:
        data: pandas DataFrame
            The DataFrame storing the training data.
        features: list of strings
            The list of feature names.
        target: string
            The name of the target.
            
    Outputs:
        trn_preds: pandas Series
            Training predictions for target.
        tst_preds: pandas Series
            Testing predicitons for target.
    """
    
    # fit the linear regression model
    model = sm.OLS(endog=trn_data[target], exog=sm.add_constant(trn_data[features])).fit()
    
    # show the summary
    display(model.summary())
    
    # calculate train and test predictions
    trn_preds = model.predict(sm.add_constant(trn_data[features]))
    tst_preds = model.predict(sm.add_constant(tst_data[features]))
    
    return trn_preds, tst_preds