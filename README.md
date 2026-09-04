# Integração Numérica da Função Gaussiana

Este projeto implementa e compara diferentes métodos para calcular a integral definida:

<a>
    <img>
        alt="func_integral"
        width="250px"
        style="padding-right:10px;"
        align="center"
        src="https://github.com/user-attachments/assets/cfc96ac6-2551-4c1e-89a2-c07038409681" 
    </>
</a>

<br/>

Como essa integral não possui antiderivada elementar, utilizamos técnicas numéricas e simbólicas para obter aproximações de alta precisão. O valor de referência (obtido com SymPy) é:

<a>
    <img>
        alt="valor_aprox"
        width="250px"
        style="padding-right:10px;"
        align="center"
        src="https://github.com/user-attachments/assets/0376b2e8-49ac-4aee-bd46-0b4ea30a95ab" 
    </>
</a>

<br/>

## Métodos implementados

1. **Regra de Simpson composta (implementação manual)**  
   - Fórmula clássica com \(n\) subintervalos (n deve ser par).  
   - Permite entender o funcionamento do método e a influência do número de subintervalos no erro.

2. **SciPy (`scipy.integrate`)**  
   - `quad`: integração adaptativa (QUADPACK) com alta precisão.  
   - `simpson`: regra de Simpson sobre uma malha fixa (mesma lógica da implementação manual, porém vetorizada).  
   - `trapezoid`: regra do trapézio para comparação.

3. **SymPy**  
   - Integração simbólica, resultando em:
   
<a>
    <img>
        alt="func_erro"
        width="250px"
        style="padding-right:10px;"
        align="center"
        src="https://github.com/user-attachments/assets/156cc5e7-8136-4a84-afe1-4b3de817f100" 
    </>
</a>

   - Avaliação numérica com precisão arbitrária.

## Pré-requisitos

- Python 3.7 ou superior
- Bibliotecas: `numpy`, `scipy`, `sympy`

Instale as dependências com:

```bash
pip install numpy scipy sympy