# CRM inmobiliario con IA

Proyecto de CRM y asistente de IA presentado en mi experiencia de desarrollo. Esta ficha resume la arquitectura documentada en la referencia técnica pública. No incluye código del producto ni acceso a entornos de clientes.

## Problema y alcance

Reunir clientes, propiedades, oportunidades y calendario en una aplicación web con un asistente contextual. La documentación de referencia describe un prototipo funcional y diferencia el modo demostración de las integraciones configuradas.

## Arquitectura documentada

| Capa | Tecnología y función |
| --- | --- |
| Interfaz y aplicación | Next.js, React y TypeScript |
| Datos y autenticación | Supabase, PostgreSQL y políticas de acceso por empresa |
| Asistente | Integración documentada con OpenAI |
| Automatización | n8n como servicio externo de integración |
| Interfaz visual | Tailwind CSS y componentes reutilizables |

## Validación del snapshot

Se han ejecutado TypeScript y la compilación de Next.js sobre el snapshot `ad3c06e5e6dca8e9cf0342845f670b1b48478851`. La navegación de dashboard y clientes se ha revisado en modo demo local con datos sintéticos. No se han comprobado servicios externos ni una base de datos real.

## Validación del snapshot

Se han ejecutado TypeScript y la compilación de Next.js sobre el snapshot `ad3c06e5e6dca8e9cf0342845f670b1b48478851`. La navegación de dashboard y clientes se ha revisado en modo demo local con datos sintéticos. No se han comprobado servicios externos ni una base de datos real.

## Estado y límites

La existencia de un módulo en código o documentación no acredita su uso en producción. La referencia documenta una demostración local y conexiones reales pendientes de configuración. No se afirma que todos los canales, automatizaciones o proveedores estén activos.

No se ha identificado una licencia de republicación del código. Esta presentación contiene únicamente una descripción técnica; se mantienen fuera de ella los datos de clientes, las credenciales, los accesos de prueba y las configuraciones internas.

[Referencia técnica pública: CRM Inmobiliario Demo](https://github.com/iazticontact/crm-inmobiliario-demo/blob/main/README.md)

[Volver al perfil](README.md) · [Contactar](mailto:oier.dunabeitia@opendeusto.es)
