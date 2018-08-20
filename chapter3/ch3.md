# 函数的增长
## 渐近记号
输入规模足够大的时候，需要研究算法的渐进效率
(本章内容详见书本，符号太多)

## 标准记号与常用函数
陌生公式
1. $|x| < 1$ 时，$ln(1+x)$有如下级数展开：
$$ ln(1+x) = x-\frac{x^2}{2} +\frac{x^3}3 -\frac{x^4}4 + \frac{x^5}5- \cdots $$
2. $x>-1$时，有如下不等式：
$$\frac{x}{1+x} \le ln(1+x) \le x $$其中仅在$x=0$时等号成立
3. 斯特林近似公式（Stirling）
$$n! = \sqrt{2\pi n}(\frac{n}{e})^n(1+\Theta(\frac{1}{n}))$$
$n! = \sqrt{2\pi n}(\frac{n}{e})^ne^{{\alpha}_n}$，其中$\frac{1}{12n+1}<{\alpha}_n<\frac{1}{12n}$



