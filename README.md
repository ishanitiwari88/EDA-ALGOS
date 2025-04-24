# Exploratory Data Analysis Algorithms
## 1. Frequency counting and distribution analysis
Basic Frequency Counting Process:  
- Identify the variable you want to analyze
- Count occurrences of each unique value
- Organize these counts in a systematic way (table, visualization, etc.)  

**Types of Frequency Distributions**
- For categorical data:
  - Create frequency tables showing counts for each category
  - Calculate percentages/proportions for each category
- For numerical data:
  - Create bins (ranges of values)
  - Count observations falling into each bin
  - Present as histograms, frequency polygons, etc.

**Distribution Analysis**
After counting frequencies, you analyze the resulting distribution:
- Shape: Is it symmetric, skewed, uniform, bimodal?
- Central tendency: Where is data centered? (mean, median, mode)
- Spread: How dispersed is the data? (range, variance, standard deviation)
- Outliers: Are there extreme values?

## 2. Pattern Detection in Time Series
A time series is a sequence of data points indexed in chronological order.

### Components of a Time Series   
1. Trend: The long-term movement or direction in the data
2. Seasonality: Regular, predictable patterns that repeat at fixed intervals
3. Cyclical components: Irregular fluctuations without fixed frequencies
4. Random/Irregular variations: Unpredictable fluctuations that don't fit other patterns

### Basic Pattern Detection Techniques  
- Visual Inspection
  - Line plots to see overall patterns
  - Seasonal plots (grouping by season/period)
  - Lag plots to detect autocorrelation (A lag is just a shifted version of your time series data. essentially, it's the value of the variable from a previous time step.)  
- Moving Averages - This is used to smooth out your data, so it's easier to see the trend without being distracted by random spikes or dips.
  - Simple Moving Average (SMA) - (avg. of last n values)
    ```
    Values:     5   6   7   8   9
    3-day SMA:      (5+6+7)/3 = 6
                  (6+7+8)/3 = 7
                 (7+8+9)/3 = 8
    ```
  - Weighted Moving Average (WMA) - similar to SMA but gives more importance to recent values.
    ```
    #weights - 3, 2, 1
    Values:  5, 6, 7
    WMA = (7×3 + 6×2 + 5×1) / (3+2+1) = (21 + 12 + 5)/6 = 6.33
    ```
  - Exponential Moving Average (EMA) - Applies exponentially decreasing weights
- Decomposition Methods - These break your time series into three parts:
      1. Trend
      2. Seasonality: Repeating patterns (e.g., every Monday, every December)
      3. Residual: Random noise
  -  Additive Decomposition (Data = Trend + Seasonality + Residual) - Used when components add up
  -  Multiplicative decomposition (Data = Trend × Seasonality × Residual) -  Used when seasonal effects are percentage-based (e.g., sales double every Diwali)
-  Autocorrelation Analysis
  - Autocorrelation Function (ACF): Correlation between series and lags; helps detect repeating patterns or seasonality.
  - Partial Autocorrelation Function (PACF): Correlation after removing effects of smaller lags- Shows the pure correlation between the series and a certain lag, removing the influence of earlier lags.

### Advanced Pattern Detection Methods
1. **Fourier Analysis / Spectral Analysis**
   Fourier analysis breaks down your time series into different rhythmic patterns (like waves) of different speeds.
   > Suppose you're analyzing electricity usage in a building throughout the year. Fourier analysis could reveal:
   >  - A daily pattern (high during work hours, low at night)
   >  - A weekly pattern (lower on weekends)
   >  - A seasonal pattern (higher in summer due to AC, higher in winter due to heating)  
   > It would tell you exactly how strong each of these patterns is, helping you understand what drives electricity consumption.
   - Main Algorithms-
     - Fast Fourier Transform (FFT): quickly figures out which wave patterns are present
     - Periodogram: Shows strngth of each pattern is at different frequencies
     - Power Spectral Density: Measures how energy in signal is spread across different frequencies.

2. **Wavelet Analysis**
   Similar to Fourier analysis but can pinpoint when patterns start and stop within your data.
   > Imagine monitoring a patient's heartbeat data. Wavelet analysis could:
   >  - Detect a sudden irregular heartbeat that lasted just a few seconds
   >  - Show when the heart rhythm changed from normal to abnormal
   >  - Identify specific types of irregularities by their unique patterns
   > Regular analysis might miss these brief changes, but wavelets catch them because they track both the pattern and when it occurs.
   - Discrete Wavelet Transform (DWT): Breaks your signal into different components at different scales
   - Continuous Wavelet Transform (CWT): Gives a more detailed picture but requires more computing power
   - Multi-Resolution Analysis: Looks at your data at different levels of detail simultaneously

3. **Change Point Detection**
   finds moments when your data fundamentally changes its behavior.
   > A retail store tracking daily sales might use change point detection to:
   > - Identify when a marketing campaign started affecting sales
   > - Detect when a competitor opened nearby
   > - Spot when customer behavior patterns shifted
   > - Find out exactly when seasonal shopping patterns begin and end
   > This helps them understand exactly when and how their business environment changes.
Main Algos:
- CUSUM (Cumulative Sum): Adds up deviations from the average until they get big enough to signal a change
- PELT (Pruned Exact Linear Time): finds optimal places to split your data
- Binary Segmentation: Repeatedly splits data at the most obvious change points
- Bayesian Change Point Detection: Uses probability to determine where changes likely occurred

4. **Machine Learning Approaches**
   Main Algorithms:
   - **ARIMA**: Predicts future values based on past values and errors
   - **Prophet**: Facebook's tool that handles seasonal patterns and holidays really well
   - **LSTM Networks**: Special neural networks with a "memory" that can learn long-term patterns
   - **Isolation Forests**: Finds weird data points by seeing how easy they are to separate from normal points
> A weather forecasting system might use:
> - ARIMA to predict basic temperature trends
> - Prophet to account for seasonal patterns and special events
> - LSTMs to capture complex relationships between temperature, humidity, pressure, etc.
> - Isolation Forests to detect unusual weather events that don't fit typical patterns
> This combination helps them make accurate forecasts while identifying unusual weather phenomena.

WHICH METHOD TO USE AND WHEN-  
- _Fourier Analysis_ while finding regular, repeating patterns in stable data
- _Wavelet Analysis_ when the patterns change over time or you need to find when changes happen
- _Change Point Detection_ while identifying exactly when the data behavior fundamentally shifts
- _Machine Learning Approaches_ when you have complex patterns, want to make predictions, or need to find anomalies





   
   
