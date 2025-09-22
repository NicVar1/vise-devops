# actividad-vise-devops

Este repositorio contiene la implementación de una **API REST en JSON** para la empresa ficticia **VISE**, desarrollada como parte de la materia **DevOps**.  

La API permite:  

- **Registrar clientes** verificando restricciones según el tipo de tarjeta (Classic, Gold, Platinum, Black, White).  
- **Procesar compras** aplicando beneficios y descuentos específicos para cada tarjeta.  
- **Rechazar transacciones** cuando el cliente no cumple con las condiciones establecidas.  

## Rutas principales

### 1. `POST /client`
Registra un cliente si cumple con los requisitos del tipo de tarjeta solicitado.  

**Ejemplo de petición:**
```json
{
  "name": "John Doe",
  "country": "USA",
  "monthlyIncome": 1200,
  "viseClub": true,
  "cardType": "Platinum"
}
