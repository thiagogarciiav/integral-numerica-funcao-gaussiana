"""
Comparação de métodos para calcular a integral definida de f(x) = e¯ˣ²

Abordagens:
1. Regra de Simpson composta (implementação manual)
2. SciPy (quad adaptativo e simpson com malha fixa)
3. SymPy (integração simbólica e avaliação numérica)
"""

import math
import scipy.integrate as spi
import numpy as np
import sympy as sp

# =====================================================
# Definição da função e valor de referência
# =====================================================
def f_numpy(x):
    """Função para NumPy/SciPy."""
    return np.exp(-x**2)

def f_python(x):
    """Função para Python puro (math)."""
    return math.exp(-x**2)

# Valor de referência com alta precisão (obtido via SymPy)
valor_referencia = 0.74682413281242702540

# =====================================================
# 1. Regra de Simpson composta (implementação manual)
# =====================================================

def simpson_manual(f, a, b, n):
    """
    Calcula a integral de f(x) de a até b usando a regra de Simpson composta.
    n deve ser par.
    """
    if n % 2 != 0:
        raise ValueError("n deve ser par para a regra de Simpson.")
    h = (b - a) / n
    soma = f(a) + f(b)
    for i in range(1, n):
        x = a + i * h
        if i % 2 == 0:
            soma += 2 * f(x)
        else:
            soma += 4 * f(x)
    return (h / 3) * soma

# Escolha de n (par)
n = 100
resultado_simpson_manual = simpson_manual(f_python, 0, 1, n)
erro_simpson_manual = abs(resultado_simpson_manual - valor_referencia)

print("=" * 50)
print("1. Regra de Simpson composta (manual)")
print(f"   n = {n}")
print(f"   Resultado: {resultado_simpson_manual:.15f}")
print(f"   Erro absoluto: {erro_simpson_manual:.2e}")

# =====================================================
# 2. SciPy
# =====================================================

print("\n" + "=" * 50)
print("2. SciPy")

# 2a. Integração adaptativa com quad
resultado_quad, erro_quad = spi.quad(f_numpy, 0, 1)

print(f"   a) quad (adaptativo):")
print(f"      Resultado: {resultado_quad:.15f}")
print(f"      Erro estimado: {erro_quad:.2e}")
print(f"      Erro real: {abs(resultado_quad - valor_referencia):.2e}")

# 2b. Regra de Simpson com malha fixa (usando scipy.integrate.simpson)
x_vals = np.linspace(0, 1, n + 1)  # n+1 pontos -> n subintervalos
y_vals = f_numpy(x_vals)

resultado_scipy_simpson = spi.simpson(y_vals, x=x_vals)
erro_scipy_simpson = abs(resultado_scipy_simpson - valor_referencia)

print(f"   b) Simpson com malha fixa (n={n}):")
print(f"      Resultado: {resultado_scipy_simpson:.15f}")
print(f"      Erro absoluto: {erro_scipy_simpson:.2e}")

# 2c. Regra do trapézio (apenas para comparação)
resultado_trapezio = spi.trapezoid(y_vals, x=x_vals)
erro_trapezio = abs(resultado_trapezio - valor_referencia)

print(f"   c) Trapézio com malha fixa (n={n}):")
print(f"      Resultado: {resultado_trapezio:.15f}")
print(f"      Erro absoluto: {erro_trapezio:.2e}")

# =====================================================
# 3. SymPy
# =====================================================

print("\n" + "=" * 50)
print("3. SymPy")

x_sym = sp.symbols('x')
f_sym = sp.exp(-x_sym**2)

# Integral indefinida
integral_indefinida = sp.integrate(f_sym, x_sym)
print(f"    Integral indefinida: {integral_indefinida}")

# Integral definida simbólica
integral_definida = sp.integrate(f_sym, (x_sym, 0, 1))
print(f"    Integral definida simbólica: {integral_definida}")

# Avaliação numérica com 20 dígitos
resultado_sympy = integral_definida.evalf(20)
print(f"   Valor numérico (20 dígitos): {resultado_sympy}")
print(f"   Erro absoluto (vs referência): {abs(float(resultado_sympy) - valor_referencia):.2e}")

# =====================================================
# Resumo comparativo
# =====================================================

print("\n" + "=" * 50)
print("Resumo comparativo")
print(f"{'Método':<30} {'Resultado':<20} {'Erro absoluto':<15}")
print("-" * 65)
print(f"{'Simpson manual (n=100)':<30} {resultado_simpson_manual:<20.15f} {erro_simpson_manual:<15.2e}")
print(f"{'SciPy quad':<30} {resultado_quad:<20.15f} {abs(resultado_quad - valor_referencia):<15.2e}")
print(f"{'SciPy simpson (n=100)':<30} {resultado_scipy_simpson:<20.15f} {erro_scipy_simpson:<15.2e}")
print(f"{'SciPy trapezoid (n=100)':<30} {resultado_trapezio:<20.15f} {erro_trapezio:<15.2e}")
print(f"{'SymPy (evalf)':<30} {float(resultado_sympy):<20.15f} {abs(float(resultado_sympy) - valor_referencia):<15.2e}")