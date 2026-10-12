# GIPUZKOA 360

Una consulta puede ser breve y el desplazamiento ocupar horas. El proyecto de DeustoAI Labs combina una exploración territorial de los 88 municipios de Gipuzkoa con escenarios acotados de visita sanitaria completa.

## Producto y metodología

La demo territorial permite cambiar criterios, consultar un municipio, comparar resultados y revisar fuentes. Muestra cálculos guardados y reproducibles; no es una conversación en directo. El código incluye herramientas para consultar, comparar y simular criterios territoriales mediante un agente. El portal conversacional privado no se ha probado en esta revisión.

Los escenarios de movilidad reconstruyen viaje, espera, paseo, consulta y regreso únicamente donde hay datos suficientes. Su alcance documentado se limita a paradas admitidas de Zegama, Segura e Idiazabal y a la fecha del escenario; **la cobertura de 88 municipios corresponde al análisis territorial, no a 88 simulaciones completas de transporte**.

Python, pandas y GeoPandas sostienen el tratamiento y análisis de datos. Eustat aporta población, geoEuskadi geometría municipal y Open Data Euskadi registros sanitarios. [Fuentes y periodos del proyecto](https://github.com/Asier-Comba/Guipuzkoa360/blob/main/FUENTES.md).

Distancia geométrica no equivale a tiempo de viaje. Horarios programados y paseo modelado no son viajes observados. No se conocen citas disponibles ni capacidad asistencial; un escenario no acredita un ahorro real ni una recomendación clínica.

## Selección y contexto internacional

**Seleccionado entre los tres mejores proyectos de más de 60 equipos del Gipuzkoa AI Hackathon 2026**, según la información facilitada por Oier al equipo de revisión. La presentación está prevista para el **5 de noviembre de 2026 en Tabakalera, Donostia**. A fecha de revisión, 12 de octubre, las páginas oficiales consultadas no publican una lista nominal de seleccionados ni la cifra total de equipos: estos dos datos proceden del equipo y no se atribuyen a una certificación pública.

La [web oficial del hackathon](https://gipuzkoa-ai-hackathon.com/) identifica la colaboración con MIT Media Lab y MIT City Science, y anuncia la presentación de los tres mejores proyectos del Urban Challenge el 5 de noviembre. Es una selección del Urban Challenge; no se confunde con los premios de la final del 17 de octubre.

La [City Science Network](https://citysciencenetwork.org/) describe el Summit como su encuentro anual internacional y sitúa la jornada del 5 de noviembre en Tabakalera; el programa está sujeto a cambios. El [MIT Media Lab](https://www.media.mit.edu/projects/city-science-lab-san-sebastian/overview/) documenta City Science Lab @ Gipuzkoa y su colaboración territorial.

La referencia al MIT describe **el contexto del evento y de la red**. No afirma que el MIT haya premiado, seleccionado directamente o avalado individualmente a este proyecto, ni una relación laboral con la institución.

## Equipo y procedencia

Trabajo colaborativo de **DeustoAI Labs — Universidad de Deusto**.

| Integrante | Área documentada |
| --- | --- |
| Oier Duñabeitia Berezo | Ingesta oficial, geografía, calidad de datos, reproducibilidad e integración |
| Asier Comba | Herramientas y arquitectura del agente, runtime, validación y cierre técnico |
| Hugo Fernández Díez | Producto, visualización, integración y pruebas conversacionales |

[Repositorio original](https://github.com/Asier-Comba/Guipuzkoa360) · [Equipo y referencias del historial](https://github.com/Asier-Comba/Guipuzkoa360/blob/main/docs/TEAM.md). Snapshot de origen revisado: `43169aa8b3b6b3e0e004f86aa93a1cdd31c22ece`. No se atribuye el trabajo completo a una sola persona.

## Validación conservada

El 12 de octubre se superaron **1.087 pruebas Python y 17 pruebas Node de contrato** en la copia local recuperada. Se conservaron los commits W1 consultados por SHA. Estas cifras corresponden a la validación anterior; el refinamiento editorial no las vuelve a presentar como pruebas nuevas.

La copia propia de código continúa pendiente de autorización de republicación. No se alteraron el repositorio original ni su despliegue.

[Explorar demo](https://asier-comba.github.io/Guipuzkoa360/) · [Volver al perfil](../README.md)
