class Solution(object):
    def kClosest(self, points, k):
        """
        :type points: List[List[int]]
        :type k: int
        :rtype: List[List[int]]
        """

        def distance(point):
            return point[0]**2 + point[1]**2

        # Mediana das Medianas (pior caso O(n)) para selecionar o k-ésimo menor
        def select_kth(points, k):
            if len(points) <= 5:
                return sorted(points, key=distance)[k]

            # Divide em grupos de 5 e acha a mediana de cada grupo
            groups = [points[i:i+5] for i in range(0, len(points), 5)]
            medians = [sorted(group, key=distance)[len(group)//2] for group in groups]
            pivot = select_kth(medians, len(medians) // 2)

            # Particiona os pontos com base na distância ao pivot
            pivot_dist = distance(pivot)
            lows = [p for p in points if distance(p) < pivot_dist]
            highs = [p for p in points if distance(p) > pivot_dist]
            pivots = [p for p in points if distance(p) == pivot_dist]

            if k < len(lows):
                return select_kth(lows, k)
            elif k < len(lows) + len(pivots):
                return pivot
            else:
                return select_kth(highs, k - len(lows) - len(pivots))

        # Encontra o valor de corte (distância) usando mediana das medianas
        threshold_point = select_kth(points, k - 1)
        threshold = distance(threshold_point)

        # Coleta todos os pontos com distância <= threshold
        result = []
        for p in points:
            if distance(p) < threshold:
                result.append(p)
            elif distance(p) == threshold and len(result) < k:
                result.append(p)
            if len(result) == k:
                break

        return result
