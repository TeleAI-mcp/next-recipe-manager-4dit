"""Configuration module for Next Recipe Manager."""

class Config:
    """Application configuration."""
    
    def __init__(self):
        self.debug = False
        self.database_url = "sqlite:///recipes.db"
        
config = Config()