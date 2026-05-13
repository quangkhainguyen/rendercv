import pydantic

from .bases.entry import BaseEntry
from .bases.entry_with_complex_fields import BaseEntryWithComplexFields


class BaseExperienceEntry(BaseEntry):
    company: str = pydantic.Field(
        examples=["Microsoft", "Google", "Princeton Plasma Physics Laboratory"],
    )
    position: str = pydantic.Field(
        examples=["Software Engineer", "Research Assistant", "Project Manager"],
    )
    technologies: list[str] | None = pydantic.Field(
        default=None,
        description="Technologies or tools used in this role.",
        examples=[
            ["Python", "Django", "AWS"],
            ["React", "TypeScript", "GraphQL"],
        ],
    )


# This approach ensures ExperienceEntryBase keys appear first in the key order:
class ExperienceEntry(BaseEntryWithComplexFields, BaseExperienceEntry):
    pass
