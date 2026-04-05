# AI Learning Roadmap

> Personal study plan for learning AI from scratch.
>
> **Background:** Software Engineer | C++ & Python

---

## Table of Contents

- [Phase 1 — Math Foundations](#phase-1--math-foundations)
- [Phase 2 — Python for AI Ecosystem](#phase-2--python-for-ai-ecosystem)
- [Phase 3 — Classical Machine Learning](#phase-3--classical-machine-learning)
- [Phase 4 — Deep Learning](#phase-4--deep-learning)
- [Phase 5 — Specialization](#phase-5--specialization)
- [Phase 6 — Projects](#phase-6--projects)
- [Daily Notebook Index](#daily-notebook-index)
- [Resources](#resources)
- [Progress Tracker](#progress-tracker)

---

## Phase 1 — Math Foundations
> **Estimated:** 2–3 weeks (Days 1–10)
> **Goal:** Understand the math that powers neural networks — not memorize formulas, but *see why they work*

### 1.1 Linear Algebra (Days 1–3)

| Day | Topic | Key Concepts | Notebook |
|-----|-------|-------------|---------|
| 1 | Vectors & Matrices | Vectors as data, `W @ x + b` = one layer, dot product, cosine similarity | `day-01-linear-algebra.ipynb` |
| 2 | Eigenvalues, SVD, PCA | Eigenvectors as important directions, SVD decomposition, low-rank approximation, PCA from scratch | `day-02-eigenvalues-svd-pca.ipynb` |
| 3 | Matrix ops in NumPy | Broadcasting, batch operations, `einsum`, shapes in practice | `day-03-numpy-matrix-ops.ipynb` |

**What you'll understand after this:**
- Why a neural network layer is just `W @ x + b`
- How PCA compresses data by keeping only important directions
- Why LoRA can fine-tune a 7B model with 1000× less compute

### 1.2 Calculus & Gradients (Days 4–6)

| Day | Topic | Key Concepts | Notebook |
|-----|-------|-------------|---------|
| 4 | Derivatives & Partial Derivatives | Slope, rate of change, partial derivatives, gradient vector | `day-04-derivatives.ipynb` |
| 5 | Chain Rule & Backpropagation | Chain rule step by step, manual backprop through 2-layer net | `day-05-chain-rule-backprop.ipynb` |
| 6 | Gradient Descent | Loss landscape, learning rate, SGD, momentum — implement from scratch | `day-06-gradient-descent.ipynb` |

**What you'll understand after this:**
- Exactly how a neural network learns — weight update = `w -= lr * gradient`
- Why deep networks can have vanishing/exploding gradients
- Why Adam optimizer converges faster than plain SGD

### 1.3 Probability & Statistics (Days 7–10)

| Day | Topic | Key Concepts | Notebook |
|-----|-------|-------------|---------|
| 7 | Probability Basics | Random variables, distributions, mean, variance, standard deviation | `day-07-probability-basics.ipynb` |
| 8 | Gaussian & Common Distributions | Normal distribution, softmax as probability, sampling | `day-08-distributions.ipynb` |
| 9 | Bayes' Theorem & MLE | Bayes' theorem, maximum likelihood estimation, cross-entropy derived from MLE | `day-09-bayes-mle.ipynb` |
| 10 | Phase 1 Capstone | Implement linear regression with gradient descent using only NumPy | `day-10-capstone-linear-regression.ipynb` |

**What you'll understand after this:**
- Why cross-entropy loss is used for classification (it comes from MLE)
- What dropout is really doing (Bernoulli sampling)
- How Bayesian reasoning connects to probabilistic AI models

---

## Phase 2 — Python for AI Ecosystem
> **Estimated:** 1–2 weeks (Days 11–17)
> **Goal:** Get fluent with the tools every AI engineer uses daily

| Day | Topic | Key Concepts | Notebook |
|-----|-------|-------------|---------|
| 11 | NumPy Deep Dive | Vectorized ops, broadcasting rules, `reshape`, `transpose`, `einsum` | `day-11-numpy-deepdive.ipynb` |
| 12 | Pandas for Data | DataFrames, load CSV, groupby, merge, handle missing data | `day-12-pandas.ipynb` |
| 13 | Matplotlib & Seaborn | Plot loss curves, histograms, scatter plots, confusion matrices | `day-13-visualization.ipynb` |
| 14 | Scikit-learn Pipelines | Preprocessing, train/test split, cross-validation, evaluation metrics | `day-14-sklearn-pipelines.ipynb` |
| 15 | PyTorch Tensors | Tensors vs NumPy arrays, autograd, GPU basics | `day-15-pytorch-tensors.ipynb` |
| 16 | PyTorch nn.Module | Build layers, `forward()`, loss functions, optimizer step | `day-16-pytorch-nn.ipynb` |
| 17 | PyTorch Training Loop | DataLoader, training loop, validation loop, save/load model | `day-17-pytorch-training-loop.ipynb` |

---

## Phase 3 — Classical Machine Learning
> **Estimated:** 3–4 weeks (Days 18–32)
> **Goal:** Understand the core algorithms that deep learning is built on top of

### 3.1 Supervised Learning

| Day | Algorithm | What You'll Implement | Notebook |
|-----|-----------|----------------------|---------|
| 18 | Linear Regression | From scratch with NumPy, then with sklearn | `day-18-linear-regression.ipynb` |
| 19 | Logistic Regression | Binary classification, sigmoid, cross-entropy loss | `day-19-logistic-regression.ipynb` |
| 20 | Decision Trees | Information gain, Gini impurity, tree depth overfitting | `day-20-decision-trees.ipynb` |
| 21 | Random Forest | Bagging, ensemble, feature importance | `day-21-random-forest.ipynb` |
| 22 | SVM | Margin maximization, kernel trick, when to use SVM vs NN | `day-22-svm.ipynb` |

### 3.2 Unsupervised Learning

| Day | Algorithm | What You'll Implement | Notebook |
|-----|-----------|----------------------|---------|
| 23 | K-Means Clustering | Centroid update loop, inertia, choosing k with elbow method | `day-23-kmeans.ipynb` |
| 24 | PCA in Practice | Apply PCA to real dataset, visualize 100D → 2D, explained variance | `day-24-pca-practice.ipynb` |

### 3.3 Model Evaluation

| Day | Topic | Concepts | Notebook |
|-----|-------|---------|---------|
| 25 | Metrics & Evaluation | Accuracy, Precision, Recall, F1, ROC-AUC, confusion matrix | `day-25-evaluation-metrics.ipynb` |
| 26 | Overfitting & Regularization | L1/L2, train vs val curves, bias-variance tradeoff | `day-26-regularization.ipynb` |

### 3.4 Kaggle Practice

| Day | Task | Notebook |
|-----|------|---------|
| 27–28 | Kaggle: Titanic survival prediction | `day-27-kaggle-titanic.ipynb` |
| 29–30 | Kaggle: House price regression | `day-29-kaggle-house-prices.ipynb` |
| 31–32 | Review + re-implement weakest areas | — |

---

## Phase 4 — Deep Learning
> **Estimated:** 5–7 weeks (Days 33–65)
> **Goal:** Build neural networks from scratch, understand every component, train real models

### 4.1 Neural Network Basics (Days 33–38)

| Day | Topic | Concepts | Notebook |
|-----|-------|---------|---------|
| 33 | Perceptron | Weighted sum, step function, single neuron learning | `day-33-perceptron.ipynb` |
| 34 | Multi-Layer Perceptron | Hidden layers, forward pass through 3 layers | `day-34-mlp.ipynb` |
| 35 | Activation Functions | ReLU, Sigmoid, Tanh, Softmax — when to use which | `day-35-activations.ipynb` |
| 36 | Loss Functions | MSE vs Cross-entropy, when to use each, implement both | `day-36-loss-functions.ipynb` |
| 37 | Backpropagation | Derive gradient manually for 2-layer net, verify with autograd | `day-37-backprop.ipynb` |
| 38 | Training a Real MLP | MNIST digit classifier with PyTorch (first real model!) | `day-38-mnist-mlp.ipynb` |

### 4.2 Training Mechanics (Days 39–43)

| Day | Topic | Concepts | Notebook |
|-----|-------|---------|---------|
| 39 | SGD & Optimizers | SGD, Adam, RMSProp — visualize convergence difference | `day-39-optimizers.ipynb` |
| 40 | Learning Rate | LR too high/low, LR scheduling, warmup | `day-40-learning-rate.ipynb` |
| 41 | Batch Normalization | Why it speeds up training, implement it manually | `day-41-batch-norm.ipynb` |
| 42 | Dropout | How it prevents overfitting, implement and visualize | `day-42-dropout.ipynb` |
| 43 | Train/Val/Test tracking | Plot loss curves, early stopping, model checkpointing | `day-43-training-best-practices.ipynb` |

### 4.3 Convolutional Neural Networks (Days 44–50)

| Day | Topic | Concepts | Notebook |
|-----|-------|---------|---------|
| 44 | Convolution operation | Kernel, stride, padding — compute output size manually | `day-44-convolution.ipynb` |
| 45 | Pooling & CNN layers | Max pooling, global average pooling, receptive field | `day-45-pooling-cnn-layers.ipynb` |
| 46 | Build a CNN from scratch | 3-layer CNN on CIFAR-10 | `day-46-cnn-cifar10.ipynb` |
| 47 | Classic architectures | LeNet → VGG → ResNet — what changed and why | `day-47-cnn-architectures.ipynb` |
| 48 | Transfer learning | Fine-tune ResNet-18 on custom data | `day-48-transfer-learning.ipynb` |
| 49 | Object detection intro | YOLO concept, bounding boxes, IoU | `day-49-object-detection-intro.ipynb` |
| 50 | CNN project | Train image classifier on a dataset of your choice | `day-50-cnn-project.ipynb` |

### 4.4 Recurrent Neural Networks (Days 51–56)

| Day | Topic | Concepts | Notebook |
|-----|-------|---------|---------|
| 51 | Sequences & RNNs | Why order matters, hidden state, unrolling through time | `day-51-rnn-basics.ipynb` |
| 52 | Vanishing gradient problem | Why plain RNN fails on long sequences | `day-52-vanishing-gradient.ipynb` |
| 53 | LSTM | Forget/input/output gates — understand each one | `day-53-lstm.ipynb` |
| 54 | GRU | Simplified LSTM, when to use GRU vs LSTM | `day-54-gru.ipynb` |
| 55 | Time series forecasting | Predict sensor data with LSTM | `day-55-lstm-timeseries.ipynb` |
| 56 | Text generation | Character-level language model with LSTM | `day-56-text-generation-lstm.ipynb` |

### 4.5 Transformers & Attention (Days 57–65)

| Day | Topic | Concepts | Notebook |
|-----|-------|---------|---------|
| 57 | Attention mechanism | Query/Key/Value, scaled dot-product attention | `day-57-attention.ipynb` |
| 58 | Self-attention | How tokens attend to each other, attention maps | `day-58-self-attention.ipynb` |
| 59 | Multi-head attention | Why multiple heads, concatenate + project | `day-59-multihead-attention.ipynb` |
| 60 | Transformer architecture | Encoder block, decoder block, positional encoding | `day-60-transformer-architecture.ipynb` |
| 61 | BERT | Masked LM, next sentence prediction, fine-tuning | `day-61-bert.ipynb` |
| 62 | GPT | Causal LM, autoregressive generation, prompt engineering | `day-62-gpt.ipynb` |
| 63 | Fine-tuning a pre-trained model | Use Hugging Face to fine-tune BERT on text classification | `day-63-finetuning-bert.ipynb` |
| 64 | LoRA | Low-rank adaptation, why it works, implement a simple version | `day-64-lora.ipynb` |
| 65 | Phase 4 project | Build an end-to-end NLP or vision pipeline | `day-65-phase4-project.ipynb` |

---

## Phase 5 — Specialization
> **Estimated:** 3–4 weeks (Days 66–90)
> Choose the path that fits your goals

| Path | Best For | Key Topics |
|------|----------|-----------|
| **Computer Vision** | Working with images, video | Detection, segmentation, tracking, CLIP |
| **NLP / LLMs** | Language, chat, documents | RAG, prompt engineering, LLM fine-tuning |
| **Edge AI / Embedded ML** | Deploying AI on devices | TensorFlow Lite, ONNX, TensorRT, C++ inference |
| **Reinforcement Learning** | Agents, games, robotics | Q-learning, PPO, environments |

---

## Phase 6 — Projects
> Build something real — this is what you show on a resume/portfolio

| Level | Project | Skills Used |
|-------|---------|------------|
| Beginner | Iris flower classifier (sklearn) | Phase 2–3 |
| Beginner | House price predictor | Phase 3 |
| Intermediate | CIFAR-10 image classifier (CNN) | Phase 4.3 |
| Intermediate | Text sentiment analyzer (BERT) | Phase 4.5 |
| Intermediate | Time series forecaster (LSTM) | Phase 4.4 |
| Advanced | End-to-end image classifier with REST API | Phase 4 + deployment |
| Advanced | Fine-tune LLM on domain data | Phase 4.5 + 5 |
| Advanced | Edge AI: PyTorch → ONNX → C++ inference | Phase 5 |

---

## Daily Notebook Index

> All notebooks live in `notebooks/` folder

| Notebook | Phase | Topic |
|----------|-------|-------|
| `day-01-linear-algebra.ipynb` | 1.1 | Vectors, `W@x+b`, dot product |
| `day-02-eigenvalues-svd-pca.ipynb` | 1.1 | Eigenvalues, SVD, PCA from scratch |
| *(more added as you progress)* | | |

---

## Resources

### Free Courses
| Course | Provider | Best For |
|--------|----------|---------|
| [Practical Deep Learning](https://course.fast.ai) | fast.ai | Best hands-on start |
| [CS231n — CNNs](https://cs231n.stanford.edu/) | Stanford | Computer Vision deep dive |
| [CS224n — NLP](https://web.stanford.edu/class/cs224n/) | Stanford | NLP & Transformers |
| [Deep Learning Specialization](https://www.deeplearning.ai/courses/deep-learning-specialization/) | DeepLearning.AI | Comprehensive theory |
| [Andrej Karpathy — Neural Nets from Scratch](https://www.youtube.com/@AndrejKarpathy) | YouTube | Best intuition builder |

### Books
| Book | Level | Free? |
|------|-------|-------|
| Neural Networks and Deep Learning — Nielsen | Beginner | [Yes](http://neuralnetworksanddeeplearning.com/) |
| Hands-On ML — Aurélien Géron | Beginner–Mid | No |
| Deep Learning — Goodfellow, Bengio, Courville | Advanced | [Yes](https://www.deeplearningbook.org/) |

### Practice Platforms
- [Kaggle](https://www.kaggle.com) — datasets, competitions, free GPUs
- [Hugging Face](https://huggingface.co) — pre-trained models, fine-tuning
- [Papers With Code](https://paperswithcode.com) — papers + implementations

---

## Progress Tracker

### Status Legend
- `[ ]` Not started
- `[~]` In progress
- `[x]` Completed

### Phase 1 — Math Foundations

| Day | Topic | Status | Notes |
|-----|-------|--------|-------|
| 1 | Vectors, matrices, dot product | `[x]` | Completed |
| 2 | Eigenvalues, SVD, PCA | `[~]` | In progress |
| 3 | NumPy matrix ops | `[ ]` | |
| 4 | Derivatives & partial derivatives | `[ ]` | |
| 5 | Chain rule & backprop | `[ ]` | |
| 6 | Gradient descent from scratch | `[ ]` | |
| 7 | Probability basics | `[ ]` | |
| 8 | Distributions | `[ ]` | |
| 9 | Bayes' theorem & MLE | `[ ]` | |
| 10 | Capstone: linear regression from scratch | `[ ]` | |

### Phase 2 — Python AI Stack

| Day | Topic | Status |
|-----|-------|--------|
| 11–17 | NumPy, Pandas, Matplotlib, sklearn, PyTorch | `[ ]` |

### Phase 3 — Classical ML

| Day | Topic | Status |
|-----|-------|--------|
| 18–32 | Regression, Trees, SVM, K-Means, PCA, Kaggle | `[ ]` |

### Phase 4 — Deep Learning

| Day | Topic | Status |
|-----|-------|--------|
| 33–38 | MLP, activations, loss, backprop, MNIST | `[ ]` |
| 39–43 | Optimizers, LR, BatchNorm, Dropout | `[ ]` |
| 44–50 | CNNs, transfer learning | `[ ]` |
| 51–56 | RNN, LSTM, GRU | `[ ]` |
| 57–65 | Transformers, BERT, GPT, LoRA | `[ ]` |

### Milestone Log

| Date | Milestone | Notes |
|------|-----------|-------|
| 2026-04-05 | Started AI learning journey | Day 1 complete |
| 2026-04-05 | Day 2 in progress | Eigenvalues, SVD, PCA |

---

*Started: April 5, 2026*
