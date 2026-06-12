import time
from dataclasses import dataclass, field
from typing import Dict, Mapping


ALLOWED_EVENT_TYPES = {"click", "email_open", "signup", "paid_conversion"}


def needs_update(last_timestamp: float, now: float | None = None, interval: int = 30) -> bool:
    """
    Return True if ``now - last_timestamp`` exceeds ``interval`` seconds.
    ``now`` defaults to ``time.time()`` for convenience.
    """
    if now is None:
        now = time.time()
    return (now - last_timestamp) >= interval


@dataclass
class AnalyticsEngine:
    """
    Simple in‑memory analytics engine that aggregates events per source
    and provides snapshot data.
    """
    # source -> event_type -> count
    _data: Dict[str, Dict[str, int]] = field(default_factory=dict)

    def record_event(self, source: str, event_type: str, count: int = 1) -> None:
        """
        Record ``count`` occurrences of ``event_type`` for ``source``.
        Raises:
            ValueError: if ``event_type`` is unknown or ``count`` is negative.
        """
        if event_type not in ALLOWED_EVENT_TYPES:
            raise ValueError(f"Unsupported event type: {event_type}")
        if count < 0:
            raise ValueError("count must be non‑negative")

        source_stats = self._data.setdefault(source, {})
        source_stats[event_type] = source_stats.get(event_type, 0) + count

    def snapshot(self) -> Dict[str, Mapping]:
        """
        Return a snapshot of the current analytics.
        Structure:
        {
            "total": {event_type: total_count, ...},
            "by_source": {
                source: {event_type: count, ...},
                ...
            }
        }
        """
        total: Dict[str, int] = {et: 0 for et in ALLOWED_EVENT_TYPES}
        for source_stats in self._data.values():
            for et, cnt in source_stats.items():
                total[et] += cnt

        # Deep copy to avoid external mutation
        by_source = {
            src: dict(stats) for src, stats in self._data.items()
        }

        return {"total": total, "by_source": by_source}

    def compare_with_api(
        self,
        api_data: Dict[str, Mapping],
        tolerance: float = 0.05,
    ) -> bool:
        """
        Compare the internal snapshot with ``api_data``.
        Returns True if every metric is within ``tolerance`` (relative difference).
        Missing keys are treated as zero.
        """
        snapshot = self.snapshot()

        def _relative_diff(a: int, b: int) -> float:
            if a == b == 0:
                return 0.0
            return abs(a - b) / max(abs(a), abs(b))

        # Compare totals
        for et in ALLOWED_EVENT_TYPES:
            internal = snapshot["total"].get(et, 0)
            external = api_data.get("total", {}).get(et, 0)
            if _relative_diff(internal, external) > tolerance:
                return False

        # Compare per‑source breakdown
        for src, internal_stats in snapshot["by_source"].items():
            external_stats = api_data.get("by_source", {}).get(src, {})
            for et in ALLOWED_EVENT_TYPES:
                internal = internal_stats.get(et, 0)
                external = external_stats.get(et, 0)
                if _relative_diff(internal, external) > tolerance:
                    return False

        # Also ensure there are no extra sources in api_data that we missed
        for src, external_stats in api_data.get("by_source", {}).items():
            if src not in snapshot["by_source"]:
                # treat missing internal as zero
                for et in ALLOWED_EVENT_TYPES:
                    external = external_stats.get(et, 0)
                    if external != 0 and tolerance < 1.0:
                        return False

        return True
