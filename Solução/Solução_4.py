class Solution(object):
    def kClosest(self, points, k):
        """
        :type points: List[List[int]]
        :type k: int
        :rtype: List[List[int]]
        """
        # Ordena os pontos pela distância ao quadrado até a origem
        points.sort(key=lambda p: p[0]**2 + p[1]**2)
        # Retorna os k primeiros
        return points[:k]