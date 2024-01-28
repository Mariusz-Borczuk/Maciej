from pydantic import BaseModel
from typing import List, Optional
#coś takiego albo na odwrót hehe
class PackageBase(BaseModel):
    name: str
    type: Optional[str] = None
    description: Optional[str] = None

class PackageCreate(PackageBase):
    pass

class Package(PackageBase):
    id: int
    Elf_id: int
     
class Config:
        orm_mode = True

class ElfBase(BaseModel):
    name: str

class ElfCreate(ElfBase):
    pass

class Elf(ElfBase):
    id: int
    packages: List[Package] = []

    class Config:
        orm_mode = True