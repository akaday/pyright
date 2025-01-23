import datetime

__all__ = ["tzid_from_tzinfo", "tzid_from_dt", "tzids_from_tzinfo"]

def tzids_from_tzinfo(tzinfo: datetime.tzinfo | None) -> tuple[str, ...]: ...
def tzid_from_tzinfo(tzinfo: datetime.tzinfo | None) -> str | None: ...
def tzid_from_dt(dt: datetime.datetime) -> str | None: ...
def tzinfo2tzids(tzinfo: datetime.tzinfo | None) -> set[str]: ...
