class Solution:
    def checkOverlap(self, radius, xCenter, yCenter, x1, y1, x2, y2):

        # Find the closest x-coordinate in the rectangle
        closest_x = max(x1, min(xCenter, x2))

        # Find the closest y-coordinate in the rectangle
        closest_y = max(y1, min(yCenter, y2))

        # Distance from circle center to closest point
        dx = xCenter - closest_x
        dy = yCenter - closest_y

        # Compare squared distance with squared radius
        return dx * dx + dy * dy <= radius * radius