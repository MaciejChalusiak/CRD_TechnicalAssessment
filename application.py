from dataclasses import dataclass
from math import ceil


@dataclass(frozen=True)
class Security:
    name: str
    target_pct: float
    current_pct: float
    unit_price: float
    asset_amount: float

    def __post_init__(self):
        self._validate_unit_price()
        self._validate_target_pct()
        self._validate_current_pct()

    def _validate_unit_price(self):
        if self.unit_price <= 0:
            raise ValueError(f"unit_price for {self.name} have to be > 0")

    def _validate_target_pct(self):
        if not (0 <= self.target_pct <= 100):
            raise ValueError(f"target_pct for {self.name} have to be in range 0-100")

    def _validate_current_pct(self):
        if not (0 <= self.current_pct <= 100):
            raise ValueError(f"current_pct for {self.name} have to be in range 0-100")

    @property
    def shares_to_variance(self) -> int:
        target_variance_pct = (self.current_pct - self.target_pct) / 100
        target_variance = target_variance_pct * self.asset_amount / self.unit_price
        return ceil(target_variance)
