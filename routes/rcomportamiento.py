from fastapi import APIRouter, Depends
from controllers.ccomportamiento import *
from models.mcomportamiento import Mcomportamiento
from typing import List
from auth.auth_route import protected_route

router = APIRouter()

nuevo_comportamiento = Ccomportamiento()


@router.post("/crear_comportamiento/")
async def crear_comportamiento(comportamiento: Mcomportamiento, get_protected_route: dict = Depends(protected_route)):
    rpta = nuevo_comportamiento.crear_comportamiento(comportamiento)
    return rpta


@router.get("/obtener_comportamiento/{comportamiento_id}", response_model=Mcomportamiento)
async def obtener_comportamiento(comportamiento_id: int, get_protected_route: dict = Depends(protected_route)):
    rpta = nuevo_comportamiento.obtener_comportamiento(comportamiento_id)
    return rpta


@router.get("/obtener_comportamientos/", response_model=List[Mcomportamiento])
async def obtener_comportamientos(get_protected_route: dict = Depends(protected_route)):
    rpta = nuevo_comportamiento.obtener_comportamientos()
    return rpta


@router.put("/actualizar_comportamiento/")
async def obtener_comportamientos(comportamiento: Mcomportamiento, get_protected_route: dict = Depends(protected_route)):
    rpta = nuevo_comportamiento.actualizar_comportamiento(comportamiento)
    return rpta
