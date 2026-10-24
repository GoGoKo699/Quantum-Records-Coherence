# Exact pairwise independence does not restore exponential suppression

The generic fact that pairwise independence is weaker than full independence is established prior work, including in the quantum-Darwinism setting [Feller et al. (2021)](../references/related-work.md). The result here combines exact conditional pairwise independence with arbitrarily small fixed positive total correlation, local readability, and algebraically large attainable visibility for an increasing number of records.

## 1. Finite construction

Let $N\ge2$, let $M=\ell N$ for an integer $\ell\ge2$, and choose an integer $m$ with $0<m<M/2$. Set $a=m/M$. Let $R_0$ be the ordered $N$-bit sample drawn without replacement from a population of $M$ bits containing $m$ ones; let $R_1$ be its bitwise complement. For $K=\sum_iY_i$,

$$
R_0(K=k)=\frac{\binom mk\binom{M-m}{N-k}}{\binom MN},
$$

and the law is uniform within each weight shell. In particular,

$$
\mathbb E_{R_0}Y_i=a,\qquad
\operatorname{Cov}_{R_0}(Y_i,Y_j)=-\frac{a(1-a)}{M-1}\quad(i\ne j).
$$

Define

$$
p=\frac{1-\sqrt{1-4Ma(1-a)/(M-1)}}2,
\qquad t=\frac{p-a}{1-2a},
$$

and $P_0=(1-t)R_0+tR_1$, $P_1=tR_0+(1-t)R_1$. The parameters below ensure real square roots and $0<t<1/2$. Every conditional marginal error is $p$.

Total covariance gives

$$
\operatorname{Cov}_{P_0}(Y_i,Y_j)
=-\frac{a(1-a)}{M-1}+t(1-t)(1-2a)^2=0.
$$

The equality follows from $p(1-p)=Ma(1-a)/(M-1)$ and $p=a+t(1-2a)$. Two binary variables with zero covariance are independent, so **every pair** factorizes exactly under each $P_x$. The diagonal quantum completion makes this exact conditional independence of the two-fragment density operators, not merely of one measured correlator.

To enforce the readability bound, choose

$$
a_* = \frac{1-\sqrt{(1-2\varepsilon)^2+4\varepsilon(1-\varepsilon)/M}}2,
\qquad m=\lfloor Ma_*\rfloor.
$$

For sufficiently large $N$, $m>0$ and the construction is valid. Since $a\le a_*$ and $a(1-a)$ is increasing below $1/2$, it gives $p\le\varepsilon$.

## 2. An explicit finite correlation certificate

Let $Q_a=\operatorname{Bern}(a)^{\otimes N}$. After $i$ draws, the conditional probability $q_i$ of a one in the next draw has mean $a$ and variance

$$
\mathbb E(q_i-a)^2=\frac{i\,a(1-a)}{(M-1)(M-i)}.
$$

The chain rule and the elementary inequality $d(q\|a)\le(q-a)^2/[a(1-a)]$ yield

$$
D(R_0\|Q_a)\le S_{N,M}:=
\sum_{i=0}^{N-1}\frac{i}{(M-1)(M-i)}.
$$

The elementary inequality follows by applying $\ln z\le z-1$ to both terms of binary relative entropy. Mixture entropy obeys $H(P_x)\ge H(R_0)$, so

$$
T_x=Nh(p)-H(P_x)
\le S_{N,M}+N[h(p)-h(a)]=:\widehat C_{N,M}.
$$

This bound is directly computable and does not require an asymptotic normal approximation.

## 3. Arbitrarily small fixed budgets

Keep $\ell$ fixed and let $N\to\infty$. The floor prescription gives $a,p\to\varepsilon$ and

$$
Nt\longrightarrow\alpha_\ell
=\frac{\varepsilon(1-\varepsilon)}{\ell(1-2\varepsilon)^2}>0.
$$

A Riemann sum (or harmonic-number identity) gives

$$
S_{N,\ell N}\longrightarrow-\ln(1-1/\ell)-1/\ell,
$$

while

$$
N[h(p)-h(a)]\longrightarrow
\frac{\varepsilon(1-\varepsilon)}{\ell(1-2\varepsilon)}
\ln\frac{1-\varepsilon}{\varepsilon}=\alpha_\ell J_\varepsilon.
$$

Consequently

$$
\widehat C_{N,\ell N}\longrightarrow
G_\varepsilon(\ell):=-\ln(1-1/\ell)-1/\ell+\alpha_\ell J_\varepsilon,
\qquad G_\varepsilon(\ell)\longrightarrow0\quad(\ell\to\infty).
$$

For any prescribed $C>0$, choose a fixed integer $\ell$ with $G_\varepsilon(\ell)<C$. For all sufficiently large $N$, the construction satisfies $T_x\le C$ and the error bound, with exact pairwise independence.

The affinity inequality from [Matching constructions](constructions.md), valid for any complemented pair of laws, gives

$$
v=B(P_0,P_1)\ge2\sqrt{t(1-t)},\qquad
\liminf_{N\to\infty}\sqrt N\,v\ge2\sqrt{\alpha_\ell}>0.
$$

The general converse gives $v=O(N^{-1/2})$, so these examples have $v=\Theta(N^{-1/2})$. We do not claim the optimal coefficient under the *additional* pairwise-independence restriction.

## 4. Realization and resource boundary

Use the diagonal positive completion and its purifying isometry from [the model](model.md). Alternatively the star circuit works with the initial noisy record law $R_0$ in place of independent noise, and has visibility exactly $2\sqrt{t(1-t)}$. In that version the initial record noise has the negative dependence quantified by $S_{N,M}$; it is not free independent thermal noise. Preparing the correlated hypergeometric input is an additional resource, and no linear gate bound for that preparation is claimed here.
