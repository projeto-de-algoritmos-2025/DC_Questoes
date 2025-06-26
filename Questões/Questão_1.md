


# [3193. Count the Number of Inversions](#)

**Dificuldade:** Hard


## Descrição

Você recebe um inteiro `n` e um array 2D `requirements`, onde `requirements[i] = [end_i, cnt_i]` representa o índice final e a contagem de inversões de cada requisito.

Um par de índices `(i, j)` de um array de inteiros `nums` é chamado de **inversão** se:

- `i < j` e
- `nums[i] > nums[j]`

Retorne o número de permutações `perm` de `[0, 1, 2, ..., n - 1]` tal que para todos os `requirements[i]`, o prefixo `perm[0..end_i]` tenha exatamente `cnt_i` inversões.

Como a resposta pode ser muito grande, retorne o resultado módulo `10^9 + 7`.



## Exemplos

### Exemplo 1

**Input:**  
```

n = 3, requirements = \[\[2,2],\[0,0]]

```

**Output:**  
```

2

```

**Explicação:**  
As duas permutações são:

- `[2, 0, 1]`  
  Prefixo `[2, 0, 1]` tem inversões `(0, 1)` e `(0, 2)`.  
  Prefixo `[2]` tem 0 inversões.

- `[1, 2, 0]`  
  Prefixo `[1, 2, 0]` tem inversões `(0, 2)` e `(1, 2)`.  
  Prefixo `[1]` tem 0 inversões.

---

### Exemplo 2

**Input:**  
```

n = 3, requirements = \[\[2,2],\[1,1],\[0,0]]

```

**Output:**  
```

1

```

**Explicação:**  
A única permutação que satisfaz é `[2, 0, 1]`:

- Prefixo `[2, 0, 1]` tem inversões `(0, 1)` e `(0, 2)`.  
- Prefixo `[2, 0]` tem uma inversão `(0, 1)`.  
- Prefixo `[2]` tem 0 inversões.

---

### Exemplo 3

**Input:**  
```

n = 2, requirements = \[\[0,0],\[1,0]]

```

**Output:**  
```

1

```

**Explicação:**  
A única permutação que satisfaz é `[0, 1]`:

- Prefixo `[0]` tem 0 inversões.  
- Prefixo `[0, 1]` tem 0 inversões.

---

## Restrições

- `2 <= n <= 300`
- `1 <= requirements.length <= n`
- `requirements[i] = [end_i, cnt_i]`
- `0 <= end_i <= n - 1`
- `0 <= cnt_i <= 400`
- O input é gerado de forma que existe pelo menos um `i` tal que `end_i == n - 1`.
- Todos os valores de `end_i` são únicos.
```

