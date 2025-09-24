import pytest
from datetime import datetime
from app.models.client import Client, CardType
from app.models.purchase import Purchase
from app.services.purchase_service import purchase_service

class TestPurchaseService:
    
    def test_gold_card_weekday_discount(self):
        client = Client(
            client_id=1,
            name="Test User",
            country="USA",
            monthly_income=600,
            vise_club=False,
            card_type=CardType.GOLD
        )
        
        # Lunes con compra > 100 USD
        purchase = Purchase(
            client_id=1,
            amount=150.0,
            currency="USD",
            purchase_date=datetime(2025, 9, 22),  # Lunes
            purchase_country="USA"
        )
        
        success, processed, error = purchase_service.process_purchase(client, purchase)
        
        assert success == True
        assert processed.discount_applied == 22.5  # 15% de 150
        assert processed.final_amount == 127.5
        assert "15%" in processed.benefit
    
    def test_black_card_restricted_country_purchase(self):
        client = Client(
            client_id=1,
            name="Test User",
            country="USA",
            monthly_income=2500,
            vise_club=True,
            card_type=CardType.BLACK
        )
        
        purchase = Purchase(
            client_id=1,
            amount=100.0,
            currency="USD",
            purchase_date=datetime(2025, 9, 22),
            purchase_country="China"  # País restringido
        )
        
        success, processed, error = purchase_service.process_purchase(client, purchase)
        
        assert success == False
        assert "China" in error
        assert "Black" in error
