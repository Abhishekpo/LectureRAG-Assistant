# LectureRAG-Assistant - Test Questions

This document contains a comprehensive set of test questions for evaluating your RAG system's performance across different difficulty levels and reasoning requirements.

## 🎯 Testing Strategy

The questions are organized into three tiers:

1. **Basic Factual Retrieval** - Direct lookup from lecture
2. **Conceptual Understanding** - Requires explanation and reasoning
3. **Multi-step Reasoning** - Requires connecting multiple concepts

---

## 🟢 TIER 1: Basic Factual Retrieval (Easy Wins)

These questions test if your system can pull **exact information directly from the text**.

**⚠️ If your system fails here → chunking or retrieval is broken.**

### Question 1.1
```
What is the probability of a royal straight flush in poker?
```
**Expected Answer Type**: Exact numerical value from lecture
**Why It Matters**: Tests basic text retrieval

### Question 1.2
```
How many possible 5-card poker hands are there?
```
**Expected Answer Type**: Specific number mentioned in lecture
**Why It Matters**: Tests if system can find specific calculations

### Question 1.3
```
What is the probability of each atomic event in poker?
```
**Expected Answer Type**: Definition and formula from lecture
**Why It Matters**: Tests understanding of poker probability basics

### Question 1.4
```
What is the probability of getting four of a kind?
```
**Expected Answer Type**: Direct calculation from lecture
**Why It Matters**: Tests retrieval of specific probability calculations

### Question 1.5
```
What are the three coins mentioned in question 14.1?
```
**Expected Answer Type**: Coins A, B, C with their head probabilities
**Why It Matters**: Tests factual retrieval with specific parameters

### Question 1.6
```
List the probabilities of heads for coins A, B, and C.
```
**Expected Answer Type**: A: 20%, B: 60%, C: 80%
**Why It Matters**: Tests numerical fact extraction

---

## 🟡 TIER 2: Conceptual Understanding (Medium)

These questions test **reasoning and explanation**, not just text lookup.

**⚠️ If your system succeeds here but fails Tier 3 → retrieval is working but context formatting may have issues.**

### Question 2.1
```
Why is P(A∣B∩A) = 1? Explain the mathematical reasoning.
```
**Expected Answer**: 
- When A and B both occur, conditional probability of A given (B and A) is 1
- Because B∩A ⊆ A, so if B∩A happened, A definitely happened
- Probability of A given A is always 1

### Question 2.2
```
Why are coin flips independent when x is known?
```
**Expected Answer**:
- When bias probability x is fixed, each flip has the same probability
- Results of previous flips don't affect probability of next flip
- Each flip is a fresh random event with the same parameters

### Question 2.3
```
Why are coin flips NOT independent when x is unknown?
```
**Expected Answer**:
- When x is unknown, we must consider all possible values of x
- Each flip's result provides information about x
- This changes our belief about future flip probabilities
- Observing heads increases belief in higher x values
- This affects prediction of next flip

### Question 2.4
```
What does "independence" mean in probability theory?
```
**Expected Answer**:
- Two events are independent if P(A∩B) = P(A)×P(B)
- Or equivalently: P(A|B) = P(A)
- One event's outcome doesn't change probability of another
- Can condition on one without affecting probabilities of others

### Question 2.5
```
Explain the concept of conditional independence (A ⊥ B | C).
```
**Expected Answer**:
- A and B are conditionally independent given C if:
  P(A∩B|C) = P(A|C)×P(B|C)
- When we know C, A and B don't influence each other
- They may be dependent unconditionally but independent given C

### Question 2.6
```
How does the "wrapper problem" illustrate conditional independence?
```
**Expected Answer**:
- Candy type and wrapper color are independent when you know the box
- But before opening box, they share information about which box you have
- This is an example of explaining away or conditional independence

---

## 🔴 TIER 3: Multi-Step Reasoning (Important)

These test if your system **connects ideas** and applies reasoning across concepts.

**⚠️ This checks if your context formatting and chunk retrieval is working correctly.**

### Question 3.1
```
Which coin (A, B, or C) is most likely given two heads and one tail? 
Why? Show your reasoning using Bayes rule.
```
**Expected Answer**:
- Coin C is most likely (computed value: 0.384)
- Coin A is least likely (significantly lower probability)
- Use Bayes rule: P(Coin | 2H, 1T) ∝ P(2H, 1T | Coin) × P(Coin)
- Calculate likelihood for each coin:
  - P(2H, 1T | A) = C(3,2) × 0.2² × 0.8¹ = 3 × 0.04 × 0.8 = 0.096
  - P(2H, 1T | B) = C(3,2) × 0.6² × 0.4¹ = 3 × 0.36 × 0.4 = 0.432
  - P(2H, 1T | C) = C(3,2) × 0.8² × 0.2¹ = 3 × 0.64 × 0.2 = 0.384
- Normalize to get posterior probabilities

### Question 3.2
```
How do you apply Bayes rule in the coin problem? 
What is the formula and how does it help us identify the coin?
```
**Expected Answer**:
- Formula: P(Coin_i | Observations) = P(Obs | Coin_i) × P(Coin_i) / P(Obs)
- Likelihood: How likely are the observations given each coin
- Prior: Initial belief about each coin's probability
- Posterior: Updated belief after seeing observations
- This helps because coins with higher likelihood of producing observed data become more probable

### Question 3.3
```
Why can we ignore the denominator in Bayes rule when comparing coin probabilities?
```
**Expected Answer**:
- When comparing P(Coin_i | Obs) across different coins, denominator P(Obs) is the same
- Since all coins produce the same observations, we only care about relative probabilities
- We can use: P(Coin_i | Obs) ∝ P(Obs | Coin_i) × P(Coin_i)
- The ∝ symbol means "proportional to"
- Then normalize all unnormalized probabilities so they sum to 1

### Question 3.4
```
In the burglary and earthquake problem, explain why burglary and 
earthquake are conditionally independent given alarm.
```
**Expected Answer**:
- Without knowing alarm state: burglary and earthquake are dependent
  - Both can cause alarm, so one affects belief in other
- Given alarm (alarm = true or alarm = false):
  - If alarm is known, observing burglary doesn't change P(earthquake | alarm)
  - The alarm "explains" the connection between them
  - This is explaining away: if alarm is true, other causes become less likely

### Question 3.5
```
Use the candy box problem to explain how prior knowledge affects inference.
What is the probability of getting a red wrapper?
```
**Expected Answer**:
- Two types of boxes: 75% chocolate, 25% anchovy
- Chocolate box: 70% red wrappers
- Anchovy box: 10% red wrappers
- P(red wrapper) = P(red|chocolate)×P(chocolate) + P(red|anchovy)×P(anchovy)
- = 0.7 × 0.75 + 0.1 × 0.25
- = 0.525 + 0.025 = 0.55 (or 55%)
- Prior (box type) affects likelihood of observed wrapper color

### Question 3.6
```
Walk through the Bayes rule calculation to find P(chocolate | red wrapper).
Show each step.
```
**Expected Answer**:
- Numerator: P(red|chocolate) × P(chocolate) = 0.7 × 0.75 = 0.525
- Denominator: P(red) = 0.55 (from previous calculation)
- Posterior: P(chocolate|red) = 0.525 / 0.55 ≈ 0.955 or 95.5%
- Red wrapper makes chocolate box much more likely
- This is inverse probability: going from observation to cause

---

## 📊 Testing Checklist

### For Each Question, Verify:

- [ ] **Relevance**: Did the system return relevant chunks from the lecture?
- [ ] **Accuracy**: Is the answer factually correct from the lecture?
- [ ] **Completeness**: Does the answer address all parts of the question?
- [ ] **Clarity**: Is the explanation clear and understandable?
- [ ] **Reasoning**: Does the answer show working/steps (for Tier 2 & 3)?

### Success Criteria:

- **Tier 1**: Should get 100% correct (these are direct lookups)
- **Tier 2**: Should get 80%+ correct (some interpretation needed)
- **Tier 3**: Should get 60%+ correct (requires multi-step reasoning)

---

## 🚀 Running the Tests

```bash
# Start the RAG system
python rag_answer.py

# Copy and paste each question
# Evaluate the response using the checklist above
```

---

## 📈 Interpreting Results

### If Tier 1 Fails (< 80% success):
- **Problem**: Chunking or retrieval is broken
- **Solutions**: 
  - Check `chunks.txt` formatting
  - Verify embeddings are computed correctly
  - Test `search_chunks.py` with simple queries

### If Tier 1 Passes but Tier 2 Fails:
- **Problem**: Retrieval works but system struggles with reasoning
- **Solutions**:
  - Increase `top_chunks` from 3 to 5
  - Check if relevant context chunks are being retrieved
  - Verify LLM model is running properly

### If Tier 2 Passes but Tier 3 Fails:
- **Problem**: Single-chunk understanding works, but multi-step reasoning fails
- **Solutions**:
  - Retrieve more chunks (increase `top_chunks`)
  - Ensure chunks are in logical order
  - Check if prompt is clear about showing reasoning

### All Tiers Pass:
- **Excellent!** Your RAG system is working effectively
- Consider testing on new lecture content

---

## 💡 Tips for Better Results

1. **Be Specific**: Ask questions that reference specific numbers or concepts
2. **Show Your Work**: Ask the system to "explain your reasoning" or "show steps"
3. **Ask Follow-ups**: If first answer is incomplete, ask follow-up questions
4. **Test Edge Cases**: Ask about things not directly in lecture
5. **Compare Models**: Try different Ollama models for embedding and chat

---

## 📝 Notes

- These questions are based on lecture content about probability, Bayes rule, and conditional independence
- The expected answers are derived from the actual lecture transcript
- Difficulty levels are designed to test different aspects of the RAG system
- Use Tier 1 to verify basic functionality before moving to harder questions

**Happy Testing! 🎓**
