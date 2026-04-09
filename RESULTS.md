# WSPI Road Classification - Results Summary

## Project
CNN-based road surface classifier (dry, ice, mixed, snow). Dataset: ~9k images (6k snow, 1k dry, 1k ice, 1k mixed). Trained on Kaggle with T4 GPU.

## From-Scratch CNN Results

### Run 1 - Baseline (Original architecture)
- 2 conv layers, 3 FC layers, 1.8M parameters
- 30 epochs, SGD lr=0.001
- Loss plateaued at epoch 10 (~0.01) - model memorized training data

| | Test | CV |
|---|---|---|
| Overall | 98.3% | 23.3% |
| Dry | 92.3% | 6.7% |
| Ice | 98.7% | 13.3% |
| Mixed | 90.2% | 0.0% |
| Snow | 99.8% | 40.0% |

**Takeaway:** High test accuracy was misleading - model memorized camera-specific patterns. 1.8M parameters on 9k images caused severe overfitting.

---

### Run 2 - New architecture (Reduced parameters)
- 3 conv layers, AdaptiveAvgPool, 2 FC layers, ~3k parameters
- 10 epochs, SGD lr=0.001
- Loss still dropping at epoch 10 - not enough training time

| | Test | CV |
|---|---|---|
| Overall | 81.5% | 25.0% |
| Dry | 0.0% | 0.0% |
| Ice | 89.3% | 13.3% |
| Mixed | 0.0% | 0.0% |
| Snow | 99.7% | 86.7% |

**Takeaway:** Fewer parameters prevented memorization but 10 epochs wasn't enough. Model only learned snow.

---

### Run 3 - 30 epochs (Same architecture)
- 30 epochs, SGD lr=0.001
- Loss dropped to 0.25

| | Test | CV |
|---|---|---|
| Overall | 90.3% | - |
| Dry | 82.1% | - |
| Ice | 100.0% | - |
| Mixed | 1.6% | - |
| Snow | 99.3% | - |

**Takeaway:** More epochs helped dry and ice significantly. Mixed still broken due to class imbalance - snow dominates training.

---

### Run 4 - Weighted loss
- Added weighted CrossEntropyLoss inversely proportional to class size
- 30 epochs, SGD lr=0.001

| | Test | CV |
|---|---|---|
| Overall | 92.3% | 16.7% |
| Dry | 84.6% | 6.7% |
| Ice | 100.0% | 13.3% |
| Mixed | 70.5% | 6.7% |
| Snow | 94.6% | 40.0% |

**Takeaway:** Weighted loss fixed mixed on test set (0% → 70.5%). Snow dropped as expected since model now shares attention across all classes. CV still poor.

---

### Run 5 - Augmentation (30 epochs)
- Added RandomHorizontalFlip, RandomRotation(15), ColorJitter
- Separate train/test transforms
- 30 epochs with weighted loss

| | Test | CV |
|---|---|---|
| Overall | 69.0% | 26.7% |
| Dry | 97.4% | 33.3% |
| Ice | 100.0% | 6.7% |
| Mixed | 13.1% | 6.7% |
| Snow | 67.1% | 60.0% |

**Takeaway:** CV improved but model hadn't finished learning - loss still dropping. Augmentation makes training harder so more epochs needed.

---

### Run 6 - Augmentation (50 epochs)
- Same as Run 5 but 50 epochs
- Loss dropped to 0.38

| | Test | CV |
|---|---|---|
| Overall | 75.2% | 33.3% |
| Dry | 92.3% | 40.0% |
| Ice | 100.0% | 6.7% |
| Mixed | 73.8% | 33.3% |
| Snow | 70.0% | 53.3% |

**Takeaway:** Best CV result for scratch model. Test accuracy trades memorization for generalization - model learning real patterns but data diversity limits further improvement.

---

## VGG16 Pretrained Results

### Run 1 - Baseline (lr=0.001)
- VGG16 with frozen features, trainable classifier
- 10 epochs, Adam lr=0.001
- Loss bounced between 0.4–0.9 (lr too high)

| | Test | CV |
|---|---|---|
| Overall | 98.0% | 36.7% |
| Dry | 98.7% | 20.0% |
| Ice | 100.0% | 26.7% |
| Mixed | 77.0% | 6.7% |
| Snow | 99.8% | 93.3% |

---

### Run 2 - Lower learning rate (lr=0.0001)
- Stable training, loss dropped smoothly to 0.02

| | Test | CV |
|---|---|---|
| Overall | 98.4% | 36.7% |
| Dry | 97.4% | 6.7% |
| Ice | 100.0% | 46.7% |
| Mixed | 88.5% | 6.7% |
| Snow | 99.3% | 86.7% |

**Takeaway:** Best overall pretrained result. Stable training improved mixed on test set. CV same overall but different per-class distribution.

---

## Key Findings

1. **Data is the bottleneck, not the model.** Multiple architectures (scratch CNN, VGG16 pretrained, teammate's models) all converge around 33-40% on external CV data. The training images are too similar to each other and too different from real-world images.

2. **Reducing parameters fixed overfitting.** Going from 1.8M to 3k parameters forced the model to learn patterns instead of memorizing.

3. **Weighted loss fixed class imbalance.** Mixed class went from 0% to 70%+ on test set once the model was penalized for ignoring smaller classes.

4. **Augmentation improved generalization.** CV accuracy improved from ~17% to 33% on the scratch model with augmentation, confirming the model was learning more robust features.

5. **Pretrained models generalize slightly better.** VGG16 hit 36.7% CV vs 33.3% for scratch, showing pretrained features help but can't overcome limited data diversity.

6. **Test set accuracy is misleading with homogeneous data.** 98%+ test accuracy meant nothing when CV accuracy was 23-36%. Always test on truly external data.

## What Would Improve Results
- More diverse training images from different cameras, locations, and conditions
- A "not road" category for images that don't clearly show a road surface