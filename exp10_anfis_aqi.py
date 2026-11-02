import itertools
import numpy as np
import matplotlib.pyplot as plt

X = np.array([
    [20, 40, 24, 35],
    [35, 65, 28, 45],
    [50, 90, 30, 55],
    [70, 120, 32, 60],
    [90, 150, 34, 65],
    [110, 180, 35, 70],
    [130, 210, 36, 72],
    [150, 240, 38, 75],
    [170, 270, 39, 78],
    [190, 300, 40, 80],
    [210, 330, 41, 82],
    [230, 360, 42, 84],
    [250, 390, 43, 86],
    [270, 420, 44, 88],
    [290, 450, 45, 90],
    [310, 480, 46, 92],
    [40, 80, 27, 50],
    [100, 160, 33, 68],
    [180, 290, 39, 76],
    [260, 410, 44, 89]
], dtype=float)

aqi = np.array([35, 55, 78, 105, 132, 160, 188, 215, 245, 275, 305, 335, 365, 395, 425, 455, 68, 145, 260, 385], dtype=float)

feature_min = np.array([0, 0, 0, 0], dtype=float)
feature_max = np.array([350, 500, 50, 100], dtype=float)
X = (X - feature_min) / (feature_max - feature_min)
target = aqi / 500.0

mf_centers = np.array([[0.25, 0.75] for _ in range(X.shape[1])], dtype=float)
mf_sigmas = np.full((X.shape[1], 2), 0.25, dtype=float)
rules = list(itertools.product([0, 1], repeat=X.shape[1]))
consequents = np.zeros((len(rules), X.shape[1] + 1), dtype=float)

def calculate_output(sample):
    memberships = np.zeros((X.shape[1], 2))
    for feature in range(X.shape[1]):
        for membership in range(2):
            center = mf_centers[feature, membership]
            sigma = max(mf_sigmas[feature, membership], 0.05)
            memberships[feature, membership] = np.exp(-((sample[feature] - center) ** 2) / (2 * sigma ** 2))

    firing = []
    for rule in rules:
        strength = 1.0
        for feature, membership in enumerate(rule):
            strength *= memberships[feature, membership]
        firing.append(strength)

    firing = np.array(firing)
    normalized = firing / (np.sum(firing) + 1e-12)
    augmented = np.append(1.0, sample)
    rule_outputs = consequents @ augmented
    output = np.sum(normalized * rule_outputs)
    return output, normalized, rule_outputs, memberships

learning_rate = 0.015
premise_rate = 0.00008
epochs = 2500
loss_history = []

for epoch in range(epochs):
    total_loss = 0.0
    for index in np.random.default_rng(epoch).permutation(len(X)):
        sample = X[index]
        expected = target[index]
        predicted, normalized, rule_outputs, memberships = calculate_output(sample)
        error = expected - predicted
        total_loss += error ** 2
        augmented = np.append(1.0, sample)
        consequents += learning_rate * error * normalized[:, None] * augmented[None, :]

        for rule_index, rule in enumerate(rules):
            contribution = normalized[rule_index] * (rule_outputs[rule_index] - predicted)
            for feature, membership in enumerate(rule):
                center = mf_centers[feature, membership]
                sigma = max(mf_sigmas[feature, membership], 0.05)
                difference = sample[feature] - center
                center_gradient = error * contribution * difference / (sigma ** 2)
                sigma_gradient = error * contribution * (difference ** 2) / (sigma ** 3)
                mf_centers[feature, membership] += premise_rate * center_gradient
                mf_sigmas[feature, membership] += premise_rate * sigma_gradient
                mf_sigmas[feature, membership] = np.clip(mf_sigmas[feature, membership], 0.05, 0.8)
                mf_centers[feature, membership] = np.clip(mf_centers[feature, membership], 0.0, 1.0)

    loss_history.append(total_loss / len(X))

predictions = []

for sample in X:
    output, _, _, _ = calculate_output(sample)
    predictions.append(np.clip(output, 0, 1) * 500)

predictions = np.array(predictions)
rmse = np.sqrt(np.mean((predictions - aqi) ** 2))

test_reading = np.array([160, 255, 38, 76], dtype=float)
normalized_test = (test_reading - feature_min) / (feature_max - feature_min)
test_output, _, _, _ = calculate_output(normalized_test)
predicted_aqi = np.clip(test_output, 0, 1) * 500

print("ANFIS AQI Prediction")
print("Inputs: PM2.5, PM10, Temperature, Humidity")
print("Number of inputs:", X.shape[1])
print("Number of Gaussian membership functions:", X.shape[1] * 2)
print("Number of Sugeno rules:", len(rules))
print("Training epochs:", epochs)
print("Training RMSE:", round(rmse, 2))
print("Test PM2.5:", test_reading[0], "µg/m³")
print("Test PM10:", test_reading[1], "µg/m³")
print("Test temperature:", test_reading[2], "°C")
print("Test humidity:", test_reading[3], "%")
print("Predicted AQI:", round(predicted_aqi, 2))

plt.figure(figsize=(8, 5))
plt.plot(loss_history)
plt.title("ANFIS Training Error")
plt.xlabel("Epoch")
plt.ylabel("Mean Squared Error")
plt.grid(True)
plt.show()

plt.figure(figsize=(8, 5))
plt.plot(aqi, label="Target AQI", marker="o")
plt.plot(predictions, label="ANFIS Predicted AQI", marker="x")
plt.title("ANFIS AQI Training Results")
plt.xlabel("Training Sample")
plt.ylabel("AQI")
plt.legend()
plt.grid(True)
plt.show()
