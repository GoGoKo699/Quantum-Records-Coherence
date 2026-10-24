# Sharp upper bound

Use the [operational model](model.md). Write

$$
h(p)=-p\ln p-(1-p)\ln(1-p),\qquad
d(p\|q)=p\ln\frac pq+(1-p)\ln\frac{1-p}{1-q},
$$

with continuous endpoint conventions, and define

$$
J_\varepsilon=d(\varepsilon\|1-\varepsilon)
=(1-2\varepsilon)\ln\frac{1-\varepsilon}{\varepsilon}>0.
$$

## 1. Independent endpoint

If $C=0$, relative entropy zero implies $P_x=Q_x$ and affinity factorizes. Put $p_i=P_0(Y_i=1)\le\varepsilon$ and $q_i=P_1(Y_i=1)\ge1-\varepsilon$. The one-bit affinity is

$$
\sqrt{p_iq_i}+\sqrt{(1-p_i)(1-q_i)}\le2\sqrt{\varepsilon(1-\varepsilon)}.
$$

For example, writing $p_i=\sin^2\alpha_i$ and $q_i=\sin^2\beta_i$ makes this the monotonicity of $\cos(\beta_i-\alpha_i)$ on the allowed angular interval. Therefore

$$
v\le[2\sqrt{\varepsilon(1-\varepsilon)}]^N.
$$

The products $P_0=\operatorname{Bern}(\varepsilon)^{\otimes N}$ and $P_1=\operatorname{Bern}(1-\varepsilon)^{\otimes N}$, followed by the model's positive completion, attain equality. The same one-fragment argument gives $v\le2\sqrt{\varepsilon(1-\varepsilon)}$ for any $C$.

## 2. Relative entropy controls rare-event probability

For $s>0$ and $C\ge0$, let

$$
u(C,s)=\max\{p\in[e^{-s},1]:d(p\|e^{-s})\le C\}.
$$

It equals $1$ if $C\ge s$, and $u(0,s)=e^{-s}$. If $D(P\|Q)\le C$ and $Q(A)\le e^{-s}$, then

$$
P(A)\le u(C,s).
$$

To prove this, coarse-grain to the indicator of $A$. If $P(A)\le e^{-s}$ the claim is immediate. Otherwise, binary relative entropy decreases with its second argument below its first, so

$$
d(P(A)\|e^{-s})\le d(P(A)\|Q(A))\le C.
$$

If $Q(A)=0$, finiteness of relative entropy forces $P(A)=0$.

The identity

$$
d(p\|e^{-s})=ps-h(p)-(1-p)\ln(1-e^{-s})
$$

implies $u(C,s)\le(C+\ln2)/s$. For fixed $C>0$ and $s\to\infty$, this first proves $u\to0$. The defining equality then gives

$$
u(C,s)=\frac{C+o(1)}s.
$$

This last refinement, rather than a constant-loss inequality such as $C+\ln2$, is needed for the exact coefficient.

## 3. A finite-$N$ three-region inequality

Fix $\varepsilon<t<1/2$ and let $\overline Y=N^{-1}\sum_iY_i$. Partition the outcomes into

$$
A=\{\overline Y\le t\},\quad B=\{\overline Y\ge1-t\},\quad
M=\{t<\overline Y<1-t\}.
$$

Under the product reference $Q_0$, every mean is at most $\varepsilon$. For $\lambda>0$,

$$
\mathbb E_{Q_0}e^{\lambda\sum_iY_i}
\le(1-\varepsilon+\varepsilon e^\lambda)^N.
$$

Markov's inequality and minimization over $\lambda$ give the binary Chernoff bound $Q_0(\overline Y\ge t)\le e^{-Nd(t\|\varepsilon)}$. Apply the same argument to complemented bits under $Q_1$ to obtain, with

$$
a=d(t\|\varepsilon),\qquad b=d(t\|1-\varepsilon),
$$

$$
Q_1(A),Q_0(B)\le e^{-Nb},\qquad Q_0(M),Q_1(M)\le e^{-Na}.
$$

The rare-event lemma transfers these bounds to $P_x$. Cauchy--Schwarz on each of the three disjoint regions gives

$$
B(P_0,P_1)\le2\sqrt{u(C,Nb)}+u(C,Na).
$$

Consequently a valid finite-size upper bound is

$$
v\le\min\left\{2\sqrt{\varepsilon(1-\varepsilon)},\quad
2\sqrt{u(C,Nd(t\|1-\varepsilon))}+u(C,Nd(t\|\varepsilon))\right\}.
$$

Any admissible $t$ gives a bound. Numerical minimization over $t$ only improves its value; global optimization is not required for validity.

## 4. Exact asymptotic coefficient

Fix $C>0$ and $0<\varepsilon<1/2$. For sufficiently large $N$, choose $t_N=\varepsilon+N^{-1/8}<1/2$. Then

$$
d(t_N\|\varepsilon)=\Theta(N^{-1/4}),\qquad
d(t_N\|1-\varepsilon)\longrightarrow J_\varepsilon.
$$

The middle-region contribution is $O(N^{-3/4})=o(N^{-1/2})$, while each wrong-branch typical-region contribution is at most

$$
\sqrt{\frac{C+o(1)}{NJ_\varepsilon}}.
$$

The inequalities hold uniformly over all admissible laws, including heterogeneous and nonexchangeable records. Taking the supremum proves

$$
\limsup_{N\to\infty}\sqrt N\,v_{\max}(N,\varepsilon,C)
\le2\sqrt{C/J_\varepsilon}.
$$

[Matching constructions](constructions.md) proves the reverse inequality under exactly the same assumptions, establishing the limit. This is a fixed-positive-$C$, fixed-$\varepsilon$ theorem, not an asserted uniform expansion for arbitrary sequences $C_N$ or $\varepsilon_N$.
