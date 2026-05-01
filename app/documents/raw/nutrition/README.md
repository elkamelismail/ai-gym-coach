# Nutrition Knowledge Base

This folder contains evidence-based nutrition documents used by the AI Gym Coach RAG system.

## Purpose

The goal of this knowledge base is to help the assistant answer questions about:

- Bulking
- Cutting
- Body recomposition
- Protein intake
- Carbohydrate timing
- Fat loss
- Sports nutrition
- Supplements

## Included Documents

### 1. Energy Balance and Body Weight Regulation

This document explains how body weight changes depend on the relationship between energy intake and energy expenditure. It also explains why weight loss is not always linear because the body adapts through changes in appetite, resting energy expenditure, and metabolic adaptation. :contentReference[oaicite:0]{index=0}

Main topics:
- Calories and energy balance
- Weight loss adaptation
- Energy expenditure
- Diet composition
- Body weight regulation

### 2. Nutrient Timing

This document explains how timing protein, carbohydrates, and meals can affect performance, recovery, glycogen restoration, and muscle protein synthesis. It recommends focusing first on total daily protein intake, with protein feedings distributed during the day. :contentReference[oaicite:1]{index=1}

Main topics:
- Protein timing
- Carbohydrate timing
- Pre-workout nutrition
- Post-workout nutrition
- Glycogen recovery
- Meal frequency

### 3. Sports Supplements

This document explains the role of supplements in sports nutrition. It emphasizes that supplements should support, not replace, a solid diet. It also highlights that only a few supplements have strong evidence, such as caffeine, creatine, nitrate, beta-alanine, and sodium bicarbonate. :contentReference[oaicite:2]{index=2}

Main topics:
- Supplement safety
- Evidence-based supplements
- Performance supplements
- Micronutrient deficiencies
- Doping contamination risk

## RAG Usage

These documents will be:

1. Loaded from PDF files
2. Split into text chunks
3. Converted into embeddings
4. Stored in a vector database
5. Retrieved when the user asks nutrition-related questions

## Example Questions

- Should I bulk, cut, or recomp?
- How many calories should I eat to lose fat?
- How much protein do I need?
- What should I eat before training?
- What should I eat after training?
- Which supplements actually work?
- How do I preserve muscle during a cut?
