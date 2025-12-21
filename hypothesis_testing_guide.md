# Hypothesis Testing Fundamentals

## Core Concept

Hypothesis testing answers the question: **"If a claim is true, how surprising would my observed data be?"**

We use logical reasoning by contradiction:
- Assume the claim is true
- Calculate how rare our observed result would be under that assumption
- If the result would be extremely rare, we conclude the claim is probably false

## The 5-Step Process

### Step 1: State Your Hypotheses

**Null Hypothesis (H₀)**: The claim being tested (status quo)
- Example: μ = 500 hours

**Alternative Hypothesis (H₁)**: What we suspect instead
- Example: μ ≠ 500 hours (two-tailed)
- Could also be: μ < 500 or μ > 500 (one-tailed)

### Step 2: Choose Significance Level (α)

Set your threshold for "rare enough" **before** collecting or analyzing data.
- Common choice: α = 0.05 (5%)
- This represents how often you're willing to incorrectly reject a true H₀

**Why set α beforehand?**
- Prevents bias and cherry-picking results
- Ensures comparability across studies
- Builds scientific credibility

### Step 3: Calculate Test Statistic

**Standard Error (SE)**: The standard deviation of sample means
```
SE = SD / √n
```

**Test Statistic (z-score or t-score)**: How many standard errors away from the claimed mean
```
z = (sample mean - claimed mean) / SE
```

### Step 4: Find the P-Value

**P-value**: The probability of getting your observed result (or more extreme) if H₀ is true

Interpretation using normal distribution:
- Within ±2 SE: ~95% of data (5% outside)
- Within ±3 SE: ~99.7% of data (0.3% outside)

The further your test statistic from zero, the smaller the p-value.

### Step 5: Make a Decision

**Decision Rule:**
- If p-value < α: **Reject H₀** (evidence against the claim)
- If p-value ≥ α: **Fail to reject H₀** (insufficient evidence)

**Important**: "Fail to reject" ≠ "Accept"
- Not finding evidence against something is NOT the same as proving it's true
- Could mean: claim is true, OR sample size too small, OR just got unlucky

## Key Relationships

### Sample Size Effects
- **Larger sample** → Smaller SE → More extreme test statistic → Easier to detect differences
- **Smaller sample** → Larger SE → Less extreme test statistic → Harder to detect differences

### Sampling Variability
Even if the true population mean is correct, different samples will give different sample means due to natural random variation. This is why we need standard error to measure that variability.

## Worked Example: Fitness App

**Scenario**: App claims users lose 10 pounds on average. Sample of 25 users lost 8.5 pounds (SD = 3).

1. **Hypotheses**: H₀: μ = 10, H₁: μ ≠ 10
2. **Significance level**: α = 0.05
3. **Test statistic**: 
   - SE = 3/√25 = 0.6
   - z = (8.5 - 10)/0.6 = -2.5
4. **P-value**: ≈ 0.012 (less than 0.05)
5. **Decision**: Reject H₀. Evidence suggests the app's claim is incorrect.

## Common Misunderstandings

❌ **Wrong**: "We proved the null hypothesis is false"
✓ **Right**: "We have strong evidence against the null hypothesis"

❌ **Wrong**: "Fail to reject means the null hypothesis is true"
✓ **Right**: "Fail to reject means we don't have enough evidence to conclude it's false"

❌ **Wrong**: "P-value is the probability the null hypothesis is true"
✓ **Right**: "P-value is the probability of getting our data if the null hypothesis is true"

## Visual Intuition

Think of hypothesis testing like a trial:
- **Null hypothesis** = "Innocent until proven guilty"
- **Evidence** = Your sample data
- **P-value** = How unusual this evidence would be if defendant were innocent
- **α** = Standard of proof required to convict
- **Reject H₀** = Find guilty (evidence too unusual to be coincidence)
- **Fail to reject H₀** = Not guilty verdict (insufficient evidence, but doesn't prove innocence)

## Next Steps to Explore

- One-tailed vs two-tailed tests
- Type I and Type II errors
- Different test types (t-tests, z-tests, chi-square, ANOVA)
- Power analysis and effect sizes
- Confidence intervals relationship to hypothesis tests