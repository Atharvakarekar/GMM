# import numpy as np
# from sklearn.mixture import GaussianMixture
#
# # Generate sample data
# np.random.seed(0)
# n_samples = 1000
# n_features = 2
# X = np.random.randn(n_samples, n_features)
#
# # Get user input for the number of components
# n_components = int(input("Enter the number of components for the GMM: "))
#
# # Create and fit a GMM
# gmm = GaussianMixture(n_components=n_components)
# gmm.fit(X)
#
# # Predict the cluster labels for the data points
# labels = gmm.predict(X)
#
# # Access the learned parameters of the GMM
# means = gmm.means_
# covariances = gmm.covariances_
# weights = gmm.weights_
#
# # Print the learned parameters
# print("Means:\n", means)
# print("Covariances:\n", covariances)
# print("Weights:\n", weights)

#with dataset

# import numpy as np
# from sklearn.mixture import GaussianMixture
#
# # Get user input for the number of components
# n_components = int(input("Enter the number of components for the GMM: "))
#
# # Load or generate your dataset here
# # Replace "your_dataset.csv" with the path to your own dataset file
# data = np.genfromtxt(r"C:\Users\Pratima\Downloads\GMM\CC GENERAL.csv", delimiter=",", skip_header=1, dtype=str)
#
# # Handle empty or missing values by replacing them with NaN
# data[data == ""] = np.nan
#
# # Extract the numeric data from the dataset
# X = data[:, 1:].astype(float)
#
# # Handle missing values in X by replacing them with the column mean
# column_means = np.nanmean(X, axis=0)
# nan_indices = np.isnan(X)
# X[nan_indices] = np.take(column_means, np.where(nan_indices)[1])
#
# # Create and fit a GMM
# gmm = GaussianMixture(n_components=n_components)
# gmm.fit(X)
#
# # Predict the cluster labels for the data points
# labels = gmm.predict(X)
#
# # Access the learned parameters of the GMM
# means = gmm.means_
# covariances = gmm.covariances_
# weights = gmm.weights_
#
# # Print the learned parameters
# print("Means:\n", means)
# print("Covariances:\n", covariances)
# print("Weights:\n", weights)

#with streamlit frontend


import numpy as np
from sklearn.mixture import GaussianMixture
import streamlit as st

# Streamlit front-end
st.title("Gaussian Mixture Models (GMM) with Streamlit")

# Get user input for the number of components
n_components = st.number_input("Enter the number of components for the GMM:", min_value=1, step=1, value=2)

# Load or generate your dataset here
# Replace "your_dataset.csv" with the path to your own dataset file
data = np.genfromtxt(r"C:\Users\Pratima\Downloads\GMM\CC GENERAL.csv", delimiter=",", skip_header=1, dtype=str)

# Handle empty or missing values by replacing them with NaN
data[data == ""] = np.nan

# Extract the numeric data from the dataset
X = data[:, 1:].astype(float)

# Handle missing values in X by replacing them with the column mean
column_means = np.nanmean(X, axis=0)
nan_indices = np.isnan(X)
X[nan_indices] = np.take(column_means, np.where(nan_indices)[1])

# Create and fit a GMM with user-defined number of components
gmm = GaussianMixture(n_components=n_components)
gmm.fit(X)

# Predict the cluster labels for the data points
labels = gmm.predict(X)

# Access the learned parameters of the GMM
means = gmm.means_
covariances = gmm.covariances_
weights = gmm.weights_

# Display the learned parameters using Streamlit
st.subheader("Learned Parameters")
st.write("Means:")
st.write(means)
st.write("Covariances:")
st.write(covariances)
st.write("Weights:")
st.write(weights)
