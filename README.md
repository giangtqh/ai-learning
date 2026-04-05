# AI Learning Roadmap

> Personal study plan for transitioning from Software/Telecom Engineer to AI Engineer.
>
> **Background:** Software Engineer | C++ & Python | BSc Telecommunications & Electronics | MSc Technical Electronics

---

## Table of Contents

- [Phase 1 — Math Foundations](#phase-1--math-foundations)
- [Phase 2 — Python for AI Ecosystem](#phase-2--python-for-ai-ecosystem)
- [Phase 3 — Classical Machine Learning](#phase-3--classical-machine-learning)
- [Phase 4 — Deep Learning](#phase-4--deep-learning)
- [Phase 5 — Specialization](#phase-5--specialization)
- [Phase 6 — Projects](#phase-6--projects)
- [Resources](#resources)
- [Progress Tracker](#progress-tracker)

---

## Phase 1 — Math Foundations
> Estimated: 2–4 weeks | Most already known from degree

| Topic | Why It Matters | Status |
|---|---|---|
| Linear Algebra | Matrices = data, transformations, neural nets | [ ] |
| Calculus / Gradients | Backpropagation, optimization | [ ] |
| Probability & Statistics | Bayesian inference, distributions | [ ] |
| Signal Processing | CNNs borrow from signal theory heavily | [x] Already known |

### Key Concepts
- Matrix multiplication, eigenvalues, SVD (used in PCA, embeddings)
- Partial derivatives, chain rule (used in backpropagation)
- Gaussian distributions, Bayes' theorem, likelihood (used everywhere)

### Resources
- [3Blue1Brown — Essence of Linear Algebra](https://www.youtube.com/playlist?list=PLZHQObOWTQDPD3MizzM2ZAgoEoFuK5like)
- [Khan Academy — Calculus](https://www.khanacademy.org/math/calculus-1)
- [Think Stats (free book)](https://greenteapress.com/wp/think-stats-2e/)

---

## Phase 2 — Python for AI Ecosystem
> Estimated: 1–2 weeks | You know Python, just learn the stack

```python
import numpy as np         # arrays, linear algebra
import pandas as pd        # data manipulation
import matplotlib.pyplot   # visualization
import seaborn as sns      # statistical plots
import sklearn             # classical ML
import torch               # deep learning (PyTorch)
```

### Checklist
- [ ] NumPy — vectorized math, broadcasting, matrix ops
- [ ] Pandas — DataFrames, data wrangling, groupby, merge
- [ ] Matplotlib / Seaborn — plotting loss curves, distributions
- [ ] Scikit-learn — pipelines, preprocessing, model evaluation
- [ ] PyTorch basics — tensors, autograd, GPU usage

### Resources
- [NumPy Quickstart](https://numpy.org/doc/stable/user/quickstart.html)
- [Pandas Getting Started](https://pandas.pydata.org/docs/getting_started/index.html)
- [PyTorch Official Tutorial](https://pytorch.org/tutorials/)

---

## Phase 3 — Classical Machine Learning
> Estimated: 3–5 weeks

Learn the algorithm + math behind each, then implement it.

### Supervised Learning
- [ ] **Linear Regression** — least squares, gradient descent, MSE loss
- [ ] **Logistic Regression** — sigmoid function, cross-entropy loss, binary classification
- [ ] **Decision Trees** — information gain, entropy, Gini impurity
- [ ] **Random Forest** — ensemble, bagging, feature importance
- [ ] **SVM (Support Vector Machine)** — margin maximization, kernels

### Unsupervised Learning
- [ ] **K-Means Clustering** — centroids, inertia
- [ ] **PCA (Principal Component Analysis)** — dimensionality reduction, eigendecomposition

### Model Evaluation
- [ ] Train/Validation/Test split
- [ ] Cross-validation (k-fold)
- [ ] Metrics: Accuracy, Precision, Recall, F1, ROC-AUC, RMSE
- [ ] Overfitting / Underfitting / Regularization (L1, L2)

### Practice
- Kaggle: [Titanic — Getting Started](https://www.kaggle.com/c/titanic)
- Kaggle: [House Prices Prediction](https://www.kaggle.com/c/house-prices-advanced-regression-techniques)

---

## Phase 4 — Deep Learning
> Estimated: 4–8 weeks

> **Your telecom background is a huge advantage here:**
> - FFT → Convolution → CNNs use the same math
> - Digital filters → Neural network layers
> - Noise / SNR → Regularization / Dropout

### Progression

#### 4.1 Neural Network Basics
- [ ] Perceptron — weighted sum + activation
- [ ] Multi-Layer Perceptron (MLP) — hidden layers, forward pass
- [ ] Activation functions — ReLU, Sigmoid, Tanh, Softmax
- [ ] Loss functions — MSE, Cross-entropy
- [ ] Backpropagation — chain rule, gradient flow

#### 4.2 Training Mechanics
- [ ] Stochastic Gradient Descent (SGD)
- [ ] Optimizers — Adam, RMSProp, AdaGrad
- [ ] Learning rate scheduling
- [ ] Batch normalization
- [ ] Dropout (regularization)

#### 4.3 Convolutional Neural Networks (CNN)
- [ ] Convolution operation (you know this from DSP!)
- [ ] Pooling layers
- [ ] Classic architectures: LeNet, VGG, ResNet
- [ ] Image classification, object detection

#### 4.4 Recurrent Neural Networks (RNN / LSTM)
- [ ] Sequences and time series
- [ ] Vanishing gradient problem
- [ ] LSTM and GRU gates
- [ ] Applications: speech, signal, time-series (very telecom-relevant!)

#### 4.5 Transformers & Attention
- [ ] Self-attention mechanism
- [ ] Multi-head attention
- [ ] Positional encoding
- [ ] BERT (encoder), GPT (decoder), T5 (encoder-decoder)
- [ ] Fine-tuning pre-trained models

### Resources
- [fast.ai — Practical Deep Learning (free)](https://course.fast.ai)
- [CS231n — CNNs for Visual Recognition (Stanford)](https://cs231n.stanford.edu/)
- [Andrej Karpathy's Neural Nets from Scratch (YouTube)](https://www.youtube.com/@AndrejKarpathy)
- [The Illustrated Transformer (blog)](https://jalammar.github.io/illustrated-transformer/)

---

## Phase 5 — Specialization
> Choose based on your interests and career goals

| Path | Relevance to Background | Key Topics |
|---|---|---|
| **Signal Intelligence / RF AI** | Directly applies telecom + AI | Modulation classification, spectrum sensing |
| **Computer Vision** | CNN = signal processing on 2D images | Detection, segmentation, tracking |
| **NLP / LLMs** | Transformers, language models | Fine-tuning, RAG, prompt engineering |
| **Reinforcement Learning** | Control systems → RL (similar concepts) | Q-learning, PPO, environments |
| **Edge AI / Embedded ML** | C++ skill + AI on embedded systems | TensorFlow Lite, ONNX, TensorRT |

### Recommended for your profile: **Signal Intelligence + Edge AI**
- Classify RF modulation types (AM, FM, QAM, PSK) with CNNs/LSTMs
- Deploy models to embedded/FPGA hardware using C++ and ONNX
- Combines all your existing expertise

---

## Phase 6 — Projects

Build these incrementally — each one reinforces the previous phases.

### Beginner
- [ ] **Iris Classifier** — scikit-learn, basic classification pipeline
- [ ] **House Price Predictor** — regression, feature engineering

### Intermediate
- [ ] **Image Classifier (CIFAR-10)** — CNN with PyTorch
- [ ] **Text Sentiment Analyzer** — NLP, fine-tune BERT
- [ ] **Time Series Forecaster** — LSTM on sensor/signal data

### Advanced (Leverage Your Background)
- [ ] **RF Modulation Classifier** — classify AM/FM/QAM/PSK signals using CNN/LSTM
  - Dataset: [RadioML](https://www.deepsig.ai/datasets)
- [ ] **LLM Fine-tuning** — fine-tune GPT-2 or LLaMA on domain-specific data
- [ ] **Edge AI Deployment** — export PyTorch model → ONNX → run in C++

---

## Resources

### Free Courses
| Course | Provider | Focus |
|---|---|---|
| [Practical Deep Learning](https://course.fast.ai) | fast.ai | Best practical start |
| [CS231n](https://cs231n.stanford.edu/) | Stanford | Computer Vision |
| [CS224n](https://web.stanford.edu/class/cs224n/) | Stanford | NLP |
| [Deep Learning Specialization](https://www.deeplearning.ai/courses/deep-learning-specialization/) | DeepLearning.AI | Comprehensive |

### Books
| Book | Level | Free? |
|---|---|---|
| Hands-On ML with Scikit-Learn & TensorFlow — Aurélien Géron | Beginner–Mid | No |
| Deep Learning — Goodfellow, Bengio, Courville | Advanced | [Yes (online)](https://www.deeplearningbook.org/) |
| Neural Networks and Deep Learning — Nielsen | Beginner | [Yes (online)](http://neuralnetworksanddeeplearning.com/) |

### Practice Platforms
- [Kaggle](https://www.kaggle.com) — datasets, competitions, free GPUs
- [Papers With Code](https://paperswithcode.com) — research papers + implementations
- [Hugging Face](https://huggingface.co) — pre-trained models, datasets

---

## Progress Tracker

### Weekly Schedule (Suggested)
```
Week  1-2:   NumPy + Math review (Linear Algebra, Calculus)
Week  3-5:   Scikit-learn + Classical ML (Kaggle Titanic/House Prices)
Week  6-9:   PyTorch + Deep Learning (fast.ai course)
Week 10-12:  CNN / RNN deep dives + projects
Week 13-16:  Transformers + NLP or Signal AI specialization
Week 17+:    Advanced project + Paper reading + Research
```

### Milestone Log

| Date | Milestone | Notes |
|---|---|---|
| 2026-04-05 | Started AI learning journey | Background: Telecom/Electronics Engineer |
| | | |

---

*Started: April 5, 2026*
