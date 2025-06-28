class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        total_len = len(nums1) + len(nums2)

        if total_len % 2 == 1:
            # Se o comprimento total for ímpar, a mediana é o (total_len // 2 + 1)-ésimo menor elemento
            return self.findKthElement(nums1, nums2, total_len // 2 + 1)
        else:
            # Se o comprimento total for par, a mediana é a média dos
            # (total_len // 2)-ésimo e (total_len // 2 + 1)-ésimo menores elementos
            mid1 = self.findKthElement(nums1, nums2, total_len // 2)
            mid2 = self.findKthElement(nums1, nums2, total_len // 2 + 1)
            return (mid1 + mid2) / 2.0

    def findKthElement(self, nums1, nums2, k):
        # Garante que nums1 é o array menor para otimizar a busca binária
        if len(nums1) > len(nums2):
            return self.findKthElement(nums2, nums1, k)

        m, n = len(nums1), len(nums2)

        # Trata casos base onde um dos arrays está vazio
        if m == 0:
            return nums2[k - 1]
        if n == 0:
            return nums1[k - 1]

        # Se k for 1, retorna o menor elemento entre os inícios dos arrays
        if k == 1:
            return min(nums1[0], nums2[0])
        pa = min(k // 2, m) # Número de elementos para pegar de nums1
        pb = k - pa        # Número de elementos restantes para pegar de nums2

        if nums1[pa - 1] <= nums2[pb - 1]:

            return self.findKthElement(nums1[pa:], nums2, k - pa)
        else:

            return self.findKthElement(nums1, nums2[pb:], k - pb)
