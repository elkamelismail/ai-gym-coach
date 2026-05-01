# Workout Knowledge Base

This folder contains scientific and evidence-based resources related to resistance training and muscle hypertrophy.

These documents serve as the knowledge base for the AI Gym Coach using a Retrieval-Augmented Generation (RAG) system.

---

## Included Documents

### 1. Muscle Hypertrophy Mechanisms

* Schoenfeld (2010) – *The Mechanisms of Muscle Hypertrophy*
* Topics covered:

  * Mechanical tension
  * Muscle damage
  * Metabolic stress
  * Hormonal responses (IGF-1, testosterone, growth hormone)

Key insight:
Muscle growth is primarily driven by mechanical tension, metabolic stress, and muscle damage 

---

### 2. Resistance Training Progression Models

* ACSM Position Stand – *Progression Models in Resistance Training for Healthy Adults*
* Topics covered:

  * Progressive overload
  * Training variables (volume, intensity, frequency)
  * Program design for different levels (beginner to advanced)

Key insight:
Hypertrophy is optimized with moderate loads (70–85% 1RM), 6–12 repetitions, and multiple sets 

---

## Key Training Concepts

### Progressive Overload

Gradual increase of training stress through:

* Load (weight)
* Repetitions
* Volume

This principle is essential for continued adaptation 

---

### Hypertrophy Drivers

The three main mechanisms of muscle growth:

* Mechanical tension
* Metabolic stress
* Muscle damage 

---

### Optimal Training Zones

| Goal        | Repetitions | Load (% 1RM) |
| ----------- | ----------- | ------------ |
| Strength    | 1–5         | 85–100%      |
| Hypertrophy | 6–12        | 70–85%       |
| Endurance   | 15+         | <60%         |

---

## Purpose in the Project

These documents enable the AI to:

* Generate scientifically grounded workout programs
* Recommend appropriate sets, repetitions, and intensity
* Explain training principles clearly
* Adapt recommendations to user level

---

## Usage in RAG Pipeline

1. Load PDF documents
2. Split into chunks
3. Convert to embeddings
4. Store in vector database
5. Retrieve relevant chunks during queries

---

## Notes

* Content is based on peer-reviewed research
* Avoid adding non-scientific sources
* Optimize chunk size for retrieval quality

---

## Example Queries

* What is the best rep range for hypertrophy?
* Explain progressive overload
* Build a muscle growth program
* Why is metabolic stress important?
