class Solution(object):
    def numberOfPermutations(self, n, requirements):
        """
        :type n: int
        :type requirements: List[List[int]]
        :rtype: int
        """
        MOD = 10**9 + 7

        # Requisitos como {prefixo: número de inversões}
        req_map = {end: inv for end, inv in requirements}

        # Limite de inversões relevante: 400 + n (seguro)
        MAX_INV = 400 + n

        # dp[i] = nº de permutações com i inversões até o momento
        dp = [0] * (MAX_INV + 1)
        dp[0] = 1  # permutação vazia tem 0 inversões

        # Construindo permutações de tamanho 1 até n
        for size in range(1, n + 1):
            new_dp = [0] * (MAX_INV + 1)

            # Prefix sums para somar intervalos de forma eficiente
            prefix = [0] * (MAX_INV + 1)
            prefix[0] = dp[0]
            for i in range(1, MAX_INV + 1):
                prefix[i] = (prefix[i - 1] + dp[i]) % MOD

            # Calculando new_dp usando inversões possíveis ao adicionar um novo número
            for inv in range(MAX_INV + 1):
                low = max(0, inv - (size - 1))
                high = inv

                if low > high:
                    continue

                total = prefix[high]
                if low > 0:
                    total = (total - prefix[low - 1] + MOD) % MOD

                new_dp[inv] = total

            dp = new_dp

            # Se houver requisito de inversão exato neste tamanho de prefixo
            if (size - 1) in req_map:
                target_inv = req_map[size - 1]

                if target_inv > MAX_INV or dp[target_inv] == 0:
                    return 0  # impossível satisfazer

                # Zera tudo, exceto a posição desejada
                only_required = [0] * (MAX_INV + 1)
                only_required[target_inv] = dp[target_inv]
                dp = only_required

        # A resposta está no número de permutações com inversão desejada no final
        return dp[req_map[n - 1]]
