# Recursos de la presentación

## Fotografía y capturas

Retrato: misma fotografía aportada por Oier, conservada sin modificar el contenido ni el encuadre. No se utiliza generación ni reconstrucción facial. El avatar de la cuenta es independiente.

La captura territorial procede de la demo pública real de GIPUZKOA 360, proyecto colaborativo de DeustoAI Labs. Se mantienen los créditos y límites del análisis. La captura del CRM inmobiliario se tomó en modo demo con datos sintéticos; no acredita actividad comercial ni integra servicios de clientes.

## Terminal y contacto

Terminal y botones creados para este perfil. GIF decorativo de 10 segundos, escritura progresiva y cursor. No representa compilaciones, despliegues ni pruebas reales. Versiones claras, oscuras y móviles; imágenes estáticas para movimiento reducido y enlace directo al GIF.

Los recursos claros y oscuros se seleccionan con los marcadores de tema nativos de GitHub, independientes de las consultas de tamaño y movimiento. Las variantes móviles usan `max-width: 600px`. No hay JavaScript ni CSS arbitrario en el README.

El generador `tools/generate_terminal.py` requiere Pillow y usa Consolas instalada en Windows para rasterizar el texto. No se distribuye el archivo de fuente. Todos los textos importantes se mantienen también en Markdown o en el texto alternativo.

## Iconos y licencias

Los iconos del nuevo stack proceden de [Skill Icons](https://github.com/tandpfun/skill-icons), commit `7f7e691e71aec64e8354bf697835e009d1ad80f8`. Se alojan localmente; se conserva la licencia MIT en `SkillIcons-LICENSE.txt`. Las filas móviles combinan los mismos SVG en tres o cuatro columnas. El icono SQL es una ilustración original, sin atribuirle carácter oficial.

Se conservan recursos heredados de [Simple Icons](https://github.com/simple-icons/simple-icons), CC0-1.0, y [Devicon](https://github.com/devicons/devicon), MIT, con sus avisos de licencia. Las marcas pertenecen a sus titulares. La inclusión de un icono no implica certificación ni afiliación.

Las portadas antiguas retiradas de la raíz siguen disponibles en el historial Git y en el checkpoint local. No forman parte del diseño actual.

## Refinamiento editorial del 12 de octubre

Tres grupos de stack compuestos con los iconos locales ya licenciados. El icono SQL es una ilustración vectorial original. La captura de CRM corresponde a la demo sintética auténtica de Next.js 16.4.0; no contiene clientes reales. Esta entrega anterior utilizaba una terminal de 560 px de ancho; sus recursos permanecen conservados.

La nueva captura territorial muestra el mapa completo y la tabla de resultados, con sus límites visibles. Cartografía: Eusko Jaurlaritza / Gobierno Vasco (geoEuskadi); población: Eustat; registros sanitarios: Open Data Euskadi. Se conserva la fecha del snapshot: no se recalculan resultados al revisar las fuentes actualizadas.

## Animación anterior conservada

La animación anterior `terminal-projects-*` escribe el comando y las áreas del portfolio, con cursor y salida gradual del texto. Sus cuatro GIF de 17 segundos y PNG estáticos se conservan como recursos históricos. La portada utiliza ahora la composición compacta descrita a continuación.

## Terminal compacta definitiva

La composición actual tiene cuatro líneas y un ciclo de 10 segundos. Escritorio: 500 × 145 px; móvil: 360 × 136 px antes de adaptarse al ancho disponible. En 390 px de viewport, la terminal ocupa aproximadamente 110–125 px de alto.

GitHub reescribe las condiciones de `<source>` que contienen `prefers-color-scheme`, lo que puede eliminar condiciones combinadas de tamaño o movimiento. Para preservar esas condiciones se utilizan dos enlaces con los marcadores de tema de GitHub `#gh-dark-mode-only` y `#gh-light-mode-only`; cada uno contiene su `<picture>` con consultas exclusivamente de ancho y movimiento reducido. No se introduce JavaScript ni CSS propio. Las variantes históricas de 17 segundos quedan conservadas; la presentación usa `terminal-compact-*`.
