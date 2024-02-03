# Comprehensive Evaluation
![i.jpg](https://picx.zhimg.com/80/v2-49852ba3fe5dd36d32800b729a5ca773_1440w.webp?source=1def8aca)

[methods of CE](https://link.springer.com/chapter/10.1007/978-981-15-8582-1_20)

## Multi-Criteria Decision Analysis (MCDA)
aka Multi-Criteria Decision-Making (MCDM)
[1000minds](https://www.1000minds.com/decision-making/what-is-mcdm-mcda)
https://openlibrary.org/works/OL8362416W/Multiple_criteria_decision_analysis

## Potentially All Pairwise RanKings of all possible Alternatives (PAPRIKA)

## multi-criteria optimization and compromise solution(VIKOR)
VIekriterijumsko KOmpromisno Rangiranje(VIKOR)

[examples](https://www.sciencedirect.com/topics/computer-science/vikor)

VIKOR核心就是针对归一化矩阵，通过带权值的范数为1(曼哈顿)与范数为无穷大(切比雪夫)闵可夫斯基距离求解出距离

## Technique for Order of Preference by Similarity to Ideal Solution (TOPSIS)

topsis核心就是针对归一化矩阵，通过带权值的距离公式求解出到正负理想点的距离

## Fuzzy Comprehension Evaluation Method (FCE)

### **CORE** (TL;DR):
- Converts **qualitative** evaluations to **quantitative** assessments
- Handles **uncertain** and **subjective** data effectively

### More
- One-level Evaluation
   - Define **factors $U$** and **evaluations $V$**
   - Determine **factor weights $A$**
     - $A=[a_1,a_2,...,a_n]$, and $\sum_{i=1}^na_i=1$
     - commonly use _Delphi Method_, [AHP](#analytic-hierarchy-process-ahp) and [Entropy Weight Method](#entropy-weight-method-ewm)
   - establish **judgment matrix $R$**
     - $R=(r_{ij})_{n \times m}$ 
   - Calculate final assessment with **fuzzy vector $B = A * R$**
- **Multi-level Evaluation**
   - Appropriate for **complex settings** with numerous factors
   - Assign **weights at multiple levels** for detailed analysis
- Comparison with Other Methods
   - **Accuracy** ?
      - FCE: Contextually high in complex systems
      - Quantitative: Objective but less nuanced
   - **Effectiveness**
      - FCE: Manages uncertainty well
      - Traditional: Perform poorly with ambiguity
   - **Flexibility**
      - FCE: Customizable for context
      - Other Qualitative: Less detailed than FCE
   - **Application Scope**
      - FCE: Ideal for human-centric evaluations
      - Other Methods: Depend on data nature and desired outcomes

### Applications & Examples

- FCE + Delphi
  - [Group fuzzy comprehensive evaluation method under ignorance](https://www.sciencedirect.com/science/article/abs/pii/S0957417419301058)
    - use basic probability assignment (BPA) to extract the expert's judgment information
    - accommodates ignorance and uncertainty in assessments
- FCE + AHP:
  - [Analysis of ecological carrying capacity using a fuzzy comprehensive evaluation method](https://www.sciencedirect.com/science/article/abs/pii/S1470160X20301801)
  - [Evaluating teaching performance based on fuzzy AHP and comprehensive evaluation approach](https://www.sciencedirect.com/science/article/abs/pii/S1568494614006152)
  - [Fuzzy comprehensive evaluation method for energy management systems based on an internet of things](https://ieeexplore.ieee.org/abstract/document/8016341/)

## Projection Pursuit (PP)
Three projection pursuit approaches are investigated, including principal component analysis (PCA), independent component analysis (ICA), and singular value decomposition (SVD)

### Principal Component Analysis (PCA)

### Factor Analysis (FA)

## Interpretative Structural Modeling (ISM)

Adversarial Interpretive Structure ModelingMethod (AISM)

## Analytic Hierarchy Process (AHP)

## Elimination and Choice Expressing Reality (ELECTRE)

## Rank-Sum Ratio (RSR) WRSR

## Entropy Weight Method (EWM)

## Grey Relational Analysis (GRA)

## Data envelopment analysis (DEA)

[auto formula](https://www.huaxuejia.cn/ism/CE-SAISM/vikor_aism.php)
https://www.kdnuggets.com/2022/06/21-cheat-sheets-data-science-interviews.html
https://www.researchgate.net/publication/30529921_Multi-Criteria_Analysis_A_Manual
https://www.researchgate.net/publication/275960103_An_analysis_of_multi-criteria_decision_making_methods
