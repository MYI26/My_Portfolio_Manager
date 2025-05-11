from datetime import datetime, timedelta
import random

class StockChartModel:
    def get_static_data(self, range_type: str):
        """
        מחזיר נתונים סטטיים עבור הגרף בהתאם לטווח הזמן שנבחר.
        """
        print(f"[Model] Fetching static data for range: {range_type}")  # בדיקה
        today = datetime.today()

        if range_type == "Last Week":
            prices = [random.uniform(75, 85) for _ in range(7)]
            labels = [(today - timedelta(days=i)).strftime('%d/%m') for i in reversed(range(7))]
        elif range_type == "Last Month":
            prices = [random.uniform(70, 90) for _ in range(30)]
            labels = [(today - timedelta(days=i)).strftime('%d/%m') for i in reversed(range(30))]
        elif range_type == "Last 3 Months":
            prices = [random.uniform(65, 95) for _ in range(90)]
            labels = [(today - timedelta(days=i)).strftime('%d/%m') for i in reversed(range(90))]
        else:
            prices = []
            labels = []

        print(f"[Model] Generated prices: {prices}, labels: {labels}")  # בדיקה
        return prices, labels