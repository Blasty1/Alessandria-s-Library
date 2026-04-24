>[!SUMMARY] Table of Contents
- [[Guide to Explainable AI#Introduction|Introduction]]
- [[Guide to Explainable AI#Interpretability of Traditional ML models|Interpretability of Traditional ML models]]
    - [[Guide to Explainable AI#Decision Trees|Decision Trees]]
    - [[Guide to Explainable AI#Linear Regression|Linear Regression]]
    - [[Guide to Explainable AI#Logistic Regression|Logistic Regression]]
    - [[Guide to Explainable AI#SVM|SVM]]
    - [[Guide to Explainable AI#Bayesian Models|Bayesian Models]]
- [[Guide to Explainable AI#Interpretability of Deep Learning Models|Interpretability of Deep Learning Models]]
- [[Guide to Explainable AI#XAI Techniques|XAI Techniques]]
- [[Guide to Explainable AI#Feature Attribution Methods ( Local Explanations )|Feature Attribution Methods ( Local Explanations )]]
    - [[Guide to Explainable AI#LIME (Local Interpretable Model-Agnostic Explanations)|LIME (Local Interpretable Model-Agnostic Explanations)]]
    - [[Guide to Explainable AI#SHAP ( Shapley Adaptive Explanations )|SHAP ( Shapley Adaptive Explanations )]]
    - [[Guide to Explainable AI#Integrated Gradients|Integrated Gradients]]
    - [[Guide to Explainable AI#Saliency Maps|Saliency Maps]]
    - [[Guide to Explainable AI#SmoothGrad|SmoothGrad]]
- [[Guide to Explainable AI#Visualisation  Techniques|Visualisation  Techniques]]
    - [[Guide to Explainable AI#Partial Dependence Plot: PDPs|Partial Dependence Plot: PDPs]]
    - [[Guide to Explainable AI#Individual Conditional Expectation : ICE Plots|Individual Conditional Expectation : ICE Plots]]
    - [[Guide to Explainable AI#Accumulated Local Effected: ALE Plots|Accumulated Local Effected: ALE Plots]]
- [[Guide to Explainable AI#Temporal and Sequence Data Techniques|Temporal and Sequence Data Techniques]]
    - [[Guide to Explainable AI#TimeSHAP|TimeSHAP]]
    - [[Guide to Explainable AI#Dynamic Time Warping : DTW Explainer|Dynamic Time Warping : DTW Explainer]]
- [[Guide to Explainable AI#Casual Inference Techniques|Casual Inference Techniques]]
- [[Guide to Explainable AI#Counterfactual Explanations|Counterfactual Explanations]]
    - [[Guide to Explainable AI#Nearest Neighbor Counterfactuals|Nearest Neighbor Counterfactuals]]
    - [[Guide to Explainable AI#Optimization-based Counterfactuals|Optimization-based Counterfactuals]]
    - [[Guide to Explainable AI#Prototype-based Counterfactuals|Prototype-based Counterfactuals]]
    - [[Guide to Explainable AI#Diverse Counterfactual Generation|Diverse Counterfactual Generation]]
    - [[Guide to Explainable AI#Actionable Recourse Methods|Actionable Recourse Methods]]
    - [[Guide to Explainable AI#Counterfactuals in Reinforcement Learning|Counterfactuals in Reinforcement Learning]]
- [[Guide to Explainable AI#Useful Papers About XAI|Useful Papers About XAI]]
    - [[Guide to Explainable AI#Interpretable Modeling of Deep Reinforcement Learning Driven Scheduling|Interpretable Modeling of Deep Reinforcement Learning Driven Scheduling]]
        - [[Guide to Explainable AI#Design|Design]]
        - [[Guide to Explainable AI#My Conclusion|My Conclusion]]
# Introduction
Deep Reinforcement Learning (DRL) has achieved remarkable success in complex decision-making tasks such as robotics, autonomous driving, game playing, finance, and resource management. By combining reinforcement learning’s trial-and-error optimization with the powerful representation learning capabilities of deep neural networks, DRL systems can discover highly effective strategies directly from raw data. **However**, despite their strong performance, these systems often function as “black boxes,” making it difficult for humans to understand why particular decisions or policies are produced.

**Explainable AI (XAI)** consists of techniques that help determine how models make decisions.

Explainability in DRL has therefore become increasingly important. First, many real-world applications—such as healthcare, transportation, and industrial control—require transparency for safety and regulatory compliance. Decision makers must be able to verify that the learned policies behave reasonably under diverse conditions and do not exploit unintended shortcuts or unsafe strategies. Second, explainability supports trust and adoption: users are more willing to rely on AI systems when they can interpret the reasoning behind their actions. Third, interpretable insights help developers debug models, detect biases, and improve training procedures by revealing how agents perceive environments and what factors influence their actions.

Terms that wilal be used:
- Interpretability $\rightarrow$ degree to which a human can understand the cause of a decision
	- A decision tree used for medical diagnosis can provide clear, step- by-step reasoning for its predictions, making it interpretable even for non-experts
- Transparency$\rightarrow$ openness and accessibility of the model’s structure and data,
	- Imagine a simple linear regression model predicting house prices based on features like area, location, and age of the property. The model’s coefficients can be easily inspected and interpreted, making it transparent
- Fairness$\rightarrow$ the assurance that AI systems do not produce biased results or discrimination based on sensitive attributes such as race, gender, or age
- Explainability$\rightarrow$ the extent to which the internal mechanics of a machine learning model can be understood

A common trade-off in AI is between interpretability and model complexity. Models like decision trees and linear regression are interpretable by nature but often lack the flexibility to capture complex patterns in the data . On the other hand, deep learning models and LLMs have extraordinary predictive power but are notoriously difficult to interpret.
The trade-off is illustrated in the diagram below:
![[Screenshot 2026-02-10 alle 15.35.44.png]]
![[Screenshot 2026-02-10 alle 15.46.20.png]]
The challenge is to find a balance, or use hybrid approaches that retain interpretability without sacrificing predictive power.

The setup of explainable AI techniques consists of three main methods:
1. Prediction Accuracy → measures how frequently the model’s outputs match real-world outcomes.
    1. For example, in a reinforcement learning system controlling traffic lights, accuracy would correspond to how well the learned policy actually reduces congestion compared to observed traffic outcomes.
2. Traceability → following the data and decision-making process the way back to our source
    1. The ability to follow the reasoning path that led to a particular decision.
    2. In deep reinforcement learning, traceability may involve tracking which environmental observations (e.g., sensor readings, state variables) most strongly affected the agent’s chosen action, or examining how the policy evolved during training.
3. Decision understanding → providing clear and understandable explanations about our findings in a way that humans can easily interpret.
    1. While traceability shows _how_ a decision was formed internally, decision understanding translates this information into human-readable insights, such as rules, visualizations, or natural-language explanations

Prediction accuracy ensures reliability, traceability ensures transparency of the decision process, and decision understanding ensures human interpretability

XAI is also about ensuring ethical AI development, are the decisions that the model is making fair and unbiased? Are they going to align with the values of our organization ? Are our researches and people involved in the process collaborating properly and addressing ethical challenges?

Explainability in deep reinforcement learning is usually analyzed at two complementary levels:

- local explanations → clarify why the agent selected a particular action in a specific state
    - Keys aspects are: Feature contribution analysis, Gradient-based importance and Counterfactual explanations.
- global explanations → describe how the agent behaves overall, not just in one state.
    - Key aspects are: Policy summarization, Rule extraction and Behavioral visualization.

Understanding both is important because reinforcement learning policies operate over sequential decisions rather than single predictions.

# Interpretability of Traditional ML models
While these models offer varying degrees of interpretability, their simplicity also limits their ability to capture complex, non-linear relationships in data. This trade-off underscores the core challenge in machine learning: balancing interpretability with predictive power.

## Decision Trees
They are regarded as one of the most interpretable models in machine learning.
They possess a simple, intuitive flowchart-like structure where internal nodes represent decision rules based on feature values, branches denote the outcomes of these decisions, and leaf nodes hold the final predictions. The path from the root to a leaf node provides a clear and understandable decision- making process, which is crucial for explainable AI applications.

A decision tree splits data into subsets based on the values of input features in order to separate the data in a way that reduces uncertainty or *impurity*.
Most common criteria for splitting nodes include:
	- Gini Impurity $\rightarrow$ If you have a dataset where all examples belong to the same class, the Gini impurity is zero (pure). If you have a perfectly balanced mix of different classes, the Gini impurity is higher (impure). Decision trees use this to find splits that reduce impurity—moving from mixed groups toward pure ones.
		- The idea is to get pure subset ( all data with that feature value  )
$$
G = 1 - \sum_{i=1}^n p_i^2
$$
Where $p_i$ is the proportion of instances of class $i$ in the node
	- Information Gain  $\rightarrow$  based on entropy, it aims to reduce the entropy after a split.
$$
\text{Information Gain} = \text{Entropy}(\text{parent}) - (\sum \text{Weighted Entropy}(\text{children}))
$$
Where the entropy quantifies the disorder/impurity in a subset.

We can also apply some pruning techniques to avoid that it become too complex.
Feature importance in decision trees is determined by assessing the role each feature plays in reducing the impurity of a node during the splitting process. Impurity is a measure of the disorder or randomness within the node, typically evaluated using metrics like Gini Impurity or Entropy. When a feature significantly reduces impurity, it receives a higher importance score.
![[Screenshot 2026-02-10 alle 16.16.25.png]]

## Linear Regression
Linear models, including Linear Regression and Logistic Regression, are some of the most inter- pretable machine learning models. They assume a linear relationship between the input features and the output, making it straightforward to understand the effect of each feature on the prediction
Linear Regression is a model that predicts a continuous output $y$ as a weighted sum of input features $x_i$:
$$
y = \beta_0 + \beta_1 x_1 + \beta_2 x_2 + . . . + \beta_n x_n
$$
Where:
- $\beta_0$ is the intercept/bias ( expected value of y when all features are 0 )
- $\beta_i$ is the coefficient of feature $x_i$ indicating the expected change in y for a one-unit increase in $x_i$ assuming all other features are held constant
	- A positive coefficient indicates that an increase in the feature leads to an increase in the predicted value, while a negative coefficient suggests the opposite.

While linear regression is simple and interpetable , it has several limitations:
- Assumption of Linearity
- Sensitive to Outliers
- Multicollinearity $\rightarrow$ when features are highly correlated, it becomes difficult to determine the individual effect of each feature on the 

## Logistic Regression

While Linear Regression predicts continuous outputs, **Logistic Regression** is used for classification problems where the output is discrete (e.g., binary: Yes/No, True/False, Class A/Class B). Despite its name, Logistic Regression is fundamentally different from Linear Regression as it models the probability of a discrete outcome ( used for classification ).
Logistic Regression starts with a linear model but applies a **sigmoid function** to constrain the output to the range [0, 1], representing a probability:
$$
\hat{y} = \sigma(\beta_0 + \beta_1 x_1 + \beta_2 x_2 + ... + \beta_n x_n)
$$
Where the sigmoid function is defined as:
$$
\sigma(z) = \frac{1}{1 + e^{-z}}
$$
This can be rewritten as:
$$
\hat{y} = \frac{1}{1 + e^{-(\beta_0 + \beta_1 x_1 + \beta_2 x_2 + ... + \beta_n x_n)}}
$$
Where:
- $\beta_0$ is the intercept/bias (affects the baseline probability)
- $\beta_i$ is the coefficient of feature $x_i$ indicating how much a one-unit increase in $x_i$ changes the log-odds of the positive class
  - A positive coefficient increases the probability of the positive class, while a negative coefficient decreases it
- $\sigma(z)$ ensures the output is always between 0 and 1, interpretable as a probability

Key Differences from Linear Regression:

| Aspect | Linear Regression | Logistic Regression |
|--------|-------------------|---------------------|
| **Output** | Continuous values (any real number) | Probability (0 to 1) |
| **Function** | Linear function | Sigmoid function applied to linear function |
| **Use Case** | Regression (predicting quantities) | Classification (predicting categories) |
| **Interpretation** | Direct coefficient effect on output | Coefficient effect on log-odds |
| **Decision Boundary** | N/A | Threshold (typically 0.5) |

Limitations of Logistic Regression:
- Assumption of Linear Separability: Assumes the classes can be separated by a linear boundary; performs poorly on non-linearly separable data
- Sensitive to Multicollinearity
- Class Imbalance: Can perform poorly when classes are highly imbalanced in the training data

## SVM
SVMs aim to find a hyperplane that best separates the data into different classes. The optimal hyperplane maximizes the margin, which is the distance between the hyperplane and the nearest data points from each class. These nearest points are known as support vectors, and they are fundamental to the SVM’s decision-making process.
The decision boundary / hyperplane formula is:
$$
w\cdot x + b= 0
$$
where:
- $w$ is the weight vector ( it determines its orientation )
- $b$ is the bias term ( it determines its shifting )
- $x$ represent the feature vector

The support vectors is composed by points that lies exactly on the boundary of the margin:
$$
w \cdot x_i +b = \pm 1
$$
![[Screenshot 2026-02-10 alle 17.18.02.png]]
The SVM algorithm aims to maximize this margin, which improves the model’s generalization ability. A larger margin indicates a more robust classifier, less sensitive to small variations in the data.

While SVMs provide some level of interpretability through their decision boundaries and support vectors, this is mainly applicable when using a linear kernel. For more complex datasets requiring non-linear decision boundaries, the interpretability diminishes as the kernel function introduces non-linear transformations. In such cases, post-hoc interpretability techniques, such as LIME or SHAP (discussed in later chapters), may be necessary to understand the model’s predictions

## Bayesian Models
Bayesian models provide a probabilistic framework for machine learning, allowing us to incorporate prior knowledge and quantify uncertainty in model predictions
The core idea of Bayesian inference is to update our beliefs (prior knowledge) with observed data, resulting in a new, refined belief (posterior distribution). This approach not only improves prediction accuracy but also offers insights into the confidence of the predictions, enhancing model explainability.
It relies on Bayes' Theorem:
$$
P(\theta | X) = \frac{P(X | \theta) P(\theta)}{P(X)}
$$
Where:
- $P(\theta|X)$ is the posterior distribution ( given the data, which are our model parameters )
- $P(X|\theta)$ is the likelihood ( represents the probability of the data given the model parameters )
- $P(X)$ is the marginal likelihood and it acts as a normalizing constant
- $P(\theta)$ is the prior distribution ( represents our belief about the model parameters before seeing anything ).
The posterior distributions provide a comprehensive picture of the uncertainty surrounding each parameter estimate. Instead of single-point estimates, Bayesian models offer a probabilistic view, making it easier to un- derstand the confidence we have in the learned parameters

# Interpretability of Deep Learning Models
Deep learning models, especially those based on deep neural networks, are known for their powerful predictive capabilities. However, they are often regarded as ’black boxes..
The challenge of interpretability arises due to:
- High complexity of the model $\rightarrow$ deep learning models, such as Convolutional Neural Networks (CNNs) and Recurrent Neural Net- works (RNNs), involve multiple layers of neurons, non-linear activation functions, and vast numbers of parameters. 
	- As the depth and complexity of the network increase, understanding the contribution of each individual parameter becomes infeasible.
- Non-linearity and Feature Abstraction  $\rightarrow$ the non-linear activation functions, such as ReLU and sigmoid, enable the model to learn complex patterns.
	- These non-linearities make it difficult to interpret what each layer is learning.
	- The representations in deep layers are often not directly interpretable by humans
- Lack of Explicit Structure $\rightarrow$ unlike simpler models (e.g., decision trees), deep neural networks do not have an inherent hierarchical structure that is easily understandable

//i should add interpretability for CNN, RNN and Transformers ( not in my interests right now ).

# XAI Techniques
XAI techniques can be categorized based on the interpretability of the model into:
- White-box models → models that are inherently interpretable and provide straightforward explanations for their predictions.
	-  i.e. decision trees, rule-based systems , linear/logistic regression, Naive Bayes Classifiers, KNN.
- Black-box models → models that are more complex and require additional methods for interpretation.
	- Neural Networks
	- SVMs
	- Ensemble Methods ( Random Forests )
	- Transformer Models
	- Graph Neural Networks ( GNNs )

XAI methods can be also classified into:

| Technique                         | Main Objective |
|----------------------------------|----------------|
| Model-based Techniques            | To create intrinsically interpretable models from the start (e.g., shallow Decision Trees or Linear Regression), where the model structure itself is transparent. |
| Post-hoc Interpretation           | To explain a model after training by approximating how input features influenced predictions (e.g., LIME, SHAP). |
| Counterfactual Explanations       | To identify the smallest change in input features required to alter a model’s prediction, showing actionable “what-if” scenarios. |
| Feature Attribution Methods       | To quantify the contribution or importance of each input feature to a specific prediction or to the model overall. |
| Visualization Techniques          | To present model behavior or learned representations visually (e.g., saliency maps, partial dependence plots) to improve human understanding. |
| Temporal and Sequence Data Techniques | To explain predictions in time-series or sequential models by identifying influential time steps, events, or temporal patterns. |
| Causal Inference                  | To determine cause-and-effect relationships between variables rather than simple correlations, identifying features that truly drive outcomes. |
| Graph-based Explanation           | To explain predictions on relational or graph data by identifying influential nodes, edges, or subgraphs affecting the model’s decision. |
| Multimodal Explainability         | To generate consistent explanations across multiple data modalities (e.g., text, images, audio) showing how each modality contributes to the prediction. |



# Feature Attribution Methods ( Local Explanations )

This method helps identify which input features contribute most to the predictions, enhancing the interpretability and transparency of the model

The method of feature importance analysis is versatile and applicable to various types of models:
- Tree-based models: feature importance is inherently determined by the tree structure. Nodes closer to the root indicate higher importance
- Linear Models ( Logistic / Linear Regression ): feature importance can be di- rectly interpreted based on the magnitude and sign of the coefficients
- Neural Networks:  approximations of feature importance can be derived using techniques like Integrated Gradients , SHAP values, or Layer-wise Relevance Propagation (LRP)
	- Feature importance can be approxi-mated using gradient-based methods like Integrated Gradients or Layer-wise Relevance Propagation (LRP). These methods analyze how the gradient of the output with respect to the input features changes, providing a measure of feature relevance.

## LIME (Local Interpretable Model-Agnostic Explanations)
It is a technique designed to explain the pre- dictions of any machine learning model by approximating it locally with a simpler, interpretable model.
Unlike global interpretability methods that aim to explain the entire model, LIME focuses on explaining individual predictions, making it a popular choice for understanding complex models
Mathematically, LIME minimizes the following objective function:
$$
\xi(x) = \text{arg min}_{g \in G} \mathcal{L}(f, g, \pi_x) + \Omega(g)
$$
Where:
- x is the feature
- G is a family of interpretable models
- f is the original complex model
- g is the chosen simple interpretable model
- $\pi_x$ is the proximity data point that we are looking at
	- It is the locality measure, assigning weights to perturbed samples based on their proximity to the instance x.
- $\Omega(g)$ is the regularization term ensuring the simplicity of the interpretable model

![[Screenshot 2026-02-12 alle 11.35.29.png]]

Disadvantages:
- Instability: The explanations can vary significantly with different perturbations, making the results less reliable ( LIME's explanations are highly dependent on the perturbed samples ).
- Scalability Issues: For large datasets or complex models, LIME can be computationally ex- pensive due to the need for numerous model evaluations on perturbed samples.
## SHAP ( Shapley Adaptive Explanations )

It assigns an importance value to each feature using concepts from cooperative game theory, specifically Shapley values. The method evaluates how much each feature contributes to the model’s prediction by comparing the prediction made with and without that feature across many possible subsets of input features. For each subset, the feature under evaluation is added to the subset and the change in the model’s prediction is measured. This marginal contribution is computed over many different feature combinations, and the average of these contributions determines the SHAP value of the feature. Because evaluating all possible subsets is computationally expensive, practical implementations approximate this process by sampling subsets and estimating the expected prediction when some features are treated as unknown using a background dataset. As a result, SHAP provides a consistent measure of feature importance that reflects how strongly each feature influences the model’s output for a particular prediction.

SHAP is versatile and can be applied to traditional machine learning models, complex deep learning architectures ( using gradient-based explanations ), and even large language models (LLMs).

This technique is based on the concept of Shapley values:
$$
\phi_i = \sum_{S \in N \backslash \{i\}} \frac{|S|!(|N| - |S| - 1)! }{|N|!} \left( f(S \cup  \{i\}) - f(S)\right)
$$
where:
- $N$ is the set of all features
- $S$ is a subset of features not containing $i$
- $f(S)$ is the model prediction using only the features in $S$

This formula represents the weighted average of the marginal contributions of feature i across all subsets of features. It ensures that the contributions are fairly distributed based on their impact on the prediction.

The SHAP summary plot is a comprehensive visualization that provides a global interpretation of the model. Each dot in the plot represents a single SHAP value for a particular feature in one instance of the test set. The x-axis indicates the SHAP value, which reflects the impact of the feature on the model’s output. Positive SHAP values suggest a contribution towards predicting the positive class (e.g., malignant tumor), while negative SHAP values contribute towards predicting the negative class (e.g., benign tumor).
![[Screenshot 2026-02-11 alle 14.36.15.png]]
Features are listed vertically, ranked by importance from top to bottom. "Mean concave points" is the most important feature, "mean fractal dimension" is the least important.
The color gradient from blue to red indicates the feature value, where red signifies high feature values and blue signifies low feature values. In this example, features such as mean concave points, worst area, and worst concave points are identified as having the highest impact on the model’s predictions. This suggests that the model places significant emphasis on the geometrical properties of the tumors when making a prediction.
This reveals the relationship: when the feature value is HIGH (red), the SHAP value tends to be positive (right side). When the feature value is LOW (blue), the SHAP value tends to be negative (left side).


Advantages:
- Shap can be applied to any model ( from linear models to DNN and LLMs )
- SHAP values provived both local explanations and global feature importance 

Disadvantages:
- High computational cost ( it is very expensive to evaluate all possible subsets of features )
- Limited in High-dimensional Contexts
- SHAP explanations may be less reliable for models that are sensitive to small changes in the input data or have high variance.

## Integrated Gradients
It is an attribution method that explains which input features (or states in RL) contributed most to your model's prediction or decision.
The key idea behind Integrated Gradients is to compute the accumulated gradients of the model’s output with respect to the input features as the input transitions from a baseline (e.g., a zero vector or an all-blank input) to the actual input.

Gradients are a way to measure importance: if I change feature i slightly, how much does the output change?" A large gradient = feature i has big influence. A small gradient = feature i doesn't matter much.
We don't use direct gradients ( gradient of the output w.r.t. input ) because they fail in nonlinear neural networks because of saturation and vanishing gradients.
Mathematically, the attribution for feature $x_i$ is given by:
$$
IG_i(x) = (x_i - x_i') \int_{\alpha=0}^1 \frac{\partial f(x'+ \alpha(x-x'))}{\partial x_i}d\alpha
$$
Where:
- x is the actual input
- $x'$ is the baseline input ( e.g. a zero vector )
	- The baseline is a reference input that represents "no information" or a neutral starting point.
- $\alpha$ is the interpolation parameter 
	- It goes from 0 to 1
	- It tells me where i am between the baseline ( $\alpha = 0$ ) and the actual input ( $\alpha=1$ )
	- The integral (sum of gradients along the path) tells us: "adding up all the sensitivity measurements from baseline to input, which features consistently contributed?"
		- "if I watched the decision-making process unfold step-by-step as inputs increased from baseline to actual, which features kept pushing the output forward?"
- $f(x)$ is the model's output for input $x$
- $\frac{\partial f}{\partial x_i}$ is the gradient of the model's output w.r.t the feature $x_i$
![[Screenshot 2026-02-12 alle 12.13.17.png]]
Limitations:
- Choice of Baseline: The results are sensitive to the choice of baseline input. An inappropriate baseline may yield misleading attributions.
- Computational Cost: IG requires multiple model evaluations for different interpolated inputs, making it computationally expensive for large models or high-dimensional data

## Saliency Maps
It is an intuitive post-hoc interpretation technique for neural networks.

The main idea is to use the gradient of the model’s output with respect to the input features to identify which parts of the input are most influential in the model’s prediction. Saliency maps provide a visual representation of these important regions, making them useful for tasks in computer vision and natural language processing (NLP).
They are most effective for CNN, RNN and Transformer Models.

The core idea of saliency maps is to use the gradient of the model’s output with respect to the input features to identify important regions.
$$
S(x) = \left| \frac{\partial f_c(x)}{\partial x}\right|
$$
Where:
- $S(x)$ is the saliency map for class $c$
- $x$ is the input
- $f(x)$ is our model
- $f_c(x)$ is the output of the model for class $c$
The gradient indicates how sensitive the output $f_c(x)$ is to changes in each input feature $x_i$: Features with higher gradient magnitudes are deemed more important for the prediction.
![[Screenshot 2026-02-12 alle 12.32.11.png]]
It highlights the most important pixels in the input image that contributed to the model's prediction.
It is a direct gradient so the limitations are:
- Gradient saturation: If the model’s output is saturated, the gradient values may be close to zero, making the saliency map less informative
- Saliency maps can be noisy and may highlight irrelevant features, espe- cially in high-dimensional inputs.

## SmoothGrad
SmoothGrad is a post-hoc interpretation technique designed to enhance the clarity of gradient-based saliency maps, which often suffer from noise and visual artifacts.
It works by averaging gradients over multiple noisy inputs in order to produce smoother and more visually interpretable saliency maps.
Given an input $x$ , it creates $n$ noisy samples by adding Gaussian noise ( $N(0,\sigma^2$ ) and computes the gradient of the model's output w.r.t. each noisy sample:
$$
\text{SmoothGrad}(x_i) = \frac{1}{n} \sum_{k=1}^n \frac{\partial f(x_k)}{\partial x_i}
$$
$$
x_k = x+N(0,\sigma^2)
$$
By averaging gradients over these noisy samples, SmoothGrad reduces the influence of noise in the input, making the saliency maps more interpretable
![[Screenshot 2026-02-12 alle 12.38.03.png]]
Limitations:
- Results are sensitive to the noise level $\sigma$ 
- Computing SmoothGrad requires multiple forward and backward passes, making it computationally expensive for large models or datasets.

# Visualisation  Techniques
XAI tools that help to interpret complex machine learning models by providing clear , visual insights into how features impact predictions.
Methods:
- PDPs
- ICE Plots
- ALE Plots
- Permutation Feature Importance
- Surrogate Models
- Anchors

## Partial Dependence Plot: PDPs
It is a visualization technique used in explainable AI to **show how a specific feature (or set of features) affects the model’s predictions**, while averaging out the influence of all other features. It helps to understand the _global effect_ of one feature on the output.
The partial dependence function $\hat{f}_S$ for a set of feature $S$ is defined as:
$$
\hat{f}_S = E_C[\hat{f}(x_S,x_C)]
$$
It is the expectaction of the model's prediction over the marginal distribution of the remaining features C ( C contains all the features not in S).

Algorithm:
- Select the feature(s) of interest (e.g., `x₁` = agent’s distance to obstacle).
- For each possible value of this feature, compute the model’s prediction while keeping other features at their observed values (or averaging over them).
- Plot the predicted output against the feature’s values.

The plot of $\hat{f}_S(x_s)$ against $x_S$ provides a visual representation of the feature’s effect on the model’s prediction.
![[Screenshot 2026-02-12 alle 12.57.44.png]]
In this case $x_S$ is the Median Income on California Housing Dataset and the y-axis shows the predicted house prices: this relationship aligns with economic intuition, as regions with higher median incomes generally have higher house prices due to greater purchasing power and demand.
Limitations:
- PDP works best for features that are not strongly correlated, because correlations can distort the interpretation.
- PDPs are primarily designed for continuous features and may not be as effective for categorical features with many levels.

## Individual Conditional Expectation : ICE Plots
It is a visualization technique used in post-hoc interpretation to analyze the effect of a single feature on the model’s predictions across individual data points.
It provides a more granular view than PDPs by displaying the effect for each individual observation.
ICE is more granular and actionable (you see individual patterns), while PDP shows the overall trend.
For a given data point $i$ and feature $x_j$ , ICE function is:
$$
ICE_i(x_j) = \hat{f}(x_j,x_{\backslash j}^{(i)})
$$
where:
- $\hat{f}$ is the predictive model
- $x_j$ is the feature of interest
- $x_{\backslash j}^{(i)}$ are all other features for the i-th observation, held costant.

The plot of $ICE_i(x_j)$ for each data point $i$ against $x_j$ visualizes how the prediction changes as $x_j$ varies , highlighting individual-level effects.

Limitations:
- It has the same problems of PDPs and in large data sets the plot may become cluttered, making it difficult to interpret individual lines

## Accumulated Local Effected: ALE Plots
Unlike ICE Plots and PDPs it accounts for feature dependencies and provide a more accurate representation of feature effects by avoiding the independence assumption ( it is suitable for Random Forests, Gradient Boosting, SVMs and NNs ).
The main idea of ALE Plots is to measure the local effect of a feature on the model’s prediction by calculating differences between predictions when the feature value is varied locally. Unlike PDPs, which average effects across the entire dataset, ALE Plots aggregate these local differences within predefined intervals of the feature.
$$
ALE(x_j) = \frac{1}{n} \sum_{i=1}^n \left(\hat{f}(x_j^{(i)} , x_{\backslash j} - \hat{f}(x_j^{(i-1)} , x_{\backslash j} ) \right)
$$
$x_j^{(i)}$ is the value of the feature in the i-th interval.
This approach divides the feature space into intervals and accumulates the changes in the model’s prediction across these intervals, thus accounting for the dependencies between features.

Why does it solve the problem of correlation? We are trying several type of values of each feature but not any of them is a reasonable/acceptable value in the real world: we create dinstinct and reasonable intervals where feature values can end. The interval doesn't magically know about dependencies. It selects realistic subsets of data where features naturally co-occur together, avoiding artificial combinations that break correlations: when you only modify feature X within a small interval and keep other features unchanged, you're preserving the joint probability distribution of your data.

# Temporal and Sequence Data Techniques
Temporal and sequence data present unique challenges for interpretability due to their inherent time-based dependencies and complex patterns.
## TimeSHAP
It is used for sequential and temporal data models such asRNN, LSTM and Transformer models.
It extends the SHAP framework to provide explanations for individual predictions in a temporal context, making it particularly relevant for time-series models.

The key point is that importance of features can change over time into a sequential model: TimeSHAP addresses it by decomposing Shapley values over the temporal sequence, evaluating the significance of each timestamp.
It answers the question *Which past events or time periods were most important for this prediction?*

Considering a time-series instance $x=[x_1, x_2 ,. . . ,x_T]$ where $x_t$ represents the feature vector at time $t$, the Shapley value $\phi_t$ for timestamp $t$ is formally expressed as:
$$
\phi_t = \frac{1}{|S|} \sum_{S \in \{1...T\}\backslash\{t\}} \left[f(x_{S \cup \{t\}}) - f(x_S) \right]
$$
where $S$ is a subset of timestamps, and $f()$ is the model prediction function.
The basic idea is: for each time step, you measure how much the model's prediction changes when that time step is included versus excluded. This tells you how important that time period was.
![[Screenshot 2026-02-13 alle 16.25.14.png]]
The algorithm of TimeSHAP includes the following key steps:
- Sequence Partitioning $\rightarrow$ time-series data is partitioned into meaningful segments to preserve temporal data
- Perturbation $\rightarrow$ perturbations are generated by altering parts of the sequence in order to simulate different scenarios
	- To calculate true Shapley values, you need to measure the contribution of each time step by seeing how the prediction changes when that time step is included vs. excluded. But to be mathematically exact, you'd need to evaluate the model on all possible subsets of time steps.
	- Perturbation solves it by Randomly sampling a representative subset of combinations.
- Shapley Value Computation $\rightarrow$ shapley values  are computed for each timestamp using the perturbed samples
- Visualization $\rightarrow$ show the importance of each timestamp
![[Screenshot 2026-02-13 alle 16.40.52.png]]
In the provided example, we trained a simple LSTM model on synthetic bi- nary time-series data. Using TimeSHAP, we explained the contribution of each timestamp in a specific instance. The resulting SHAP values indicate the importance of each timestamp.

Advantages:
- TimeSHAP captures the dynamic importance of features over time
- Provides explanations tailored to individual predictions, enhancing interpretability for time-series data.

Disadvantages:
- Calculating Shapley values for each timestamp can be resource- intensive, especially for long sequences.
- The quality of the explanation may depend on the perturbation strategy, requiring careful selection of sampling methods.
- TimeSHAP may struggle with very large datasets or real-time applications due to the need for extensive sampling.

## Dynamic Time Warping : DTW Explainer
It is used primarily for time-series models .
It focuses on aligning time-series sequences to measure similarity and explain model predictions by identifying the most important subsequences that influence the output.

It is a classic algorithm for measuring the similarity between two time-series sequences ( even if they differ in length or speed ).
It tries to find an optimal alignment between the sequences that minimizes the cumulative distance: given two sequences $X = [x_1, x_2, . . . ,x_m]$ and $Y=[y_1 , y_2 , . . . , y_n]$ , DTW aims to warp (stretching or compressing the time axis to match sequences together ) these sequences non-linearly in time to align similar points.
$$
DTW(X,Y) = \min_{\text{alignment}} \sum_{i=1}^k d(x_{a_i}, y_{b_i})
$$
**Alignment means**: establishing which points in sequence X should be matched with which points in sequence Y, even though they may be in different positions.
How DTW works?
- Create a Cost Matrix $\rightarrow$  Compare every point in sequence A with every point in sequence B, calculating distances between all pairs.
- Find the Optimal Warping Path $\rightarrow$  Use dynamic programming to find the path through the cost matrix that minimizes total distance while allowing sequences to "stretch" or "compress" to match each other.
- Calculate DTW Distance $\rightarrow$  The value along the optimal path is the DTW distance—lower values mean more similar sequences.

How DTW Explainer works?
- Align the input time series with a reference time series using DTW algorithm
- Compute the alignment costs and identify which parts of the input sequence have the highest influence based on the cumulative distance
- Highlight the influential subsequences.
![[Screenshot 2026-02-13 alle 17.09.17.png]]
In this example, we generated a synthetic time series and a slightly shifted reference series. The DTW algorithm finds the optimal alignment between the two sequences, even though they have different lengths and phases. The plot visualizes the warping path, showing which points in the time series are aligned with the reference series.

# Casual Inference Techniques
Causal inference techniques are essential in explainable AI (XAI) for uncovering true cause-and-effect relationships rather than mere correlations: Causal inference finds true causal relationships.
![[Screenshot 2026-02-13 alle 17.17.50.png]]

# Counterfactual Explanations
They are powerful techniques focusing on what-if scenarios to provide insights into model predictions.
By identifying minimal changes to input features that would alter the model’s output, counterfactual explanations help users understand the decision boundary of the model and suggest actionable changes.

A **counterfactual** $x'$ is an example that shows _what would need to change_ for a different outcome to happen ( a slightly modified characteristics)

## Nearest Neighbor Counterfactuals
A set of techniques that aim for identifying the closest examples in the data set that belong to a different class/prediction: the idea is to find a similar, yet different instance that demonstrates what small changes in the input could lead to a different outcome.
Formally we want to search for the nearest neighbor $x'$ of a given input $x$ such that the prediction of the model $f(x')$ is different from $y=f(x)$. 
$$
x' = \arg \min_{x' \in D, f(x') \neq y} \text{distance}(x,x')
$$
where:
- D is the dataset
- $\text{distance}(x,x')$ is the distance metric  that measures the similarity between $x$ and $x'$

The method aims to find the closest instance x′ that belongs to a different class, providing a
concrete example of how the input could be altered to change the prediction.
By examining the differences between the original instance and its counterfactual, we can better understand the sensitivity of the classifier’s decision boundary.

## Optimization-based Counterfactuals
It aims to generate alternative examples by direclty optimizing the input features to achieve a desired change in model's prediction. 
The main idea of optimization-based counterfactuals is to solve an optimization problem that balances two objectives:
1. Minimize the distance between the input $x$ and the counterfactual $x'$ to ensure changes are small and interpretable
2. Change the model prediction to a target class $y'$ different from the original prediction $y$
Formulation of the optimization problem:
$$
x' = \arg \min_{x'} \text{distance}(x,x') + \lambda \cdot \text{loss}(f(x'),y')
$$
where:
- $\lambda · \text{loss}(f(x'), y')$ ensure the model actually predicts the target class $y'$ when given $x'$
- $\lambda$ is a regularization parameter that controls the tradeoff between similarity and changing the prediction
	- Higher  $\lambda$ prioritizes achieving the target prediction (even if changes are large)
	- Lower  $\lambda$ prioritizes small, minimal changes (even if prediction doesn't change as much)
You want to change the input **as little as possible** while achieving a **specific change in prediction** — not necessarily a maximum change.
![[Screenshot 2026-02-16 alle 10.11.15.png]]

Example:
![[Screenshot 2026-02-16 alle 10.14.06.png]]
The original image, a clear "7", was slightly perturbed through the optimization process to produce the counterfactual image. This counterfactual image, although noisy, was successfully classified as an "8" by the neural network. This demonstrates how small, targeted changes to input features can significantly impact model predictions. The counterfactual generation process emphasizes the sensitivity of machine learning models to adversarial-like perturbations and provides insights into the model’s decision-making process.

## Prototype-based Counterfactuals
They leverage representative examples ( prototypes ) from the dataset: instead of generatic new data points from scratch, this technique identifies existing examples that are most similar to the input but belong to a different class.
$$
x' = \arg \min_{p \in D , f(p) \neq y} \text{distance}(x,p)
$$
where:
- $f(p)$ is the model's prediction for prototype p

In other words it works as Nearest Neighbor Counterfactuals but it does not rely directly on points by using a set of prototypes ( computed through K-NN method ) which is more computational-convenient.

## Diverse Counterfactual Generation
It is an advanced technique designed to produce multiple, distinct  counterfactual examples for a given input. The goal is not only to show one possible alternative that changes the model’s prediction but also to explore a variety of different paths the input could take to achieve the desired outcome.
The core idea of diverse counterfactual generation is to solve an opti- mization problem that not only aims to change the prediction but also maximizes the diversity of the generated counterfactuals
$$
x' = \arg \min_{x' \in D , f(x') \neq y} \text{distance}(x,x') + \lambda_1 \text{loss}(f(x'),y') - \lambda_2 \text{diversity}(x', \{x_1' , . . . , x'_{i-1}\})
$$
where:
- $\text{diversity}(x', \{x_1' , . . . , x'_{i-1}\})$ is a term that maximizes the differnce between the current counterfactual and previously generated ones
- $\lambda_1$ and $\lambda_2$ are regularization parameters controlling the trade-off between prediction change, similarity, and diversity.

Example:
![[Screenshot 2026-02-16 alle 10.44.40.png]]
We generated three distinct counterfactuals for an MNIST image. Each counterfactual is visually similar to the original image but has been modified to be classified as a different target class. The diversity term in the optimization process ensures that each counterfactual is different from the others, providing varied explanations of how the input could be altered to change the classifier’s decision. This approach helps in understanding the model’s decision boundary and offers a richer set of explanations.

## Actionable Recourse Methods
They provide counterfactual explanations that are not only theoretical but also actionable and realistic for users ( in other words they can suggest changes that individuals can feasibly make to alter the outcome ).
We want to generate a counterfactual example $x'$ for a given input $x$ such that:
- The prediction for $x'$ is different from the prediction for $x$
- The changes from $x$ to $x'$ are feasible and actionable for the use
We want to resolve the following optimization problem:
$$
x' = \arg \min_{x' \in D , f(x') \neq y} \text{distance}(x,x') + \lambda \cdot \text{action\_cost}(x',x)
$$
Subject to $f(x') = y'$
Where:
- $y'$ is the desired target prediction
- $\text{action\_cost}(x',x)$ measures the difficulty or feasibility of making changes from $x$ to $x'$
	- It is crucial because it ensures that the proposed changes are realistic (e.g. changing a user's age should be impossible while adjusting spending habits could be feasible )
	- A common definition of the action cost can be:
	$$
	\text{action\_cost}(x',x) = \sum_i w_i \cdot |x_i - x_i'|
	$$
	Where $w_i$ is the weight/difficulty associated with changing feature $i$

## Counterfactuals in Reinforcement Learning
Counterfactual explanations in reinforcement learning (RL) provide insights into the decision-making process of an agent by exploring alternative actions or states that could have led to different outcomes.
Counterfactual explanations in RL need to consider the temporal dependencies and the impact of sequential actions on future states and rewards.
In RL, the agent interacts with the environment $E$ by taking actions $a_t$ at time step $t$ based on the observed state $s_t$. The goal of counterfatuals explanations is to explore that woulde have happened if the agent had chosen a different action $a'_t$ instead of the actual action $a_t$.
The counterfactual state $s'_{t+1}$ resulting from taking action $a'_t$ can be defined using the environment's transition dynamics:
$$
s'_{t+1} = T(s_t,a'_t)
$$
where $T$ is the transition function of the environment.
The counterfactual return $G'$ is then computed as:
$$
G' = r_t + \gamma \sum_{k=1}^\infty \gamma^{k-1} r'_{t+k}
$$
where:
- $r_t$ is the immediate reward at time $t$
- $\gamma$ is the discount factor
- $r'_{t+k}$ is the reward obtained at future time steps assuming the counterfactual actions $a'_t$ was taken.
The difference between the actual return G and the counterfactual return G′ provides insights into the potential impact of alternative actions.

Example:
![[Screenshot 2026-02-16 alle 11.25.41.png]]
In this example, we compared the Q-values for the agent’s actual action with the Q-values of an alternative action. The counterfactual analysis shows the expected future reward if the agent had chosen a different action instead. Here, the Q-value for the actual action (0) is higher than that for the alternative action (1), suggesting that the agent’s decision was optimal given the expected rewards. This type of analysis helps in understanding the agent’s reasoning and provides insights into whether the agent’s choices align with maximizing long-term rewards.

It can be used for:
- Improving Interpretability $\rightarrow$ counterfactuals help to explain the agent’s behavior by showing the potential outcomes of alternative actions.
- Improving the policy $\rightarrow$ by analyzing suboptimal actions, counterfactuals can provide insights for refining the policy or adjusting the reward function.
This technique can be applied to various RL algorithms, including DQN, policy gradients, and actor-critic methods.

Limitations:
- Dependency on Environment Model   $\rightarrow$ for accurate counterfactuals, the transition dynamics of the environment need to be known or approximated, which may not always be feasible.
- High Computational Cost  $\rightarrow$ generating counterfactuals requires querying the model for alter- native actions, which can be computationally expensive, especially in high-dimensional state spaces.
- Challenges with Temporal Dependencies $\rightarrow$ the sequential nature of RL makes it challenging to isolate the impact of a single action, as future states and rewards are influenced by earlier decisions.

# Useful Papers About XAI

## Interpretable Modeling of Deep Reinforcement Learning Driven Scheduling
Link:https://arxiv.org/pdf/2403.16293
Date: 24 Mar 2024

This paper is about a framework called IRL ( Interpretable Reinforcement Learning ) to address the issue of intepretability of DRL scheduling. The core idea is to interpret DNN (i.e. DRL policy ) as a decision tree by utilizing imitation learning, IRL incorporates the Dataset Aggregation algorithm and introduces the notion of critical state to prune the derived decision tree.
It can be used to explicit how our agent is choosing between actions and contribute to the setting of rewards.

### Design
![[Pasted image 20260217150830.png]]
The design of IRL is based on imitation learning, where the DNN policy of the DRL agent acts as the teacher and generates input-output samples to construct the student decision tree.
There are two issues in the above process: 
1. the derived decision tree might not resemble the original deep neural network very well
2. the size of the decision tree could be huge.
To overcome these obstacles, they employ two techniques. They integrate the DAgger algorithm to address the former issue, and then introduce the critical state concept for the latter one.
In this study, they utilize DQN as a practical example: the DRL scheduling agent aims to  optimize scheduling performance by making decisions on when and which jobs in the waiting queue should be allocated to available computer resources; at each scheduling instance, the agent encodes both job and system information into a vector, which is fed as an input to the neural network. Based on the neural network’s output, the agent selects jobs from the wait queue and then receives a reward signal from the scheduling environment.
In DQN , the deep neural network is utilized to approximate Q-value:
- The input of DQN is a 1-D vector containing job size , job length and system utilization
- The output of DQN is a single neuron corresponding to the expected Q-value of the job.
- It is used a $\epsilon-$greedy policy in order to avoid to get stuck and allow exploration over exploitation sometimes.
During the testing or inference time, the agent selects the job with the highest Q-value.

In this work, they use a decision tree fro regression in order to interpret the DQN policy.
DQN scheduling agent replays the workload trace to produce a trajectory of ( state, Q-value) pairs and this trajectory will be used as the training dataset D of the decision tree.
- The input of the decision tree is the state 
- The output of the decision tree is the imitated output ( Q-value ) of DQN
Challenges and solutions:
- They observed  that the decision tree trained once may not resemble the DQN policy well: the decision tree agent may choose a different job from the DQN agent since the imitated Q-value by the decision tree is unlikely to precisely match the Q-value output by DQN. They introduced the DAgger algorithm to address this issue: instead of training the decision tree one time, we train it multiple times; after each training iteration, the newly generated decision tree is used to replay the workload trace and demonstrate its policy to the DQN agent. As a result, a new trajectory of (state, Q-value) pairs following the newly generated decision tree policy is produced, denoted as $D_i$. This new trajectory may contain unseen states in the training dataset $D$. As a teacher, the DQN agent assigns the Q-values to the states in this new trajectory, and aggregate this newly produced trajectory $D'_i$ into the training dataset D.
  The updated dataset $D$ is used to train the decision tree in the next iteration. This process repeats multiple times until the maximum iteration is reached. In this work, the maximum iteration is set to 5
- The generated decision tree with DAgger is normally huge , IRL introduces the concept of *critical state* with the goal of generating a reduced-sized decision tree.
	- In the design of IRL, we define critical state as the system state when the number of jobs in the waiting queue is greater than a threshold, and non-critical state as the state when the number of jobs in the waiting queue is less than or equal to the threshold.
	- Only samples with critical states ($D_{\text{critical}}$) in the dataset $D$ are used to generate the decision tree. 
Algorithm 1 shows the complete pseudo code of the IRL method.
![[Screenshot 2026-02-17 alle 15.28.49.png]]

Examples of what we would obtain by using IRL to test two types of reward function
![[Screenshot 2026-02-17 alle 15.29.40.png]]

### My Conclusion
The IRL framework is relevant to this thesis project because both address complex **sequential resource allocation problems** where interpretability of learned policies is critical for operational acceptance.

The IRL approach directly supports my secondary research question ( **RQ T.2 Explainability** ) by offering a concrete method to interpret DRL-based locomotive allocation decisions:
- **Policy Distillation**: Like the HPC scheduling problem, DRL policies for locomotive assignment are "black boxes." Converting the DNN policy into a decision tree (via imitation learning) would enable operators to understand _why_specific locomotives are selected for trips—e.g., which factors (remaining rest hours, maintenance status, location distance) the agent prioritized.
- **Critical State Identification**: IRL's "critical state" concept maps naturally to your domain. You could define critical states as periods when few locomotives are available (e.g., ≤4 free locomotives), helping identify when the policy makes high-stakes decisions.
- **Reward Function Validation**: The paper demonstrates using IRL to test reward functions. This is valuable for your project: you can verify whether your reward signal actually encourages the behaviors you want (e.g., proactive maintenance scheduling vs. reactive allocation).
