#!/bin/bash

# Array de nombres de misión espacial

missions=("Apollo" "Voyager" "Discovery" "Pathfinder" "Galaxy" "Orion" "Pioneer")

# Generar un índice aleatorio

index=$((RANDOM % ${#missions[@]}))

# Obtener el nombre de la misión espacial aleatoria

random_mission=${missions[$index]}

echo "Nombre de la misión espacial aleatoria: $random_mission"
