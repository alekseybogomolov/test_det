import cv2
import numpy as np

class PolygonUtils:
    @staticmethod
    def box_intersects_polygon(box, polygon):
        """Проверка, пересекается ли bbox с полигоном"""
        x1, y1, x2, y2 = map(int, box)
        points = [(x1, y1), (x2, y1), (x2, y2), (x1, y2)]
        return any(cv2.pointPolygonTest(polygon, pt, False) >= 0 for pt in points)

    @staticmethod
    def draw_dashed_polygon(img, polygon, color=(0, 255, 0), thickness=2, gap=15):
        """Рисование пунктирного полигона"""
        for i in range(len(polygon)):
            pt1 = polygon[i]
            pt2 = polygon[(i + 1) % len(polygon)]
            dist = int(np.linalg.norm(np.array(pt1) - np.array(pt2)))
            for j in range(0, dist, gap * 2):
                start = tuple(np.array(pt1) + (np.array(pt2) - np.array(pt1)) * j // dist)
                end = tuple(np.array(pt1) + (np.array(pt2) - np.array(pt1)) * (j + gap) // dist)
                cv2.line(img, start, end, color, thickness)