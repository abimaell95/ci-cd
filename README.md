
# 1. Introducción a CI/CD

## Definición e Importancia

**¿Qué es CI/CD?**
- **Integración Continua (CI)**: La práctica de integrar automáticamente los cambios de código de múltiples contribuyentes en un repositorio compartido varias veces al día. Cada integración se verifica mediante una compilación automatizada y pruebas automatizadas.
- **Despliegue Continuo (CD)**: La práctica de desplegar automáticamente cada cambio que pasa la etapa de CI en un entorno de producción. Esto asegura que el software siempre esté en un estado liberable.

**Beneficios de CI/CD:**
- **Tiempo de comercialización más rápido**: Al automatizar los procesos de integración y despliegue, los equipos pueden lanzar nuevas características y actualizaciones con más frecuencia y confiabilidad.
- **Mejora de la calidad**: Las pruebas automatizadas ayudan a detectar errores y problemas temprano en el proceso de desarrollo, reduciendo la probabilidad de defectos en producción.
- **Riesgo reducido**: Despliegues más pequeños y frecuentes son menos riesgosos que lanzamientos grandes e infrecuentes. Los problemas pueden identificarse y solucionarse más rápidamente.
- **Colaboración mejorada**: Las prácticas de CI/CD fomentan la colaboración entre desarrolladores, testers y equipos de operaciones, promoviendo una cultura de responsabilidad compartida.

**Ejemplos del mundo real:**
- **Netflix**: Usa un sofisticado pipeline de CI/CD para entregar actualizaciones y nuevas características a su servicio de streaming varias veces al día.
- **Amazon**: Despliega cambios en sus sistemas de producción cada 11.7 segundos en promedio, permitiendo una experimentación e innovación rápidas.
- **Etsy**: Adoptó CI/CD para mejorar la frecuencia de despliegue y reducir el impacto de los problemas en producción, resultando en una plataforma de comercio electrónico más estable y confiable.

## Explicación detallada de CI/CD:

**Integración Continua (CI)**:
- **Integración con Control de Versiones**: Los desarrolladores frecuentemente hacen commit de cambios de código a un repositorio compartido. Herramientas como Git, Subversion o Mercurial son comúnmente usadas.
- **Compilaciones Automatizadas**: Cada commit dispara un proceso de compilación automatizado, compilando el código y ejecutando pruebas unitarias para asegurar que los cambios no rompan la aplicación.
- **Ejecución Automática de Pruebas**: Se ejecutan pruebas automatizadas, incluyendo pruebas unitarias, pruebas de integración y a veces incluso pruebas de UI, para validar el código.

**Despliegue Continuo (CD)**:
- **Estrategias de Despliegue**:
  - **Despliegue Azul/Verde**: Se usan dos entornos idénticos (azul y verde). Un entorno sirve el tráfico en vivo, mientras que el otro se usa para staging de nuevas versiones. Una vez probado, el tráfico se cambia al nuevo entorno.
  - **Despliegues Canarios**: Una nueva versión se despliega gradualmente a un pequeño subconjunto de usuarios. Si no se detectan problemas, el despliegue se expande gradualmente a todos los usuarios.
  - **Actualizaciones Graduales**: La nueva versión se despliega en fases a través de la infraestructura, reduciendo el tiempo de inactividad y el riesgo.
- **Infraestructura como Código (IaC)**: La infraestructura se gestiona y provisiona a través de código (por ejemplo, Terraform, AWS CloudFormation), permitiendo versionado y reproducibilidad.
- **Gestión de Configuración**: Herramientas como Ansible, Chef o Puppet se usan para gestionar configuraciones de aplicaciones y sistemas de manera consistente a través de los entornos.

# 2. Descripción General de Herramientas CI/CD

## Herramientas CI/CD Populares

### Jenkins

**Descripción**:
- Jenkins es una herramienta de automatización de código abierto escrita en Java. Es uno de los servidores CI/CD más populares y ampliamente utilizados.

**Características**:
- Integración con una amplia gama de herramientas y tecnologías.
- Gran ecosistema de plugins.
- Soporta pipelines definidos como código (Jenkinsfile).

**Ventajas**:
- Alta flexibilidad y personalización.
- Gran comunidad y soporte.
- Integración con casi cualquier herramienta de desarrollo.

**Desventajas**:
- Configuración y mantenimiento pueden ser complejos.
- Requiere recursos significativos para grandes proyectos.

### GitHub Actions

**Descripción**:
- GitHub Actions es una plataforma de integración continua y entrega continua (CI/CD) directamente en GitHub. Permite automatizar flujos de trabajo, desde compilaciones y pruebas hasta despliegues.

**Características**:
- Integración perfecta con repositorios de GitHub.
- Gran cantidad de acciones disponibles en el Marketplace.
- Soporta definiciones de flujos de trabajo en YAML.

**Ventajas**:
- Fácil de usar para proyectos alojados en GitHub.
- No requiere configuración de servidores adicionales.
- Gratuito para proyectos públicos y generosos límites gratuitos para proyectos privados.

**Desventajas**:
- Funcionalidades avanzadas pueden requerir tiempo para aprender.
- Menos flexible que Jenkins para configuraciones complejas.

### GitLab CI

**Descripción**:
- GitLab CI es una herramienta de CI/CD integrada en GitLab, una plataforma de desarrollo de software completa.

**Características**:
- Integración nativa con GitLab.
- Pipelines definidos en `.gitlab-ci.yml`.
- Soporte para integración, pruebas y despliegue continuo.

**Ventajas**:
- Excelente integración con el ecosistema de GitLab.
- Fácil de usar y configurar.
- Funcionalidades robustas para DevOps y gestión de proyectos.

**Desventajas**:
- Limitaciones en la versión gratuita para proyectos privados.
- Puede ser más complejo que GitHub Actions para algunos usuarios.

### CircleCI

**Descripción**:
- CircleCI es una plataforma de CI/CD basada en la nube que soporta múltiples lenguajes y entornos de desarrollo.

**Características**:
- Pipelines definidos como código en YAML.
- Integración con GitHub y Bitbucket.
- Soporte para contenedores Docker.

**Ventajas**:
- Fácil de usar con una interfaz intuitiva.
- Rápida configuración y tiempos de ejecución.
- Generoso plan gratuito para proyectos pequeños.

**Desventajas**:
- Configuración avanzada puede ser compleja.
- Limitaciones en el plan gratuito para proyectos grandes.

### Travis CI

**Descripción**:
- Travis CI es una herramienta de CI/CD que se integra bien con GitHub, ofreciendo compilaciones automáticas y despliegues.

**Características**:
- Pipelines definidos en `.travis.yml`.
- Soporte para múltiples lenguajes de programación.
- Despliegue a múltiples plataformas.

**Ventajas**:
- Fácil integración con GitHub.
- Configuración sencilla y rápida.
- Gratuito para proyectos de código abierto.

**Desventajas**:
- Planes gratuitos limitados para proyectos privados.
- Puede ser más lento en comparación con otras herramientas.

### Recomendaciones de Uso

**Elección de la Herramienta**:
- **Jenkins**: Ideal para grandes organizaciones que requieren alta personalización y flexibilidad.
- **GitHub Actions**: Perfecto para proyectos alojados en GitHub que buscan una integración sencilla y efectiva.
- **GitLab CI**: Excelente para equipos que ya usan GitLab para gestión de proyectos y repositorios de código.
- **CircleCI**: Adecuado para equipos que buscan una configuración rápida y fácil de usar con soporte robusto para Docker.
- **Travis CI**: Bueno para proyectos de código abierto y pequeños proyectos privados que buscan simplicidad.


# 3. Configuración de tu Entorno

## Prerrequisitos

**Conocimientos Básicos de Git y Control de Versiones**
- **Git**: Es fundamental entender cómo funciona Git para manejar el control de versiones en tu proyecto. Conceptos como `commit`, `branch`, `merge` y `pull request` son esenciales.
- **Plataformas de Repositorios**: Familiarízate con plataformas como GitHub, GitLab o Bitbucket, ya que estas se integran fácilmente con herramientas CI/CD.

**Familiaridad con Docker**
- **Contenedores Docker**: Comprender cómo crear, gestionar y utilizar contenedores Docker es crucial, ya que muchas herramientas CI/CD utilizan Docker para crear entornos de construcción y despliegue consistentes.
- **Docker Compose**: Aprender a definir y ejecutar aplicaciones multi-contenedor con Docker Compose.

**Comprensión Básica del Ciclo de Vida del Desarrollo de Software**
- **Etapas del Desarrollo**: Conocer las diferentes etapas del desarrollo de software (desarrollo, pruebas, integración, despliegue) y cómo CI/CD encaja en este ciclo.
- **Metodologías Ágiles**: Entender las metodologías ágiles (Scrum, Kanban) puede ayudarte a implementar CI/CD de manera más efectiva.

## Configuración del Entorno

**Instalar Git**
1. **Linux**:
   ```bash
   sudo apt-get update
   sudo apt-get install git
   ```

2. **Mac**:
   ```bash
   brew install git
   ```

3. **Windows**:
   - Descargar e instalar desde [git-scm.com](https://git-scm.com/).

**Instalar Docker**
1. **Linux**:
   ```bash
   sudo apt-get update
   sudo apt-get install docker-ce docker-ce-cli containerd.io
   ```

2. **Mac y Windows**:
   - Descargar e instalar Docker Desktop desde [docker.com](https://www.docker.com/products/docker-desktop).


# 4. Integración Continua (CI)

## Conceptos

**Integración con Control de Versiones**
- La integración continua implica que los desarrolladores frecuentemente hagan commit de sus cambios a un repositorio compartido. Esto puede hacerse varias veces al día.
- **Plataformas comunes**: GitHub, GitLab, Bitbucket.
- **Beneficios**: Detectar y corregir errores más rápidamente, facilitar la colaboración y la integración de cambios de múltiples desarrolladores.

**Compilaciones Automatizadas**
- Cada commit debe desencadenar una compilación automatizada. Esto asegura que el código siempre puede compilarse y que las dependencias están correctamente configuradas.
- **Herramientas comunes**: Jenkins, GitHub Actions, GitLab CI, CircleCI.
- **Beneficios**: Garantiza que el código en el repositorio compartido siempre esté en un estado que pueda ser compilado y probado.

**Ejecución Automática de Pruebas**
- Las pruebas unitarias y de integración deben ejecutarse automáticamente como parte del proceso de CI.
- **Beneficios**: Detectar problemas antes de que el código llegue a producción, asegurar que las nuevas características no rompan el código existente.

## Práctica

**Ejemplo: Configuración de un Pipeline CI Simple con GitHub Actions para un Proyecto Node.js**

1. **Configurar un proyecto Node.js**
   - Inicializa un nuevo proyecto Node.js:
     ```bash
     mkdir my-node-app
     cd my-node-app
     npm init -y
     ```
   - Instala Mocha (un framework de pruebas) y Chai (una biblioteca de aserciones):
     ```bash
     npm install mocha chai --save-dev
     ```

2. **Escribir una Prueba Simple**
   - Crea una carpeta `test` y un archivo `test.js`:
     ```javascript
     // test/test.js
     const assert = require('chai').assert;

     describe('Array', function() {
       it('should start empty', function() {
         const arr = [];
         assert.equal(arr.length, 0);
       });
     });
     ```

3. **Configurar GitHub Actions para CI**
   - Crea un directorio `.github/workflows` en la raíz del proyecto.
   - Añade un archivo de configuración `ci.yml`:
     ```yaml
     name: Node.js CI

     on:
       push:
         branches: [main]
       pull_request:
         branches: [main]

     jobs:
       build:
         runs-on: ubuntu-latest

         strategy:
           matrix:
             node-version: [14, 16]

         steps:
           - uses: actions/checkout@v2
           - name: Use Node.js ${{ matrix.node-version }}
             uses: actions/setup-node@v2
             with:
               node-version: ${{ matrix.node-version }}
           - run: npm install
           - run: npm test
     ```

4. **Commit y Push a GitHub**
   - Añade y commitea los cambios:
     ```bash
     git add .
     git commit -m "Setup CI with GitHub Actions"
     git push origin main
     ```

5. **Monitorizar el Pipeline**
   - Ve a la pestaña "Actions" en tu repositorio de GitHub para ver el progreso del pipeline.
   - Asegúrate de que todas las pruebas pasen.


# 5. Despliegue Continuo (CD)

## Conceptos

**Estrategias de Despliegue**
- **Despliegue Azul/Verde**: Esta estrategia utiliza dos entornos idénticos, uno de los cuales (verde) es el entorno de staging donde se despliega la nueva versión, mientras que el otro (azul) es el entorno en producción. Una vez que la nueva versión está probada en el entorno verde, el tráfico se redirige al entorno verde, convirtiéndolo en el nuevo entorno azul.
- **Despliegues Canarios**: Se despliega una nueva versión a un pequeño subconjunto de usuarios para detectar problemas antes de un despliegue completo. Si no se detectan problemas, la nueva versión se despliega gradualmente a más usuarios.
- **Actualizaciones Graduales**: La nueva versión se despliega en fases a través de la infraestructura, reduciendo el tiempo de inactividad y el riesgo de problemas en producción.

**Infraestructura como Código (IaC)**
- **Definición**: IaC es la gestión y aprovisionamiento de la infraestructura a través de código en lugar de procesos manuales. Esto permite que la infraestructura sea tratada de la misma manera que el código de la aplicación.
- **Herramientas Comunes**: Terraform, AWS CloudFormation, Ansible.
- **Beneficios**: Versionado, reproducibilidad, consistencia en los entornos de desarrollo y producción.

**Gestión de Configuración**
- **Definición**: Es el proceso de gestionar la configuración de los sistemas para que se mantengan consistentes a través de los entornos.
- **Herramientas Comunes**: Ansible, Chef, Puppet.
- **Beneficios**: Consistencia, automatización de la configuración, facilidad para aplicar cambios a múltiples sistemas.

## Tarea

**Ejemplo: Configuración de un Pipeline CD para Desplegar una Aplicación Web Dockerizada usando GitLab CI/CD**

1. **Configurar un Proyecto con Docker**
   - Crear un archivo `Dockerfile`:
     ```dockerfile
     # Use an official Python runtime as a parent image
     FROM python:3.8-slim

     # Set the working directory in the container
     WORKDIR /app

     # Copy the current directory contents into the container at /app
     COPY . /app

     # Install any needed packages specified in requirements.txt
     RUN pip install --no-cache-dir -r requirements.txt

     # Make port 80 available to the world outside this container
     EXPOSE 80

     # Define environment variable
     ENV NAME World

     # Run app.py when the container launches
     CMD ["python", "app.py"]
     ```

   - Crear un archivo `docker-compose.yml`:
     ```yaml
     version: '3'
     services:
       web:
         build: .
         ports:
           - "4000:80"
     ```

2. **Configurar GitLab CI/CD**
   - Crear un archivo `.gitlab-ci.yml` en la raíz del proyecto:
     ```yaml
     stages:
       - build
       - deploy

     build:
       stage: build
       image: docker:latest
       services:
         - docker:dind
       script:
         - docker build -t myapp:latest .
         - docker tag myapp:latest registry.gitlab.com/yourusername/yourproject:latest
         - docker push registry.gitlab.com/yourusername/yourproject:latest

     deploy:
       stage: deploy
       image: google/cloud-sdk:latest
       script:
         - echo $GCLOUD_SERVICE_KEY | base64 --decode -i > ${CI_PROJECT_DIR}/gcloud-service-key.json
         - gcloud auth activate-service-account --key-file ${CI_PROJECT_DIR}/gcloud-service-key.json
         - gcloud config set project $GCLOUD_PROJECT_ID
         - gcloud auth configure-docker
         - docker pull registry.gitlab.com/yourusername/yourproject:latest
         - docker run -d -p 80:80 registry.gitlab.com/yourusername/yourproject:latest
     ```

3. **Configurar Variables de Entorno en GitLab**
   - En la configuración del proyecto en GitLab, navega a **Settings > CI/CD > Variables** y añade las siguientes variables:
     - `GCLOUD_SERVICE_KEY`: Clave de servicio para la autenticación en Google Cloud.
     - `GCLOUD_PROJECT_ID`: ID de tu proyecto en Google Cloud.

4. **Commit y Push a GitLab**
   - Añade y commitea los cambios:
     ```bash
     git add .
     git commit -m "Setup CD pipeline with GitLab CI/CD"
     git push origin main
     ```

5. **Monitorizar el Pipeline**
   - Ve a la pestaña "CI/CD" en tu repositorio de GitLab para ver el progreso del pipeline.
   - Asegúrate de que todos los stages (build y deploy) se completen exitosamente.

Este ejemplo demuestra cómo configurar un pipeline CD para construir y desplegar una aplicación web Dockerizada usando GitLab CI/CD. La misma lógica puede adaptarse a otras plataformas y herramientas de CI/CD.