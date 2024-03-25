from typing import Dict, List, Tuple
import math

class Solution:

    def confusion_matrix(self, true_labels: List[int], pred_labels: List[int]) -> Dict[Tuple[int, int], int]:
        matrix = {}
        for t, p in zip(true_labels, pred_labels):
            matrix[(t, p)] = matrix.get((t, p), 0) + 1
        return matrix

    def jaccard(self, true_labels: List[int], pred_labels: List[int]) -> float:
        matrix = self.confusion_matrix(true_labels, pred_labels)
        intersect = sum(matrix[(label, label)] for label in set(true_labels) & set(pred_labels))
        true_positives = intersect
        false_positives = sum(matrix[(t, p)] for t, p in matrix if t != p)
        false_negatives = false_positives  # Simplification for symmetric difference in clustering context
        union = true_positives + false_positives + false_negatives
        return true_positives / union if union else 0.0

    def nmi(self, true_labels: List[int], pred_labels: List[int]) -> float:
        matrix = self.confusion_matrix(true_labels, pred_labels)
        total = len(true_labels)
        true_dist = {label: true_labels.count(label) for label in set(true_labels)}
        pred_dist = {label: pred_labels.count(label) for label in set(pred_labels)}
        MI = sum((count / total) * math.log((total * count) / (true_dist[t] * pred_dist[p]), 2)
                 for (t, p), count in matrix.items() if t in true_dist and p in pred_dist)
        H_true = -sum((count / total) * math.log(count / total, 2) for count in true_dist.values())
        H_pred = -sum((count / total) * math.log(count / total, 2) for count in pred_dist.values())
        return MI / math.sqrt(H_true * H_pred) if H_true and H_pred else 0.0


""" true_labels = [0, 1, 0, 0, 1, 1, 1, 0, 1, 1]
pred_labels = [1, 0, 1, 1, 0, 1, 1, 1, 0, 1]

solution = Solution()
confusion_matrix_result = solution.confusion_matrix(true_labels, pred_labels)
print(confusion_matrix_result) """

