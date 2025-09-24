import pytest
from app.models.client import Client, CardType
from app.services.card_service import card_service

class TestCardService:
    
    def test_classic_card_no_restrictions(self):
        client = Client(
            client_id=None,
            name="Test User",
            country="USA",
            monthly_income=100,
            vise_club=False,
            card_type=CardType.CLASSIC
        )
        
        is_eligible, message = card_service.validate_card_eligibility(client)
        assert is_eligible == True
        assert "Classic" in message
    
    def test_gold_card_insufficient_income(self):
        client = Client(
            client_id=None,
            name="Test User",
            country="USA",
            monthly_income=400,
            vise_club=False,
            card_type=CardType.GOLD
        )
        
        is_eligible, message = card_service.validate_card_eligibility(client)
        assert is_eligible == False
        assert "500 USD" in message
    
    def test_platinum_card_no_vise_club(self):
        client = Client(
            client_id=None,
            name="Test User",
            country="USA",
            monthly_income=1500,
            vise_club=False,
            card_type=CardType.PLATINUM
        )
        
        is_eligible, message = card_service.validate_card_eligibility(client)
        assert is_eligible == False
        assert "VISE CLUB" in message
    
    def test_black_card_restricted_country(self):
        client = Client(
            client_id=None,
            name="Test User",
            country="China",
            monthly_income=3000,
            vise_club=True,
            card_type=CardType.BLACK
        )
        
        is_eligible, message = card_service.validate_card_eligibility(client)
        assert is_eligible == False
        assert "China" in message
