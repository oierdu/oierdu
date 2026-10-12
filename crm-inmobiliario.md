# CRM inmobiliario con IA

Prototipo colaborativo de gestión empresarial para reunir clientes, inmuebles, oportunidades y calendario. El objetivo es seguir el contexto de una operación sin repartir información entre herramientas aisladas.

![Dashboard real con empresa y datos sintéticos](assets/crm-demo.jpg)

La captura corresponde a la aplicación ejecutada localmente en **Next.js 16.4.0**, entrando por «Ver demo inmobiliaria». La empresa y las cifras son sintéticas; no representan actividad ni resultados comerciales.

## Módulos y alcance

| Módulo | Alcance comprobado |
| --- | --- |
| Clientes | Listado y ficha presentes en código; navegación revisada en demo sintética |
| Inmuebles y oportunidades | Cartera, fichas y seguimiento de estados implementados en el snapshot; no validados contra una base real |
| Calendario | Organización de eventos y agenda en código; la conexión con Google Calendar requiere configuración |
| Dashboard | Resumen de cartera, operaciones y trabajo semanal revisado con datos de ejemplo |
| Asistente | Interfaz contextual y lógica de intenciones presentes; no se acredita ejecución contra OpenAI ni acciones reales de negocio |
| Automatizaciones | Configuración y flujos de integración presentes; activación dependiente de servicios y credenciales, sin envíos externos probados |

La demo ayuda a explorar la interfaz; no convierte proveedores, canales o automatizaciones configurables en servicios activos.

## Arquitectura pública

Next.js, React y TypeScript para aplicación e interfaz; Tailwind CSS para componentes; Supabase y PostgreSQL para datos y autenticación. El código documenta conexiones con OpenAI y n8n. Esta descripción se limita a tecnologías y funciones generales, sin configuraciones internas, secretos ni información de clientes.

## Procedencia y validación

Desarrollo colaborativo con autores e historial preservados. [Referencia original y créditos](https://github.com/iazticontact/crm-inmobiliario-demo). Snapshot de origen `ad3c06e5e6dca8e9cf0342845f670b1b48478851`; preparación local `efa524f4766a089c4cd5fb6e2844f67aa7f52963`.

La preparación local superó TypeScript y compilación de Next.js, con 50 páginas generadas, tras actualizar dependencias. Se revisaron dashboard y clientes en demo con credenciales externas retiradas del proceso. Son comprobaciones conservadas de la entrega anterior, sin nueva ejecución en este refinamiento.

No se probó una base de datos real ni servicios externos. No se acredita producto comercial terminado. La copia recuperada sigue local por falta de permisos de republicación y avisos altos de dependencias pendientes.

[Volver al perfil](README.md) · [Contactar](mailto:oier.dunabeitia@opendeusto.es)
